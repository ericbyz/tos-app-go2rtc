#!/usr/bin/env bash
# Bump the pinned upstream version: UPSTREAM + config.ini + control in lockstep.
# Usage: ./scripts/bump_upstream.sh 1.9.16
set -euo pipefail

NEW_VERSION="${1:?usage: bump_upstream.sh <version>}"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${REPO_ROOT}"

# UPSTREAM
sed -i "s/^UPSTREAM_TAG=.*/UPSTREAM_TAG=v${NEW_VERSION}/" UPSTREAM
sed -i "s/^UPSTREAM_VERSION=.*/UPSTREAM_VERSION=${NEW_VERSION}/" UPSTREAM
sed -i "s/^ASSET_x86_64=.*/ASSET_x86_64=go2rtc_linux_amd64/" UPSTREAM
sed -i "s/^ASSET_aarch64=.*/ASSET_aarch64=go2rtc_linux_arm64/" UPSTREAM
sed -i "s/^SHA256_x86_64=.*/SHA256_x86_64=REPLACE_WITH_UPSTREAM_SHA256/" UPSTREAM
sed -i "s/^SHA256_aarch64=.*/SHA256_aarch64=REPLACE_WITH_UPSTREAM_SHA256/" UPSTREAM

# config.ini
python3 - "$NEW_VERSION" <<'PYEOF'
import json, sys
cfg = json.load(open("config.ini", encoding="utf-8"))
cfg["version"] = sys.argv[1]
with open("config.ini", "w", encoding="utf-8", newline="\n") as f:
    json.dump(cfg, f, ensure_ascii=False, indent=2)
    f.write("\n")
PYEOF

# DEBIAN/control version
sed -i "s/^Version:.*/Version: ${NEW_VERSION}/" DEBIAN/control

echo "bumped to ${NEW_VERSION}"
echo "NEXT STEPS:"
echo "  1. pin the new release binary SHA256s in UPSTREAM (SHA256_x86_64 / SHA256_aarch64)"
echo "  2. review upstream release notes for config schema changes"
echo "  3. run ./build.sh && ./scripts/validate.py"
echo "  4. commit, tag v${NEW_VERSION} and push to trigger CI"

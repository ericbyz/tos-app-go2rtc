#!/usr/bin/env python3
"""Generate go2rtc.lang for the TOS App Center (26 locales, English fill)."""
NAME_EN = "go2rtc Stream Hub"
AUTHOR = "ericbyz"
DESC_EN = (
    "Camera streaming hub: turn IP cameras and media sources into RTSP, "
    "low-latency WebRTC and HLS with a single lightweight binary and an "
    "embedded web UI (http://<NAS>:18238). Add streams in the browser and "
    "watch live from anywhere. Packaged unmodified from upstream AlexxIT/go2rtc "
    "(MIT); config in /etc/go2rtc/go2rtc.yaml."
)
NOTE_EN = "1. Repackaged upstream AlexxIT/go2rtc (MIT) unmodified for TOS."
NOTE_ZH = "1. 将上游 AlexxIT/go2rtc(MIT)原样封装为 TOS 应用。"

PRIMARY = [
    ("zh-cn", "go2rtc 摄像头流媒体中枢",
     "把 IP 摄像头/媒体源转成 RTSP、低延迟 WebRTC 和 HLS,单二进制零依赖,内置 Web 管理页"
     "(http://<NAS>:18238)。浏览器里添加 rtsp:// 摄像头即可直播观看、两路对讲、录制回放。"
     "上游二进制原样封装(MIT),配置位于 /etc/go2rtc/go2rtc.yaml,摄像头流在 Web UI 里管理。"),
    ("zh-hk", "go2rtc 攝像頭流媒體中樞",
     "把 IP 攝像頭/媒體源轉成 RTSP、低延遲 WebRTC 和 HLS,單二進制零依賴,內置 Web 管理頁"
     "(http://<NAS>:18238)。瀏覽器裡添加 rtsp:// 攝像頭即可直播觀看、兩路對講、錄製回放。"),
]

ORDER = ["zh-cn", "zh-hk", "en-us", "ko-kr", "ja-jp", "de-de", "fr-fr", "it-it",
         "es-es", "hu-hu", "pl-pl", "tr-tr", "ru-ru", "pt-pt", "cs-cz", "da-dk",
         "nl-nl", "nb-no", "sv-se", "el-gr", "ro-ro", "th-th", "vi-vn", "id-id",
         "ar-sa", "he-il"]

NATIVE = {
    "ja-jp": "IP カメラやメディアソースを RTSP・低遅延 WebRTC・HLS に変換するストリーミング ハブ。単一バイナリで依存なし、Web UI(http://<NAS>:18238)内蔵。上流バイナリを無改修でパッケージ化(MIT)、設定は /etc/go2rtc/go2rtc.yaml。",
    "ko-kr": "IP 카메라/미디어 소스를 RTSP·저지연 WebRTC·HLS로 변환하는 스트리밍 허브: 단일 바이너리, 의존성 없음, Web UI(http://<NAS>:18238) 내장. 업스트림 바이너리 무수정 패키징(MIT), 설정은 /etc/go2rtc/go2rtc.yaml.",
    "de-de": "Streaming-Hub für IP-Kameras und Medienquellen: RTSP, latenzarme WebRTC und HLS aus einem einzigen Binary ohne Abhängigkeiten, mit integriertem Web-UI (http://<NAS>:18238). Upstream unverändert paketiert (MIT), Konfiguration in /etc/go2rtc/go2rtc.yaml.",
    "fr-fr": "Hub de streaming pour caméras IP et sources multimédias : RTSP, WebRTC faible latence et HLS depuis un binaire unique sans dépendance, avec interface web intégrée (http://<NAS>:18238). Amont intact (MIT), configuration dans /etc/go2rtc/go2rtc.yaml.",
    "es-es": "Hub de streaming para cámaras IP y fuentes multimedia: RTSP, WebRTC de baja latencia y HLS desde un único binario sin dependencias, con interfaz web integrada (http://<NAS>:18238). Upstream intacto (MIT), configuración en /etc/go2rtc/go2rtc.yaml.",
    "ru-ru": "Стриминговый хаб для IP-камер и медиаисточников: RTSP, низколатентный WebRTC и HLS из одного бинарника без зависимостей, со встроенным веб-интерфейсом (http://<NAS>:18238). Оригинальные бинарники без изменений (MIT), конфигурация в /etc/go2rtc/go2rtc.yaml.",
}

def main(out_path):
    lines = []
    for loc in ORDER:
        name, desc = NAME_EN, NATIVE.get(loc, DESC_EN)
        for l, n, d in PRIMARY:
            if l == loc:
                name, desc = n, d
                break
        note = NOTE_ZH if loc in ("zh-cn", "zh-hk") else NOTE_EN
        lines += [f"[{loc}]", f'name = "{name}"', f'auth = "{AUTHOR}"',
                  f'descript = "{desc}"', f'note = "{note}"', ""]
    open(out_path, "w", encoding="utf-8", newline="\n").write("\n".join(lines))
    print("wrote", out_path, len(ORDER), "locales")

if __name__ == "__main__":
    main("go2rtc.lang")

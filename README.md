# tos-app-go2rtc

将 [go2rtc](https://github.com/AlexxIT/go2rtc)(摄像头流媒体中枢,MIT)打包为 [铁威马 TOS](https://www.terra-master.com) 应用中心 **deb 类应用**(x86_64 + aarch64 双架构)。

**这是什么**:TOS deb 元数据壳 + 可复现构建脚本。上游单二进制(Web UI 内嵌,Release 资产即二进制,UPSTREAM 锁定 SHA256)原样打包,本仓只产出平台元数据、systemd 单元与配置种子 —— 不修改任何上游代码。

| 项目 | 值 |
|---|---|
| 应用 ID | `go2rtc` |
| 应用形态 | deb 类 · **open_path 外开**(浏览器新标签页) |
| Web UI | `http://<NAS>:18238`(添加/预览摄像头流、两路对讲、录制) |
| 流输出 | RTSP `:18554` / WebRTC+WHEP `:18555`(种子配置固定,可改) |
| 服务 | `go2rtc.service`(专用 `go2rtc` 系统用户) |
| 配置 | `/etc/go2rtc/go2rtc.yaml`(首装种子,升级保留;Web UI 添加的流也写回此文件) |
| 数据 | `/var/lib/go2rtc`(录制/临时文件) |
| 版本 | 1.9.15(见 [UPSTREAM](UPSTREAM) 锁定) |
| 上游许可证 | MIT(全文见 [LICENSE](LICENSE),义务见 [NOTICE](NOTICE);封装层 MIT) |
| 端口登记 | 18238(Web)/ 18554(RTSP)/ 18555(WebRTC) |

## 选型说明(顶替 scrutiny 空位)

scrutiny 0.10 因硬依赖 InfluxDB 2.x 弃用后,摄像头流媒体品类由 go2rtc 顶替:
单二进制 4–6MB、零依赖、内嵌 Web UI,与 MediaMTX(已deb 在架,不同上游允许)同品类不同上游。

## 目录结构

```
tos-app-go2rtc/
├── config.ini                          # TOS 平台元数据(open_path 模式)
├── go2rtc.lang                         # 26 种语言(生成:scripts/make_lang.py)
├── packaging-extras/go2rtc.yaml.default# 配置种子(端口固定)→ /etc/go2rtc/
├── UPSTREAM                            # 版本锁定(二进制 + SHA256)
├── DEBIAN/                             # control + postinst(种子+权限)/prerm/postrm
├── init.d/go2rtc.service               # systemd(加固;-c 指定配置)
├── images/icons/go2rtc.svg             # 原创图标(摄像头 + 流)
├── scripts/                            # fetch/build_deb/unpack_check/validate/make_lang/bump
├── build.sh                            # 一键构建 ./build.sh [x86_64|aarch64]
├── LICENSE                             # 上游 MIT 全文
└── NOTICE                              # 归属与许可义务说明
```

## 本地构建

依赖:bash、curl、python3(任意平台;有 dpkg-deb 时自动优先)。

```bash
./build.sh                # 双架构(下载二进制 → 校验 → 打包 → 解包验证)
./scripts/validate.py     # 元数据校验
```

产物:`build/output/go2rtc_<platform>.deb` + `.sha256`(约 5MB)。

## 上架 Checklist(内部奖励计划 · deb 档 60 元)

1. ☐ 推送本仓 GitHub(ericbyz/tos-app-go2rtc)+ 打 tag `v1.9.15`;
2. ☐ 提交前**刷新查重**(`go2rtc`,2026-11-16 核验空白;MediaMTX 已在架但为不同上游,允许);
3. ☐ x86_64 与 ARM **分别创建应用**(独立 App ID、同一开发者账号);
4. ☐ 提交 Release 直链 + SHA256 + 上游源码仓 + 本仓构建脚本;
5. ☐ VM 实测已完成:Web UI 添加流、预览播放(见 git 记录);
6. ☐ 《参与报名表》勾选 deb 档,附仓库链接;
7. ☐ 30 天内维护 Issues 响应。

## 合规声明

- 上游二进制**原样封装**(MIT),未修改任何上游代码,许可证全文随包分发;
- 安装包内容:上游 Release 二进制 + 本仓元数据,无其他二进制;
- 不收集任何用户数据;配置与录制仅存于 NAS 本地。

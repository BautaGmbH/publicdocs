# Public documentation on BAUTA's blindsensors

## General information

## Manuals
[UF-Series German](manuals/Betriebsanleitung-UF-Serie-BJ2026+.pdf)
[UF-Series English](manuals/Operatingmanual-UF-Serie-BJ2026+.pdf)
[KB-Series German](manuals/Betriebsanleitung-KB-Serie-BJ2026+.pdf) 
[KB-Series English](manuals/Operatingmanual-KB-Serie-BJ2026+.pdf) 

## Documentation on the user frontend software 

## Documentation on the nVidia Jetson based detection system
Here is an illustration on how to connect the Eyepatch system with the nVidia Jetson analysis system. In this illustrated scenario we have a nVidia Jetson ORIN device that has only a single Ethernet port. This means in order to access the nVidia Jetson device while it is connected to the EyePatch system you need an additional USB-Ethernet-Adapter to be able and plug it into your local network. Otherwise you can not access the nVidia Jetson system operating console. In its normal operation mode this USB port is occupied by an USB LTE cellular network modem stick. 

![Connect](assets/connect_devices.png)

The ethernet port of the nVidia Jetson system is pre-configured to be in the same fixed subnet than the EyePatch. Unless you have changed the IP settings of the EyePatch system no further configuration is required. 

Notice after turning on the nVidia Jetson startup sequence takes a while before the detection process is started and therefore it connects to the EyePatch systems as it first does some internal housekeeping tasks, e.g. checking for new software updates and sending off reports. Usually this is done via the LTE cellular network modem stick, which mean it can take up to 10 minutes (if no carrier signal can be found). However the nVidia Jetson web console can be accessed already roughly 30 seconds after switching on.

To access the web console you need to know which IP the device has been assigned to then use your favourite web browser on a device that is in the same subnet as the Jetson device, and go to:

```
http://IP_OF_JETSON_DEVICE:8080 
```

You should see a screen like this

![Jetson webconsole](assets/jetson_web_console_screenshot.png)
# 关于 BAUTA 盲传感器的公开文档   

## 一般信息

一般 GDPR 规则
CCTV 最常见的合法依据是 合法利益，通常用于安全或财产保护，但仍需要进行 比例性评估，并且如果监控是大规模、系统性的，或结合了额外的分析（例如人脸识别或行为分析），通常还需要进行 DPIA（数据保护影响评估）。

你必须通过 清晰可见的标示 告知公众，并提供更详细的通知内容，包括：控制者信息、目的、法律依据、保存期限、接收方、安全措施以及投诉权利。

影像资料只能在必要的时间内保存，GDPR 并未设定统一的保存期限；通常由各国法规或监管机构的指导来决定。

对于智能摄像头，如果系统不仅是被动录制，而是进行 生物识别、自动画像分析或行为检测，风险等级会更高，因为这些功能可能触发更严格的 GDPR 要求，并且在某些国家法律下可能需要额外限制或事前授权。

成员国差异
GDPR 在整个欧盟直接适用，但成员国仍通过国家法律来影响摄像头的使用，尤其是在 公共空间、工作场所、保存期限、标示要求，以及某些“智能”功能是否需要额外批准等方面。

### Blindsensor 启动序列 

设备通电后大约需要 60 秒才能完全启动并开始发送图像。
确认 Blindsensor 正在运行并发送帧数据
在 Windows 8.1/10/11 上请下载该压缩包：

```
Blindsensor_status_check.zip
```
使用标准以太网跳线将您的 Windows 电脑连接到 Blindsensor。

在您的 Windows 电脑上任意位置解压该压缩包，例如桌面。

首先运行批处理脚本：

```
setup_ethernetconfig_to_connect_to_blindsensor.bat 
```
通过双击来运行它（可能会请求权限，请允许）。该脚本会将您的以太网适配器配置到与 Blindsensor 相同的私有本地网络中。

现在打开您喜欢的网页浏览器，并访问以下地址:
```
http://10.0.0.15:8080 
```
这将打开 EyePatch 远程网页控制台。有关该网页控制台的更多信息，请参阅下方对应的章节。

## 手册

[UF-Series German](manuals/Betriebsanleitung-UF-Serie-BJ2026+.pdf)
[UF-Series English](manuals/Operatingmanual-UF-Serie-BJ2026+.pdf)
[KB-Series German](manuals/Betriebsanleitung-KB-Serie-BJ2026+.pdf) 
[KB-Series English](manuals/Operatingmanual-KB-Serie-BJ2026+.pdf) 


## 用户前端软件文档

![Mainpage](assets/eyepatch_console_mainscreen.png)
开始页面
![Mainpage explain](assets/eyepatch_console_mainscreen_exp.png)
🟩 菜单栏 
更改设置
实时画面当前帧
重启机器

🟦 导入系统设置

🟨 系统状态

## 基于 nVidia Jetson 的检测系统文档

这是一个示例，说明如何将 EyePatch 系统 与 NVIDIA Jetson 分析系统连接起来。
在此示例场景中，我们使用的是一台 NVIDIA Jetson ORIN 设备，它只有 一个以太网端口。
这意味着：当 Jetson 设备连接到 EyePatch 系统时，如果你仍然需要访问 Jetson 的操作控制台，就必须额外使用 USB‑以太网适配器 将其接入你的本地网络。否则，你将无法访问 NVIDIA Jetson 系统的操作界面。

在正常运行模式下，这个 USB 端口通常被 USB LTE 蜂窝网络调制解调器占用。

![Connect](assets/connect_devices.png)

nVidia Jetson 系统的以太网端口已预先配置为与 EyePatch 处于同一个固定子网。  
只要你没有更改 EyePatch 系统的 IP 设置，就不需要进行任何额外的网络配置。

请注意：在开启 nVidia Jetson 后，它的启动流程需要一段时间，只有在完成内部的初始化任务后才会开始检测流程并连接到 EyePatch 系统。
这些内部任务包括：检查是否有新的软件更新、发送系统报告等。通常这些操作是通过 USB LTE 蜂窝网络调制解调器完成的。如果无法找到运营商信号，这些步骤可能会持续 最长约 10 分钟。

然而，nVidia Jetson 的 Web 控制台通常在开机约 30 秒后就可以访问，无需等待上述后台任务完成。

# Linux下 iwd无线连接

> 摘自wiki
> date：2022-03-19

iwd：iNet wireless daemon, iNet无线守护程序。特点是不依赖任何外部库。

```bash
sudo systemctl enable --now iwd.service     #后台守护
iwctl        # 进入交互式提示符
[iwd]        # help #帮助
device list    # 列出无线网卡
station wlan0 scan    # 扫描网络
station  wlan0 get-networks    # 列出可用网络
station wlan0 connect SSID     # 连接并输入密码

station wlan0 disconnect    # 断开连接
known-networks list         # 列出以前连接过的网络
known-networks SSID forget  # 忘掉已知的某一网络
```

也就这样了，CLI永远是根本。

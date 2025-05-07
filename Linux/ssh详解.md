# Linux下ssh详解

date：2022-03-25
---

## 1. 安装

openssh
软件是C/S结构，注意查看/etc/ssh/下至少有ssh_config和sshd_config两个配置文件
本地端和远程端同样要求。

## 2. 配置

远程端：

```bash
vim /etc/ssh/sshd_config
    PermitRootLogin yes
    PasswordAuthentication yes
systemctl enable --now sshd.service     #部分发行版是ssh.service
```

本地端：

```bash
ssh root@192.168.0.53
```

这种方式有安全隐患，只要密码泄露，任何人都可以登录你的远程主机

## 3. 无密码登录

创建ssh密钥

```bash
ssh-keygen -t ed25519 -f .ssh/lan   #-t加密类型 -f密钥文件名和位置，会生成一个lan私钥和lan.pub
ssh-copy-id -i .ssh/lan.pub root@ipAddress  #前提是可以密码登录远程主机
#-------登录远程主机，并配置
ssh root@ipAddress
vim /etc/ssh/sshd_config
    PasswordAuthentication no
systemctl restart sshd.service && echo "OK"
exit
#---无密码登录
ssh -i .ssh/lan root@ipAddress
```

这样既方便又安全，只要保护好你的私钥即可
<mark>END</mark>

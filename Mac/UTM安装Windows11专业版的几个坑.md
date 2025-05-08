# UTM安装Windows11专业版的几个坑

Date: 2023/05/23

---

## 1. UTM从哪里下载

两个选择：App Store 和 [UTM官网](https://mac.getutm.app/)

异同：收费和免费 🆚 功能相同

## 2. Windows11从哪里下载

### 2.1 https://uupdump.net/

首先你要有一颗以折腾为乐趣的心，和一双巧手，反正我没成功，原因懂得都懂。

### 2.2 https://next.itellyou.cn/

简单一句话：小白乐园，目前国内最好的去处。

啰嗦一句，要选arm64版的下载哦，X86平台不是不行而是异常酸爽。

## 3. 安装过程中的两个坑

### 3.1 绕过TPM

当你被警告配置过低，不能进行安装时，快捷键：

`Fn+Shift+F10` 或 `Shift+F10` 调出cmd命令行输入：`regedit`

打开注册表编辑器展开：

- HKEY_LOCAL_MACHINE\SYSTEM\Setup

- 右击新建项，命名LabConfig

- 右侧新建两个DWORD(32位)值，分别命名BypassTPMCheck和BypassSecureBootCheck; 并且把值都设为1

- 关闭注册表返回上一步进行常规安装

### 3.2 绕过联网bug

安装进入设置阶段后会卡在联网阶段，同上一步一样调出cmd命令行：

`OOBE\BYPASSNRO`

回车后自动重启再开始设置，进行常规设置

## 4. 驱动

提前下载好驱动镜像：spice-guest-tools-xxx.iso

进入系统后发现没网络，缺很多驱动。把镜像插入虚拟光驱，双击运行spice-guest-tools-xxx即可

## 5. Windows11激活

- 每个命令之后略等片刻，等对话框弹出，直接回车，再执行下一条命令

- 关键点1: 密钥

- 关键点2: 激活服务器

<mark>注意</mark>：同一个密钥在不同服务器上的表现完全不同！

```cmd
slmgr /upk
slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX
slmgr /skms kms.0t.net.cn
slmgr /ato
```

END.

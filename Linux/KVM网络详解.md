# KVM网桥详解

Date：2024.09.18

[Network bridge - ArchWiki](https://wiki.archlinux.org/title/Network_bridge)

网桥是一种虚拟网络设备，用于在两个或多个网段之间转发数据包。网桥的行为类似于虚拟网络交换机，并且以透明方式工作。网络中的其他计算机不需要知道它的存在。物理网络设备（例如 `eth1`）和虚拟网络设备（例如 `tap0`）可以连接到它。

有多种方式管理网桥……

---

## 1. With iproute2

```bash
# 创建一个新的网桥并将起状态更改为up
ip link add name bridge-name type bridge
ip link set dev bridge-name up 

# 将接口添加到桥接器中
ip link set eth1 up
ip link set eth1 master bridge-name

# 显示现有的网桥和关联的接口
bridge link

# 删除方法
ip link set eth1 nomaster
ip link set eth1 down
ip link delete bridge-name type bridge           
```

## 2. With bridge-utils

brctl即将弃用，并被视为过时

```bash
brctl addbr bridge-name
brctl addif bridge-name eth1
ip link set dev bridge-name up

# 显示当前网桥及接口
brctl show

# 删除
ip link set dev bridge-name down
brctl delbr bridge-name
```

## 3. 分配IP地址

当网桥设置好后**可以**为其分配一个IP地址

`ip address add dev bridge-name 192.168.66.66/24`

## 4. 网桥上的无线接口

[Debian](https://wiki.debian.org/BridgeNetworkConnections#Bridging_with_a_wireless_NIC)

要将无线接口添加到网桥，首先必须将无线接口分配给接入点或使用hostapd启动接入点。

就像您可以桥接两个有线以太网接口一样，您可以在以太网接口和无线接口之间桥接。但是，大多数接入点 （AP） 将拒绝源地址未向 AP 进行身份验证的帧。由于 Linux 以透明方式进行以太网桥接（不修改传出或传入帧），因此我们必须使用名为 [ebtables](https://packages.debian.org/ebtables "DebianPkg") 的程序设置一些规则来执行此操作。

ebtables 本质上与 [iptables](https://packages.debian.org/iptables "DebianPkg") 类似，不同之处在于它在 OSI 模型的数据链路层的 MAC 子层上运行，而不是在网络层上运行。在我们的例子中，这允许更改我们所有帧的源 MAC 地址。这很方便，因为我们会欺骗 AP，让他们认为我们所有的转发帧都来自向 AP 进行身份验证的计算机。

无线接口配置过于复杂且无迫切必要，略过。

<mark>END</mark>

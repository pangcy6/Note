# QEMU/KVM在archlinux下的虚拟化环境的搭建与应用

---

## 0. 背景知识

QEMU/KVM是目前最流行的虚拟化技术，它给予Linux内核提供的kvm模块，结构精简，性能损失小，而且开源免费。

但KVM作为一个企业级的底层虚拟化技术，却没有对桌面使用者做深入优化，因此如果想把它当成桌面虚拟化软件来使用，替代Virtualbox/VMWare，有一定的难度。

## 1. 安装

QEMU/KVM环境需要安装很多的组件，它们各司其职：

1. qemu：模拟各类输入输出设备（网卡、磁盘、USB端口等）
   
   - qemu底层使用kvm模拟CPU和RAM，比软件模拟的方式快很多。

2. libirt：提供简单且统一的工具和API，用于管理虚拟机，屏蔽了底层的复杂结构

3. ovmf：为虚拟机启用UEFI支持

4. virt-manager：用于管理虚拟机的GUI界面

5. virt-viewer：通过GUI界面直接与虚拟机交互

6. dnsmasq vde2 bridge-utile openbsd-netcat：网络相关组件，提供了以太网虚拟化、网络桥接、NAT网络等虚拟网络功能
    
    - dnsmasq：提供了NAT虚拟网络的DHCP和DNS解析功能
    - vde2：以太网虚拟化
    - bridge-utils：提供网络桥接相关的工具
    - openbsd-netcat：TCP/IP的瑞士军刀，不太清楚是哪个网络组件会用到它。

```bash
sudo pacman -S qemu qemu-arch-extra virt-manager virt-viewer dnsmasq vde2 bridge-utils openbsd-netcat libguestfs
```
## 2. 启动QEMU/KVM

```bash
sudo systemctl enable libvirtd
sudo systemctl start libvirtd
```
## 3. 让非root用户能正常使用KVM
sudo vim /etc/libvirt/libvirtd.conf,将以下几行取消注释
---
```bash
unix_sock_group = "libvirt"
unix_sock_ro_perms = "0777"
unix_sock_rw_perms = "0770"
```
加入libvirt组：`sudo usermod -aG libvirt $(whoami)`
然后重启libvirtd服务：`sudo systemctl restart libvirtd`，就可以正常使用了

## 4. 虚拟机磁盘映像管理

```bash
qemu-img create -f qcow2 -o Manjaro.qcow2 64G   #创建一个64G大小的磁盘映像
qemu-img resize Manjaro.qcow2 128G              #将上一步建立的磁盘扩容到128G大小，注意关机才可以
qemu-img resize --shrink Manjaro.qcow2 32G      #关机缩小磁盘大小，注意缩容很容易丢失数据，一般不用
qemu-img info Manjaro.qcow2                     #显示特定映像的详细信息
qemu-img convert -f raw -O qcow2 vm01.img vm01.qcow2    #raw ==> qcow2
qemu-img convert -f qcow2 -O raw vm01.qcow2 vm01.img
qemu-img convert -p -f vmdk -O qcow2 Metasploitable2.vmdk Metasploitable2.qcow2     #将vmware磁盘映像转换
```
直接转换vmdk文件得到的qcow2镜像，启动会报错，比如“磁盘无法挂载”。需要在网上下载安装MergelDE.zip组件，另外启动虚拟机之前，需要将硬盘类型改为IDE，才能解决这个问题。

## 5. 虚拟机管理
主要有两种方式：virsh/virt-install和virt-manager方式，第二种方式图形界面，慢慢摸索即可。下面主要简述第一种方式
先明白两个libvirt转换的两个概念：
1. Domain：指运行在虚拟机器上的操作系统的实例。一个虚拟机，或用于启动虚拟机的配置
2. Guest OS：运行在Domain中的虚拟操作系统

5.1设置默认URI`echo 'export LIBVIRT_DEFAULT_URI="qemu:///system"' >> ~/.zshrc`

5.2虚拟机网络：
```bash
sudo virsh net-list --all   #列出所有虚拟机网络
virsh net-start default     #启动默认网络
virsh net-autostart --network default   #将default网络设置为自启动
sudo virsh net-list --all   #再次检查网络状况
```

5.3创建虚拟机--virt-install
```bash
#使用iso镜像创建全新的proxmox虚拟机，自动创建一个60G的磁盘
virt-install \
    --virt-type kvm \
    --name ubuntu \
    --vcpus 4 --memory 8096 \
    --disk size=60 \
    --network network=default,model=virtio \
    --os-type linux \
    --os-variant generic \
    --graphics vnc \
    --cdrom ubuntu.iso

# 使用已存在的opensuse磁盘创建虚拟机
virt-install --virt-type kvm \
    --name opensuse15-2 \
    --vcpus 2 --memory 2048 \
    --disk opensuse15.2-openstack.qcow2,device=disk,bus=virtio \
    --disk seed.iso,device=cdrom \
    --os-type linux \
    --os-variant opensuse15.2 \
    --network network=default,model=virtio \
    --graphics vnc \
    --import
```
其中的--os-variant 用于设定OS相关的优化配置，官方文档强烈推荐设定。可选参数通过`osinfo-query os`查看

5.4虚拟机管理--virsh
```bash
virsh list      #查看正在运行的虚拟机
virsh list --all    #查看所有虚拟机，包括inactive的虚拟机
virt-viewer 8    #使用虚拟机id连接，vnc协议
virt-viewer --wait opensuse15   #使用名称连接，并等待虚拟机启动
virsh start opensuse15
virsh suspend opensuse15
virsh resume ipensuse15
virsh reboot opensuse15
virsh shutdown opensuse15
virsh destroy opensuse15    #强制关机
virsh autostart opensuse15
virsh autostart --disable opensuse15
virsh snapshot-list --domain opensuse15
virsh snapshot-create <domain>
virsh snapshot-restore <domain> <snapshotname>
virsh snapshot-delete <domain> <snapshotname>
virsh undefine opensuse15   #删除虚拟机
virsh setvcpus opensuse15 4
virsh setmem opensuse15 4096
#添加新设备
virsh attach-device
virsh attach-disk
virsh attach-interface
#删除设备
virsh detach-disk
virsh detach-device
virsh detach-interface
```



安装完必要的软件后

```bash
sudo brctl addbr br0    #创建一个桥接接口，名字叫br0
brctl show              #显示系统上所有的桥接接口
sudo brctl addif br0 en*    #将物理网卡替换成自己的网络接口名称，把网卡加入到桥接中

#下面几步删除物理网卡接口的ip地址，把物理网卡接口的IP地址配置到桥接接口上，病开启桥接接口，然后添加默认网关
sudo ip addr del dev en* 192.168.0.173/24   #使用ip a查看原来物理网卡的IP地址，删除网卡IP地址
sudo ip addr add 192.168.0.173/24 dev br0   #将IP地址配置到桥接接口
sudo ip link set up br0                     #激活桥接接口
sudo route add default gw 192.168.0.1       #设置网关
#这时就可以在virt-manager中设置桥接了

#恢复原来的状态
sudo ip link set br0 down
sudo brctl delif br0 en*
sudo ip link set en* down
sudo ip link set en* up
#然后删除virt-manager中的设置即可
```

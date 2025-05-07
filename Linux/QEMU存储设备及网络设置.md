# QEMU/KVM磁盘镜像及网络设置

---

## 1 磁盘镜像：qemu-img

支持的格式：`qemu-img -h` 显示

- raw——默认全占实际磁盘，可以dd创建

- qcow2——推荐，支持稀疏文件，支持AES加密、快照

- vda——virtualbox

- vmdk——vmware

- vpc——Microsoft

命令格式：`qemu-img [command] [-o options]`

command:

- check: 查找镜像文件中的错误

- create [-f fmt] [-o option] filename [size]
  
  - -b指定backingFile（镜像文件只记录与backingFile差异的部分）测试用非常好
  
  - `qemu-img create -f qcow2 -b test0.qcow2 test1.qcow2`——test0.qcow2已经存在，此时就可以用test1启动test0的镜像，并且改变只写入test1
  
  - 上述与选项commit [-f fmt] filename配合使用提交内容到backingFile——`qemu-img commit test1.qcow2`，此时改变才会写进test0
  
  - 可以创建多个镜像指向test0.qcow2

- convert [-c] [-f fmt] [-O output_fmt] [-o option] filename outputfilename
  
  - -c: 压缩
  
  - -f: 源文件格式
  
  - -O：输出文件格式
  
  - `qemu-img convert -O qcow2 source.vmdk target.qcow2` 

- info filename: 显示镜像文件信息

- snapshot[-l | -a snapshot| -c snapshot| -d snapshot] filename
  
  - -l: 列出所有快照
  
  - -c：创建一个快照`qemu-img snapshot -c test0_snap1 test0.qcow2`
  
  - -a：使用一个快照`qemu-img snapshot -a test0_snap1 test0.qcow2`
  
  - -d：删除一个快照

- resize filename [+|-]size——增减大小（注意qcow2不支持减少空间）`qemu-img resize test0.qcow2 +5G` 注意进入虚拟机后需要fdisk配置后才能使用新增的硬盘

## 2 网络配置

三种网络配置模式：

- 桥接——将虚拟机的网卡桥接到宿主机的物理网卡。同处一个网段，直接与外网通信

- NAT——虚拟机通过宿主机的NAT功能，转发数据包。

- 仅主机模式——极少用到，忽略。

![](E:\Documents\md\media\2023-05-09-18-18-44-image.png)

### 2.1 桥接（CentOS下举例）

管理工具：bridge-utils tunctl

```bash
lsmod | grep tun    #检查tun模块是否加载
modeprobd tun    #加载tun模块 
vim /etc/sysconfig/network-scripts/ifcfg-br0
---
DEVICE=br0
TYPE=Bridge
BOOTPROTO=static
IPADDR=192.168.0.198
PREFIX=24
GATEWAY=192.168.0.1
DNS=114.114.114.114
ONBOOT=yes

# 还需要更改原来网卡的配置文件
vim /etc/sysconfig/network-scripts/ifcfg-ens33
---
#将如下几行注释掉
#IPADDR=192.168.0.198
#PREFIX=24
#GATEWAY=192.168.0.1
#DNS=114.114.114.114
BRIDGE=br0


systemctl restart network    #重启网络
brctl show    #检查网络状况

vim /etc/qemu-ifup    #创建脚本
---
#!/bin/bash
ip link set $1 up
brctl addif br0 $1    #$1虚拟网卡名称变量


qemu-kvm -m 2048 -net nic -net tap,script=/etc/qemu-ifup test0.cow2 -vnc 0.0.0.0:0

brctl show
```

### 2.2 NAT

 宿主机安装DHCP软件：dnsmasq

## 3 libvirt和virt-manager的应用

libvirt是应用最广泛的kvm系统管理工具的应用程序接口

virt-manager--Edit--Connection Details--Virtual Networks默认网络连接，可以开关。

新建一个桥接：同上界面

Netwrok Interface: 右侧底部点击“+”号，前进：Name br0, Interface 自己的网卡--Configure：IPV4 Mode Static，Address :192.168.0.58, Gateway: 192.168.0.1 OK FINISH 记得启动

## 4 virsh的应用

virsh包含在libvirt软件包中，是管理虚拟化系统和虚拟机的命令行工具。

两种运行模式：

- 交互模式：直接virsh回车，再输入命令，得到结果，quit退出

- 非交互模式：直接在命令行输入hypervisor名称，在后面接要执行的命令。

virsh常用命令：

- list：列出正在运行的虚拟机

- list --all：列出所有虚拟机

- start xxx：启动虚拟机

- reboot xxx：重启

- reset xxx: 强制重启

- shutdown xxx

- destory <id> :销毁一个虚拟机，拔掉虚拟机的电源

`virsh -c qemu+ssh://192.168.0.198/system` 连接远程虚拟机并进入交互模式。

## 5 virtio的基本概念和应用

kvm系统是基于硬件虚拟化的系统，CPU的运行效率是相当高的，但其他I/O设备是kvm使用qemu纯软件模拟的方式，效率较为低下。为解决这一问题，采用了virtio技术，virtio是一个半虚拟化技术，需要修改Guest OS的源代码。 所以windows系统需要另外安装virtio驱动。

Linux 实现方式：`virsh edit test0`

```bash
find /lib/modules/3.10.0-1160.el7.x86_64/ -name "virtio"
# 查看宿主机是否加载了virtio模块


virsh edit test0
#找到<devices>下的硬盘位置将bus='ide'改成bus='virtio'
#下面一行改成<address type='pci'/>
#找到bridge网卡部分
#<model type='virtio'/>
#OK
```

修改完后运行效率提升明显

不清楚在virt-manager中设置是否生效，以上是命令行模式

**生效！更简单。**

Windows：

在宿主机中安装驱动：virtio-win

会自动生成/usr/share/virtio-win/virtio-win-0.1.171.iso

将iso挂载的虚拟机光驱--将硬盘和网卡设置成virtio--启动会蓝屏--destory id

解决这个小问题：

1. 将Windows虚拟机的引导磁盘改回ide

2. 添加一块virtio磁盘：`qemu-img create -f qcow2 <filepath> <size>`

3. edit xxx, 在配置文件中添加这个新磁盘，并将模式设为virtio

4. 将virt-win.iso挂载到虚拟光驱中

5. 启动系统，在设备管理器里安装磁盘virtio驱动

6. 将引导磁盘改为virtio，正常启动系统

以上是修改一个现存的Windows虚拟机。

新建一个Windows虚拟机：

```bash
virt-install \
--name win7
--vcpus 3 \
--memory 4096 \
--disk /root/kvmlab/img/win7.qcow2,size=20,bus=virtio \
--cdrom /root/kvmlab/iso/windows7.iso \
--network bridge=br0,model=virtio \
--graphics vnc,port=5901,listen=0.0.0.0

#安装程序会找不到磁盘
virsh
virsh# attach-disk win7 /root/kvmlab/iso/virtio-win-0.1.171.iso hda --type cdrom

#回到安装界面，加载驱动，位置在viostor--w7-amd64 
#再次换回安装镜像继续即可 
```

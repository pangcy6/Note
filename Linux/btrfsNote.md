# btrfs详解

## 重要技术特性:

- 支持写时复制COW,保证数据的可靠性
- 更好的扩展性支持,利用动态inode创建,Extent,B-tree实现
- 支持非常大的单个文件与总容量
- 支持文件快速检查功能,基于数据及元数据校验码机制,将数据,元数据的某些属性保存下来,下次读取时可根据这些数学快速检测是否受损,如果损坏还能尝试修复,这样极大的提高数据的准确性
- 支持将多个物理卷组成一个Btrfs文件系统,并内置RAID,支持将数据,元数据以RAID,single,dup等方式在多个物理卷中存储.
- 支持创建多个子卷,子卷可以单独挂载
- 支持透明压缩功能,自动占用CPU资源对传入/出的文件进行压缩/解压
- 支持快照,支持对子卷,文件进行快照,还能对快照进行快照

## 管理命令:

```bash
btrfs subvolume    # 用于管理子卷
btrfs filesystem   # 用于管理文件系统
btrfs balance      # 用于调整数据,元数据存储负载均衡
btrfs device       # 用于管理设备
btrfs rescue       # 用于救援
btrfs quota        # 用于设置磁盘配额
```

## 1.格式化

```bash
mkfs.btrfs [options] Device ...
    # -L 指定卷标
    # -m 指定元数据如何跨设备文件存储,raid0,raid1,raid5,raid6,raid10,single,dup
    # -d 指定数据如何跨设备文件存储,(同上)
    # -f 强制格式化

mkfs.btrfs -f -L myBtrfs /dev/sdb/ /dev/sdc    
```

## 2.调整Btrfs逻辑边界

```bash
# 查看文件系统组成
btrfs filesystem show /data/
# 缩减
btrfs filesystem resize -10G /data/
# 使用全部空间
btrfs filesystem resize max /data/
```

## 3.添加删除物理设备

```bash
# 添加
btrfs device add /dev/sdd /dev/sde /data/
# 删除设备
btrfs device del /dev/sde /data
```

## 4.管理数据,元数据存放磁盘及方式

```bash
# 新添加硬盘后,需要将数据均匀的存放到各个磁盘上
btrfs balance start /data/
# 修改数据的存放方式为RAID5
btrfs balance start -dconvert=raid5 /data/
```

## 5.启用透明压缩机制

```
mount -o remount,compress=lzo /dev/sdb /data/
```

## 6.子卷

```bash
# 创建
btrfs subvolume create /data/log
# 查看子卷的简要信息
btrfs subvolume list /data/
# 详细信息
btrfs subvolume show /data/log/

# 挂载子卷,一般如果挂载父卷则自动挂载所有子卷

# 单独挂载子卷
mount -o subvol=log /dev/sdb /mnt/
```

## 7.快照卷的管理

```bash
# 创建快照
btrfs subvolume snapshot /data/log /data/log_snap
# 查看
btrfs subvolume list /data/
# 删除
btrfs subvolume delete /data/log_snap/

# 快照的快照.(创建快照之前最好将磁盘设为只读挂载)
btrfs subvolume sapshot /data/log_snap/ /data/log_snap_snap
# 文件快照
cp --reflink 1.t 1.t_snap

# 恢复快照卷
btrfs subvolume delete log
mv log_snap log
```

## 8.文件系统转换,回退

```bash
# ext4 --> btrfs
fsck -f /dev/sd3    #检查磁盘是否损坏,剩余空间
btrfs-convert /dev/sde
# 验证
btrfs filesystem show
# 回滚
btrfs-convert -r /dev/sde
```

## 其他说明:

写时复制更新机制（CoW）：复制、更新及替换指针，而非就地更新；
    修改一个文件，不是直接修改源文件，而是将文件先复制一份，对目标新复制的文件进行修改，然后将文件名本来是指向原来的文件空间转而转向新空间

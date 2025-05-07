# systemd笔记

systemd 是 Linux 下的一款系统和服务管理器，兼容 SysV 和 LSB 的启动脚本。systemd 的特性有：支持并行化任务；同时采用 socket 式与 D-Bus总线式激活服务；按需启动守护进程（daemon）；利用 Linux 的 cgroups监视进程；支持快照和系统恢复；维护挂载点；各服务间基于依赖关系进行精密控制。systemd 完全可以替代 Arch 默认的sysvinit启动系统。

## ACPI 电源管理

systemd 能够处理某些电源相关的 ACPI 事件，通过 /etc/systemd/logind.conf 的下列选项配置：

- HandlePowerKey：按下电源键后的动作
- HandleSleepKey：按下挂起键后的动作
- HandleHibernateKey: 按下休眠键后的动作
- HandleLidSwitch：合上笔记本盖后待机
- 动作可以是 ignore, poweroff, reboot, halt, suspend, hibernate 或 kexec.

系统默认设置为:

- HandlePowerKey=poweroff
- HandleSuspendKey=suspend
- HandleHibernateKey=hibernate
- HandleLidSwitch=suspend

## 分析系统状态

输出激活的单元：`systemctl`
以下命令等效：`systemctl list-units`
输出运行失败的单元：`systemctl --failed`
所有可用的单元文件存放在 /usr/lib/systemd/system/ 和 /etc/systemd/system/ 目录（后者优先级更高）。查看所有已安装服务：`systemctl list-unit-files`

## 使用单元

一个单元可以是系统服务（.service）、挂载点（.mount）、sockets（.sockets）。
使用 systemctl 控制单元时，通常需要使用单元文件的全名，包括扩展名（例如 sshd.service）。但是有些单元可以在systemctl中使用简写方式。
如果无扩展名，systemctl 默认把扩展名当作 .service。例如 netcfg 和 netcfg.service 是等价的。
挂载点会自动转化为相应的 .mount 单元。例如 /home 等价于 home.mount。
设备会自动转化为相应的 .device 单元，所以 /dev/sda2 等价于 dev-sda2.device。

立即激活单元：

    # systemctl start <单元>

立即停止单元：

    # systemctl stop <单元>

重启单元：

    # systemctl restart <单元>

命令单元重新读取配置：

    # systemctl reload <单元>

输出单元运行状态：

    $ systemctl status <单元>

检查单元是否配置为自动启动：

    $ systemctl is-enabled <单元>

开机自动激活单元：

    # systemctl enable <单元>

取消开机自动激活单元：

    # systemctl disable <单元>

显示单元的手册页（必须由单元文件提供）：

    # systemctl help <单元>

重新载入 systemd，扫描新的或有变动的单元：

    # systemctl daemon-reload

## 电源管理

如果你正登录在一个本地的systemd-logind用户会话，**且当前没有其它活动的会话**，那么以下命令无需root权限即可执行。否则（例如，当前有另一个用户登录在某个tty），systemd将会自动请求输入root密码。
重启：

    $ systemctl reboot

退出系统并停止电源：

    $ systemctl poweroff

待机：

    $ systemctl suspend

休眠：

    $ systemctl hibernate

混合休眠模式（同时休眠到硬盘并待机）：

    $ systemctl hybrid-sleep

## 日志

自版本 38 起，systemd 提供了自己日志系统（logging system），称为 journal. 使用 systemd
日志，无需额外安装日志服务（syslog）。读取日志的命令：

    # journalctl

## 过滤输出

journalctl可以根据特定字段过滤输出，例如：
显示本次启动后的所有日志：

    # journalctl -b

不过，一般大家更关心的不是本次启动后的日志，而是上次启动时的（例如，刚刚系统崩溃了）。目前还没有这项功能，正在
systemd-devel@lists.freedesktop.org 讨论中。
目前的折中方案是：

    # journalctl --since=today | tac | sed -n '/-- Reboot --/{n;:r;/-- Reboot --/q;p;n;b r}' | tac

以上命令输出本日内的所有启动信息。但要注意，如果日志很多，该命令执行时间会比较漫长。
动态跟踪最新信息：

    # journalctl -f

显示特定程序的所有消息:

    # journalctl /usr/lib/systemd/systemd

显示特定进程的所有消息:

    # journalctl _PID=1

显示指定单元的所有消息：

    # journalctl -u netcfg

## 日志大小限制

如果按上面的操作保留日志的话，默认日志最大限制为所在文件系统容量的 10%，即：如果 /var/log/journal 储存在 50GiB
的根分区中，那么日志最多存储 5GiB 数据。可以修改 /etc/systemd/journald.conf 中的 SystemMaxUse 来指定该最大限制。如限制日志最大 50MiB：

    SystemMaxUse=50M

## 启动过程分析

systemd 提供了一个分析启动过程的工具 —— systemd-analyze。可以用它看看哪些单元拖慢了开机过程，并据此进行优化。安装
python2-dbus、python2-cairo 软件包后该工具才能工作。
查看开机过程在内核/用户空间消耗的时间：

    $ systemd-analyze

小贴士: 如果在 /etc/mkinitcpio.conf 的 HOOKS 数组添加 timestamp，并重新生成启动内存镜像（mkinitcpio -p linux），systemd-analyze
还可以显示处理该启动镜像花费的时间。
按照耗费时间顺序，输出启动每个单元耗费的时间：

    $ systemd-analyze blame

生成类似于 bootchart 的开机过程图表：

    $ systemd-analyze plot > plot.svg

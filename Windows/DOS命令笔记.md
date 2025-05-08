# DOS命令笔记

1. DOS(Disk Operation System)是一类操作系统的名称，它主要包括Shell(command.com), IO接口(io.sys)两个部分。Shell是dos的外壳，负责将用户输入的命令翻译成操作系统能够理解的语言。目前常用的DOS有包括：MS-DOS PC-DOS，FreeDOS，ROM-DOS等。
2. DOS是单用户、单任务的操作系统。
3. DOS的组成：
   - BOOT         引导程序
   - IO.SYS        输入输出处理程序
   - MSDOS.SYS     文件处理程序
   - COMMAND.COM  命令处理程序
4. DOS的启动(读取文件)顺序：
    开机--> IO.SYS -->MSDOS.SYS-->CONFIG.SYS-->COMMAND.COM-->AUTOEXEC.BAT（自动批处理文件）

## 1. 目录操作

### 1.1 cd  （change directory）

显示当前目录名或改变当前目录

cd [/d] [drive:] [path]        进入指定盘符下的目录

cd [..]                                返回到上级目录

cd \                                    返回到当前盘符的根目录

cd                                    显示当前驱动器和目录

使用 /D 命令行开关(MS-DOS中默认为打开)，除了改变驱动器的当前目录之外，还可改变当前驱动器。 
如果扩展命令名被启用，CHDIR 会如下改变:
1.当前的目录字符串会被转换成使用磁盘名上的大小写。
2.CHDIR 命令不把空格当作分隔符，因此有可能将目录名改为一个带有空格但不带有引号的子目录名。例如：
  cd \winnt\profiles\username\programs\start menu
  而在扩展功能停用的情况下，您必须像这样键入命令：
  cd "\winnt\profiles\username\programs\start menu"

### 1.2 deltree (delete tree)

删除一个目录及目录下的所有文件和子目录
deltree [-y] [drive:]path [[drive:] path [,,,]]
-y 开关项，直接执行命令，而不等待确认

### 1.3 dir (directory)

显示目录中的文件和子目录列表

dir [drive:][path][filename]

/a    显示具有指定属性的文件

attibutes    D 目录，R 只读文件， H 隐藏文件，A 准备存档的文件，S 系统文件，- 表示否的前缀

/b    使用空格式（没有标题信息或摘要）

/c    在文件大小中显示千位数分隔符，默认值。/-c停用千位数分隔符

/o    按分类书序列出文件

sortorder    N 按字母顺序，S 从小到大排列，E 按扩展名，D 按日期，G 按组目录优先，- 颠倒顺序前缀

### 1.4 md (make dir)

创建目录，可创建多级目录结构

md [dirve:]path

md \a\b    相当于md \a    cd \a    md \b

### 1.5 path

为可执行文件显示或设置一个搜索路径

path [[drive:]path[;...][;%path%]]

键入path;    清除所欲搜索路径设置并指示cmd.exe只在当前目录中搜索

键入path    显示当前路径

将%path%    包括在新的路径设置会将旧路径附加到新设置

实例：指定三个搜索目录，path c:\user\taxes;b:\user\invest;b:\bin

### 1.6 rd (remove directory)

删除一个目录，在删除目录前，必须先删除他的所有文件和子目录。目录为空。

rd [/s] [/q] [drive:]path

/s     除目录本身外，还讲删除指定目录下的所有子目录和文件，用于删除目录树

/q     安静模式，带/s删除目录树时不要求确认

### 1.7 tree

图形化显示目录结构

tree [drive:] [path] [/f] [/a]

/f    显示在每个目录中的文件名

/a    指定tree使用文本字符代替图形字符显示子目录之间的连线

## 2. 文件操作

### 2.1 attrib

显示或更改文件属性

attrib [options] [drive:] [path] filename [/s [/d]]

- options
  - r 只读属性
  - a 存档文件属性
  - s 系统文件属性
  - h 隐藏文件属性
  - “+” 设置属性
  - “-” 清除属性
- /s  处理当前文件夹及其子文件夹中的匹配文件
- /d  也处理文件夹

例：`attrib -r e:\public\jones\*.* /s` 将jones及其子目录下的文件属性删去只读属性

### 2.2 call

从一个批处理程序中调用另一个批处理程序，而不会引起第一个批处理的中止

call [drive:] [path] filename [batch-parameters]

### 2.3 copy

将一份或多份文件复制到另一个位置；本命令也可用来合并文件

COPY [/D] [/V] [/N] [/Y | /-Y] [/Z] [/A | /B ] source [/A | /B] [+ source [/A | /B] [+ ...]] [destination [/A | /B]]

 source     指定要复制的文件。

 /A        表示一个 ASCII 文本文件。

 /B        表示一个二进位文件。

 /D       允许解密要创建的目标文件

 destination 为新文件指定目录和/或文件名。

 /V       验证新文件写入是否正确。

 /N       复制带有非 8dot3 名称的文件时，

​          尽可能使用短文件名。

 /Y       不使用确认是否要改写现有目标文件的提示。

 /-Y      使用确认是否要改写现有目标文件的提示。

 /Z       用可重新启动模式复制已联网的文件。

例：`copy note.txt letter.doc /a`

### 2.4 del

删除一个或数个文件

DEL [/P] [/F] [/S] [/Q] [/A[[:]attributes]] names

 names     指定一个或数个文件或目录列表。通配符可被用来删除多个文件。如果指定了一个目录，目录中的所有文件都会被删除。

 /P      删除每一个文件之前提示确认。

 /F      强制删除只读文件。

 /S      从所有子目录删除指定文件。

 /Q      安静模式。删除全局通配符时，不要求确认。

 /A      根据属性选择要删除的文件。

 attributes   R 只读文件           S 系统文件

​         H 隐藏文件           A 存档文件

​         \- 表示“否”的前缀

### 2.5 ren (rename)

改变一个或多个文件名，可以改变所有匹配指定文件名的文件名称。不能跨驱动器改变文件名，也不能将文件移到其他目录。要改变子目录命或移到文件，可使用move命令。

ren [drive:] [path] filename1 filename2

### 2.6 replace

替换文件。用源目录中的文件代替目标目录中的同名文件。还可以使用replace在目标目录中加入文件。

EPLACE [drive1:][path1]filename [drive2:][path2] [/P] [/R] [/S] [/W] [/U]

 [drive1:][path1]filename 指定源文件。

 [drive2:][path2]     指定要替换文件的目录。

 /A            把新文件加入目标目录。不能和/S 或 /U 命令行开关搭配使用。

 /P            替换文件或加入源文件之前会先提示您进行确认。

 /R            替换只读文件以及未受保护的文件。

 /S            替换目标目录中所有子目录的文件。不能与 /A 命令选项搭配使用。

 /W            等您插入磁盘以后再运行。

 /U            只会替换或更新比源文件日期早的文件。不能与 /A 命令行开关搭配使用。

例：`replace a:\phones.cli c:\ /s` 

### 2.7 type

显示文本文件内容，只可查看而不能修改

type [drive:] [path] filename

## 3. 功能操作

### 3.1 chcp

显示当前活动字符集的代号，对于支持字符集切换的所有设备，可以改变当前的活动字符集。

chcp [nnn]

### 3.2 cls

清屏

### 3.3 date

显示日期并提示根据需要来修改日期。

date [mm-dd-yy]

### 3.4 mem

显示计算机中已使用和自有的内存量

### 3.5 move

移动文件并重命名文件和目录

move [/y | /-y] [drive:] [path] filename1[,...] destination

### 3.6 shutdown

用法: shutdown [-i | -l | -s | -r | -a] [-f] [-m \\computername] [-t xx] [-c "comment"] [-d up:xx:yy]

   没有参数        显示此消息(与 ? 相同)

​    -i           显示 GUI 界面，必须是第一个选项

​    -l           注销(不能与选项 -m 一起使用)

​    -s           关闭此计算机

​    -r           关闭并重启动此计算机

​    -a           放弃系统关机

​    -m \\computername    远程计算机关机/重启动/放弃

​    -t xx          设置关闭的超时为 xx 秒

​    -c "comment"      关闭注释(最大 127 个字符)

​    -f           强制运行的应用程序关闭而没有警告

​    -d [u][p]:xx:yy     关闭原因代码

​                u 是用户代码

​                p 是一个计划的关闭代码

​                xx 是一个主要原因代码(小于 256 的正整数)

​                yy 是一个次要原因代码(小于 65536 的正整数)

### 3.7 taskkill

结束至少一个进程，可以根据进程id后图形名称来结束进程。

TASKKILL [/S system [/U username [/P [password]]]] { [/FI filter] [/PID processid | /IM imagename] } [/F] [/T]

例如:

  TASKKILL /S system /F /IM notepad.exe /T

  TASKKILL /PID 1230 /PID 1241 /PID 1253 /T

  TASKKILL /F /IM notepad.exe /IM mspaint.exe

  TASKKILL /F /FI "PID ge 1000" /FI "WINDOWTITLE ne untitle*"

  TASKKILL /F /FI "USERNAME eq NT AUTHORITY\SYSTEM" /IM notepad.exe

  TASKKILL /S system /U domain\username /FI "USERNAME ne NT*" /IM *

  TASKKILL /S system /U username /P password /FI "IMAGENAME eq note*"

### 3.8 tasklist

显示应用程序和本地或远程系统上运行的相关任务或进程的列表

TASKLIST [/S system [/U username [/P [password]]]] [/M [module] | /SVC | /V] [/FI filter] [/FO format] [/NH]

## 4. 磁盘操作

### 4.1 chkdsk

检查磁盘状态并显示状态报告；还能修正磁盘错误。

CHKDSK [volume[[path]filename]]] [/F] [/V] [/R] [/X] [/I] [/C] [/L[:size]]

 volume     指定驱动器(后面跟一个冒号)、装入点或卷名。

 filename    仅用于 FAT/FAT32: 指定要检查是否有碎片的文件。指定要用CHKDSK进行碎片检查的一个或一组文件的路径及名称。可用通配符（*和?）指定多个文件。

 /F       修复磁盘上的错误。

 /V       在 FAT/FAT32 上: 显示磁盘上每个文件的完整路径和名称。 在 NTFS 上: 如果有清除消息，将其显示。

 /R       查找不正确的扇区并恢复可读信息(隐含 /F)。

 /L:size    仅用于 NTFS: 将日志文件大小改成指定的 KB 数。如果没有指定大小，则显示当前的大小。

 /X        如果必要，强制卷先卸下。 卷的所有打开的句柄就会无效(隐含 /F)。

 /I        仅用于 NTFS: 对索引项进行强度较小的检查。

 /C        仅用于 NTFS: 跳过文件夹结构的循环检查。

例：chkdsk c:

chkdsk c: > status

### 4.2 ipconfig

显示IP地址、子网掩码、缺省网关

ipconfig /all    显示本机TCP/IP配置的详细信息

ipconfig /release    DHCP哭护短手工释放IP地址

ipconfig /renew    DHCP客户端手工向服务器刷新请求

ipconfig /flushdns    清除本地DNS缓存内容

ipconfig /displaydns    显示本地DNS内容

ipconfig /registerdns    显示客户端手工向服务器进行注册

ipconfig /showclassid    显示网络适配器的DHCP类别信息

ipconfig /setclassid    设置网络适配器的DHCP类别

### 4.3 net

net指令是一个由众多命令作为参数组成的庞大命令集

NET [ ACCOUNTS | COMPUTER | CONFIG | CONTINUE | FILE | GROUP | HELP | HELPMSG | LOCALGROUP | NAME | PAUSE | PRINT | SEND | SESSION | SHARE | START | STATISTICS | STOP | TIME | USE | USER | VIEW ]

net help    显示每个命令的概要

net command /help | net help command    显示某个具体命令的用法

### 4.4 netstat

显示协议统计信息和当前TCP/IP网络连接

netstat -h    显示在线帮助

### 4.5 nslookup

显示可用来诊断域名系统DNS基础结构的信息

### 4.6 pathping

是一个由路由跟踪工具，它将ping和tracert命令的功能和两个工具所不提供的其他信息结合起来。

pathping命令定期将数据包发送到通往最终目标的路径上的每个路由器，然后基于从每个跃点饭后的数据包来计算结构

pathping baidu.com

### 4.7 ping

验证与远程计算机的连接
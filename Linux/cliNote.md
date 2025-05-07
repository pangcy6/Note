# 《The Linux command line》不完全笔记

原文pdf下载地址:
<http://sourceforge.net/projects/linuxcommand/files/TLCL/13.07/TLCL-13.07.pdf/download>

**Graphical user interfaces make easy tasks easy, while command line interfaces make difficult tasks possible.**

## 1 shell是什么

shell --bash/zsh,在虚拟控制台与内核的交互界面.
terminal emulator --gnome-terminal/xterm/rxvt-unicode等终端仿真器,简称终端,在GUI环境下对虚拟控制台的仿真。

启动终端仿真器后如下所示：

`[me@linuxbox ~]$`

含义为：username@machinename workDirectory
    $:非root用户
    #:root用户

退出终端对话：

`[me@linuxbox ~]$ exit`

## 2 导航

类UNIX系统文件系统树形结构

绝对路径：从根目录开始，直到目标目录或文件。
相对路径：从当前工作目录开始到目标目录或文件。

    .   --  当前目录
    ..  --  当前目录的父目录

## 3 Linux系统

一般命令形式：

    command -options arguments
        #option--选项,命令的执行方式
        #argument--参数,命令作用的对象

在类UNIX系统中一个基本的观念是：**一切皆为文件**
这意味着包括Windows观念影响下的设备也是文件.

在Linux中文件后缀名并不决定文件类型和内容，仅仅是方便记忆区分，所以要确定文件类型需要：

    file filename

ASCII--发音"As Key"

自由的含义之一是：Linux没有秘密可言。

/proc 是一个Linux内核维护的虚拟文件系统，它包含的文件是内核的**窥视孔**。该文件是可读的，从中可以看到内核是如何监管计算机的。

/tmp 是供用户存放各类程序创建的临时文件的目录。某些配置使得每次系统重启时都会清空该目录。
**这暗示着在做某些危险,琐碎动作时,可以cd到此目录下.**

/usr/local 由源代码编译好的程序通常放在/usr/local/bin下,测试好的可以被所有用户使用的脚本也要安装在/usr/local/bin下.

$HOME/bin 存放仅能自己使用的脚本.

## 4 操作文件与目录

通配符表格

| 通配符           | 匹配项                   |
|:------------- |:--------------------- |
| *             | 匹配任意多个字符（包括0个和1个）     |
| ?             | 匹配任意单个字符（不包括0个）       |
| [characters]  | 匹配任意一个属于字符集 中的字符      |
| [!characters] | 匹配任意一个不属于字符集中的字符      |
| [[:class:]]   | 匹配任意一个属于指定**字符类**中的字符 |

常用的字符类

| 字符类       | 匹配项                   |
|:--------- |:--------------------- |
| [:alnum:] | 匹配任意一个字母或数字(标点特殊字符除外) |
| [:alpha:] | 匹配任意一个字母(a-z,A-Z)     |
| [:digit:] | 匹配任意一数字               |
| [:lower:] | 匹配任意一个小写字母            |
| [:upper:] | 匹配任意一个大写字母            |

通配符示例

| 模式                     | 匹配项                          |
|:---------------------- |:---------------------------- |
| *                      | 所有文件                         |
| g*                     | 以g开头的任一文件                    |
| b*.txt                 | 以b开头，中间有任意多个字符，并以.txt结尾的任一文件 |
| Data???                | 以Data开头，后面跟3个字符的任一文件         |
| [abc]*                 | 以abc中的任一个开头的任一文件             |
| BACKUP.[0-9][0-9][0-9] | 以BACKUP.    开头，后面紧跟3个数字的任一文件 |
| [[:upper:]]*           | 以大写字母开头的任一文件                 |
| [![:digit:]]           | 不以数字开头的任一文件                  |
| *[[:lower:]123]        | 以小写字母或数字1、2、3中的任一个结尾的任一文件    |

cp命令选项:

| option           | meaing                              |
|:---------------- |:----------------------------------- |
| -a,--archive     | 复制文件和目录及其属性,包括所有权和权限.默认具有操作用户的默认权限. |
| -i,--interactive | 在覆盖一个已经存在的文件前,提示用户进行确认.默认直接覆盖.      |
| -r,--recursive   | 递归复制目录及其内容.注意与-a的异同.                |
| -u,--update      | 只复制目标目录不存在或相对源文件较旧的文件.              |
| -v,--verbose     | 显示复制过程--没啥用.                        |

**强烈建议**:
Linux系统默认用户是明智的,会为自己的行为负责任,不需要系统指指点点!
rm命令会直接删除目标,不提示,不可恢复!
所以:用alias创建rm别名是必须的.

`alias rm='rm -i'`

### 4.6 创建链接
链接分为硬链接和符号链接：

```sh
ln file link    #创建硬链接
ln -s file link    #创建符号链接
```

> 提到硬链接时，可以想象文件是由两部分组成的，即包含文件内容的数据部分和包含文件名的名称部分。创建硬链接时，实际上是创建了额外的名称，这些名称都指向同一数据部分。系统分配了一系列的盘块给所谓的索引节点（inode）,该节点随后一文件名称部分建立关联。因此，每个硬链接都指向包含文件内容的具体索引节点。
> 
> > 文件名是由硬链接创建的,所以一个文件至少有一个硬链接
> > 硬链接被删除时,只是删除了这个链接,文件依然存在.
> > 硬链接不能引用与自身不在一个磁盘分区内的文件.
> > 硬链接不能引用目录

> 符号链接创建了一种特殊类型的文件，它包含了指向目标文件或目录的文本指针。类似于Windows下的快捷方式,但比他早多了.
> 
> > 符号链接与他指向的文件几乎没有区别,符号链接里改变的内容会同步到文件中,反之亦然.
> > 删除符号链接,文件依然存在
> > 如果先删除文件,符号链接依然存在,只是不指向任何文件.称之为坏链接,在cli显示红色,删除即可.

> 符号链接在现代系统中更常用

## 5 命令的使用

type--显示命令的类型

which--显示可执行程序的位置

获取命令帮助:

```sh
command --help
info command
man command
```

apropos--显示合适的帮助文档

```sh
☁  ~  apropos mkfs
jfs_mkfs (8)         - create a JFS formatted partition
mkfs (8)             - build a Linux filesystem
mkfs.bfs (8)         - make an SCO bfs filesystem
mkfs.cramfs (8)      - make compressed ROM file system
mkfs.ext2 (8)        - create an ext2/ext3/ext4 filesystem
mkfs.ext3 (8)        - create an ext2/ext3/ext4 filesystem
mkfs.ext4 (8)        - create an ext2/ext3/ext4 filesystem
mkfs.ext4dev (8)     - create an ext2/ext3/ext4 filesystem
mkfs.fat (8)         - create an MS-DOS filesystem under Linux
mkfs.jfs (8)         - create a JFS formatted partition
mkfs.minix (8)       - make a Minix filesystem
mkfs.msdos (8)       - create an MS-DOS filesystem under Linux
mkfs.ntfs (8)        - create an NTFS file system
mkfs.reiserfs (8)    - The create tool for the Linux ReiserFS filesystem.
mkfs.vfat (8)        - create an MS-DOS filesystem under Linux
mkfs.xfs (8)         - construct an XFS filesystem
☁  ~  man 8 mkfs.fat
```

apropos:发音[,æprә'pәu]，适当的，恰好的

whatis--显示命令简要概述

    whatis moc                                               14-12-02 14:46
    mocp (1)             - Console audio player

其他程序文档一般存放在/usr/share/doc下
其中用gzip压缩的.gz文档,可以用==zless==查看,类似less

## 6 I/O重定向

重定向功能可以改变输出内容发送的**目的地**,也可以改变输入内容的**来源地**.

cat: 合并文件.除接受文件名参数外, 还接受标准输入,用Ctrl-D表示输入结束.
sort: 对文本行排序
uniq: 报告或删除文件中重复的行
wc: 打印文件中的换行符、字和字节的个数
grep: 打印匹配行
head: 输出文件的第一部分的内容
tail：输出文件的最后一部分内容,==选项-f持续监视,直到Ctrl-C停止==
tee: 读取标准输入的数据，并将其内容输出到标准输出和文件中

标准输出：standard output 通常表示为 stdout
标准错误：standard error 通常表示为 stderr
标准输入：standard input 通常表示为 stdin

重定向符号">"--如果文件不存在,则创建并写入;如果存在,则==清空文件重新写入==.
重定向符号">>"--如果文件不存在,则创建并写入;如果存在,则==从文件末尾继续写入==.

用重定向清空文件内容或创建一个新的空文件

    > filename    #与touch效果相似

shell内部文件描述符：

- stdin    0
- stdout    1
- stderr    2  

```sh
ls -l /usr/bin > ls-output.txt
ls -l /bla/blabla 2> ls-error.txt
ls -l /bin/usr 2> /dev/null            #把错误信息丢弃到黑洞文件

# 把标准输出和标准错误输出重定向到一个文件中
ls -l /bin/usr > ls-output.txt 2>&1    #传统方式
ls -l /bin/usr &> ls-output.txt        #现代的,效率更高的方式    
```

标准输入重定向：

```sh
cat < lazy_dog.txt
    The quick brown fox jumped over the lazy dog.
```

管道一般形式：

```sh
command1 | command2
ls -l /usr/bin | less    #实例
ls $HOME /usr/bin | sort | less    #sort按字母顺序排列
ls /bin /usr/bin | sort | uniq | less    #uniq默认删除所有的重复行
ls /usr/bin | tee ls.txt | grep zip    #tee--T--象形。哈哈老外也开始懂得汉字的精髓之一了。
```

grep一般形式

```sh
grep pattern [file...]
grep -i    #忽略大小写
grep -v    #取反
```

##7 透过shell看世界    

###7.1扩展(expansion)

```sh
$ echo *
Desktop Documents ls-output.txt Public Videos
```

echo并没有直接显示\*，Shell会在echo执行前把*扩展成他的代表任意多个字符的含义后，再执行echo.

路径名扩展 pathname expansion:

```sh
echo D*
echo *s
echo [[:upper:]]*
```

算术扩展math expansion：

    $((expresion))

算术扩展只支持整数，可以支持多种运算符号。

| 运算符 | 描述  |
|:--- |:--- |
| +   | 加   |
| -   | 减   |
| *   | 乘   |
| /   | 整除  |
| %   | 取余  |
| **  | 幂   |

嵌套形式：

```sh
$ echo $(($((5**2))*3))
75

#等同于
$ echo $(((5**2)*3))
75

# 花括号扩展brace expansion:
$ echo front-{A,B,C}-back
front-A-back front-B-back front-C-back

$ echo num_{1..4}
num_1 num_2 num_3 num_4

$ echo {Z..A}    # 会逆向输出从Z到A

# 花括号嵌套：
$echo a{A{1,2},B{3,4}}b
aA1b aA2b aB3b aB4b

# 按月份建立目录实例：
$ mkdir -p Pics/{2009..2014}-0{1..9} Pics/{2009..2014}-{10..12}
$ mkdir -p Pics/{{2009..2014}-0{1..9},{2009..2014}-{10..12}}    #效率更高的方式

# 命令替换
$ echo $(ls)
$ ls -l $(which cp)
$ file $(ls /usr/bin | grep zip)
$ ls -l `which cp`        #早期的写法
```

### 7.2 引用(quoting)

用于控制扩展

```sh
$ echo text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER
text /home/me/ls-output.txt a b foo 4 me
# 在双引号中除"$, \, `"外都失去意义
$ echo "text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER"
text ~/*.txt {a,b} foo 4 me
# 使用单引号抑制所有的扩展
$ echo 'text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER'
text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER
```

**随着引用级别的加强，越来越多的扩展被抑制！**

echo -e可以解释转义字符

- \a 响铃
- \b 退格
- \n 换行
- \r 回车
- \t 制表符

## 8 高级键盘技巧

在虚拟控制台可以使用的光标移动技巧（GUI界面难免有冲突）

| 组合键    | 作用                      |
|:------ |:----------------------- |
| Ctrl-A | 光标移到行首                  |
| Ctrl-E | 光标移到行尾                  |
| Ctrl-F | 光标右移一个字符，同右箭头           |
| Ctrl-B | 光标左移一个字符，同左箭头           |
| Alt-F  | 光标右移一个单词                |
| Alt-B  | 光标左移一个单词                |
| Ctrl-L | 清空屏幕，并把光标移动到左上角，同clear. |

文本编辑命令

| 组合键    | 作用                 |
|:------ |:------------------ |
| Ctrl-D | 删除光标处的字符           |
| Ctrl-T | 使光标处的字符和它前面的字符对调位置 |
| Alt-T  | 使光标处的单词和它前面的单词对调位置 |
| Alt-L  | 从光标处到单词尾的字符转换成小写字母 |
| Alt-U  | 从光标处到单词尾的字符转换成大写字母 |

剪切和粘贴命令

| 组合键           | 作用                            |
|:------------- |:----------------------------- |
| Ctrl-K        | 剪切从光标到行尾的文本                   |
| Ctrl-U        | 剪切从光标到行首的文本                   |
| Alt-D         | 剪切从光标到词尾的文本                   |
| Alt-Backspace | 剪切从光标到词头的文本，如果光标在词头，那么剪切前一个单词 |
| Ctrl-Y        | 把killing-ring缓冲区里的内容粘贴到光标位置   |

### 8.2 历史命令

```sh
# 搜索特定历史命令
$ history | grep pacss
  229  pacss traceroute
  243  pacss ssh
  253  pacss stat
  260  pacss gzip
  261  pacss bzip2
  262  pacss rsync
  589  pacss wps
  597  pacss abs
  619  pacss mousepad
# 前面的数字是在历史命令列表中的行数

$ !243    # 重新执行pacss ssh命令

$ !!        #重新执行上一条历史命令
# 如果在需要root权限的情况下,忘了sudo.只要:
$ sudo!!    # 把上一条命令加上sudo执行
```

## 9 权限

UNIX-like系统是多任务(multitasking)多用户(multiuser)系统
Windows系统是多任务,**伪**多用户系统
这就是形成权限概念的根本原因

一个文件包含三类权限:

- owner--属主
- group--群组
- other--其它人(除了上述两类之外的任何人)

每类里又包含三种权限

- r--readable
- w--writeable
- x--execute/search

```sh
☁  ~  id
uid=1000(me) gid=100(users) 组=100(users),10(wheel),14(uucp),24(rfkill),90(network),91(video),92(audio),93(optical),95(storage),98(power),108(vboxusers)
[root@Arch ~]# id
uid=0(root) gid=0(root) 组=0(root),1(bin),2(daemon),3(sys),4(adm),6(disk),10(wheel),19(log)
```

四个重要定义文件

- /etc/passwd--用户信息
- /etc/shadow--密码信息
- /etc/group--组用户信息
- /etc/gshadow--组密码信息

### 9.2 chmod

数字模式助记:

| 数字  | 二进制 | 文件权限 |
|:--- |:--- |:---- |
| 0   | 000 | ---  |
| 1   | 001 | --x  |
| 2   | 010 | -w-  |
| 3   | 011 | -wx  |
| 4   | 100 | r--  |
| 5   | 101 | r-x  |
| 6   | 110 | rw-  |
| 7   | 111 | rwx  |

如果有权限肯定有r权限，所以1,2,3是不合理的存在，实际情况下并不出现。

符号表示法:

| 符号  | 含义    |
|:--- |:----- |
| u   | user  |
| g   | group |
| o   | other |
| a   | all   |

符号表示法操作符:

| 符号  | 含义            |
|:--- |:------------- |
| +   | 添加权限          |
| -   | 去除权限          |
| =   | 指定权限(其他权限全去除) |

实例:

```sh
$ chmod 640 filename
$ chmod u+x g-w o= filename
$ chmod -x filename        #默认全部去掉(添加)权限
```

### 9.3 特殊权限

setuid--当把它应用到一个==可执行程序==时,有效用户ID将从实际用户ID(实际运行该程序的用户)设置成该程序所有者的ID.当普通用户运行一个设置了"setuid root"属性的程序时,该程序将以超级用户的权限运行.很明显,这会带来安全方面的问题,因此设置setuid的程序尽量控制在一个极小的范围内.

setgid--当对一个==目录==设置了setgid时,在该目录下创建的文件将由该目录所在群组所有,而不是由创建者所在群组所有.

sticky--如果对一个==目录==设置了sticky位,那么将阻止用户删除或重命名文件,除非用户是这个目录的所有者、文件的所有者、root用户.

设置语法:

```sh
chmod u+s programm    # 授予程序setuid权限
ls -l programm
-rwsr-xr-x

chmod g+s dir1    # 授予目录setgid权限
ls -l dir1
drwxrwsr-x

chmod +t dir2    # 授予目录sticky位权限
ls -l dir2
drwxrwxrwt
```

### 9.4 chown--改变文件的属主和群组

```sh
# chown owner[:group] file ...
```

## 10 进程

- ps: 显示当前进程的所有情况
- top: 实时显示当前进程的资源使用情况
- jobs: 列出所有当前活动作业的情况
- bg: 设置在后台中进行作业
- fg: 设置在前台进行作业
- kill: 发送信号给某个进程
- killall： 杀死指定名字的进程
- Ctrl-C: 中断一个进程
- Ctrl-Z：暂停一个进程

```sh
$ command &     #在后台运行
[1] 1236
$ jobs        #显示所有的活动作业
[1]+ Running    commmand &
$ fg %1        #把编号为1的进程移到前台
command
$ command    #在前台时按下Ctrl-Z
[1]+ Stopped        command
$fg %1        #继续在前台运行
或者 
$ bg %1        #在后台继续运行
```

kill并不是杀死进程，而是发送一个信号到指定进程，继而依据特定信号做出特定动作。这暗示着进程都在随时侦听着信号（进程间通信）。

kill命令一般形式

```sh
$ kill -[signal] pid...
```

signal:

- 1    挂起
- 2    中断，快捷键Ctrl-C
- 9    强行杀死，从内核终止，进程来不及收拾后续工作，其他手段无效时的无奈之举。
- 15 终止信号，默认信号，进程自行停止
- 18 恢复之前收到STOP信号的进程
- 19 暂停信号，快捷键Ctrl-Z

killall一般形式：

```sh
killall [-u user] [-signal] name...
```

## 11 环境

printenv--打印部分或全部环境变量
set--同时显示shell变量和环境变量
echo $variable--显示某个变量

login shell的启动文件:

| 文件              | 说明                               |
|:--------------- |:-------------------------------- |
| /etc/profile    | 适用于所有用户的全局配置文件                   |
| ~/.bash_profile | 用户个人的启动文件,可扩展或重写/etc/profile中的配置 |
| ~/.bash_login   | 若~/.bash_profile缺失,bash尝试读取此脚本   |
| ~/.profile      | 若上述两脚本均缺失,则尝试读取此脚本               |

non-login shell的启动文件

| 文件               | 说明                               |
|:---------------- |:-------------------------------- |
| /etc/bash.bashrc | 适用于全局所有用户的配置脚本                   |
| ~/.bashrc        | 用户的个人启动文件,可扩展或重写/etc/bash.bashrc |

## 12 vim

学习vim更像是学习乐器、游泳或骑自行车,理论只占极小的一部分,更重要的是实际操作,变成肌肉记忆和条件反射.

例子:把文档中所有的Line替换为line

    :%s/Line/line/g
    :%s/line/Line/g        # 逆向操作

:--进入命令模式
%--确定操作范围.%代表文档全部,"1,$"同样也是从第一行到最后一行;"n,m"代表从第n行到m行
s--指定了具体操作.本例是搜索并替换.
/Line/line--源文本/目标文本
g--global代指全局.意思是每一行里的每一个符合条件的文本;如果没有指明,那只匹配每一行里第一个符合条件的文本.

## 13 定制提示符

```sh
[me@linuxbox ~]$ echo $PS1
[\me@\h \W]\$ 
```

提示符中用到的转义字符

- \a    响铃
- \d    当前日期,如:Mon May 26
- ==\h    本地主机名,不带域名==
- \H    完整的主机名
- \j    当前shell进行的任务个数
- \l    当终端设备名称
- \n    换行符
- \r    回车符
- \s    shell程序的名称
- \t    当前24小时制时间 小时:分钟:秒
- \T    当前12小时制时间
- ==\A    24小时制    小时:分钟==
- ==\u    当前用户名==
- \v    shell版本号
- \w    当前工作目录
- ==\W    当前工作目录最后一部分==
- \\!    当前命令历史编号
- ==\$    在非root用户下输出$,在root用户下输出#==
- \\[    标志一个或多个非打印字符系列的开始,用于移动光标或改变颜色
- \\]    标志着非显示字符序列的结束    

```sh
$ ps1_old=$PS1        #备份提示符
PS1=$ps1_old        #复原提示符
```

**颜色**:

用"\\["和"\\]"封装

文本颜色转义字符|背景颜色字符:

    \033[0;30m    黑色        \033[0;40m
    \033[0;31m    红色        \033[0;41m
    \033[0;32m    绿色        \033[0;42m
    \033[0;33m    棕色        \033[0;43m
    \033[0;34m    蓝色        \033[0;44m
    \033[0;35m    紫色        \033[0;45m
    \033[0;36m    青色        \033[0;46m
    \033[0;37m    淡灰色        \033[0;47m
    \033[1;30m    深灰色
    \033[1;31m    淡红色
    \033[1;32m    淡绿色
    \033[1;33m    黄色
    \033[1;34m    淡蓝色
    \033[1;35m    淡紫色
    \033[1;36m    淡青色
    \033[1;37m    白色

恢复到原来的颜色: \\[\033[0m\\]

**注意**:
文本属性:

    0    正常
    1    粗体
    4    下划线
    5    闪烁(不推荐,一些终端不支持)
    7    斜体

## 14 软件包管理

## 15 存储介质

## 16 网络

主要网络命令:

- ping:    向网络主机发送数据包,测试网络是否连接
- traceroute:    显示数据包到网络主机的路由路径
- netstat:    显示网络连接,路由表,网络接口数据,伪连接,及多点传送成员等信息
- ftp:    文件传输命令
- lftp:    改善后的文件传输命令
- wget:    非交互式网络下载命令
- ssh:    远程系统登录命令 ssh username@target.com
- scp:    secure copy 远程复制文件命令 scp username@target.com:document.txt  .
- sftp:    安全文件传输 sftp username@target.com

## 17 搜索

- locate:通过文件名查找文件,需配合updatedb,安装包为mlocate.
- find:在文件目录系统中查找文件
- xargs:在标准输入中建立,执行命令行
- touch:更改文件的时间日期
- stat:显示文件或文件系统的状态

几个非典型的find命令

```sh
$ find ~ -type f -name "*.jpg" -size +1M | wc -l
840
$ find ~ \( -type f -not -perm 0600 \) -or \( -type d -not -perm 0700 \)
$ find ~ -type f -name  "*.BAK" -delete    #找到家目录下以.BAK结尾的文件并删除.**危险操作**
$ find ~ -type f -name "*.BAK" -exec rm '{}' ';'    #同上一条命令,exec后接shell命令,{}为当前目录";"为命令结束标志.
```

使用-ok交互式操作

```sh
$ find ~ -type f -name "foo*" -ok rm '{}' ';'
< rm ... /home/me/bin/foo > ? n
< rm ... home/me/bin/foo/foo.txt> ? y
```

玩一下:

```sh
# 在/tmp/play下创建100个目录,每个目录下有52个空文件
mkdir -p /tmp/play/dir-{00{1..9},0{10..99},100}
touch /tmp/play/dir-{00{1..9},0{10..99},100}/file-{{A..Z}.txt,{a..z}.txt}

☁  ~  stat cliNote.pdf 
  文件："cliNote.pdf"
  大小：261089        块：512        IO 块：4096   普通文件
设备：808h/2056d    Inode：4588353     硬链接：1
权限：(0644/-rw-r--r--)  Uid：( 1000/    cool)   Gid：(  100/   users)
最近访问：2014-12-10 16:57:15.474016303 +0800
最近更改：2014-12-09 16:20:15.081137176 +0800
最近改动：2014-12-09 16:20:15.081137176 +0800
创建时间：-
☁  ~  
```

## 18 归档和备份

文件压缩程序:

- gzip:压缩和解压缩文件程序
- bzip2:块排序文件压缩程序

文件归档程序:

- tar:磁带归档工具(tape archive的缩写)
- zip:打包和压缩文件

文件同步程序:

- rsync:远程文件和目录同步

**数据压缩是一个移除数据冗余信息的过程!**
压缩算法一般分为:**无损**压缩和**有损**压缩(mp3,jpeg等)

```sh
$ ls -l /etc > etc.txt | gzip etc.txt    #压缩生成etc.txt.gz文件
$ ls -l /etc | gzip > etc.txt.gz        #同上,效率更高
$ gunzip etc.txt    #解压缩etc.txt.gz生成etc.txt文件
$ gzip -d etc.txt    #同上,解压缩
$ gzip -r etc.txt    #递归压缩
```

bzip2速度慢压缩率更高,除-r外gzip~~参数~~选项全支持,专用解压工具bunzip2

==**强制压缩一个已经压缩的文件只能是文件更大!!!**==

zip:

```sh
$ zip options zipfile file1...        #zip调用一般形式
$ zip -r foo.zip some_dir            #递归压缩some_dir目录
$ unzip foo.zip        #解压缩
$ unzip -l foo.zip foo/dir/file        #仅解压提取特定文件
```

rsync:

```sh
$ rsync options source destination    #一般形式
# -a 进行递归归档并保存文件属性
# -v 详细输出
# -delete 删除备份中残存的而源设备中已经不存在的文件,第一次备份时可以不用.
# 一个典型的备份到外部设备的命令,可以设置为alias别名
$ sudo rsync -av -delete /etc /home /usr/local /media/backup
# 一个与远程同步的例子
$ rsync -av -delete rsync://rsync.gtlib.getech.edu/fedora-linux-core fedora-devel
```

## 19 正则表达式--Regular Expression

简单的说:正则表达式是一套符号表示法,用于识别文本模式
通过特定方式，搜索、截取、替换等等方式处理文本
==Regular Expression即“描述某种规则的表达式”之意。--引自维基百科==

```sh
# global regular expression print-->grep
$ grep [options] regex [files...]    #grep一般形式
$ grep root /etc/passwd        #实例
# regex 代表某个正则表达式
# -i 忽略大小写
# -v 非匹配 默认是匹配
# -l 输出匹配文件名而非匹配项本身
# -h 多文件搜索时,抑制文件名输出
$ grep bzip list*.txt    #对列表文件进行搜索包含gzip的文件
list-bin.txt:bzip2
list-bin.txt:bzip2recover
$
```

### 19.2 元字符和文字

正则表达式元字符包括:

    ^ $ . [ ] { } - ? * + ( ) | \
    其它所有字符都是文字字符.    

==注意==:正则表达式元字符在命令行里使用时,要用单引号括起来,以免与shell扩展混淆.

元字符"."用于匹配任意==一个==字符

```sh
$ ls /usr/bin | grep -h '.zip'
bunzip2@
bzip2
bzip2recover
funzip
...
# 并不包括zip,"."元字符将匹配长度增加到了4个字符,而"zip"只有三个字符所以不匹配
```

    元字符"^","$"被正则表达式当作锚,"^"开头;"$"结尾

```sh
$ ls /usr/bin | grep -h '^zip'
$ ls /usr/bin | grep -h 'zip$'
```

中括号表达式和字符类:

```sh
$ ls /usr/bin | grep -h '[bg]zip'    #匹配bzip和gzip
bzip2*
bzip2recover*
gzip*

# 在中括号中第一个字符是"^"时,代表否定,否则失去特殊意义;"-"表示字符范围
$ ls /usr/bin | grep -h '[^bg]zip'    #包含zip字符串但前面既不是b也不是g的程序
bunzip2@
funzip*
gunzip*
hunzip*
hzip*
p7zipForFilemanager*
preunzip*
prezip*
prezip-bin*
unzip*
unzipsfx*

# 查找/usr/bin下以大写字母开头的文件
$ ls /usr/bin | grep '^[A-Z]'
KateDJ*
Magick-config*
Magick++-config*
MagickCore-config*
MagickWand-config*
NetworkManager*
VBox*
VBoxBalloonCtrl@
VBoxHeadless@
VBoxManage@
VBoxSDL@
VBoxTunctl*
VirtualBox@
Wand-config*
X@
Xorg*
Xorg.bin*
Xorg.wrap*
```

### 19.3 POSIX字符类

为了兼容ASCII排序和字典排序的混乱,POSIX推出了统一的字符类

| 字符类        | 描述                               |
|:---------- |:-------------------------------- |
| [:alnum:]  | 字母字符和数字字符;在ASCII中,与[A-Za-z0-9]等效 |
| [:word:]   | 比[:alnum:]只是多了一个下划线_             |
| [:alpha:]  | 字母字符;在ASCII中与[A-Za-z]等效          |
| [:blank:]  | 空格和制表符                           |
| [:cntrl:]  | ASCII控制符                         |
| [:digit:]  | 数字0-9                            |
| [:graph:]  | 可见字符                             |
| [:lower:]  | 小写字母                             |
| [:punct:]  | 标点符号                             |
| [:print:]  | 可打印字符,[:graph:]加上空格              |
| [:space:]  | 空白字符,包括空格、制表符、回车符、换行符、垂直制表符以及换页符 |
| [:upper:]  | 大写字母                             |
| [:xdigit:] | 表示十六进制的字符                        |

实例：

```sh
ls /usr/sbin/[[:upper:]]*    # 列出所有以大写字母开头的文件
```

### 19.4 扩展正则表达式

正则表达式分为:基本正则表达式和扩展正则表达式.
grep -E使用扩展正则表达式.

基本正则表达式只承认如下元字符，==其他元字符需要加上转义字符“\”才具有元字符功效==

    ^ $ [ ] . *

扩展正则表达式除了上述元字符外增加了如下元字符,==加上转义字符后变成普通字符==

    ( ) { } ? + |

---

```sh
# “|”意思是：或
☁  ~  ls /usr/bin | grep -E '^(bz|gz|zip)'    #匹配以bz,gz或zip开头的文件名
grep: warning: GREP_OPTIONS is deprecated; please use an alias or script
bzcat@
bzdiff*
bzgrep*
bzip2*
bzip2recover*
bzmore*
gzexe*
gzip*
zip*
zipcloak*
zipcmp*
zipgrep*
zipinfo*
zipmerge*
zipnote*
zipsplit*
ziptorrent*

☁  ~  ls /usr/bin | grep -E '^bz|gz|zip'        #不带括号匹配的是以bz开头或者是包含gz和zip的文件名
grep: warning: GREP_OPTIONS is deprecated; please use an alias or script
bunzip2@
bzcat@
bzdiff*
bzgrep*
bzip2*
bzip2recover*
bzmore*
funzip*
gunzip*
gzexe*
gzip*
hunzip*
hzip*
p7zipForFilemanager*
preunzip*
prezip*
prezip-bin*
unzip*
unzipsfx*
zip*
zipcloak*
zipcmp*
zipgrep*
zipinfo*
zipmerge*
zipnote*
zipsplit*
ziptorrent*
```

？--匹配某元素==1次==或0次;或者“前面的元素有没有都行”
比如中国大陆固定电话格式为0nnnnnnnnnn或0nn-nnnn-nnnn或0nnn-nnn-nnnn,n为数字。
那么构建正则表达式为：

    ^0[0-9]{10}$ 
    ^0[0-9]{2}[0-9]?-[0-9]{3}[0-9]?-[0-9]{4}$    # 好像多选了哦～～，分两次筛选即可。

*--匹配某元素==多次==或0次
比如选取：以大写字母开始，中间包含若干大小写字母和空格，以.结束的字符串

    [[:upper:]][[:upper:][:lower:] ]*\.

上例分为三个部分：包含[:upper:]的中括号表达式，包含[:upper:][:lower:]和空格的中括号表达式以及修饰它的*，用转移符转义的“.”
其实是定义一个句子的粗糙例子。

+--匹配某元素==多次==或==一次==;也就是说“前面的元素至少出现一次”
比如：

    ^([[:alpha:]]+ ?)+$
    # 以字母开始，若干字母间每次间隔最多一个空格
    # 这个例子值得好好理解！

{}--以指定次数匹配某元素

- {n}:前面的元素恰好出现n此则匹配
- {n,m}:前面的元素出现n次到m次之间则匹配
- {n,}:前面的元素出现超过n次则匹配
- {,m}:前面的元素出现不超过m次则匹配

比如匹配合法手机号:

```sh
$ echo 13801018888 | grep -E '^1[0-9]{10}'
13801018888
$ echo 4839201a |grep -E '^1[0-9]{10}'
$
```

find命令的test选项可以用正则表达式表示

    find pathname --regex '正则表达式'

locate类似

    locate --regex '正则表达式'
    locate --regex '/bin/(bz|gz|zip)'

vim也支持==基本正则表达式==搜索

    /([0-9]\{3\}) [0-9]\{3\}-[0-9]\{4\}
    # 基本正则表达式用扩展元字符“{}”需要转义

## 20 文本处理

sort--排序

```sh
☁  ~  du -s /usr/share/* | head
11844    /usr/share/abiword-3.0
924    /usr/share/aclocal
160    /usr/share/aclocal-1.14
552    /usr/share/alsa
136    /usr/share/appdata
8    /usr/share/application-registry
368    /usr/share/applications
28    /usr/share/apps
1700    /usr/share/autoconf
1100    /usr/share/automake-1.14
☁  ~  du -s /usr/share/* | sort -nr | head
du: 无法读取目录"/usr/share/polkit-1/rules.d": 权限不够
638072    /usr/share/dic
270868    /usr/share/locale
127120    /usr/share/gtk-doc
126016    /usr/share/doc
104888    /usr/share/fonts
76288    /usr/share/icons
75304    /usr/share/man
53888    /usr/share/gimp
43248    /usr/share/gir-1.0
42140    /usr/share/sunpinyin
$
```

重要的文本处理程序sort和awk需要专门学习,这里讲得不透彻.

## 21 格式化输出

## 22 打印

## 23 编译程序

==./configure==--configure程序其实是源代码树下的一个shell脚本，它的任务就是分析生成环境。
最重要的结果就是生成了Makefile,Makefile是指导make命令如何生成可执行程序的配置文件，是make命令能执行的前提。

==make==--作用就是输入了Makefile（该文件描述了生成最后可执行程序时的各部分之间的联系和依赖关系），生成目标文件*.o

==sudo make install==--按照install脚本指引安装最终可执行程序和帮助文档等到系统中，可执行程序一般放置在/usr/loca/bin下。

## 24 编写第一个脚本

==shell脚本就是按照特定规则包含一系列shell命令的文件==。shell读取这个文件，然后执行里面的命令。

```sh
#!/usr/bin/bash
# 保持编程传统第一个脚本hello_world.sh

echo 'Hello World!'
```

"#!"称之为：shebang,读音[ʃi'bæŋ]，翻译：住所

脚本应该放置在~/bin/    (个人) 或 /usr/local/bin/ (全局)
==其他不成熟的脚本可以放置在~/bin/src/下，这样并不在$PATH中，以免出现不可预测的风险==

脚本的注释：

- 位置在被解释语句的上一行，或被解释行后加一个制表符
- 注释不仅是为别人看，也可能是几个月之后的自己
- 升级、调试脚本时，需要关闭的行。在确认新版运行正常时再删除

## 25 启动一个项目

变量命名规则

- 变量名由数字,字母和下划线组成
- 变量名的第一个字符是字母或下划线
- 变量名中不允许空格和标点,驼峰式命名是个好习惯，比如：theShellScript

常量是一个有确定名称和值的特殊变量
普遍的约定

- 常量：~~全部字母大写~~ 首字母大写
- 变量：~~全部字母小写加下划线~~ 驼峰式命名
- 系统变量：全部~~用~~是大写字母

对于shell编程来说常量和变量本质上是一回事

```sh
variable=value    # 变量定义一般格式,注意赋值符两侧不能有空格
b="a strin"    # 变量值带有空格必须使用引号
echo $variable    # 变量引用,或者:echo ${variable}
echo ${b}g        # 当变量名与上下文边界不清晰时必须使用{}
a string
```

### 25.4 here文档

here文档是I/O重定向的一种特殊形式,在脚本中嵌入正文文本,然后将其输入到一个命令的标准输入中.
一般工作方式:

```sh
command << token
text
token    # token必须单独一行,并且末尾没有空格

# 实例
cat << _EOF_    # _EOF_含义是文件结尾,当<<换为<<-时,忽略文本行的Tab缩进
blabla
sometxt
text
...
# 结束_EOF_必须是单独一行,且末尾直接回车.EOF-->end of file
_EOF_
```

默认情况下,here文档内的单引号和双引号都失去在shell中的特殊含义.这样就可以在here文档中随意嵌入引号.
如果将here文档的重定向操作符"<<"改为"<<-",将忽略在here文档开始的Tab字符.这样就能缩进here文档,增加可读性.

```sh
#!/usr/bin/bash

# Script to retrieve a file via ftp

Ftp_server=ftp.nl.debian.org
Ftp_path=/debian/dists/lenny/main/installer-i386/current/images/cdrom
Remote_file=debian-cd_info.tar.gz

ftp -n <<- _EOF_
    open $Ftp_server
    user anonymous me@linuxbox
    cd $Ftp_path
    hash
    get $Remote_file
    bye
    _EOF_
ls -l $Remote_file    
```

## 26 自顶向下的设计--Top-Down Design

在做大型项目时将复杂的庞大的任务,拆分成小的,简单的任务--直到能用一条命令执行
==这种先确定上层步骤，然后逐步细化这些步骤的过程叫做自顶向下的设计==
为了项目的清晰、维护、移植，还要有模块化的设计.

###26.1 shell函数
shell函数两种形式

```sh
function name {
commands
return
}

name () {
commands
return
}
# 函数引用形式
$(name)
```

比如下面的代码实例:

```sh
#!/usr/bin/sh

# Program to output a system information page

# 常量一般设置为大写字母
TITLE="System Information Report for $HOSTNAME"
CURRENT_TIME=$(date +"%x %r %Z")
TIME_STAMP="Generated $CURRENT_TIME, by $USER"

# 函数定义格式之一,其中最少有一条语句
function report_uptime {
    return    # 非必须
}

# 函数定义格式之二,函数定义必须在被调用之前.
report_disk_space () {
    echo $(df -h)
}

report_home_space () {
    return
}

cat << _EOF_
<html>
    <head>
        <title>$TITLE</title>
    </head>

    <body>
        <h1>$TITLE</h1>
        <p>$TIME_STAMP</p>        
        $(report_uptime)    
        $(report_disk_space)
        $(report_home_space)
    </body>
</html>
_EOF_
```

### 26.2 局部变量

全局变量在整个程序期间会一直存在,局部变量仅在定义他的函数内有效,一旦函数结束,他们就不再存在.

局部变量定义形式:

    local foo
    foo=some

局部变量代码实例:

```sh
#!/usr/bin/sh

# 测试局部变量(local variable)和全局变量(global variable)脚本

foo=0    # global variable foo
funct_1 () {
    local foo    # variable foo local to funct_1

    foo=1
    echo "funct_1:foo = $foo"
}

funct_2 () {
    local foo    # variable foo local to funct_2

    foo=2
    echo "funct_2: foo = $foo"
}

echo "global: foo = $foo"
funct_1
echo "global: foo = $foo"
funct_2
echo "global: foo = $foo"
```

运行结果:

```sh
global: foo = 0
funct_1:foo = 1
global: foo = 0
funct_2: foo = 2
global: foo = 0
```

这个特性可以让脚本中的函数相互独立,并且也与脚本本身独立(变量独立)
为代码重用提供了便利.

完整版的sys_info.sh:

```sh
#!/usr/bin/bash

# Program to output a system information page

# 常量一般设置为大写字母
TITLE="System Information Report for $HOSTNAME"
CURRENT_TIME=$(date +"%x %r %Z")
TIME_STAMP="Generated $CURRENT_TIME, by $USER"

# 函数定义格式之一,其中最少有一条语句
function report_uptime () {
    cat <<- _EOF_
        <h2>System Uptime</h2>
        <pre>$(uptime)</pre>
        _EOF_
    return    # 非必须
}

# 函数定义格式之二,函数定义必须在被调用之前.
report_disk_space () {
    cat <<- _EOF_
    <h2>System Disk Space</h2>
    <pre>$(df -h)</pre>
    _EOF_
}

report_home_space () {
    cat <<- _EOF_
        <h2>Home Space Utilization</h2>
        <pre>$(du -sh $HOME)</pre>
        _EOF_
    return
}

cat <<- _EOF_
        <!DOCTYPE HTML>
        <html>
            <head>
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
                <title>$TITLE</title>
            </head>

            <body>
                <h1>$TITLE</h1>
                <p>$TIME_STAMP</p>        
                $(report_uptime)    
                $(report_disk_space)
                $(report_home_space)
            </body>
        </html>
        _EOF_        
```

### Summing up

自顶向下构建步骤，在细化步骤时考虑有无必要构建shell函数，在构建函数时注意使用局部变量。

## 27 流控制 if语句

if语句一般格式

```sh
if commands; then
    commands
elif commands; then
    commands
...    
else
    commands
fi    
```

### 27.2 退出状态

在shell中命令退出状态成功为**0**,失败为**非0**.
可以用: echo $?
查看上一条命令的退出状况
==if语句真正的作用是评估命令的成功或失败==

### 27.3 使用test命令

经常和if一起使用的是test命令,两种基本形式:

```sh
test expresion    #一般形式
[ expresion ]    #更流行的形式
```

测试文件的表达式

| 表达式             | 成为true的条件                    |
|:--------------- |:---------------------------- |
| file1 -ef file2 | 两个文件是硬链接                     |
| file1 -nt file2 | file1比file2新                 |
| file1 -ot file2 | file1比file2旧                 |
| -b file         | 文件存在并且是块(设备)文件               |
| -c file         | file存在并且是字符(设备)文件            |
| -d file         | file存在并且是目录                  |
| -e file         | file存在                       |
| -f file         | file存在且是普通文件                 |
| -g file         | file存在且分配了组ID                |
| -G file         | file存在且属于有效组ID               |
| -k file         | file存在且具有“粘滞位（sticky bit）”属性 |
| -L file         | file存在且是一个符号链接               |
| -O file         | file存在且属于一个有效用户ID            |
| -p file         | file存在且是一个命名管道               |
| -r file         | file存在且有效用户可读                |
| -s file         | file存在且长度大于0                 |
| -u file         | file存在且设置了setuid属性           |
| -w file         | file存在且可写                    |
| -x file         | file存在且可执行                   |

文件测试实例:

```sh
#!/usr/bin/sh

#文件状态测试

FILE=~/.bashrc

if [ -e "$FILE" ]; then        # 尽管""不是必须,但加上可以避免参数为空是的错误
    if [ -f "$FILE" ]; then
        echo "$FILE is a regular file."
    fi
    if [ -d "$FILE" ]; then
        echo "$FILE is a directory."
    fi
    if [ -r "$FILE" ]; then
        echo "$FILE is readable."
    fi
    if [ -w "$FILE" ]; then
        echo "$FILE is writable."
    fi
    if [ -x "$FILE" ]; then
        echo "$FILE is executable/searchable."
    fi    
else
    echo "$FILE does not exist."
    exit 1
fi

exit
```

将上述脚本封装成函数形式,以备移植,更为了结构清晰.

```sh

test-file () {
    # Evaluate the status of a file

    local File    # 不要忘了设置局部变量
    $File=~/.bashrc

    if [ -e "$File" ]; then
        if [ -f "$File" ]; then
            echo "$File is a regular file."
        fi    
        if [ -d "$File" ]; then
            echo "$File is a directory."
        fi    
        if [ -r "$File" ]; then
            echo "$File is readable."
        fi    
        if [ -w "$File" ]; then
            echo "$File is writable."
        fi    
        if [ -x "$File" ]; then
            echo "$File is executable/serachable."
        fi    
    else
        echo "$File is not exist."
        return 1
    fi
}
```

#### 27.3.2 字符串表达式

测试字符串表达式

| 表达式              | 成为true的条件                                |
|:---------------- |:---------------------------------------- |
| string           | string不为空                                |
| -n string        | string的长度大于0                             |
| -z string        | string的长度等于0                             |
| string1==string2 | string1和string2相等,同string1=string2但用得比较少 |
| sring1!=string2  | string1和string2不相等                       |
| string1>string2  | 排序时string2在前(默认排序从小到大)                   |
| string1<string2  | 排序时string1在前                             |

==警告!!!==
==在使用test命令时,"<"">"必须要引号（或\\转义）! 否则会被识别为重定向从而造成潜在的破坏性后果！==

#### 27.3.3 整数表达式

整数判断操作:

| 表达式                   | 成为true的条件         |
|:--------------------- |:----------------- |
| integer1 -eq integer2 | -eq equal相等       |
| integer1 -nq integer2 | -nq not equal     |
| integer1 -le integer2 | -le less equal    |
| integer1 -lt integer2 | -lt less than     |
| integer1 -ge integer2 | -ge greater equal |
| integer1 -gt integer2 | -gt greater than  |

脚本实例:

```sh

#!/usr/bin/sh

# evaluate the value of an integer.

Int=-5

if [ -z "$Int" ]; then    # 判断变量是否未定义
    echo "INT is empty." >&2    # 输出到stderr
    exit 1    # 抛出错误退出符1,并退出
fi
if [ $Int -eq 0 ]; then
    echo "INT is zero."
else
    if [ $Int -lt 0 ]; then
        echo "INT is negative."
    else
        echo "INT is positive."
    fi
    if [ $((Int % 2)) -eq 0 ]; then
        echo "INT is even."
    else
        echo "INT is odd."
    fi    
fi

# 运行结果
INT is negative.
INT is odd.
```

### 27.4 更现代的test命令版本

**复合命令**:
相当于增强版的test命令,语法:

```sh
    [[ expresion ]]
```

[[]]和test命令类似,支持所有的表达式,还增加了一个很重要的字符串表达式

```sh
string=~regex    #string与扩展的正则表达式匹配,则返回true
```

[[]]增加的另一个特性是==操作符支持模式匹配，就像路径扩展名那样,这使得在评估文件名和路径时非常有用。

```sh

#!/usr/bin/bash
File=boo.bar

if[[ "$File" == foo.* ]]; then
    echo "$File matches pattern 'foo.*'"
fi

# 运行结果
foo.bar matches pattern 'foo.*'
```

上例中如果INT含有整数以外的其他值就会失败,所以改进版本如下:

```sh

#!/usr/bin/bash

# test-integer2: evaluate the value of an integer.

Int=-5

# "$Int" =~ ^-?[0-9]+$:-->变量以一个可选的“-”开头（有没有都行），包含一个或多个0-9之间的数字，且以0-9之间的数字结尾
if [[ "$Int" =~ ^-?[0-9]+$ ]]; then
    if [ $Int -eq 0 ]; then
        echo "INT is zero."
    else
        if [ $Int -lt 0 ]; then
            echo "INT is negative."
        else
            echo "INT is positive."
        fi
        if [ $((Int % 2)) -eq 0 ]; then
            echo "INT is even."
        else
            echo "INT is odd."
        fi    
    fi
else
    echo "INT is not an integer." >&2
    exit 1
fi
```

### 27.5 (())--Design for integer

(())用于算术真值测试.当算术计算的结果为**非零**值时,则为true.
使用(())可以重写以上脚本:

```sh

#!/bin/bash 
# test-integer2a: evaluate the value of an integer. 
INT=-5 
if [[ "$INT" =~ ^-?[0-9]+$ ]]; then 
    if ((INT == 0)); then 
        echo "INT is zero." 
    else 
        if ((INT < 0)); then 
            echo "INT is negative." 
        else 
            echo "INT is positive." 
        fi 
        if (( ((INT % 2)) == 0)); then 
            echo "INT is even." 
        else 
            echo "INT is odd." 
        fi 
    fi 
    else 
        echo "INT is not an integer." >&2 
        exit 1 
fi
```

注意这里使用了大于号,小于号等来测试相等性,在处理整数时这种语法看起来更加自然.但注意只能处理整数!

###27.6 组合表达式

组合表达式用逻辑操作符连接起来:

&&--与
||--或
!--非

代码实例:

```sh
#!/bin/bash 
# test-integer4: determine if an integer is outside a 
# specified range of values. 
MIN_VAL=1 
MAX_VAL=100 
INT=50 

if [[ "$INT" =~ ^-?[0-9]+$ ]]; then 
    if [[ ! (INT -ge MIN_VAL && INT -le MAX_VAL) ]]; then     # 注意“！”取反符号
        echo "$INT is out of $MIN_VAL to $MAX_VAL." 
    else 
        echo "$INT is within range." 
    fi 
else 
        echo "INT is not an integer." >&2 
        exit 1 
fi
```

## 28 从键盘读取(与用户交互)

###28.1 read--从标准输入读取输入值
read一般语法格式:

    read [-options] [variable]

read选项:

| 选项        | 描述                         |
|:--------- |:-------------------------- |
| a         | 将输入值从索引0开始赋值给array         |
| e         | 使用readline处理输入,使用普通命令行模式输入 |
| p         | 使用prompt字符串提示用户输入          |
| n num     | 从输入中最多读取num个字符             |
| r         | 原始模式,转义字符\失去意义             |
| s         | 保密模式,输入不在屏幕回显,用于输入密码之类     |
| t seconds | 输入超时,超时后read返回一个非0的退出状态    |

代码:

```sh
#!/bin/bash 
# read-integer: evaluate the value of an integer. 
echo -n "Please enter an integer -> " 
read int 
if [[ "$int" =~ ^-?[0-9]+$ ]]; then 
    if [ $int -eq 0 ]; then 
        echo "$int is zero." 
    else 
        if [ $int -lt 0 ]; then 
            echo "$int is negative." 
        else 
            echo "$int is positive." 
        fi 
        if [ $((int % 2)) -eq 0 ]; then 
            echo "$int is even." 
        else 
            echo "$int is odd." 
        fi 
    fi 
else 
    echo "Input value is not an integer." >&2 
    exit 1 
fi
```

read将输入值赋值给多个变量

```sh

#!/usr/bin/bash
echo -n "Enter one or more values --> "
read var1 var2 var3 var4

echo "var1 = '$var1'"
echo "var2 = '$var2'"
echo "var3 = '$var3'"
echo "var4 = '$var4'"

# 说明：
#    输入以空格间隔
#    如果输入少于4个，那么后面的为空变量
#    等于4个，分别赋值
#    多于4个，前三个分别赋值，其余全部赋值给$var4
```

==如果read命令后没有变量，则会为所有的输入分配一个shell默认变量$REPLY==

### 28.2验证输入

程序好坏的区别仅在于是否能处理突发情况,而输入异常是突发情况的常见环节.所以验证输入是保证程序健壮的必须任务.

下例是对输入的验证

```sh

#!/bin/bash 
# read-validate: validate input 

invalid_input () { 
    echo "Invalid input '$REPLY'" >&2 
    exit 1 
} 

read -p "Enter a single item > " 

# input is empty (invalid) 
[[ -z $REPLY ]] && invalid_input 

# input is multiple items (invalid) 
(( $(echo $REPLY | wc -w) > 1 )) && invalid_input    # wc -w 总共有几个单词word,这里是验证字符间是否输入了空格

# is input a valid filename? 
if [[ $REPLY =~ ^[-[:alnum:]\._]+$ ]]; then 
    echo "'$REPLY' is a valid filename." 
    if [[ -e $REPLY ]]; then 
        echo "And file '$REPLY' exists." 
    else 
        echo "However, file '$REPLY' does not exist." 
    fi 
    # is input a floating point number? 
    if [[ $REPLY =~ ^-?[[:digit:]]+\.[[:digit:]]+$ ]]; then 
        echo "'$REPLY' is a floating point number." 
    else 
        echo "'$REPLY' is not a floating point number." 
    fi 
    # is input an integer? 
    if [[ $REPLY =~ ^-?[[:digit:]]+$ ]]; then 
        echo "'$REPLY' is an integer." 
    else 
        echo "'$REPLY' is not an integer." 
    fi 
else 
    echo "The string '$REPLY' is not a valid filename." 
fi
```

此脚本的知识点包括：shell函数、[[]]、（（））、&&、if及适量的正则表达式

### 28.3 菜单

```sh

#!/bin/bash 

# read-menu: a menu driven system information program 

clear    # 清空屏幕

# 这种echo方式，将按格式输出到stdout
echo " 
Please Select: 
1. Display System Information 
2. Display Disk Space 
3. Display Home Space Utilization 
0. Quit 
" 
read -p "Enter selection [0-3] > " 

if [[ $REPLY =~ ^[0-3]$ ]]; then 
    if [[ $REPLY == 0 ]]; then 
        echo "Program terminated." 
        exit 
    fi 
    if [[ $REPLY == 1 ]]; then 
        echo "Hostname: $HOSTNAME" 
        uptime 
        exit 
    fi 
    if [[ $REPLY == 2 ]]; then 
        df -h 
        exit 
    fi 
    if [[ $REPLY == 3 ]]; then 
        if [[ $(id -u) -eq 0 ]]; then 
            echo "Home Space Utilization (All Users)" 
            du -sh /home/* 
        else 
            echo "Home Space Utilization ($USER)" 
            du -sh $HOME 
        fi 
        exit 
    fi 
else 
    echo "Invalid entry." >&2 
    exit 1 
fi
```

exit可以退出程序,并防止执行多余的代码.但程序的多出口容易逻辑混乱,不是一个好主意.

## 29 流控制,while和untill循环

while语法:

```sh

while [[ condition ]]; do
    statements
done    
```

前面menu脚本的while实现:

```sh

#!/usr/bin/bash

# while-menu: a menu driven system information program

DELAY=3        # Number of seconds to display results

while [[ $REPLY != 0 ]]; do        #$REPLY系统默认(预定义)读取键盘输入变量
    clear    #清空屏幕，一般情况下和sleep n 搭配使用，否则输出来不及看到就clear了。
    cat <<- _EOF_
        Please Select:

        1. Display System Information
        2. Display Disk Space
        3. Display Home Space Utilization
        0. Quit
    _EOF_
    read -p "Enter selection [0-3] > "

    if [[ $REPLY =~ ^[0-3]$ ]]; then
        if [[ $REPLY == 1 ]]; then
            echo "Hostname: $HOSTNAME"
            uptime
            sleep $DELAY
        fi
        if [[ $REPLY == 2 ]]; then
            df -h
            sleep $DELAY
        fi
        if [[ $REPLY == 3 ]]; then
            if [[ $(id -u) -eq 0 ]]; then
                echo "Home Space Utilization (All users)"
                du -sh /home/*
            else
                echo "Home Space Utilization ($USER)"
                du -sh $HOME
            fi
            sleep $DELAY
        fi
    else
        echo "Invalid entry.--输入错误,请重试!" >&2
        sleep $DELAY
    fi
done
echo "Program terminated.--程序退出,多谢使用!"
```

这个while循环比较特殊，一般的while循环如下实例

```sh

#!/usr/bin/bash
# simpleWhile
count=1

while [ $count -lt 6 ]; do
    echo $count
    count=$(( count + 1 ))
done
echo "Finished!"
```

有初始值，有累加

### 29.3 跳出循环

bash内建了两个控制循环内部程序流的命令:

break--终止并跳出循环,程序从循环**后**的语句继续执行,若循环后没有语句,则终止程序.
continue--**跳过循环剩余**部分,直接开始下一次循环迭代.

### until
语法:

    until commands; do
        commands
    done

until和while几乎镜像对称，比如上例的until重写
while的含义是：当...成立时，那么做什么。有可能一次也不执行
until的含义是：做什么，直到...时为止。最少执行一次

```sh

#!/usr/bin/bash
# simpleUntil

count=1

until [ $count -gt 6 ]; do
    echo $count
    count=$(( count + 1 ))
done
echo "Finished!"
```

## 30 故障排除debug

    语法错误可以藉由带语法高亮的编辑器减少出现概率.
    逻辑错误
        条件表达错误
        从1开始错误,系统默认从0开始
        非预期的情形,(对极端状况估计不足)

### 30.1 防御编程

在涉及删除命令等危险操作时，一定要把各种情况都搞清楚，做到逻辑严密

比如：

    cd $dirName
    rm *

如果$dirName不存在，就会cd错误，留在原目录，那么删除的就是工作目录下的所有内容

    cd $dirName && rm *

情况有所改善，如果cd失败，后面的rm就不会执行;但还有$dirName为空值的情况，隐藏着删除用户主目录的隐患

    [[ -d $dirName ]] && cd $dirName && rm *

先验证目录存在，再cd，最后rm;前两步全部成立才执行操作。从根本上杜绝了隐患。    

###30.2 输入值验证

一条普世的编程法则是：==只要程序接受用户的输入，那么程序必须能处理任何输入值！==，有时输入值验证极富挑战性。

    [[ $REPLY =~ ^[0-3]$ ]]

### 30.3 测试

打桩：echo关键部位
极限：各种极端情况，正确的输入、错误的输入、没有输入...

### 30.4 调试

找到问题域：分段注释代码

### 30.5 追踪

在适当位置插入echo提示字段，提示脚本运行到哪一步出现的问题。
echo行不缩进以利于和原来的代码区分，在debug结束后容易注释掉和删除。

    echo "运行到了*部分，开始干..." >&2

bash自带了分步追踪

    #!/bin/bash -x        #全局追踪
    
    #局部追踪
    set -x
    someCodeLine
    ...
    set +x

分步追踪前面显示的是$PS4

debug就像侦探情节：画定嫌犯区域-找到嫌犯-定罪/改造-释放

## 31 流控制--case分支

语法:

    case $variable in
        valu1) commands
            commands go on
            ;;
        valu2) commands
            commands go on
            ;;
        ...
        *) commands        # 除上述匹配的变量值之外所有的情况，这是最重要的一个特性。
            commands go on
            ;;
    esac

用case重写menu.sh

```sh
#!/usr/bin/bash

# case_menu.sh: a menu driven system information program

clear
echo "
    Please Selection:
    A. Display System Information
    B. Display Disk Space
    C. Display Home SpaceUtilization
    Q. Quit
"

read -p "Enter selection [A,B,C or Q] > "

case $REPLY in
    q|Q) echo "Program terminated.--程序退出,多谢使用!"        # 多个变量值匹配
        exit
        ;;
    a|A) echo "Hostname: $HOSTNAME"
        uptime
        ;;
    b|B) df -h
        ;;
    c|C) if [[ $(id -u) -eq 0 ]]; then
            echo "Home Space Utilization (All Users)"
            du -sh /home/*
        else
            echo "Home Space Utilization ($USER)"
            du -sh $HOME
        fi
        ;;
    *) echo "Invalid entry.--输入错误,请重试" >&2
        exit 1
        ;;
esac        
```

对于有限多的离散选项case特别适合

case模式范例：

| 模式           | 描述                              |
|:------------ |:------------------------------- |
| a)           | 字符a匹配                           |
| [[:alpha:]]) | 只要是单个字母即匹配                      |
| ???)         | 三个字符即匹配                         |
| *.txt)       | 以.txt结尾即匹配                      |
| *)           | 用于最后一项，不属于前面任意的都不匹配。同时排除了任何非法的值 |

## 32 位置参数

本章讲解脚本接受shell命令选项和参数的能力.

### 32.1 访问命令行

    shell提供了一组位置参数的变量
        $0--一直是命令本身的名字
        $1--第一个位置参数
        $2,$3...依次类推,超过$9后:${10}...加大括号
        $#--参数个数(不包括$0)
        $*和$@--不加引号同样代表参数本身的列表
            --加引号
            "$*"--将所有参数解释成一个字符串
            "$@"--将所有参数解释成一个参数数组

比如展示"$*"和"$@"区别的脚本

```sh

#!/bin/bash
#arguments diffrent

echo '$* output'
for arg in "$*"
do
    echo $arg
done

echo '$@ output'
for arg in "$@"
do
    echo $arg
done
```

可以./argument.sh * 测试输出结果的不同

#### 32.1.2 shift--处理大量参数

shift--每次执行shift命令后,所有参数的值均下移一位.实际上通过shift一次只处理除$0之外的一个参数,而完成所有程序任务.
比如:

```sh

#!/bin/bash
# while-argument.sh

count=1

while [[ $# -gt 0 ]]; do
    echo "Argument \$$count = $1."        #注意\$$原因
    count=$(($count + 1))
    shift
done

# 运行结果
$ ./while-argument.sh a b cd
Argument $1 = a
Argument $2 = b
Argument $3 = cd
```

#### 32.1.3 简单的应用程序

basename--移除文件名的路径部分
basename $0--移除除了脚本"路径+文件名"外所有的文件名路径

示例:

```sh
#!/bin/bash
# file-info.sh
# 程序运行方式是:file-info.sh filename
# 会显示文件filename相关信息.

progName=$(basename -$0)

if [[ -e $1 ]]; then
    echo -e "\nFile type"    #\n先换行再打印
    file $1
    echo -e "\nFile status"
    stat $1
else
    echo "$progName: usage: $progName File" >&2
    exit 1
fi
```

将上例封装成函数:==有问题!!!还是对上例没搞明白==

```sh

#!/bin/bash
# fileInfoFuncRew.sh

progName=$(basename $0)

fileInfo () {
    # fileInfo function to display file infomation

    if [[ -e $1 ]]; then
        echo -e "\nFile Type:"
        file $1
        echo -e "\nFile Statuse:"
        stat $1
    else
        echo "$FUNCNAME: usage: $FUNCNAME File" >&2
        return 1
    fi
}

$(fileInfo)
```

### 32.2 处理多个位置参数

### 32.3 更完整的应用程序

### 32.4 Summing up

## 33 流控制--for循环

for循环采用在循环期间进行序列处理的机制

### 33.1 shell的传统语法形式

    for variable [in words]; do
        commands
    done
    
    # variable--循环时会增值的变量名
    # words--是一列将按顺序赋值给variable的可选项
    # commands--是每次循环都会执行的命令

命令行直接使用实例:

```sh
$ for i in {A..D}; do echo $i; done        # 命令行直接使用形式
$ for i in distros*.txt; do echo $i; done    #路径扩展名形式
```

脚本实例:

```sh

#!/bin/bash
# longestWord.sh: Find longest string in a file
# longestWord.sh filenames...
# 打印出filename里最长的字符串

while [[ -n $1 ]]; do
    if [[ -r $1 ]]; then
        maxWord=
        maxLen=0

        for i in $(strings $1); do    # strings打印指定文件的(默认)可打印字符串
            len=$(echo $i | wc -c)
            if (( len > maxLen )); then
                maxLen=$len
                maxWord=$i
            fi
        done
        echo "$1: '$maxWord' ($maxLen characters.)"
    fi
    shift
done
```

上例的全for重写

```sh

#!/bin/bash 
# longest-word2 : find longest string in a file 
for i; do 
    if [[ -r $i ]]; then 
        max_word= 
        max_len=0 
        for j in $(strings $i); do 
            len=$(echo $j | wc -c) 
            if (( len > max_len )); then 
                max_len=$len 
                max_word=$j 
            fi 
        done 
            echo "$i: '$max_word' ($max_len characters)" 
    fi 
done
```

### 33.2 C语言形式:

    for (( expresion1, expresion2, expresion3 )); do
        commands
    done
    
    #expresion1--初始值
    #expresion2--边界条件
    #expresion3--步进

实例:

```sh
#!/usr/bin/bash

# simeple_counter: demo of C style for command

for (( i=0, i<6, i=i+1 ));  do
    echo $i
done
```

## 34 字符串和数字

前面的章节都是对文件层面处理,本章开始操作文件内的字符串和数字

### 34.1 参数扩展(Parameter Expansion)

1.基本参数

变量$a和${a}在不与其他字符紧紧相邻的情况下完全一样,如果引起混淆那么必须${a}

```sh
$ a=foo
$ echo "$a_file"
$            # 输出为空$ab没有定义
$ echo ${a}_file
$ foo_file
```

2.空变量扩展的管理

有的参数扩展用于处理不存在的变量和空变量.这些参数扩展在处理缺失的位置参数和给参数赋默认值的时候很有用处.

A.parameter为空,则扩展为word;parameter非空,则扩展为parameter的值

```sh
# 一般语法形式
${parameter:-word}
$ foo=
$ echo ${foo:-"变量值未设定"}
变量值未设定
$ echo $foo

$ foo=bar
$ echo ${foo:-"变量值未设定"}
bar
$ echo $foo
bar
```

B.parameter为空,则扩展为word,同时word赋值给parameter;parameter非空,则扩展为parameter的值

```sh
# 一般语法形式
${parameter:=word}
$ foo=
$ echo ${foo:=unset}
unset
$ echo $foo
unset
$ foo=bar
$ echo ${foo:=unset}
bar
$ echo $foo
bar
# 注意:位置参数和其他特殊参数不能以这种方式赋值
```

C.parameter为空,脚本出错退出,并把word输出到stderr;parameter非空,则扩展为parameter的值

```sh
# 一般语法形式
${parameter:?word}
$ foo=
$ echo ${foo:?"parameter is empty!"}
Bash foo: parameter is empty!
$ echo $?
1
$ foo=bar
$ echo ${foo:?"parameter is empty!"}
bar
$ echo $?
0
```

D.parameter为空,不产生任何扩展;parameter非空,word的值将取代parameter的值,然而parameter的值不发生变化

```sh
# 一般语法形式:
${parameter:+word}
$ foo=
$ echo ${foo:+"set?"}

$ foo=bar
$ echo ${foo:+"set?"}
set?
$ echo $foo
bar
```

3.返回变量名的扩展

极特殊的情况下才会用到

    ${!prefix*}
    ${!prefix@}

4.字符串操作

A.

```sh
${#parameter}
# 扩展为parameter字符串的字符个数;如果参数是"@","*"则扩展成位置参数的个数.
$ foo="This string is long."
$ echo "'$foo' is ${#foo} characters long."
'This string is long.' is 20 characters long.

${parameter:offset[:length]}
# 扩展从"减去offset个字符"开始,直到字符串结尾,除非length特别指定.
$ echo ${foo:5}
string is long.
$ echo ${foo:2:9}
is string
# offset小于0,:后要加空格以示与${parameter:-word}区别,作用是从末尾开始数起
# length不能小于0
$ echo ${foo: -5}
long.
$ echo ${foo: -5:2}
lo

${parameter#[#]*.}
# 一个#去除最短匹配,两个#去除最长匹配,"."为边界符号
$ foo=file.txt.zip
$ echo ${foo#*.}
txt.zip
$ echo ${foo##*.}
zip

${parameter%[%].*}
# 与#只有一点不同:从字符串末尾去除
$ echo ${foo%.*}
file.txt
$ echo ${foo%%.*}
file

# 替换文本直接看实例吧
$ foo=JPG.JPG
$ echo ${foo/JPG/jpg}
jpg.JPG
$ echo ${foo//JPG/jpg}
jpg.jpg
$ echo ${foo/#JPG/jpg}
jpg.JPG
$ echo ${foo/%JPG/jpg}
JPG.jpg
$ echo $foo
JPG.JPG
```

使用参数扩展进行字符串操作可以替代其他常用的外部程序,可以大幅度的提高执行效率
比如前例中longest-word2的重写:

```sh

#!/bin/bash
# longest-word3:find longest string in a file

for i; do
    if [[ -r $i ]]; then
        maxWord=
        maxLen=
        for j in $(strings $i); do
            len=${#j}
            if (( len > maxLen )); then
                maxLen=$len
                maxWord=$j
            fi
        done
        echo "$i: '$maxWord' ($maxLen characters)"
    fi
    shift
done
```

用time命令比较两个版本的效率

```sh
$ time longest-word2.sh dirlist-usr-bin.txt
dirlist-usr-bin.txt: 'scrollkeeper-get -extended-content-list' (38 characters)

real    0m3.618s
user    0m1.544s
sys        0m1.768s
$ time longest-word3.sh dirlist-usr-bin.txt
dirlist-usr-bin.txt: 'scrollkeeper-get -extended-content-list' (38 characters)

real    0m0.060s
user    0m0.056s
sys        0m0.008s
```

可以看出执行速度3.618s/0.060s,进步巨大!

###34.2 算术计算和扩展

基本形式:

    $((expression))
    # expression是一个有效的算术表达式

表34-1 不同数字进制的表达方式:

| 符号          | 描述     |
|:----------- |:------ |
| Number      | 十进制    |
| 0nmber      | 八进制    |
| 0xnumber    | 十六进制   |
| base#number | base进制 |

表34-2 赋值操作符:

| 运算符              | 描述                                    |
|:---------------- |:------------------------------------- |
| parameter=value  | 最基础的赋值操作                              |
| parameter+=value | parameter=parameter+value             |
| parameter*=value | parameter=parameter*value             |
| parameter/=value | parameter=parameter/value             |
| parameter%=value | parameter=parameter%value             |
| parameter++      | parameter=parameter+1                 |
| parameter--      | parameter=parameter-1                 |
| ++parameter      | parameter=parameter+1(和上面的有区别,看后面的例子) |
| --parameter      | parameter=parameter-1                 |

++在参数前,参数在返回前增加;++在参数后,+1在参数返回后增加.--同理.
示例:

```sh
$ foo=1
$ echo $((foo++))
1
$ echo $foo
2

$ foo=1
$ echo $((++foo))
2
$ echo $foo
2
```

位操作
据说很高效,但太繁琐且不易理解.--略

==((expr1?expr2:expr3)):相当于最简单的if/then/else==
如果有赋值操作,错误的方式是:
~~((a<0?a-=4:a+=5))~~
正确的方式:
((a<0?(a-=4):(a+=5)))

一个实例:

```sh

#!/bin/bash
# arith-loop: script to demonstrate arithmetic operators

# 在表达式里0代表false,1代表true;与程序退出状态相反.注意注意~~
finished=0
a=0
printf "a\ta**2\ta**3\n"    # 格式化输出
printf "=\t====\t====\n"

until ((finished)); do
    b=$((a**2))
    c=$((a**3))
    printf "%d\t%d\t%d\n" $a $b $c    # 格式化输出一般形式
    ((a<10?++a:(finished=1)))        # if/then/else最简单表现形式.
done
```

### 34.3 bc--一种任意精度计算语言

主要内容就是如何调用外部程序.本系统集成的计算器是galculator

## 35 数组

数组是一次可以存放多个值的变量,数组的组织形式和表格一样.
数组中的单元叫做元素,包括数据和索引(也叫下标)
bash只支持一维数组.

    $ a[1]=foo
    $ echo ${a[1]}
    foo

花括号不能省略,防止shell对[]进行扩展.

另一种创建数组的方式:

    declare -a a

### 35.1 数组赋值

```sh
# 给单一元素赋值,subscript从0开始的整数
name[subscript]=value
# 给数组赋多值
name=(value1 value2...)
days=(Sun Mon Tue Wed Thu Fri Sat)
```

实例:

```sh

#!/bin/bash
# hours.sh: script to count files by modification time

usage () {
    echo "usage: $(basename $0) directory" >&2
}

# Check that argument is a directory
if [[ ! -d $1 ]]; then
    $(usage)
    exit 1
fi

# Iniialize array
for i in {0..23}; do hours[i]=0; done

# Collect data
for i in $(stat -c %y "$1"/* | cut -c 12-13); do
    j=${i/#0}
    ((++hours[j]))
    ((++count))
done

# Display data
echo -e "Hour\tFiles\tHour\tFiles"
echo -e "----\t----\t----\t----"
for i in {0..11}; do
    j=$((i + 12))
    printf "%02d\t%d\t%02d\t%d\n" $i ${hours[i]} $j ${hours[j]}
done
printf "\nTotal files = %d\n" $count
```

## 36 其他命令

简言之就是逐渐加深对操作系统的理解,及部分特殊命令在脚本当中的调用.
包括:
组命令与子shell,trap,wait,命名管道等等

---

## 总结

bash脚本的编写不同于其他语言,更重要的基础就是对操作系统的理解!

--END--END--END--

Edit by [Remarkable](https://github.com/jonschlinkert/remarkable) 
https://github.com/jonschlinkert/remarkable

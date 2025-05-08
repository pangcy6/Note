# tmux使用详解

## 简介

tmux是一个优秀的终端复用软件，类似GNU Screen，但来自于OpenBSD，采用BSD授权。使用它最直观的好处就是，通过一个终端登录远程主机并运行tmux后，在其中可以开启多个控制台而无需再“浪费”多余的终端来连接这台远程主机；当然其功能远不止于此。

## 安装tmux

Arch Linux下安装只需要:`sudo pacman -S tmux`
安装完成后输入命令tmux即可打开软件，界面十分简单，类似一个下方带有状态栏的终端控制台；但根据tmux的定义，在开启了tmux服务器后，会首先创建一个会话，而这个会话则会首先创建一个窗口，其中仅包含一个面板；也就是说，这里看到的所谓终端控制台应该称作tmux的一个面板，虽然其使用方法与终端控制台完全相同。
tmux使用C/S模型构建，主要包括以下单元模块：

| 名称      | 解释                     |
|:------- |:---------------------- |
| server  | 服务器.输入tmux命令时就开启了一个服务器 |
| session | 会话.一个服务器可以包含多个会话       |
| window  | 窗口.一个会话可以包含多个窗口        |
| pane    | 面板.一个窗口可以包含多个面板        |

## 系统级操作

```
$ tmux        #简单开启,包括:一个server,一个编号为0的session,一个编号修改为1的window,一个pane
$ tmux new -s sessionName    #创建一个名字为sessionName的session
$ tmux attach -t sessionName    # 重新开启名字为sessionName的session
$ tmux switch -t sessionName    # 切换到
$ tmux list-sessions    # 列出现有的session
```

## 常规操作

类似各种平铺式窗口管理器，tmux使用键盘操作，常用快捷键包括：

**Ctrl+b 激活控制台；此时以下按键生效**

系统级操作:

| key    | function                                        |
|:------ |:----------------------------------------------- |
| ?      | 列出所有快捷键；按q返回                                    |
| d      | 脱离当前会话；这样可以暂时返回Shell界面，输入tmux attach能够重新进入之前的会话 |
| D      | 选择要脱离的会话；在同时开启了多个会话时使用                          |
| Ctrl+z | 挂起当前会话                                          |
| r      | 强制重绘未脱离的会话,同时也是重新载入配置文件.                        |
| s      | 选择并切换会话；在同时开启了多个会话时使用                           |
| :      | 进入命令行模式；此时可以输入支持的命令，例如kill-server可以关闭服务器        |
| [      | 进入复制模式；此时的操作与vi/emacs相同，按q/Esc退出                |
| ~      | 列出提示信息缓存；其中包含了之前tmux返回的各种提示信息                   |

窗口级操作:

| key | function           |
|:--- |:------------------ |
| c   | 创建新窗口              |
| &   | 关闭当前窗口             |
| 数字键 | 切换至指定窗口            |
| p   | 切换至上一窗口            |
| n   | 切换至下一窗口            |
| l   | 在前后两个窗口间互相切换       |
| w   | 通过窗口列表切换窗口         |
| ,   | 重命名当前窗口；这样便于识别     |
| .   | 修改当前窗口编号；相当于窗口重新排序 |
| f   | 在所有窗口中查找指定文本       |

面板级操作:

| key      | function                                                                            |
|:-------- |:----------------------------------------------------------------------------------- |
| ”        | 将当前面板平分为上下两块                                                                        |
| %        | 将当前面板平分为左右两块                                                                        |
| x        | 关闭当前面板                                                                              |
| !        | 将当前面板置于新窗口；即新建一个窗口，其中仅包含当前面板                                                        |
| Ctrl+方向键 | 以1个单元格为单位移动边缘以调整当前面板大小                                                              |
| Alt+方向键  | 以5个单元格为单位移动边缘以调整当前面板大小                                                              |
| Space    | 在预置的面板布局中循环切换；依次包括even-horizontal、even-vertical、main-horizontal、main-vertical、tiled |
| q        | 显示面板编号                                                                              |
| o        | 在当前窗口中选择下一面板                                                                        |
| 方向键      | 移动光标以选择面板                                                                           |
| {        | 向前置换当前面板                                                                            |
| }        | 向后置换当前面板                                                                            |
| Alt+o    | 逆时针旋转当前窗口的面板                                                                        |
| Ctrl+o   | 顺时针旋转当前窗口的面板                                                                        |

## 配置

tmux的系统级配置文件为/etc/tmux.conf(但在Arch中找不到这个文件,Arch果然特立独行=_=)，用户级配置文件为$HOME/.tmux.conf。配置文件实际上就是tmux的命令集合，也就是说每行配置均可在进入命令行模式后输入生效。
下面是一个$HOME/.tmux.conf的示例，其中包括了一些常用的配置：

    #此类配置可以在命令行模式中输入show-options -g查询
    set-option -g base-index 1                        #窗口的初始序号；默认为0，这里设置为1
    set-option -g display-time 5000                   #提示信息的持续时间；设置足够的时间以避免看不清提示，单位为毫秒
    set-option -g repeat-time 1000                    #控制台激活后的持续时间；设置合适的时间以避免每次操作都要先激活控制台，单位为毫秒
    set-option -g status-keys vi                      #操作状态栏时的默认键盘布局；可以设置为vi或emacs
    set-option -g status-right "#(date +%H:%M' ')"    #状态栏右方的内容；这里的设置将得到类似23:59的显示
    set-option -g status-right-length 10              #状态栏右方的内容长度；建议把更多的空间留给状态栏左方（用于列出当前窗口）
    set-option -g status-utf8 on                      开启状态栏的UTF-8支持
    
    #此类设置可以在命令行模式中输入show-window-options -g查询
    set-window-option -g mode-keys vi    #复制模式中的默认键盘布局；可以设置为vi或emacs
    set-window-option -g utf8 on         #开启窗口的UTF-8支持
    
    #将激活控制台的快捷键由Ctrl+b修改为Ctrl+a
    set-option -g prefix C-a
    unbind-key C-b
    bind-key C-a send-prefix
    
    #添加自定义快捷键
    bind-key z kill-session                     #按z结束当前会话；相当于进入命令行模式后输入kill-        session
    bind-key h select-layout even-horizontal    #按h将当前面板布局切换为even-horizontal；相当于进入命令行模式后输入select-layout even-horizontal
    bind-key v select-layout even-vertical      #按v将当前面板布局切换为even-vertical；相当于进入命令行模式后输入select-layout even-vertical

完整的$HOME/.tmux.conf示例:

```

#==Base config==========================#

set -g default-terminal "screen-256color"
set -g display-time 3000
set -g history-limit 10000
set -g base-index 1
set -g pane-base-index 1
set -s escape-time 0
setw -g mode-keys vi
set-option -g visual-bell off    # 开关高亮提醒on/off

# 非当前窗口有事件发生时,状态栏会有高亮显示.
set -g visual-activity on
setw -g monitor-activity on

# 关闭自动命名,(自己重命名后保持状态)
setw -g automatic-rename off

# 鼠标支持
set -g mode-mouse on
set -g mouse-select-pane on
set -g mouse-resize-pane on
set -g mouse-select-window on

# Use F4 instead of c-b as the prefix
unbind C-b
set -g prefix F4
bind F4 send-prefix
bind r source-file ~/.tmux.conf\; display "Configration Reloaded!"

#=======Action config===================#

# Server action
# :--进入命令模式
# : kill-server        关闭服务器
# ?--列出所有可用的快捷键

# Session action
unbind C-z
bind z suspend-client    # 挂起当前会话
# : kill-session    关闭会话,关闭最后一个窗口也会关闭session和server
# (/)--前/后切换session
# d--脱离当前会话,重回shell;tmux attach重回会话
# D--选择要脱离的会话(多个会话时)
# s--选择并切换会话(多个会话时)
# [--复制模式,ESc/q退出
# #--list-buffers
# =--choose-buffer
# ]--粘贴
# ~--列出提示信息缓存

# Window action
unbind &
bind q kill-window    #无警告关闭window
# c--创建新窗口
# 数字键--切换到指定编号窗口
# p--切换到前一窗口
# n--切换到下一窗口
# l--在前后两个窗口间切换
# w--通过窗口列表切换
# ,--重命名窗口
# .--修改窗口编号,相当于重新排列窗口顺序
# f--在所有窗口中查找文本

# pane action
unbind '"'
unbind %
bind | split-window -h    #直观方式建立pane布局
bind - split-window -v
# vim style 切换pane焦点
bind h select-pane -L
bind j select-pane -D
bind k select-pane -U
bind l select-pane -R
bind x kill-pane    # 关闭当前pane
# 方向键--切换pane焦点
# !--将当前面板置于新窗口
# Ctrl-方向键--以1个单元重置窗口大小
# Alt-方向键--以5个单元重置窗口大小
# Ctrl-o--顺时针旋转面板
# Alt-o--逆时针旋转面板
# Space--在系统预置的面板布局中切换
# {/}--向前/后置换面板

#===Statusbar config=============#

set -g status-justify centre
set -g status-left "#[fg=cyan]S#S:#[fg=yellow]W#I.#[fg=magenta]P#P"
set -g status-left-attr bright
set -g status-left-length 30
set -g status-utf8 on
set -g status-interval 1

# pane间分割线的颜色
set -g pane-border-fg cyan
set -g pane-border-bg black
set -g pane-active-border-fg blue
set -g pane-active-border-bg black

# default statusbar colors
set -g status-fg cyan
set -g status-bg black
setw -g window-status-fg cyan
setw -g window-status-bg default
setw -g window-status-attr dim
setw -g window-status-current-fg magenta
setw -g window-status-current-bg black
#setw -g window-status-current-attr bright
```

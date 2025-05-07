# Hyprland Wiki 重点内容

Date: 2024.08.17
[URL](https://wiki.hyprland.org/)

---

Wayland 合成器是一个完全自主的显示服务器，就像 Xorg 本身一样。不可能像在 Xorg 上那样将 Wayland 合成器与窗口管理器和合成器混合使用。

## 1. Installation

包安装：

```bash
sudo pacman -S hyprland
yay -S hyprland-git     # Developer version
```

手动构建：

```bash
yay -S gdb ninja gcc cmake meson libxcb xcb-proto xcb-util xcb-util-keysyms libxfixes libx11 libxcomposite xorg-xinput libxrender pixman wayland-protocols cairo pango seatd libxkbcommon xcb-util-wm xorg-xwayland libinput libliftoff libdisplay-info cpio tomlplusplus hyprlang hyprcursor hyprwayland-scanner xcb-util-errors hyprutils-git
```

源码编译安装：

```bash
git clone --recursive https://github.com/hyprwm/Hyprland
cd Hyprland
make all && sudo make install
```

## 2. Configuring

主配置文件默认位置：~/.config/hypr/hyprland.conf
配置文件保存后就会**重新加载**。每个配置行都是一个命令，后跟一个值。`COMMAND = VALUE`。

```bash
exec-once = command will execute only on launch
exec = command will execute on each reload
```

在配置文件中可用source关键字来获取另一个文件：`source = ~/.config/hypr/myColor.conf`
这意味着可将配置文件分成若干个文件, 然后source

设置壁纸程序：hyprpaper or swaybg

env关键字的工作方式与 exec-once类似，只会在Hyprland启动时触发一次。

### 2.1 Monitors

配置语法：

```
monitor = name, resolution, position, scale
```

列出所有可用的monitors：

```
hyctl monitors all
```

example

```bash
# 将DP-1放在DP-2 的左侧
monitor = DP-1, 1920x1080@60, 0x0, 1
monitor = DP-2, 1920x1080, 1920x0, 1

# 也可使用负数，效果相同; 同理可知上下排列
monitor = DP-1, 1920x1080@60, -1920x0, 1
monitor = DP-2, 1920x1980, 0x0, 1
```

### 2.2 Binds

Basic：

```
bind = MODS, key, dispatcher, params
#Example:
bind = $mainKey, F, exec firefox
```

鼠标：

```bash
bind = SUPER, mouse:272, exec, amongus      # 鼠标按键
bind = SUPER, mouse_down, workspace, e-1    # 滚轮，调整工作区
```

全局键绑定：

```bash
bind = SUPER, F10, pass, ^(com\.obsproject\.Studio)$
```

Media: 音量控制

```bash
bindel = SHIFT, UP, exec, wpctl set-volume @DEFAULT_AUDIO_SINK@ 2%+
bindel = SHIFT, DOWN, exec, wpctl set-volume @DEFAULT_AUDIO_SINK@ 2%-
bindel = , XF86AudioRaiseVolume, exec, wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%+
```

### 2.3 hyprctl

自带工具，通过CLI或脚本控制合成器的某些部分。

## 3. 实用工具

所有wm都不是完整的桌面环境，需要搭配其他实用工具来完善使用体验。

### 3.1 必备工具

- 通知守护进程：dunst, mako and swaync
- 屏幕共享：pipewire + wireplumber
- GUI权限密码输入：polkit-kde-agent
- 状态栏：waybar 详情参阅：https://github.com/Alexays/Waybar/wiki/Module:-Hyprland

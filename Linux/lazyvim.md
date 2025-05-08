# LazyVim for Ambitious Developers
URL: <https://lazyvim-ambitious-devs.phillips.codes/course/chapter-1/>
Date: 2025-04-27 19:41

---

## 1. Introduction and Installation

预备:
1. neovim
2. a nerd font
3. git
4. fzf, lazygit, ripgrep, fd 

Cleanup command:
```bash
$ rm -rf ~/.config/nvim
$ rm -rf ~/.local/share/nvim
$ rm -rf ~/.local/state/nvim
$ rm -rf ~/.cache/nvim
```

Installation:
```bash
$ git clone https://github.com/LazyVim/starter ~/.config/nvim
$ rm -rf ~/.config/nvim/.git
```

> Lazy.nvim严格上来说是插件管理器，而LazyVim是一组捆绑在一起的插件和配置。其中之一就是 Lazy.nvim。
`Space+l`进入Lazy.nvim, `q`退出

## 2. 模态编辑

LazyVim 中的“模式”简单来说就是不同的按键在不同的模式下有不同的含义。
给定键的行为取决于当前模式。

Normal模式下的几个释义:
- p: put, paste
- C-r: redo
- i: insert
- a: append, after
- o: Open a new line.
- gi: Go to the last place you entered Insert mode, and enter Insert mode again.

## 3. 导航

flash.nvim插件给出了一种导航模式: 可以三次击键定位到目标
- s: 启动/激活flash.nvim(seek模式)
- 目标字符: 目标字符后出现"标签字符"
- 标签字符: 直接跳转
**如果目标字符太多, 标签用尽, 可输入两个进一步精确查找目标**
适用于当前视图可见的字符, 如果想通篇搜索需要另外的方式(如内置的"/")
**思维模型:** s进入导航模式后, 你的眼神已经盯着目标位置了, 点击目标位置字符, 此时后面出现亮色的导航标签符号, 键盘点击即可.
一切显得那么自然, 有点<mark>眼随心动, 眼到手到</mark>的意思!

滚屏:
- C-d: 向下半屏(down)
- C-u: 向上半屏(up)
- C-f: 向下一屏(forward)
- C-b: 向上一屏(back)

按单词移动:
- w: 下一单词的首字母(单词判断标准为连续的纯字母, 如: range(num)被视为四个单词)
- e: 下一单词的尾字母
- b: 前一单词首字母
- W: 仅以空格识别为单词分隔符
- B: 同上

行内移动:
- ^: 非空字符行首
- 0: 绝对行首
- $: 行尾
- I: 行首并Insert
- A: 行尾Append

行间移动:
- G: 尾行
- gg: 首行
- nG: 第n行
- :n: 第n行
- C-o: 回到上一个位置

## 4. 打开文件

snacks.nvim 文件选择器插件
`Space Space`: 打开"当前项目中的文件"选择器
直接输入关键词选中即可
`Space f f` root: 当前项目的根目录
`Space f F` cwd: 当前工作目录--即终端在哪个目录打开的neovim, 

`Space e/E` 资源管理器:  -- root/cwd
- 在根目录时`<Backspace>`去往更高一级目录
- `?`: 显示快捷键

## 5. 配置和插件基础

插件的三个类别:
1. LazyVim本身预安装的, 如: snacks.nvim等
2. Lazy Extras, 默认未启用
3. 第三方插件

懒加载扩展模式打开: `:LazyExtras`
导航, `x`启用/禁用
重启生效

### 5.1 禁用内置插件
`~/.config/nvim/lua/plugins/disabled.lua`
```zsh
return {
    { "akinsho/bufferline.nvim", enabled = false },
}
```

## 6. 基本编辑

### 6.1 vim命令思维模型
motion: `s`, `hjkl`, 'web'... 统称为移动命令
count: 计数
verb: d, c... 动词--操作
<verb><count><motion>一个完整的操作
`d3W`: 删除后面的三个以空格分隔的单词
<动作><介词><移动>: 另外一个更常用的方法
`ci"`: 删除""内的全部内容并进入Insert模式   # c: change, i: inside 后跟的是成对出现的符号
`da[`: 删除[]里的内容,包括[]一起删除        # d: delete, a: all   

动词/动作:
- d: 删除   d3w, 3dw亦可, d^
- c: 删除并进入Insert   cw, 
    - c$ 等效 C
    - d$ == D
- 整行: dd, cc
- dl == x, 5dh == 5X
- r: 替换
- C-r: 进入替换模式, ESC退出
- ~: 反转光标下字符的大小写
- .: 再做一次
- u: undo撤销

### 6.2 宏

录制:
q<单字母名字>操作q
回放:
Q: 最近的录制
@<单字母名字>

## 8. 可视模式 剪贴板 寄存器和选择

### 8.1 可视模式
- v: 字符选取模式
- V: 行模式
- C-v: 列模式

Python中批量添加"#"注释:
- C-v行首若干
- I #<space>
- ESC ESC两遍

同理, 用处不太大的批量行尾添加
- C-v行尾若干
- A "foo"
- ESC两遍
一般行尾参差不齐, 列模式不好用; 一般用宏替代, 当然行首也可用宏替代
更通用的办法: 宏录制对一行的操作, 重复播放

### 8.2 剪贴板
每次使用`d`或`c`时, 删除的文本都会自动剪切到剪贴板.
p: 粘贴
y: 复制(yank)
    `ya{`: 复制包括大括号在内的所有内容
    思维模型: 先明确要复制再划定复制范围

> 如果思维模型一直停留在经典的先划定范围再复制的话, 那么就结合可视化模式进行操作
> 不仅如此, 可视化模式同时允许`d`和`c`等操作
同理: `gv`可快速回到上次可视化操作的地方, 同时进入可视化模式

### 8.3 寄存器
寄存器是一种存储要稍后访问的文本字符串的方法
Registers are a way to store a string of text to be accessed later
Vim中有几十个其他寄存器.

#### 命名寄存器
存入: `"ad3w`, 则存入a寄存器. 一般语法: `"a<verb>{<count>}<motion>`
追加存入: `"A<verb>{<count>}<motion>`
查看最近: `"`
粘贴: `"ap`

这样最少可以有26个命名寄存器可用, 每个寄存器中有若干内容, 大幅提高粘贴效率

**Tips**:
*虽然听起来很美好, 但记忆负担过重, 以及操作繁琐, 并不推荐使用, 仅作了解皆可.*

## 9 缓冲区/窗口/标签和会话

### 9.1 Scratch Buffers 暂存缓冲区

*Tips:*
暂存缓存区是保存项目笔记(README)的便捷区域
- `<Space>.`打开的浮动窗口就是这个缓存区
- 写入保存至当前工作目录
- `q`: 退出/隐藏这个浮动窗口
- 随时`<Space>.`调出
非常方便快捷!
从它保存的位置可以推断出: **最好在项目根目录进入Neovim!**, 同时还统一了"root"和"cwd"!

`<Space>S`: 查看所有的临时缓冲区

### 9.2 窗口

- `<Space>wv`: 左右窗口
- `<Space>ws`: 上下窗口
- `<Space>wh/l/j/k`: 光标在窗口间移动
- `<Space>wq`: 关闭窗口, 如果当前只有一个窗口则退出Neovim
- `<Space>wd`: 关闭窗口, 如果当前只有一个窗口则报错并拒绝关闭
- `<Space>wo`: 除当前窗口外, 关闭其他窗口
- `<Space>w+/-`: 调节窗口高度
- `<Space>w>/<`: 调节窗口宽度
- `<Space>w=`: 重置窗口高宽

如上表可见, 重复的`<Space>w*`操作起来异常繁琐! 有一种超神的"Hydra mode"可完美解决
- `<Space>w<Space>`: 进入Hydra模式, 此时可随意单键创建/移动/关闭/调节窗口, 直到`<Esc>`退出"Hydra模式"

#### 另外两个模式
- `<Space>uz`: 进入/退出禅模式
- `<Space>uZ`: 进入/退出缩放模式
<mark>用处不大!</mark>

### 9.3 标签
`<Space><Tab>`: 打开标签页菜单
有时间慢慢玩一下就明白了

### 9.4 代码折叠
顾名思义, 仅对代码结构起效; `z`打开折叠菜单
将光标移动至代码"结构"行, `zc`折叠, `zo`打开折叠.

后面还有很多, 目前用不上, 略过
Done: 2025-04-28 07:21

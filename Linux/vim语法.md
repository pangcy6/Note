# Vim语法/原则

[source](https://www.bilibili.com/video/BV1s4421A7he/?spm_id_from=333.1007.top_right_bar_window_default_collection.content.click&vd_source=6221163a0ce8d87d3ee621206658632c)
Date: 2024.11.19
Author: 郁结YuJie

---

## 1.初识Vim

> Edit Text at the Speed of Thought 《Practical Vim》

**高效的移动、编辑、批量操作。**

Normal模式基本移动：

- hjkl：上下左右
- gg：跳到第一行
- G：跳到最后一行
- <C-u>/<C-b>：向上翻半/一页    up & backforward
- <C-d>/<C-f>: 向下翻半/一页    down & forward
- {No.}gg: 跳到第No.行
- zz/zt/zb: 光标行 设置为屏幕居中/第一行/最后一行

进入Insert模式：

- i：insert，当前光标之前开始插入
- a：append，当前光标之后开始插入
- o：下方插入新的一行，然后开始输入
- s：删除当前光标的字符，然后开始输入
- I：当前行首开始输入
- A: 当前行尾开始输入
- O：上方插入新的一行，开始输入
- S：删除当前行，然后开始输入

Command模式：

- :w
- :q
- :q!
- :wq
- :h {command}: 现实关于Command命令的帮助

Visual模式：

- v：进入可视模式
- 进入可视模式后可用Normal模式下的移动命令选择文本
- x/y: 剪切/复制；回到Normal下p粘贴
- V：进入行可视模式
- <C-v>：进入列可视模式

## 2.移动与编辑

hjkl是基于字符的移动，虽精确但低效。

基于单词的移动(汉语！)：

- w：word，跳到下一个单词的开头
- b：back，跳到上一个单词的开头
- e：end，跳到下一个单词的结尾
- ge：e的反向版本，跳到上一个单词的结尾
- W、B、E: 大写版本对应的单词是连续的非空字符,包括连字符等（如：open-source,对于W来说就是一个单词，w则是3个单词)

基于搜索的移动：

- 行内搜索
  - f{char}/t{char}: 跳到本行下一个`char`字符出现处/出现前
  - ;/,: 快速向后/向前重复ft查找
  - F{char}/T{char}: 小写版本的反向搜索
- 文件中搜索：
  - /{pattern}：跳到文件中下一个`pattern`出现的地方
  - ?{pattern}: 反向
  - `pattern`可以是正则表达式
  - `*`：表示当前光标下的单词，等价于`/{pattern}`
  - n/N: 相反方向的重复查找

基于标记的移动：

- m{mark}: 把当前位置标记为`mark`
- `\`{mark}`: 跳到名为`mark`的标记位置
- `mark`：是a-z的字符
- 内置标记：
  - `\`\``: 上次跳转前的位置
  - `\`.`: 上次修改的位置
  - `\`^`: 上次插入的位置
- 其他实用跳转：（Shift+456）
  - 0/^/$: 跳到本行的行首/非空字符的行首/行尾
  - %: 跳到匹配的配对符处

Operator + Motion = Action
**`操作符 + 移动` 是非常重要的操作逻辑，允许你组合出各种动作**
常见操作符：

- c：change，修改，删除内容并进入插入模式
- d；delete, 删除
- y：yank，复制
- v: visual，选中文本，进入可视模式

几个例子：

- dgg：删除到第一行
- ye：复制到单词结尾
- d$: 删除到行尾
- dt;: 删除直到分号为止的内容。（t, till)

重复操作：

- `.`: 重复上一次的修改
- u：撤销上次的修改 undo
- <C-r>: 重做上一次的修改

批量操作：
{count}{action}: 重复`count`次`action`动作

- 4j：向下移动4行
- 3dW：删除3个单词
- 2yy：复制2行
- 4p：粘贴4次

## 3.文本对象操作

{operator}{textobjects}的操作逻辑
格式：i/a + 对象
其中i代表"inner", 内部；a代表"all",额外包括周围的空格或配对符
常见的对象：

- w/W, s, p: 单词(word)、句子(sentence)、段落(paragraph)
- (/), [/], {/}, </>, '/": 配对符定义的对象

文本对象操作：例子
文本对象提供了为文本赋予了**结构化**的含义，允许我们以一个语义对象作为操作单元
{count}{operator}{textobjects}

- diw: 删除一个单词
- ci(：修改小括号内部
- yi{: 复制大括号内部
  配合`.`命令或[count]可以简单的完成多次对特定语义对象的操作

textobjexts VS motion
{operator}{motion} and {operator}{textobjects}
解耦了操作与操作的对象，大大提升了操作效率

- `motion`是能够移动光标的命令，可以单独使用（如wbe）
- 文本对象只能跟在`operator`后面，不能独立使用
- `motion`通过光标的移动确定`operator`的作用范围，玩味更加灵活但不够明确
- `textobjects`则是显式地指定操作的对象，范围明确

通过安装扩展程序来实现更加强大的操作，如：vim-easymotion, vim-surround等等

操作符与命令补充：

- gu/gU/g~: 操作符，转小写/转大写/翻转大小写
- J：join，连接两行
- <C-a>/<C-x>: 增加/减小数字
- g<C-A>: 创建递增序列
- </>: 左/右缩进

**建议：让你的命令更模块化**：
尽量使你的命令更模块化，具有清晰的含义与作用范围，以便于和`.`等命令协同。
如：`daw`比`dw`具有更清晰的语义，也更模块化

`vi{d`效果上等同于`diw`,但第一个操作可以不必光标跳到目标位置

练习技巧：
刚开始不熟练时，可能不确定`motion`或`textobjects`具体覆盖了哪部分文本，可以先用
`v{motion}`/`v{textobjects}`将范围选中，再执行c/d/y等操作。
熟练掌握后，尽可能直接使用完整的命令进行操作，`diw`比`viwd`更加模块化，也更容易进行重复操作

## 4.寄存器与宏

寄存器：
Vim提供了许多寄存器用于存放内容，可以理解为剪贴板；一个字符对应一个寄存器（如a-z，0-9）
特别的寄存器：

- `"`: 默认寄存器，平时复制、删除的内容都存放在这里
- `%`: 当前文件名
- `.`: 上一次插入的内容
- `:`: 上一次执行的命令
  通过`:reg {register}`查看对于寄存器中的内容

指定寄存器：
在复制/删除/粘贴等操作前加上`"{register}`就可以指定本次操作的寄存器

- `"ayy`：将这一行复制到`a`寄存器中
- `"bdiw`：将单词删除，保存到`b`寄存器中
- `"cp`：将`c`寄存器中的内容粘贴出来
  常见用途：将想要持久保存的文本放到指定寄存器里，随时进行粘贴，避免被覆盖
  寄存器字符大写：在寄存器中添加内容而非覆盖

**宏**(Macro)：录制一系列键盘操作，并允许我们重放这些操作
操作系列存储在指定的寄存器中：

- `q{register}`: 开始录制宏，存在寄存器`register`中
- 录制过程中安`q`退出录制
- `@{register}`: 重放寄存器`register`中的操作
- `@@`重放上一次宏操作

注意：**`.`命令对宏不生效，`.`命令只记录上一次修改，而宏可能包含多次修改**

建议：让你的宏对连续重放友好

1. 让你的光标移动更加适应一般情况，general
2. 假设你要在多个特定的位置进行特定的操作，一个好的习惯是在宏录制的最后，跳转到下一个需要编辑的位置。即：宏包括{编辑动作} + {跳转到下一个需要编辑的位置}

通过大写的寄存器，在宏的后面添加命令
极致的宏重放操作：[count]@{register}

## 5.命令模式

命令模式的操作对象以“行”为基本单位

Ex命令的格式
`:[range] {excommand} [args]`

- range: 可选的作用范围，缺省为本行
- args：参数

一些ExCommand (`[x]`为可选的寄存器)

- `:[range] d [x]`  delete
- `:[range] y [x]`  yank
- `:[range] p [x]`  print 

range & address: 指定范围
range 由一个活两个address构成，即：{address} or {address},{address}
`address`可以是：

- `{lineNo}`: 行号
- `{lineX},{lineY}`: 从第X行到第Y行
- `$`: the last line
- `.`: 光标所在行
- `/{pattern}/`: next `pattern` 所在的行
- `.+3`: 光标往下第三行
- `$-4`: 文件倒数第5行
- `%`: 当前文件的所有行，特殊的range
- `0`: 作为虚拟的行地址，可以用来将内容插入到第一行

行的复制、移动和粘贴

- `:[range] copy {address}` 把`range`中的行复制到`address`后面
- `:[range] move {address}` 把`range`中的行移动到`address`后面
- `:[address] put [x]` 把寄存器`x`中的内容粘贴到`address`后面

Ex命令和Normal模式下的编辑有区别吗？

- 命令模式下的编辑操作以“行”为单位
- 命令模式下的编辑操作无需移动光标

批量操作：Normal命令
格式：`:[range] normal {command}`
含义：对`range`中的所有行执行normal模式下的命令`command`

- 将`range`设置为`%`，可以对整个文件的所有行执行
- `:[range] normal .`: 配合`.`命令，效果超群
  - 常用做法：先做一次修改，再用normal命令在指定的行上完成操作
- `.`命令只记录一次修改，用宏可以实现记录多个操作
- `:[range] normal @{register}`
  - 常用做法：先把想要的操作录制成宏，再用normal命令在指定的行上重放宏
- 实例：
  - `:1，4 normal I# `: 在前四行的行首添加“#空格” 
  - `:% normal I# `: 在所有行的行首添加
  - `:., $ normal @a`: 从当前行到文件结尾所有行重放宏a

批量操作：global命令
格式：`:[range] global/{pattern}/[cmd]`
含义：对`range`中包含`pattern`的所有行执行Command模式下的Ex命令
`cmd`缺省为`print`
注意：`normal`也是Ex命令
`:[range] global/{pattern}/normal {command}`: 对`range`中所有带`pattern`的行，执行normal模式下的命令`command`
例子：`:% global /TODO/d`: 删除所有含`TODO`的行
`Vi{global/old_api/normal O//TODO:upgrade it!`: 进入行Visual模式选择花括号之中的内容全局选择包含`old_api`的行执行normal模式下的：在前面一行添加`//TODO:upgrade it!`内容

替换命令
`:[range]s/{pattern}/{string}/[flags]`: 将`pattern`替换为`string`

- s: subtitute/代替
- flags:
  - g: 替换每一行的所有匹配
  - i：忽略大小写
  - c：替换前进行确认
  - n：计数而不是替换

小结：

- 了解常见的Ex命令
- 了解`address`和`range`的概念
- **掌握如何使用Normal命令批量运行Normal模式的命令**
- **掌握如何使用global命令批量运行command模式的Ex命令**

## 6.总结与回顾

高效移动，高效编辑，高效批量操作
![img](https://s3.bmp.ovh/imgs/2024/11/20/bff2704eef373b39.png)

几点经验：

- Edit text at the speed of thought
- 将想要的操作分解为移动和编辑的组合
- 让你的操作（移动、编辑）含义明确
- 时刻思考，想要的效果能否分解为一系列的重复的操作（Vim对重复操作十分友好）

<mark>END!</mark>
2024.11.20

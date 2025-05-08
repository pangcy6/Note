# vim笔记

---

> Vim the Six Billion Dollar edidtor
> Better,Stronger,Faster.

## 练级攻略

Vim自带的教程:

- vimtutor
- vimtutor zh_cn

### 第一级 - 存活

        i → Insert 模式，按 ESC 回到 Normal 模式.
        x → 删当前光标所在的一个字符。
        :wq → 存盘 + 退出 (:w 存盘, :q 退出)   （注：:w 后可以跟文件名）
        dd → 删除当前行，并把删除的行存到剪贴板里
        p → 粘贴剪贴板
    
    推荐:
    
        hjkl (强烈推荐使用其移动光标，但不必需) →你也可以使用光标键 (←↓↑→). 注: j 就像下箭头。
        :help <command> → 显示相关命令的帮助。你也可以就输入 :help 而不跟命令。（注：退出帮助需要输入:q）

### 第二级 - 感觉良好

1. **各种插入模式**
   
        a → 在光标后插入
        o → 在当前行后插入一个新行
        O → 在当前行前插入一个新行
        cw → 替换从光标所在位置后到一个单词结尾的字符

2. **简单的移动光标**
   
        0 → 数字零，到行头
        ^ → 到本行第一个不是blank字符的位置（所谓blank字符就是空格，tab，换行，回车等）
        $ → 到本行行尾
        g_ → 到本行最后一个不是blank字符的位置。
        /pattern → 搜索 pattern 的字符串（注：如果搜索出多个匹配，可按n键到下一个）

3. **拷贝/粘贴**
   
        P → 粘贴
        yy → 拷贝当前行当行于 ddP

4. Undo/Redo
   
        u → undo
        <C-r> → redo

5. **打开/保存/退出/改变文件(Buffer)**
   
        :e <path/to/file> → 打开一个文件
        :w → 存盘
        :saveas <path/to/file> → 另存为 <path/to/file>
        :x， ZZ 或 :wq → 保存并退出 (:x 表示仅在需要时保存，ZZ不需要输入冒号并回车)
        :q! → 退出不保存 :qa! 强行退出所有的正在编辑的文件，就算别的文件有更改。
        :bn 和 :bp → 你可以同时打开很多文件，使用这两个命令来切换下一个或上一个文件。
        （注：我喜欢使用:n到下一个文件）
   
   ### 第三级 - 更好,更强,更快.
   
   **更好**

Vim重复

    . → (小数点) 可以重复上一次的命令
    N<command> → 重复某个命令N次

下面是一个示例:

- 2dd → 删除2行
- 3p → 粘贴文本3次
- 100idesu [ESC] → 会写下 “desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu desu “
- . → 重复上一个命令—— 100 “desu “.
- 3.→ 重复 3 次 “desu” (注意：不是 300，你看，VIM多聪明啊).

**更强**  
更有效率的移动光标

1. NG → 到第 N 行 （注：注意命令中的G是大写的，另我一般使用 : N 到第N行，如 :137 到第137行）

2. gg → 到第一行。（注：相当于1G，或 :1）

3. G → 到最后一行。

4. 按单词移动：
   
   - w → 到下一个单词的开头。
   
   - e → 到下一个单词的结尾。
     
     > 如果你认为单词是由默认方式，那么就用小写的e和w。默认上来说，一个单词由字母，数字和下划线组成（注：程序变量）
     
     > 如果你认为单词是由blank字符分隔符，那么你需要使用大写的E和W。（注：程序语句

![move](http://yannesposito.com/Scratch/img/blog/Learn-Vim-Progressively/word_moves.jpg)

**最强**的光标移动

- % : 匹配括号移动，包括 (, {, [. （注：你需要把光标先移到括号上）
- \*和 #:  匹配光标当前所在的单词，移动光标到下一个（或上一个）匹配单词（*是下一个，#是上一个）

**更快**

你一定要记住光标的移动，因为很多命令都可以和这些移动光标的命令连动。很多命令都可以如下来干：

    <start position><command><end position>

 例如 0y$ 命令意味着：

- 0 → 先到行头
- y → 从这里开始拷贝
- $ → 拷贝到本行最后一个字符

你可可以输入 ye，从当前位置拷贝到本单词的最后一个字符。

你也可以输入 y2/foo 来拷贝2个 “foo” 之间的字符串。

还有很多时间并不一定你就一定要按y才会拷贝，下面的命令也会被拷贝：

- d (删除 )
- v (可视化的选择)
- gU (变大写)
- gu (变小写)
- 等等

可视化选择是一个很有意思的命令，你可以先按v，然后移动光标，你就会看到文本被选择，然后，你可能d，也可y，也可以变大写等

### 第四级 - Vim超能力

在当前行上移动光标: 0 ^ $ f F t T , ;

        0 → 到行头
        ^ → 到本行的第一个非blank字符
        $ → 到行尾
        g_ → 到本行最后一个不是blank字符的位置。
        fa → 到下一个为a的字符处，你也可以fs到下一个为s的字符。
        t, → 到逗号前的第一个字符。逗号可以变成其它字符。
        3fa → 在当前行查找第三个出现的a。
        F 和 T → 和 f 和 t 一样，只不过是相反方向。
        dt" → 删除所有的内容，直到遇到双引号"

![tmove](http://yannesposito.com/Scratch/img/blog/Learn-Vim-Progressively/line_moves.jpg)        

区域选择 

    <action>a<object> 或 <action>i<object>

- action可以是任何的命令，如 d (删除), y (拷贝), v (可以视模式选择)。
- object 可能是： w 一个单词， W 一个以空格为分隔的单词， s 一个句字， p 一个段落。也可以是一个特别的字符："、 '、 )、 }、 ]。

假设你有一个字符串 (map (+) ("foo")).而光标键在第一个 o 的位置。

        vi" → 会选择 foo.
        va" → 会选择 "foo".
        vi) → 会选择 "foo".
        va) → 会选择("foo").
        v2i) → 会选择 map (+) ("foo")
        v2a) → 会选择 (map (+) ("foo"))

![action](http://yannesposito.com/Scratch/img/blog/Learn-Vim-Progressively/textobjects.png)

块操作: C-v

块操作，典型的操作： 0 C-v C-d I-- [ESC]

    ^ → 到行头
    <C-v> → 开始块操作
    <C-d> → 向下移动 (你也可以使用hjkl来移动光标，或是使用%，或是别的)
    I-- [ESC] → I是插入，插入“--”，按ESC键来为每一行生效。

![block](http://yannesposito.com/Scratch/img/blog/Learn-Vim-Progressively/rectangular-blocks.gif)    

自动提示： C-n 和 C-p

在 Insert 模式下，你可以输入一个词的开头，然后按 C-p或是C-n，自动补齐功能就出现了……  
![note](http://yannesposito.com/Scratch/img/blog/Learn-Vim-Progressively/completion.gif)

**宏录制： qa 操作序列 q, @a, @@**

    qa 把你的操作记录在寄存器 a。
    于是 @a 会replay被录制的宏。
    @@ 是一个快捷键用来replay最新录制的宏。

示例:
在一个只有一行且这一行只有“1”的文本中，键入如下命令：

    qaYp<C-a>q→
        qa 开始录制
        Yp 复制行.
        <C-a> 增加1.
        q 停止录制.
    @a → 在1下面写下 2
    @@ → 在2 正面写下3
    现在做 100@@ 会创建新的100行，并把数据增加到 103.

![宏](http://yannesposito.com/Scratch/img/blog/Learn-Vim-Progressively/macros.gif) 

**可视化选择： v,V,C-v**  
一旦被选好了，你可以做下面的事：

- J → 把所有的行连接起来（变成一行）
- < 或 > → 左右缩进
- = → 自动给缩进 （注：这个功能相当强大，我太喜欢了）

![v](http://yannesposito.com/Scratch/img/blog/Learn-Vim-Progressively/autoindent.gif)

在所有被选择的行后加上点东西：

    <C-v>
    选中相关的行 (可使用 j 或 <C-d> 或是 /pattern 或是 % 等……)
    $ 到行最后
    A, 输入字符串，按 ESC。

![add](http://yannesposito.com/Scratch/img/blog/Learn-Vim-Progressively/append-to-many-lines.gif)

**分屏: :split 和 vsplit.**

下面是主要的命令，你可以使用VIM的帮助 :help split. 你可以参考本站以前的一篇文章VIM分屏。

    :split → 创建分屏 (:vsplit创建垂直分屏)
    <C-w><dir> : dir就是方向，可以是 hjkl 或是 ←↓↑→ 中的一个，其用来切换分屏。
    <C-w>_ (或 <C-w>|) : 最大化尺寸 (<C-w>| 垂直分屏)
    <C-w>+ (或 <C-w>-) : 增加尺寸

![split](http://yannesposito.com/Scratch/img/blog/Learn-Vim-Progressively/split.gif)

---

### 结束语

    上面是作者最常用的90%的命令。
    我建议你每天都学1到2个新的命令。
    在两到三周后，你会感到vim的强大的。
    
    有时候，学习VIM就像是在死背一些东西。
    幸运的是，vim有很多很不错的工具和优秀的文档。
    运行vimtutor直到你熟悉了那些基本命令。
    其在线帮助文档中你应该要仔细阅读的是 :help usr_02.txt.
    你会学习到诸如  !， 目录，寄存器，插件等很多其它的功能。

学习vim就像学弹钢琴一样，一旦学会，受益无穷。

### Some else

hotkey

    :map  I# <ESC>
    :map  0xx
    
    :n1,n2s/^/# /g
    :n1,n2s/^# //g

Read in somefile

    :r /path/to/filename

run program in vim:

    :!command

put the result of command in vim

    :r !command

==========================================================================================================

# 台湾高见龙的视频教程

[bilibili](https://www.bilibili.com/video/BV1KK411w7wi?from=search&seid=7768804738401130377)

基本操作:

- i = insert
- I = 行首insert
- a = append
- A = 行尾insert
- o = new line
- O = 上一行insert
- ESC/Ctrl + [ = Normal
- :w = 存档
- :q = 离开
- :q! = 不存档离开
- :wq/:x = 存档离开

光标移动:

- Ctrl + z = 把当前任务暂存至背景
- fg = 恢复之前的工作
- hjkl = 左下上右
- w/W = 向前进一个word
- b/B = 向后退一个word
- { = 移动到上一个段落
- } = 移动到下一个段落
- gg = 整个文档第一行
- G = 整个文档最后一行
- 0 = 行首
- $ = 行尾

搜索:

- /word = 搜索word
- :set hlsearch = 高亮搜索目标 
- fx/Fx = 向后/前搜索同一行最近的x
- zz/zt/zb = 把目标行放置在中部/头部/尾部

选取,复制,贴上:

- v = 切换到Visual模式
- V = 切换到Visual模式并选取一整行
- y/yy = 复制/复制一行
- p/pp = 贴上/按整行贴上
- :set clipboard=unnamed = 让剪贴板和暂存器共通
- y$/y0 = 复制光标处到行尾/行首 其他同理
- u = undo
- Ctrl + r = redo
- "ay = 把内容存到a暂存器
- "by = 把内容存到b暂存器
- "ap = 贴上a暂存器的内容
- :reg = 查看目前所有暂存器的内容   #vim有48个暂存器
- x = 删除光标所在文字并把删除的内容放到暂存器
- d = 删除选取的内容,放入暂存器
- D = 删除光标后的内容,放入暂存器
- dd = 删除整行,放入暂存器
- c = 类似d,并且进入insert模式
- C = 删除光标后的内容并进入insert模式
- r = 进入replace模式一次
- R = 持续进入replace模式,按Esc退回到Normal
- > > /<< = 增加/减少缩进
- = = 按特定语言特点进行符合语法的排版

编辑多个文档:

- :e filename = 开启文档
- :tabe = 开新标签页
- gt/gT = 跳转到下一个/上一个标签页
- :new = 新增水平分割窗口
- :vnew = 新增垂直分割窗口
- Ctrl+ww = 窗口跳转 
- vim -o/O = 用水平/垂直分割窗口打开文档
- vim -p = 用标签页的方式打开多个档案

buffer/window/tab:

- A buffer is the in-memory text of a file.
- A window is a viewport on a buffer
- A tab is a collection of windows.

Buffer:资料保存
Window:展示资料
Tab:排版布局

vim file1 file2 file3
这时,就存在一个buffer,默认显示file1,可见的就是一个window,至于tab各个window的存在形式是也.
:ls 显示打开的文件,并分配编号
:b2 显示file2
:b 全名或部分文件名 直接到某个文件
:bn 下一个文件
:bp 前一个文件
:bl 最后一个
:bf 最前面一个
Ctrl+^: 最近的两个文件切换  #这个最实用一般情况下最多就是打开两个文件
:bd 关掉当前文件
:tab ba 把全部的Buffer展开成Tab

更多选取方式:

Ctrl+v: 进入Visual Block模式,批量加入注释很好用

viw: 在单词的任意位置精确选取这个单词
vi": 选取""内的所有内容 #i inner 
vit: 选取tag里的内容    #t tag
va": 上述内容加上""本身选取 #a around
v{: 选取光标所在上一段落(程序中)    #v可以换成d或c的哦 d=delete, c=change
v}: 选取光标所在下一段落

diw: 直接删除光标所在单词
ciw: 删除并进入insert模式

vim text object:
名词:
w = word
s = sentence
p = paragraph
t = tag
'
"
(
[
{

动词:
y = yank
p = paste
d = delete
c = change
r = replace
v = visual

范围:
i = inner
a = aroud

量词:
数字

组合技!:
viw: 选word
vis: 选取句子
dis: 删除句子
cis: 删除句子并进入insert
yis: 复制一个句子
......

其他实用的小技巧:
0: 到行首
^: 到行首第一个非空白字符
Ctrl+f: 向前一页
Ctrl+b: 向后一页

先选取某一段落zf: 折叠这一段落
zfip: 上述操作的组合技!
zd: 展开折叠部分
.: 重复动作,需要慢慢体会

编辑模式下(终端模式下也适用):
Ctrl+w: 回删一个word
Ctrl+u: 回删光标前的所有

设定:
:help key-notation 特殊键设定帮助
其他内容请参考~/.vim/vimrc

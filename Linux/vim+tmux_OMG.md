# vim + tmux - OMG! Code

[source](https://www.youtube.com/watch?v=5r6yzFEXajQ&list=TLPQMjAwMzIwMjIz27Oo6I6rdA&index=4)
date: 2022-03-21

## 1. vim

> But I need an IDE
> No you don't!

Why vim?

- highly customizable
- runs everywhere
- works with many programming languages
- scriptable

*MacOS*:`brew install macvim --override-system-vim`

### 1.1 Modal editing

Change the meaning of the keys in each mode of operation

- Normal mode: navigate the structure of the file
- Insert mode: editing the file
- Visual mode: highlight portions of the file to manipulate at onece
- Ex mode: command mode

> DON'T USE ARROW KEYS
> DON'T USE MOUSE
> You're a programmer. Strive to be lazy.
> 
> > h j k l

- ^E: scroll the window down
- ^Y: scroll the window up
- ^F: scroll down one page
- ^B: scroll up one page
- H: Move cursor to the top of the window
- M: move cursor to the middle of the window
- L: Move cursor to the bottom of the window
- gg: go to top of file
- G: go to bottom of file

### 1.2 The secret sauce

- text objects and motions
- the DOT command
- macros

#### 1.2.1 Text objects and motions

> Think of a file as more than indevidual characters
> text objects:

- w: words
- s: sentences
- p: paragraphs
- t: tags (available in XML/HTML files)

Motions:

- a: all
- i: in
- t: (un)'til
- f: find forward
- F: find backward

Combine with commands
Commands:

- d: delete(also cut)
- c: change(delete, then place in insert mode)
- y: yank(copy)
- v: visually secect

<mark>语法：{command} {text object or motion}</mark>

Example:

- diw: delete in word
- caw: change all word (cw: change [part of] word after cursor)
- yi): yank all text inside parentheses (di[: delete in []删除中括号中的全部内容)
- dt(space): delete until the space including the space
- df(space): delete until the space including the space
- va": visually select all inside doublequwtes and including doublequotes
  - va'
  - va(
  - va<
  - ...

#### 1.2.2 Repetition The DOT command

> Repeat the last command
> It's powerful!
> By the way. u means undo and . means redo

Additional commands:

- dd/yy: delete/yank the current line
- p/P: past new line below/above current line
- D/C: delete/change until end of line
- ^/$: move to the beginning/end of line
- I/A: move to the beginning/end of line and insert
- o/O: insert new line below/above current line and insert

顶级后悔药：`:earlier 2m`回到2分钟之前的状态!哈哈哈哈哈哈！
终极杀手锏：`:q!`

> Try and make actions repeatable: PRACTICE IT!
> BE CAREFUL: Not everything is repeatable. at least with the DOT command

#### 1.2.3 Macro

> A sequence of commands recorded to a register

Record a macro:

- q{register}
- (do the thing)
- q

play a macro

- @{register}

<mark>NB!!!</mark>

### 1.3 Plugins

- vundle: plugin manager
- nerdtree: file drawer
- ctrlp: fuzzy file finder
- fugitive: git tool
- syntastic: syntax checker/linter

## 2. tmux

- Terminal multiplexer
- View and control multiple consoles
- Preconfigure environments

<mark>tmux new-session -s {session-name}</mark>

> Don't copy someone else's configurations, Make it your own.
> You can steal idea but not code.

## 3. vim+tmux=vimux

I love vimux!

# Markdown 语法说明
---
## 概述
Markdown的目标是实现“易读易写”。语法全由一些符号所组成，这些符号经过精挑细选，其作用一目了然。比如：在文字两旁加上星号，看起来就像*强调*。Markdown的列表看起来，嗯，就是列表。Markdown的区块引用看起来就真的像是引用一段文字，就像你曾在电子邮件中见过的那样。
###兼容HTML
Markdown语法的目标是：成为一种适用于网络的**书写**语言。

Markdown不是想取代HTML，他的理念是：能让文档更容易读、写和随意改。HTML是一种**发布**的格式，Markdown是一种**书写**的格式。这样，Markdown的格式语法只涵盖纯文本可以涵盖的范围。

不在Markdown涵盖范围之内的标签，都可以直接在文档里面用HTML撰写。不需要额外标注这是HTML或是Markdown;只要直接加标签就可以了。

要制约的只有一些HTML区块元素--比如div,table,pre,p等标签，必须在前后加上空行与其他内容区隔开，还要求它们的开始标签与结尾标签不能用制表符或空格来缩进。

例子：在Markdown文件里加上一段HTML表格：

	这是一个普通段落。

	<table>
		<tr>
			<td>foo</td>
		</tr>
	</table>
	
	这是另一个普通段落。

**注意**:
在HTML区块标签见的Markdown格式语法将不会被处理。
HTML的区段（行内）标签span,cite,del可以在Markdown的段落、列表或标题里随意使用。
和处在HTML区块标签间不同，Markdown语法在HTML区段标签*间*是有效的。

### 特殊字符自动转换
在HTML文件中，有两个字符需要特殊处理：< 和 &。<符号用于起始标签，&用于标记HTML实体，如果你只是想要显示这些字符的原型，你必须要使用实体的形式，像是"&lt"和"&amp"(无引号)。

Markdown让你可以自然的书写字符，需要转换的由他来处理好了。

**注意**：

在code范围内，不论是行内还是区块，<和&两个符号都**一定**会被转换成HTML实体。
## 区块元素
### 段落和换行
一个Markdown段落是由一个或多个连续的文本行组成，它的前后要有一个以上的空行。普通段落不该用空格或制表符来缩进。

“由一个或多个连续的文本行组成”这句话暗示了Markdown允许段落内的强迫换行，如果你确实想依赖Markdown来插入br /标签的话，在插入处先键入两个以上的空格然后回车。
### 标题
Markdown支持两种标题的语法，类setext和类atx形式。

类setext形式：

	This is an H1
	=======

	This is an H2
	------------------
任何数量的=和-都可以有效果。

类atx形式：

	# 这是H1
	## 这是H2
	......
	###### 这是H6
### 区块引用：
代码：

	> This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,
	> consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
	> Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.
	> 
	> Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
	> id sem consectetuer libero luctus adipiscing.
效果：
> This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,
> consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
> Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.
> 
> Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
> id sem consectetuer libero luctus adipiscing.

区块引用嵌套：
代码：

	> This is the first level of quoting.
	>
	> > This is nested blockquote.
	>
	> Back to the first level.
效果：
> This is the first level of quoting.
>
> > This is nested blockquote.
>
> Back to the first level.

### 列表
无序列表：  
使用星号*、加号+、减号-作为列表标记

	* Red
	* Green
	* Blue
效果：

* Red
* Green
* Blue

代码等同于：

	+ Red
	+ Green
	+ Blue

或：

	- Red
	- Green
	- Blue
显示效果：

- Red
- Green
- Blue
	- 这是一个二级嵌套
		- 同样的三级嵌套
			- 四级怎么样？
				- 再有呢？

有序列表：

使用数字接着一个英文句号,后面一定要接着至少一个空格或制表符。

等效代码：	

	1. Red
	2. Green
	3. Blue

或：

	1. Red
	1. Green
	1. Blue

甚至：

	8. Red
	1. Green
	1000. Blue

都输出一样的效果：

8. Red
1. Green
1000. Blue

虽然Markdown语法宽松但还是推荐第一种代码写法，原因？.......你猜!

避免出现过敏现象：

	1986\. What a great season.

### 表格

代码：

	|name | age | phone|
	|--- | --- | ---|
	|Tom|32|5593268|
	|zhang|23|8982392|
	|Li|33|13903128888|
效果：

|name | age | phone|
|--- | --- | ---|
|Tom | 32 | 5593268|
|zhang | 23 | 8982392|
|Li | 33 | 13903128888|

### 代码区块
只需要缩进四个空格，或一个制表符即可，直到没有缩进或文件结束。

    <div class="footer">
        &copy; 2004 Foo Corporation
    </div>

### 分隔线
你可以在一行中用三个以上的星号、减号、底线来建立一个分隔线，行内不能有其他东西。你也可以在星号或是减号中间插入空格。下面每种写法都可以建立分隔线：

	* * *

	***

	*****

	- - -

	---------------------------------------

## 区段元素
### 链接
Markdown 支持两种形式的链接语法：** 行内式**和**参考式**两种形式。

不管是哪一种，链接文字都是用 [方括号] 来标记。

行内式：

	This is [an example](http://example.com/ "Title") inline link.
	[This link](http://example.net/) has no title attribute.
显示效果：
This is [an example](http://example.com/ "Title") inline link.
[This link](http://example.net/) has no title attribute.

参考式：参考式的链接是在链接文字的括号后面再接上另一个方括号，而在第二个方括号里面要填入用以辨识链接的标记：

	This is [an example][id] reference-style link.

你也可以选择性地在两个方括号中间加上一个空格：

	This is [an example] [id] reference-style link.

接着，在文件的任意处，你可以把这个标记的链接内容定义出来：

	[id]: http://example.com/  "Optional Title Here"

效果：
This is [an example][id] reference-style link.
This is [an example] [id] reference-style link.
[id]: http://example.com/  "Optional Title Here"

链接内容定义的形式为：

-    方括号（前面可以选择性地加上至多三个空格来缩进），里面输入链接文字
-    接着一个冒号
-    接着一个以上的空格或制表符
-    接着链接的网址
-    选择性地接着 title 内容，可以用双引号或是括弧包着

代码：

	[foo]: http://example.com/  "Optional Title Here"
	[foo]: http://example.com/  (Optional Title Here)

网址定义只有在产生链接的时候用到，并不会直接出现在文件之中。
下面是一个参考式链接的范例：

	I get 10 times more traffic from [Google] [1] than from
	[Yahoo] [2] or [MSN] [3].

 	 [1]: http://google.com/        "Google"
 	 [2]: http://search.yahoo.com/  "Yahoo Search"
	 [3]: http://search.msn.com/    "MSN Search"
显示效果：

I get 10 times more traffic from [Google] [1] than from
[Yahoo] [2] or [MSN] [3].

  [1]: http://google.com/        "Google"
  [2]: http://search.yahoo.com/  "Yahoo Search"
  [3]: http://search.msn.com/    "MSN Search"

如果改成用链接名称的方式写：

	I get 10 times more traffic from [Google][] than from
	[Yahoo][] or [MSN][].

	  [google]: http://google.com/        "Google"
	  [yahoo]:  http://search.yahoo.com/  "Yahoo Search"
	  [msn]:    http://search.msn.com/    "MSN Search"
显示效果相同。

参考式的链接其实重点不在于它比较好写，而是它比较好读。使用 Markdown 的参考式链接，可以让文件更像是浏览器最后产生的结果，让你可以把一些标记相关的元数据移到段落文字之外，你就可以增加链接而不让文章的阅读感觉被打断。

### 强调

Markdown 使用星号（*）和底线（_）作为标记强调字词的符号，被 * 或 _ 包围的字词会被转成用 <em\>标签包围，用两个 * 或 _ 包起来的话，则会被转成 <strong\>
如果你的 * 和 _ 两边都有空白的话，它们就只会被当成普通的符号。

### 代码

如果要标记一小段行内代码，你可以用反引号把它包起来（`），例如：
	
	Use the `printf()` function.

显示效果：
Use the `printf()` function.

### 图片

Markdown 使用一种和链接很相似的语法来标记图片，同样也允许两种样式： 行内式和参考式。

行内式的图片语法看起来像是：

	![Alt text](/path/to/img.jpg)
	![Alt text](/path/to/img.jpg "Optional title")

详细叙述如下：

- 一个惊叹号 !
-   接着一个方括号，里面放上图片的替代文字
-    接着一个普通括号，里面放上图片的网址，最后还可以用引号包住并加上 选择性的 'title' 文字

参考式的图片语法则长得像这样：

	![Alt text][id]

「id」是图片参考的名称，图片参考的定义方式则和连结参考一样：

	[id]: url/to/image  "Optional title attribute"

到目前为止， Markdown 还没有办法指定图片的宽高，如果你需要的话，你可以使用普通的 <img\> 标签。

![wallpaper](http://img.vim-cn.com/cf/c333e0f339a5ec37d7f00f45c501333e070e99.jpg  "beauty girl")

## 其它
### 反斜杠
Markdown 可以利用反斜杠来插入一些在语法中有其它意义的符号
Markdown 支持以下这些符号前面加上反斜杠来帮助插入普通的符号：

	\   反斜线
	`   反引号
	*   星号
	_   底线
	{}  花括号
	[]  方括号
	()  括弧
	#   井字号
	+   加号
	-   减号
	.   英文句点
	!   惊叹号

### 自动链接
Markdown 支持以比较简短的自动链接形式来处理网址和电子邮件信箱，只要是用尖括号包起来， Markdown 就会自动把它转成链接。一般网址的链接文字就和链接地址一样，例如：

	<http://example.com/>
显示效果：
<http://example.com/>
e-mail:

	<address@example.com>

<address@example.com>

## 免费编辑器

Windows平台

- [MarkdownPad](http://markdownpad.com/)
- [MarkPad](http://code52.org/DownmarkerWPF/)

Linux平台

- [Retext](http://sourceforge.net/p/retext/home/ReText/)
- [Remarkable](http://remarkableapp.net/)

Mac平台

- [Mou](http://25.io/mou/)

在线编辑

- [Markable.in](http://markable.in/)
- [Dillinger.io](http://dillinger.io/)

浏览器插件

- [Made](https://chrome.google.com/webstore/detail/made/oknndfeeopgpibecfjljjfanledpbkog)(chrome)







Edit By Remarkable.

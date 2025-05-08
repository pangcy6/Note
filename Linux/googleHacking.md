# Google Hacking笔记

date:2022-03-19
---

> 特殊的需求当然需要特殊的方法才能解决；所谓hacking其实就是使用一些特殊的语法，搜索出意想不到的结果。

## 基本搜索

- 逻辑与：AND, +
- 逻辑或：OR, |
- 逻辑非：NOT, -
- 完整匹配：“关键词”
- 通配符：
  - \*：single-word wildcards
  - . : single-character wildcards
  - ? : 
- 同义词或近义词：~
- 分组：（）如：("web security" | websecrity)

## 高级搜索

- intext：搜索正文中含有关键字的网页。如：intext:后台登录
- intitle：标题中含有关键字的网页。如：intitle:后台登录
- allintitle：类似不过可以多指定几个关键字。如：allintitle:后台登录 管理员
- inurl：url中包含关键词的网页。如: 
  - inurl:Login
  - inurl:/admin/login.php        #管理员登录页面
  - inurl:/phpmyadmin/index.php   #后台数据库管理页面
- allinurl:可以包含多个关键词。如：allinurl:Login admin
- site: 指定访问的站点，或者某大网站次级域名遍历。如：site:baidu.com inurl:Login
- filetype: 指定访问的文件类型。如：site:baidu.com filetype:pdf
- link: 指定链接的网页。如：link:baidu.com
- related: 网页布局相似的网页。如：related:xjtu.edu.cn
- cache: 网页快照。如：cache:hackingspirits.com guest,返回指定缓存并包含guest关键词
- info：返回站点的指定信息.如：info:baidu.com
- define: 返回某个词语的定义，如：define:Hacker
- phonebook: 电话本查询美国街道地址和电话号码信息。如：phonebook:Lisa+CA

## 查找网站后台

- site:xx.com intext:管理
- site:xx.com inurl:login
- site:xx.com intitle:后台

## 查看服务器使用的程序

- site:xx.com filetype:asp
- site:xx.com filetype:php
- site:xx.com filetype:jsp
- site:xx.com filetype:aspx

## 查看上传漏洞

- site:xx.com inurl:file
- site:xx.com inurl:load

## Index of

利用Index of语法去发现允许目录浏览的web网站

- index of /admin
- index of /passwd
- index of /password
- index of /mail
- "index of /"+passwd
- "index of /"+password.txt
- "index of /" +.htaccess
- "index of /root"
- "index of /cgi-bin"
- "index of /logs"
- "index of /config"

## inurl

而上面这些命令中用的最多的就是 inurl: 了，利用这个命令，可以查到很多意想不到的东西

- 利用 allinurl:winnt/system32/ 查询：列出的服务器上本来应该受限制的诸如“system32” 等目录，如果你运气足够好，你会发现“system32” 目录里的“cmd.exe” 文件，并能执行他，接下来就是提升权限并攻克了。
- 查询 allinurl:wwwboard/passwd.txt 将列出所有有“WWWBoard Password vulnerability”漏洞的服务器，阅读更多请参见下面链接。
- 查询 inurl:.bash_history 将列出互联网上可以看见 “inurl:.bash_history” 文件的服务器。这是一个命令历史文件，这个文件包含了管理员执行的命令，有时会包含一些敏感信息比如管理员键入的密码。
- 查询 inurl:config.txt 将看见网上暴露了“inurl:config.txt”文件的服务器，这个文件包含了经过哈希编码的管理员的密码和数据库存取的关键信息。

还有一些其他一些使用“inurl:”和“allinurl:”查询组合的例子

- inurl:admin filetype:txt
- inurl:admin filetype:db
- inurl:admin filetype:cfg
- inurl:mysql filetype:cfg
- inurl:passwd filetype:txt
- inurl:”wwwroot/*.”
- inurl:adpassword.txt
- inurl:webeditor.php
- inurl:file_upload.php
- inurl:gov filetype:xls “restricted”
- index of ftp +.mdb allinurl:/cgi-bin/ +mailto

inurl:id=1 查找有可能存在SQL注入的网站

<mark>终极技巧：https://www.exploit-db.com/google-hacking-database</mark>

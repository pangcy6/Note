# Alist之MacOS

[source](https://www.youtube.com/watch?v=HdtWoXHnSdI)

Author:程序员老张

Date: 2024.10.10

---

## 0.概览

- 下载内容

- 启动程序

- 挂载网盘

- 开机自启动

## 1. 下载内容

Alist官网：https://alist.nn.ci/zh/

项目地址：https://github.com/alist-org/alist

下载alist-darwin-arm64.tar.gz

## 2. 启动程序

- 将alist解压到新建文件夹Alist，进入终端`./alist server`
  
  - 如果报错：`sudo xattr -r -d com.apple.quarantine /Users/YOURNAME/Alist/alist`
  
  - Try again.

- 根据提示得到服务端口5244，可能需要的下载程序如aria2等

- 浏览器打开：localhost:5244

- 再重新打开终端：`./alist admin`得到原始登录密码，输入登录

- 出现图标即标志着alist启动成功

- 可点击管理--个人资料--更改自己的密码

## 3. 挂载网盘

官网有详细的各个网盘挂载的教程，下面仅以阿里网盘挂载为例。

- 管理--存储--添加--阿里云盘

- 挂载路径：/阿里--提取文件夹：提取到最前--排序：修改时间--排序方式：升序

- 根文件夹ID：root

- token:
  
  - 登录自己的阿里云盘，F12或检查
  
  - Application--Local Storage--当前的网络地址--token点击
  
  - 下方找到：refresh_token的值，复制
  
  - 粘贴到刷新令牌中，保存

- 回到首页可以发现阿里云盘已经挂载成功了

- 其他网盘可以按照官网帮助即可

上述步骤已过时失效，请参阅官方帮助文档：https://alist.nn.ci/zh/guide/drivers/aliyundrive_open.html

## 4. 开机自启动

在Alist文件夹中创建alist.command文件

```bash
#!/bin/bash
cd /Users/YOURNAME/Alist
./alist server

# 保存后赋予执行权限
chmod +x alist.command
```

- 退出原来的服务--就是关闭已经运行的终端

- 系统偏好设置--通用--登录项--加号

- 将Alist目录中的alist.command添加到登录项

- 打开访达--前往--连接服务器

- 填写：http://127.0.0.1:5244/dav

- 再次开启终端`./alist server`

- 回到访达填写用户名，密码--连接

- 用户名和密码就是alist的

此时，就可以在访达的位置中看到127.0.0.1了

如果有更多网盘那就添加吧，和本地磁盘有点区别但是不大！

免费硬盘空间是对抗苹果税的有利武器。



## 5. 正常使用优化

1. 启动`./alist server`--打开localhost:5244--或者下一步

2. Finder--前往--连接服务器

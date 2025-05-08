# Windows命令行激活

> 管理员身份运行cmd

1. slmgr /upk    #卸载原本的密钥

2. slmgr /ipk *key* #安装新密钥

3. slmgr /skms kms.cangshui.net #设定激活服务器

4. slmgr /ato #激活

5. slmgr /xpr #查看过期时间

6. slmgr /d1v #查看激活信息

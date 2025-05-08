# Windows 11 安装

2022-04-11
---

在选择完版本之后安装不能继续进行，需要执行如下步骤：

1. Shift+F10打开cmd
2. regedit打开注册表编辑器
3. HKEY_LOCAL_MACHINE\SYSTEM\Setup新建项LabConfig
4. 新建32位DWORD值--BypassTPMCheck--数值数据00000001，十六进制
5. 再新建一个32位DWORD值--BypassSecureBootCheck--数值数据00000001，十六进制
6. 关闭编辑器，cmd
7. 回到安装程序，返回上一步即可；余下步骤皆是普通操作

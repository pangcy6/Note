# Rime鼠须管安装配置
Date: 2025-04-27
官网: <https://rime.im/>

## 1. 安装

### 1.1
二选一:
- 官网下载*.pkg包安装
- `brew install --cask quirrel`

### 1.2
下载"雾凇拼音"
```bash
# 进入Library目录
cd ~/Library
# 备份原有Rime配置
mv Rime Rime.old
# 下载雾凇拼音
git clone --depth=1 https://github.com/iDvel/rime-ice.git Rime-ice
# 建立软链接
ln -s Rime-ice Rime
```

### 1.3
退出登录/最好是重启电脑
- 点击"menuBar"上的输入法图标--打开键盘设置
- 点击"+", 选择"简体中文"--添加
- 选择鼠须管--完成
- 菜单栏点击鼠须管--重新部署(对配置文件修改后都要重复这个操作才生效)

### 1.4 自定义皮肤

下载< https://gist.github.com/lewangdev/f8ebbba24f464e915fb7d36857fcbbe5>并解压
`mv *.yaml ~/Library/Rime`
重新部署

## 2. 自定义

### 2.1 默认输入英文

文件: `~/Library/Rime-ice/rime_ice.schema.yaml`
```
...
Switches:
    - name: ascii_mode
      reset: 1
      states: [ 中, A ]
    - name: ascii_punct
      reset: 1
      states: [ ¥, $ ]
...
```
> 所有输入都是英文标点, 不可切换
> 若想可以切换注释掉第二个`reset`或者改为0

### 2.2 Neovim 由Insert回到Normal时自动切换英文输入

文件: `~/Library/Rime-ice/default.yaml`
```
...
bindings:
    # Neovim <Escape> 切换到英文输入
    - { when: always, accept: Escape, toggle: ascii_mode }
...
```

Done!

# Git极简操作
Date: 2025-05-08
---

## 0 Configuration

### mkdir && cd
```bash
git init
# Global config
git config --global user.name "Your name"
git config --global user.email "name@example.com"
git config --global init.defaultBranch main
# View all configuration:
git config --list
```

### SSH
```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
cat ~/.ssh/id_rsa.pub | pbcopy
```

登录 GitHub，进入 Settings → SSH and GPG keys → New SSH key：
- Title：自定义名称（例如 My Laptop）。
- Key type：保持默认 Authentication Key。
- Key：粘贴复制的公钥内容（以 ssh-ed25519 或 ssh-rsa 开头）。

```bash
# 检查远程仓库是否SSH格式
git remote -v
# 如果不是进行修改
git remote set-url origin git@github.com:yourusername/repo-name.git
# 验证连接, 出现Hi,XXX即为成功
ssh -T git@github.com
# 推送(需要add和commit)
git push origin main
```


## 1 实操

```bash
# 添加文件到暂存区
git add .
git add file1 file2
# 将暂存区文件添加到本地仓库并说明
git commit -m "message."
# 推送到远程仓库
git push origin main
```

`.gitignore`文件示例
```bash
# 将不上传的文件列在此处
mode_modeles/
*.log
.env
.DS_Store
```

如果远程仓库文件已存在, 如(README), 需要先拉取再推送:
```bash
git pull origin main --allow-unrelated-histories
git push origin main
```

***Done***!

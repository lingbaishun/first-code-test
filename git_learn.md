# Git学习
### 配置

>ssh-keygen
添加key到github上的settings中ssh key

### 初始化git仓库

>git init
### 添加文件到仓库
>git add file
>git commit -m 'message'

### 克隆git上代码
>git init
>git clone git@github.com:lingbaishun/first-code-test.git
### 链接github
>git remote add origin git@github.com:lingbaishun/first-code-test.git

### 查看链接
>git remote -v

### 推送代码

>git pull origin master
>git push origin master

### 掌握工作区状态

>git status
### 若git status告诉有文件被修改，查看修改
>git diff
### 查看提交历史，用来确定回退到哪个版本
>git log

- 简化修改版本日志
>git log --pretty=oneline
### 查看命令历史，用来确定回到未来哪个版本
>git reflog
### 版本切换
- 回退到上一个版本
>git reset --hard HEAD^

- 回退到上上个版本
>git reset --hard HEAD^^

- 穿梭版本
>git reset --hard commit_id

- **场景一**
  当你改了工作区某个文件的内容，想直接丢弃工作区的修改时
  
  >git checkout --file
- **场景二**
  当你不但改了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步：
  - **第一步**：回到场景一
  >git reset HEAD file 
  
  - **第二步**：按照场景一操作
- **场景三**
  已经提交了不合适的修改到版本库时，想要撤销本次提交。用版本回退

### 删除文件

>rm test.txt
- 确实要删的
  >git rm test.txt
  git commit
- 误删
  >git checkout --test.txt
###分支（个人理解：相当于一个草稿本）
- 查看分支
  
  >git branch
- 创建分支
  
  >git branch name
- 切换分支
  git checkout name
- 创建+切换分支
  git checkout -b name
- 合并某分支到当前分支
  git merge name
- 删除分支
  git branch -d name
#### 分支冲突
当分支提交与主分支同时提交同一份文件的修改，会产生冲突，需要手动修改文件解决冲突
使用git status查看冲突文件
- 查看分支合并情况图
  >git log --graph --pretty=oneline --abbrev-commit
###pull时冲突
解决方法：https://www.cnblogs.com/baby123/p/6588378.html 。

合并分支时候
>git merge --no-ff-m "merge with no-ff" dev

参数--no-ff表示禁用fast forward。fast forward模式下删除分支后会丢失分支信息。

- 修改bug时，通常创建bug分支进行修复，然后合并，最后删除。
- 当手头工作没有完成时，先把工作现场储藏起来
  >git stash

  然后修复bug，修复后恢复工作检查并删除stash内容
  >git stash pop

  等同于
  >先：git stash apply
   再：git stash drop

- 丢弃没有合并过的分支
  
  >git branch -D name

### 推送

- 查看远程库信息
  
  >git remote -v
- 本地新建分支如果不推送到远程，对其他人就是不可见的
- 从本地推送分支
  >git push origin branch_name

  如果推送失败，先用git pull抓取远程再提交
- 在本地创建和远程分支对应的分支
  >git checkout -b branch_name origin/branch_name

  本地和远程分支的名称最好一致
- 创建本地分支和远程的关联
  
  >git branch --set-upstream branch_name origin/branch_name
- 从远程抓取分支，使用git pull，如果有冲突，要先处理冲突。

  ### 多人协作
- 首先可以试图用git push origin branch_name推送自己的修改
- 如果推送失败，则因为远程分支比你的本地更新，需要先用git pull试图合并
- 如果合并有冲突，则解决冲突，并在本地提交
- 没有冲突或者解决掉冲突后，再用git push origin branch_name推送就能成功
  

如果git pull提示 no tracking information，则说明本地分支和远程分支的链接关系没有创建，用命令
>git branch --set-upstream-to branch_name origin/branch_name

### 设置标签（版本号）
tag就是一个让人容易记住的有意义的名字，它跟某个commit绑在一起

- 创建一个新的标签，默认为HEAD，也可以指定一个commit_id
  
  >git tag tagname
- 指定标签信息
  
  >git tag -a tagname -m 'message'
- 删除一个本地标签
  
  >git tag -d tagname
- 删除一个远程标签
  
  >git push orgin :refs/tags/tagname
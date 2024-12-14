# Python仿抖音表白
## 有自动截图和把截图自动发送邮箱功能
![image](example/20241214174259.png)
## 使用方法
### 1.安装依赖
```shell
pip install -r requirements.txt
```
### 2.配置
### 打开config/config.ini配置文件并修改下列配置
```ini
[sender-config]
host = smtp.example.com      # 发送邮箱的smtp服务器
port = 25                    # 发送邮箱的smtp服务器端口
sender = sender@example.com  # 发送邮箱
pwd = your_password_here     # 发送邮箱的授权码不是密码

[recivers-config]
reciver1 = receiver1@example.com  # 接收邮箱
reciver2 = receiver2@example.com  # 接收邮箱
reciver3 = receiver3@example.com  # 接收邮箱

# Tips：发送邮箱的授权码不是密码，授权码是在邮箱设置里面生成的
# Tips：接受邮箱可以有多个，用reciver1,reciver2,reciver3...表示
```
### 3.运行（需要依赖pyton环境）
```shell
python main.py
```
### 4. pyinstaller打包（打包为exe程序不需要配置额外的python环境）
打包好的exe程序可以在其他没有安装python环境的主机上运行，适合给不会使用python的人使用，只需要把dist文件夹下的dylove.exe文件拷贝到其他主机上即可运行
### dylove.exe.spec配置文件
如果需要打包为exe程序，需要配置dylove.exe.spec文件。
配置文件内容如下（只写出了需要修改的部分）：
```python
datas=[('font/STXINGKAI.ttf', 'font'),
       ('img/bg.png', 'img'),
       ('img/biu.png', 'img'),
       ('img/heart.png', 'img'),
       ('music/bg.mp3', 'music'),
       ('config/config.ini', 'config')],
```
### 打包
项目中已经有配置好的dylove.exe.spec文件，只需要执行下面的命令即可打包
```shell
pyinstaller  dylove.exe.spec # windows
```
打包完成后会在dist文件夹下生成dylove.exe文件
### 5.运行exe程序
双击dist文件夹下的dylove.exe即可运行
### 6.deylove.exe.spec配置文件消失
如果dylove.exe.spec配置文件消失，可以通过下面的命令重新生成
```shell
pyinstaller -F -w -i ico.png --name=dylove.exe main.py  # windows 生成独立的exe文件
```
```shell
pyinstaller -D -w -i ico.png --name=dylove main.py  # windows 生成绿色版exe文件
```
### 7.注意事项
- 请确保发送邮箱开启了smtp服务
- 请确保config/config.ini配置文件正确且文件编码为utf-8换行符为LF
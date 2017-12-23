## 启动应用

基于 Python3 开发，通过 virtualenv 建立开发环境

```
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

依赖软件包安装完成后，通过以下命令启动应用：

```
$ FLASK_DEBUG=1 FLASK_APP=app.py flask run
```

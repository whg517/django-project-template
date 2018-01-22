# django-project-template


## How to install

### 1. Create Project

你应该把下面 `project_name` 换成你自己的项目名称

```bash
$ django-admin startproject \
  --template=https://github.com/kiven517/django-project-template/archive/master.zip \
  --name=Procfile \
  project_name
```

### 2. Create your working environment

在当前项目下生成 python 虚拟环境，你也可以选择放在其他地方，或者使用其他环境。

```bash
cd project_name
$ virtualenv --no-site-package venv
$ source venv/bin/activate
```

如果是 Windows 环境，应该执行 `source venv/Scripts/activate` 

### 3. 安装 package
```bash
$ pip install -r requirements/local.txt
```

### 4. Run project

通过 PyCharm 打开项目目录，点击右上角添加 `Edit Configurations` 添加 Django Server 

![Edit Configurations](http://ono3vb8rf.bkt.clouddn.com/Fqj-RwuAmZQLFjr1e_fWrFvld4Qa.png)

打开 Run/Debug Configurations，点击右上角加号，添加一条 Django server

![Run/Debug Configurations](http://ono3vb8rf.bkt.clouddn.com/Fj2Jdu2iag4gkBDLUFCxOwpQsc5Y.png)

修改 Name 为 Project 名称，然后点击 ok

![Django server](http://ono3vb8rf.bkt.clouddn.com/FiAn2TWl6hIakt4zpmNZnZeHyaq1.png)

点击右上角绿色三角运行。

浏览器访问 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

如果访问，进入 Django 欢迎页，则项目基本配置和运行正常


## Features

Production-ready configuration for Static Files, Database Settings, template dir, etc.
Latest Python 3.6 runtime environment.

### 使用分离式的设置文件

新建项目会将 settings.py 替换为文件夹，生成多个设置文件 

| 设置文件 | 目的 |
| --- | --- |
| base.py | 基本设置文件，在各个环境中都相同的设置可以发入其中。|
| local.py | 当开发是使用的设置文件。可以设置开发是的选项，包括 DEBUG，log 的等级，是否开启某些工具等。 |
| production.py | 当部署到正式服务器上所用的设置。 | 

其中在 manage.py 文件中默认使用 local.py 配置。即默认情况下使用 `python manage.py runserver` 运行项目时使用的是开发环境。
在 wsgi.py 文件中默认使用 production.py 配置。即生产环境中使用 Nginx-uWSGI-django 模式部署，则使用生产环境

> 针对 wsgi.py 文件中使用 production.py 文件，在运行 `python manage.py runserver` 命令并不会加载 production.py 中指定配置。
因为 `os.environ.setdefault()` 方法会首先检查是否设置过默认环境。具体可以查看相关源码

如果在开发环境要测试生产环境下程序运行，只需把 manage.py 文件中的注释代码更改一下即可。

当然也可以使用如下方式加载不同环境

```bash
$ python manage.py shell --settings=mysite.settings.local

$ python manage.py runserver --settings=mysite.settings.local
```

当然如果你熟悉 DJANGO_SETTINGS_MODULE 和 PYTHONPATH 的话, 也可以事先设置好 DJANGO_SETTINGS_MODULE 和 PYTHONPATH 环境变量, 这样做的好处就是你不必使用--settings了.

如果你对virtualenv有深入的了解的话, 也可以在postactivate脚本中设置 DJANGO_SETTINGS_MODULE 和 PYTHONPATH.

###  将关键信息和设置文件分离

> 注意： 默认使用配置文件获取 key

将SECTET_KEY, AWS key文件, API key文件等关键信息放入设置文件中也是违反基本原则的. 因为:

- 配置环境不同时关键信息会改变, 程序却不会.
- 关键信息不是程序.
- 关键信息应当是隐蔽的, 如果储存在了版本管理系统中, 则任何有权访问该版本库的用户都能获知这些关键信息.
- 许多PAAS服务无法为每台服务器编辑设置文件, 即使可以, 这也是不正确的做法.

在使用bash的Mac或Linux中设置环境变量比较容易, 你只需要将以下代码加入.bashrc, .bash_profile, 或.profile其中之一即可. 如果多个项目 使用相同的API, 并且关键信息都不同时, 可以将以下代码加入到virtualenv的bin/activate脚本中:

    export SOME_SECRET_KEY=654-3jgwg-4r3-2t4h-76jk
    export ANOTHER_SECRET_KEY=y5y-5jk8-75i5h-5g4/.-,o.

如果使用的是windows系统, 则设置稍微复杂一点. 如果使用cmd.exe,你必须使用setx命令一个一个的设置。或者打开 计算器==>属性==>高级系统设置==>环境变量，来添加。
一个较好的方式是使用virtualenv的 bin/activate.bat

    > setx OME_SECRET_KEY=654-3jgwg-4r3-2t4h-76jk

#### 获取环境变量

考虑到SOME_SECRET_KEY无法被获取到的话, 就会出现KeyError错误, 导致django项目无法启动. 这很好, 但KeyError没有提供更有 用的信息, 导致debug的困难, 因此, 我们在base.py(希望你还记得这是哪个文件)加入以下function, 为我们提供哪个关键信息无法获取的信息:

```python
# settings/base.py
import os
# 通常你不应该从django引入任何代码, 但ImproperlyConfigured是个例外
from django.core.exceptions import ImproperlyConfigured

def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured('error_msg')
```

#### 无法使用环境变量时

当我们使用apache时, 我们会发现, django无法使用环境变量. 这时, 我们推荐将关键信息储存在JSON格式的文件中, 已达到将关键信息和代码分离的 目的. 首先我们可以创建secrets.json文件:

```json
{
    "FILENAME": "secrets.json",
    "SOME_SECRET_KEY": "654-3jgwg-4r3-2t4h-76jk"
}
```

在settings中使用该文件:

```python
# settings/base.py

import json
# 通常你不应该从django引入任何代码, 但ImproperlyConfigured是个例外
from django.core.exceptions import ImproperlyConfigured

# 读取json文件
with open("secrets.json") as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        raise ImproperlyConfigured('error_msg')

SOME_SECRET_KEY = get_secret('SOME_SECRET_KEY')
```

**注意：** 默认的，项目模板采用的是使用 json 获取。但是该文件不应该被 git 追踪。所以你应该自己在项目根目录下建立并自行配置该文件
在 base.py 文件中也保留使用 django 随机生成的 SECRET_KEY 字段，如果需要，请自行打开注释。

### 使用不同的部署文件(requirements.txt)

部署文件(requirements.txt)中储存的是该django项目的依赖库, 一般使用pip freeze --local生成. 本着"只安装需要的模块"的原则, 不同的设 置文件, 应当对应不同的requirements.txt文件. 就像分离式的settings文件一样, 我们使用分离式的requirements文件. 
在 requirements 目录中应对不同情况下的 requirements 文件

在base.txt中, 储存的是所有开发环境中都会用到的依赖库。
文件中配置了 pip 使用国内镜像源，加开安装速度

```
-i https://pypi.tuna.tsinghua.edu.cn/simple

django==1.11.9
```

在local.txt中, 储存的是本地开发时用到的依赖库:
文件继承 base.txt 
```
-r base.txt

ipython
```

当重新配置本地开发环境时, 可以使用以下代码安装依赖库:

```bash
pip install -r requirements/local.txt
```



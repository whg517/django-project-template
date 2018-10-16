# django-project-template

## How to install

### 1. Create Project

你应该把下面 `project_name` 换成你自己的项目名称

```bash
$ django-admin startproject \
  --template=https://github.com/huagang517/django-project-template/archive/master.zip \
  --name=Procfile \
  project_name
```

### 2. Use Pycharm Open It
![Pycharm Django](http://ono3vb8rf.bkt.clouddn.com/FtQjfMTD-DQbTpf0dExvK-z6Cd5j.gif)

### 3. Change `DJANGO_SETTINGS_MODULE`

将 `DJANGO_SETTINGS_MODULE` 更改为当前项目的配置。可参照 `manage.py` 文件

```
[tool:pytest]
DJANGO_SETTINGS_MODULE = demo.settings.development
```

## Features

Production-ready configuration for Static Files, Database Settings, template dir, etc.
Latest Python 3.6 runtime environment.

### 使用分离式的设置文件

新建项目会将 settings.py 替换为文件夹，生成多个设置文件 

| 设置文件 | 目的 |
| --- | --- |
| base.py | 基本设置文件，在各个环境中都相同的设置可以发入其中。|
| development.py | 当开发是使用的设置文件。可以设置开发是的选项，包括 DEBUG，log 的等级，是否开启某些工具等。 |
| production.py | 当部署到正式服务器上所用的设置。 | 

其中在 manage.py 文件中默认使用 development.py 配置。即默认情况下使用 `python manage.py runserver` 运行项目时使用的是开发环境。
在 wsgi.py 文件中默认使用 production.py 配置。即生产环境中使用 Nginx-uWSGI-django 模式部署，则使用生产环境

> 针对 wsgi.py 文件中使用 production.py 文件，在运行 `python manage.py runserver` 命令并不会加载 production.py 中指定配置。
因为 `os.environ.setdefault()` 方法会首先检查是否设置过默认环境。具体可以查看相关源码

如果在开发环境要测试生产环境下程序运行，可按如下方式设置：

1. 在启动命令中通过 `--settings` 参数指定配置

```bash
$ python manage.py shell --settings=mysite.settings.production

$ python manage.py runserver --settings=mysite.settings.production
```

2. 使用 `DJANGO_SETTINGS_MODULE` 环境变量

建议不要设置在系统环境变量中或者当前用户环境变量中。如果设置了，将会导致其他项目在启动的时候找不到对应的配置。

3. 如果测试环境是使用 WSGI 启动的 Django，可以在 postactivate 脚本中设置 DJANGO_SETTINGS_MODULE 。

### 使用 Pipenv 管理虚拟环境

[Python Dev Workflow for Humans](https://pipenv.readthedocs.io/en/latest/)

Pipenv 是一个强大的虚拟环境管理工具，类似于 node 的 npm 。项目根目录下的 `Pipfile` 是定义的依赖，安装完成后会再生成 `Pipfile.lock` 文件。

```bash
pip install requests # 安装依赖
pip install -d ipython # 安装开发环境下的依赖。
```

### 生产模式下读取 `settings.conf` 配置

生产模式下的 Django settings 可以通过在根目录创建 `settings.conf` 传入配置，如果配置已存在，则会覆盖。

### 集中管理 apps

跟目录 `apps` 包集中放置所有 app 。

### [isort](https://github.com/timothycrosley/isort)

使用 isort 对项目导包进行格式化

```
isort
```

### [pytest](https://docs.pytest.org/en/latest/contents.html)

通过 `pytest-django` 使用 pytest 测试 django 。

### [coverage](https://coverage.readthedocs.io/en/v4.5.x/)

coverage 是生成测试报告的一个工具。

通过 [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) 插件可以在测试的同时生成测试报告。

```
pytest-cov
```

### [tox](https://tox.readthedocs.io/en/latest/index.html)

使用 tox 做自动化处理。

对于 isort 检测会直接输出检测结果，而非帮助修改。

对于 flake8 采用非严格模式(命令前置 `-` )，输出结果，而不是终止自动化。

## TODO list


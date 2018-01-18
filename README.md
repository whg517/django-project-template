# django-project-template


## Features

Production-ready configuration for Static Files, Database Settings, template dir, etc.
Latest Python 3.6 runtime environment.

## How to install

### Before

#### Django 运行模式

`DJANGO_EXECUTION_ENVIRONMENT` 是 django 执行环境模式的一个变量

值如下
- `LOCAL`  这代表当前环境为开发模式。
- `TEST`  这代表当前环境为测试模式。
- `PRODUCTION`  这代表当前环境为生产模式

如果您处于开发环境中，那么您应该在 `~/.bash_profile` 文件最后中加入 `DJANGO_EXECUTION_ENVIRONMENT=LOCAL` 这条环境变量，然后执行 `source ~/.bash_profile`
 
当然上述操作是针对 Linux 环境的操作，如果你是在 Windows 中开发的话，你应该在 "计算机" ==> "属性" 中加入环境变量。

关于环境模式，你可以在创建 Django Project 后，查看 `manage.py` 中的代码

#### SECRET_KEY 配置

通过拆分多种模式的 `settings` 配置，让我们轻松应对在不同情况下的项目配置。这里一个关键配置就是 `SECRET_KEY`

你应该配置非生产环境下的 `SECRET_KEY` 。通过在环境变量中加入 `SECRET_KEY=xxxxxxxx`。

生产环境下的 `SECRET_KEY` 是由 django-admin 随机生成的。你应该注意保证其安全性。

具体细节，你可以在创建 Django Project 后，查看项目中 `settings` 目录

### Create Project

你应该把下面 `project_name` 换成你自己的项目名称

```bash
$ django-admin.py startproject \
  --template=https://github.com/kiven517/django-project-template/archive/master.zip \
  --name=Procfile \
  project_name
```

### Create your working environment

在当前项目下生成 python 虚拟环境，你也可以选择放在其他地方，或者使用其他环境。

```bash
cd project_name
$ virtualenv --no-site-package venv
$ source venv/bin/activate
```

如果是 Windows 环境，应该执行 `source venv/Scripts/activate` 


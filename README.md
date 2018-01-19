# django-project-template


## Features

Production-ready configuration for Static Files, Database Settings, template dir, etc.
Latest Python 3.6 runtime environment.

## How to install

### Create Project

你应该把下面 `project_name` 换成你自己的项目名称

```bash
$ django-admin startproject \
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


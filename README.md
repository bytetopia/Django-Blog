# Django-Blog

基于 Django 框架的简易个人博客。

Personal blog powered by Python and Django.

---

## 简介

关于博客这件事，基于 jekyll 和 hexo 的博客都试过，csdn 和博客园和 segment fault 都写过，总不能觉得满意…… 最后还是决定自己造一个了_(:з)∠)_

预览网址： http://codingcat.cn

## 相关技术

当前版本： v 0.5

基于 Django 搭建而成
- 前端页面：样式基于 Bootstrap 4
- 管理后台：直接用了 Django 自带的 Admin
- Markdown：编辑器使用 Editor.md ，前台渲染使用 showdown.js 和 highlight.js
- 数据库：基于 Mysql
- 搜索：基于 haystack 和 whoosh （注：由于需要配置中文分词，项目直接内置了一份haystack的源码，而无需再安装haystack的包）
- 标签文字云：JQCloud

项目不断更新完善中。欢迎 star、fork 和 PR。

## 本地部署流程

#### 安装依赖
项目基于 Python 3，需要在项目根目录下运行
```commandline
pip3 install -r requirements.txt
```

#### 修改数据库
在 DjangoBlog/settings.py 中，找到 DATABASES 部分，修改为你自己的 mysql 数据库位置和账户。


#### 数据库建表
在项目根目录下运行
```commandline
python3 manage.py makemigrations
python3 manage.py migrate
```

#### 创建管理员账号
在项目根目录下运行
```commandline
python3 manage.py createsuperuser
```
然后按照提示，设置管理员的用户名密码即可。

#### 本地运行
在项目根目录下运行
```commandline
python3 manage.py runserver 8888
```
可修改为其他端口。

运行后在浏览器访问 http://127.0.0.1:8888 即可看到站点。

访问 http://127.0.0.1:8888/manager 查看管理后台。

#### 重建索引
首次运行，可在项目根目录下运行
```commandline
python3 manage.py rebuild_index
```
以重建搜索索引。后续当数据库有修改时，将自动重建，无需手动干预。

## 个性化定制
可根据你的需要修改项目中的内容。（这部分说明，后续再详细补充）

## 更新日志
v0.5 2018/09/05 优化markdown渲染效果
v0.4 2018/08/22 增加搜索功能，增加文章加锁功能
v0.3 2018/08/18 增加评论功能
v0.2 2018/08/17 支持markdown编辑器
v0.1 2018/08/12 搭建原始框架
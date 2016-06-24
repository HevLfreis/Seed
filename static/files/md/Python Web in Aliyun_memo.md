# Python Web 部署全攻略
### flask/django+apache+mod_wsgi
***

## 开始
网上部署django和flask的教程有很多，但是都很老，而且都不是很完整或者有些坑没有提及。本文记录我在阿里云上部署python web的全过程。  
1. 服务器: 阿里云 ubuntu 14.04 LTS  
2. python 2.7.6, apache2 2.4.7, mysql 5.5.49, mod_wsgi 3.4  
3. 目标：一台服务器上部署多个django和flask项目  
***
## 1. mysql

1. 安装mysql相关包  
    ```
    sudo apt-get install mysql-server mysql-client libmysqlclient-dev
    ```
2. 开启、检查、进入mysql  
    ```
		service mysql start  
		sudo netstat -tap | grep mysql  
		mysql -u root -p  
    ```
3. mysql的备份还原
    ```
    mysql -u root -p database < dump.sql
    mysqldump -u root -p database > dump.sql
    ```

4. mysql一些配置项 [mysqld]
    * 如果你的工程是从win环境下开发，需要将大小写敏感设置不敏感，因为win下mysql不区分大小写，linux下区分。
        ```
        lower_case_table_names = 1
        ```
    * 设置mysql连接池的回收时间，解决flask-sqlalchemy下长时间不操作session被回收出现的：MySQL server has gone away错误，后文配置flask会再次提到。
        ```
        interactive_timeout = 3600
        wait_timeout = 3600
        ```
> [mysql配置参数参考](http://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html)

***
## 2. python环境
因为ubuntu已经安装好了python2.7和3.0，所以这里只要安装相关包即可。
1. 安装相关包
    ```
    sudo apt-get install python-pip
    sudo apt-get install python-dev
    
    sudo pip install MySQL-python
    
    sudo pip install virtualenv
    ```
* 关于virtualenv：因为python项目都要依赖大量的包，所以可以为不同的python项目配置一个虚拟环境，把项目的相关依赖都装到这个虚拟环境中，这样不同项目的依赖之间就不会产生冲突。[官方文档](https://virtualenv.pypa.io/en/stable/)。  
首先进入到你的项目目录下，比如 ``/home/user/projects/DjangoApp`` 。  
运行 ``virtualenv venv`` ，这时候项目目录下会多一个venv文件夹，这就是我们的虚拟环境了，在虚拟环境下安装的包都会放到这个目录下。  
    * 启动虚拟环境：``source bin/activate``  
    * 这时候shell会变成：``(venv) root@ubuntu:/home/user/projects/DjangoApp/``  
    * 然后你就可以： ``pip something in this venv``  
    * 退出虚拟环境：``deactivate``
***
## 3. apache
1. 安装apache2
    ```
    sudo apt-get install apache2
    ```
2. 安装mod-wsgi，[官方文档](http://modwsgi.readthedocs.io/en/develop/index.html)
    ```
    sudo apt-get install libapache2-mod-wsgi
    ```
## 4. 部署django
1. 安装django
    ```
    sudo pip install django
    ```
2. 为了可以正确地把model同步到服务器的mysql里，将你的django项目中migration文件夹下文件都删除。
3. 拷贝项目到 ``/home/user/projects/DjangoApp`` , 路径任意，后面配置apache时候保持一致就可。
4. 修改 settings.py
    ``` python
    DEBUG = False
    # 只有这里列出的主机名才能访问你的django网站，比如'www.mysite.com'， *代表任意。
    ALLOWED_HOSTS = ['*'] 
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'djangoapp',
            'USER': 'root',
            'PASSWORD': '12345678',
            'HOST': '127.0.0.1',   # 把 localhost 改成 127.0.0.1
            'PORT': '3306',
        }
    }
    
    # 静态文件目录，假定在/DjangoApp/static 下
    STATIC_URL = '/static/'
    
    STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static').replace('\\', '/'),
    ]
    ```
5. 修改 wsgi.py
    ``` python
    import os
    from os.path import dirname, abspath
    
    PROJECT_DIR = dirname(dirname(abspath(__file__)))
    
    import sys
    sys.path.insert(0, PROJECT_DIR)
    
    os.environ["DJANGO_SETTINGS_MODULE"] = "DjangoApp.settings"
    
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    ```
6. 同步数据库
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
7. 配置apache  
    首先建立站点： ``sudo vim /etc/apache2/sites-available/djangosite.conf``，每个站点对应一个conf文件。   
    添加：
    ```
    <VirtualHost *:80>
        ServerName djangoapp.domain.com
        ServerAlias domain.com
        ServerAdmin hevlhayt@foxmail.com
    
        Alias /static/ /home/user/projects/DjangoApp/static/
    
        <Directory /home/user/projects/DjangoApp/static>
            Require all granted
        </Directory>
    
        WSGIDaemonProcess djangoapp python-path=/home/user/projects/DjangoApp:/home/user/projects/DjangoApp/venv/lib/python2.7/site-packages processes=2 threads=15 display-name=%{GROUP}
        WSGIProcessGroup djangoapp
        WSGIScriptAlias / /home/user/projects/DjangoApp/DjangoApp/wsgi.py
        WSGIApplicationGroup %{GLOBAL}
    
        <Directory /home/user/projects/DjangoApp/DjangoApp>
            <Files wsgi.py>
                Require all granted
            </Files>
        </Directory>
    </VirtualHost>
    ```
* 关于WSGI的相关配置
    1. **WSGIDaemonProcess**：因为我们要在一个apache服务器中配置多个python web，最好的办法就是用daemonprocess为每个app分配独立的进程，上面的配置里我们选了2进程15线程的配置，在我们让apache服务器运行起来后，我们可以用  ``ps -aux | grep 'wsgi'`` 看到相应的进程信息。
    2. **WSGIApplicationGroup**：用来解决一些和C库相关的python包，比如scipy，networkx报：End of script output before headers或者其他错误。  
    文档原文：
        > Any WSGI applications in the global application group will always be executed within the context of the first interpreter created by Python when it is initialised. Forcing a WSGI application to run within the first interpreter can be necessary when a third party C extension module for Python has used the simplified threading API for manipulation of the Python GIL and thus will not run correctly within any additional sub interpreters created by Python.

8. 用户上传文件夹权限
    ```
    chown -R www-data:www-data /upload
    sudo chmod -R g+w /upload
    ```
9. 启用站点
    ```
    sudo a2ensite djangosite
    service apache2 reload
    ```
    
10. 用以上步骤可以配置多个django应用，将不同django应用配置到不同WSGIProcessGroup后，只要保证端口号不同或者ServerName不同，apache就可以根据你的端口号和ServerName找到对应的django项目，达到多项目配置目的
11. **enjoy it！**
***
## 5. 部署flask
1. 安装flask
    ```
    sudo pip install Flask
    sudo pip install Flask-SQLAlchemy
    ```
2. 在flask项目根目录下建立app.wsgi，yourapp就是flask的主程序  
    ```
    from yourapp import app as application

    import sys
    sys.path.insert(0, '/home/user/projects/FlaskApp')
    ```
    
3. 在yourapp.py中，设置  
    ```
    app.config['SQLALCHEMY_POOL_RECYCLE'] = 1800
    ```
    这个值要比mysql中设置的timeout小，我是1800,3600的配置，再也没有gone away过，其他值应该也可以。
    
4. 同样先建立站点，然后配置apache
    ```apache
    <VirtualHost *:80>
        ServerName flaskapp.domain.com
    
        WSGIDaemonProcess flaskapp python-path=/home/user/projects/FlaskApp:/home/user/projects/FlaskApp/venv/lib/python2.7/site-packages processes=2 threads=15 display-name=%{GROUP}
        WSGIProcessGroup flaskapp
        WSGIScriptAlias / /home/user/projects/FlaskApp/app.wsgi
        WSGIApplicationGroup %{GLOBAL}
    
        <Directory /home/user/projects/FlaskApp>
            Require all granted
        </Directory>
    </VirtualHost>
    ```
    
5. 启用站点，重启apache，enjoy it！


***

# 结束
    

    
    
    



















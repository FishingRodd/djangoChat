

introduce:实现基本websocket聊天室和文件上传功能

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```



## develop by

Django==4.0.2

django-admin-global-sidebar==0.2.0

django-cors-headers==3.13.0

django-filter==22.1

djangorestframework==3.13.1

djangorestframework-simplejwt==5.1.0

**channels**==4.0.0

**daphne**==4.0.0

mysqlclient==2.1.0

~~*The env provided is incomplete*~~



## description

The project has a total of 6 interfaces

- http://localhost:*/user/login
- http://localhost:*/user/register
- http://localhost:*/user/getAll
- http://localhost:*/chat/uploadfile
- http://localhost:*/chat/downloadById/1
- http://localhost:*/chat/getAllfile

ws interfaces

- ws://localhost:*/chat/room

## remark

Note that mysql is configured in the setting.py file 
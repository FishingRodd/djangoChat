python manage.py runserver

## develop by

Django==4.0.2
django-admin-global-sidebar==0.2.0
django-cors-headers==3.13.0
django-filter==22.1
django-simpleui==2022.3.15
django-static-fontawesome==5.14.0.0
django-static-jquery3==5.1.0
djangorestframework==3.13.1
djangorestframework-jwt==1.11.0
djangorestframework-simplejwt==5.1.0
**channels**==4.0.0
**daphne**==4.0.0
PyMySQL==1.0.2
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
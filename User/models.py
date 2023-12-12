from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class User(AbstractBaseUser, PermissionsMixin):
# class User(models.Model):
    uid = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=255, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=255, verbose_name='密码')
    last_login = models.DateTimeField(auto_now=True, verbose_name='最后登录时间')
    isdelete = models.BooleanField(default=False)

    USERNAME_FIELD = 'nickname'

    class Meta:
        db_table = 'user'


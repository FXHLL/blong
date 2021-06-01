from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):

    mobile=models.CharField(max_length=11,unique=True,blank=False)
    # 头像
    avatar=models.ImageField(upload_to='avatar/%Y%m%d/',blank=True)
    # 简介
    user_desc=models.CharField(max_length=500,blank=True)

    # 修改默认的字段为号码
    USERNAME_FIELD = 'mobile'
    class Meta:
        db_table='tb_users'
        verbose_name='用户管理'
        verbose_name_plural=verbose_name

        def _str_(self):
            return self.mobile
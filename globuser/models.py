from django.db import models

# Create your models here.
# 创建一个用户类，继承models.Model的类
class User(models.Model):

    class Meta:
        # app别名的单数
        verbose_name = '用户'
        # app别名的复数
        verbose_name_plural = '用户'

    # 用户名，非空，默认为空
    firstname = models.CharField('用户名', max_length=50, null=False, default='')
    # 账号，唯一，非空
    username = models.CharField('账号', max_length=150, null=False, unique=True)
    # 密码，非空
    password = models.CharField('密码', max_length=128, null=False)
    # 账号注册时间
    reg_jojn = models.DateTimeField('注册时间',auto_now=True, null=False)
    # 账号状态：1-正常
    #         2-锁定
    #         其他-异常
    status = models.IntegerField('登陆状态', null=False, default=1)


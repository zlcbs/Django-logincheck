# Generated by Django 2.1.3 on 2018-11-09 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globuser', '0002_auto_20181109_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='reg_jojn',
            field=models.DateTimeField(auto_now=True, verbose_name='注册时间'),
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.IntegerField(default=1, verbose_name='登陆状态'),
        ),
    ]
from django.contrib import admin
from globuser.models import User


# Register your models here.

# User模型的管理器
@admin.register(User)
class Admin_user(admin.ModelAdmin):
    # list_display设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ['id', 'firstname', 'username', 'reg_jojn']

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50

    # readonly_fields 设置只读字段
    readonly_fields = ['reg_jojn']

    # list_editable 设置默认可编辑字段
    #list_editable = ['status']

    # list_display_links 设置哪些字段可以点击进入编辑界面
    list_display_links = ('id','firstname')

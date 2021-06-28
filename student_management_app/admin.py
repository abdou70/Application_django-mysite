from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from student_management_app.models import CostumUser


class UserModel(UserAdmin):
    pass 


admin.site.register(CostumUser,UserModel )
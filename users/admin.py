from django.contrib import admin

# 모델 import
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


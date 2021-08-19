from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# 모델 import
from .models import User

@admin.register(User)
class UserAdmin(UserAdmin):
    '''
    * UserAdmin 상속받는다.
    * Django에서 제공하는 필드와 내가 만든 필드를 병합
    * UserAdmin.fieldsets + Custom Fieldsets
    '''
    # 생성할때 파란색으로 표시되는 구역
    fieldsets = UserAdmin.fieldsets + (
        (
            # 커스텀 이름
            "회원가입",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "birthdate",
                )
            },
        ),
    )
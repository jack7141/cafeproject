from django.contrib.auth.models import AbstractUser
from django.db import models

from CafeProject.ConsVar import ConstVar
# ----------------------------------------------------------------------------------------------------------------------
# AbstractUser 상속하면 migrations 폴더에 자동으로 폼들이 생성된다
# ----------------------------------------------------------------------------------------------------------------------
class User(AbstractUser):
    '''
    유저 Table
    * 성별
    * 유저 사진
    * 생일
    '''
    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(
        choices=ConstVar.GENDER_CHOICES, max_length=10, null=True, blank=True
    )
    birthdate = models.DateField(null=True)


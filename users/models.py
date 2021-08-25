from django.contrib.auth.models import AbstractUser
from django.db import models

from ConsVar import ConstVar
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
    avatar = models.ImageField(blank=True, upload_to='avatars', verbose_name='사진')

    # 선택사항은 튜플로 구현하여 DB에 저장되는 값과 데이터를 읽어올때 값을 따로 처리
    gender = models.CharField(
        choices=ConstVar.GENDER_CHOICES, max_length=10, null=True, blank=True, verbose_name='성별'
    )
    email = models.EmailField(blank=True, verbose_name='이메일 주소')
    birthdate = models.DateField(null=True, verbose_name='생일')


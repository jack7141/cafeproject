from django.db import models
from core import models as CoreModle
from ConsVar import ConstVar
from users import models as userModel

class Cafe(CoreModle.TimeStampedModel):
    '''
    * core에서 데이터가 생성되는 날짜와 업데이트되는 날짜를 상속받아서 사용한다.

    '''
    # 카페이름
    cafeName = models.CharField(max_length=30)

    # 설명
    description = models.TextField()

    # 시
    city = models.CharField(
        choices=ConstVar.CITY_CHOICES, max_length=10, null=True, blank=True, verbose_name='시'
    )

    # 구
    country = models.CharField(
        choices=ConstVar.COUNTRY_CHOICES, max_length=10, null=True, blank=True, verbose_name='구'
    )

    # 동
    district = models.CharField(
        choices=ConstVar.DISTRICT_CHOICES, max_length=10, null=True, blank=True, verbose_name='동'
    )

    # 주소
    address = models.CharField(max_length=150)
    
    # 예약시간
    check_in = models.TimeField()

    # 나가는 시간
    check_out = models.TimeField()
    
    # 예약 유/무
    instant_book = models.BooleanField(default=False)
    
    # 예약자
    host = models.ForeignKey(userModel.User, on_delete=models.CASCADE)


from django.db import models
from core import models as CoreModle
from ConsVar import ConstVar
from users import models as userModel
from phonenumber_field.modelfields import PhoneNumberField


class MenuItem(CoreModle.TimeStampedModel):
    '''
    * 다대다의 메뉴 관리 모델
    '''

    menu = models.CharField(max_length=80, null=True, blank=True, verbose_name='메뉴')
    price = models.IntegerField(null=True, blank=True, verbose_name='가격')

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.menu}, {self.price}'

class CafeType(CoreModle.AbstractItem):
    class Meta:
        verbose_name_plural = "카페 종류"

class Menu(MenuItem):
    class Meta:
        verbose_name_plural = "메뉴"

class Photo(CoreModle.TimeStampedModel):
    pass

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

    # 카페사이트
    website = models.CharField(max_length=200, null=True, blank=True)
    
    # 카페전화번호
    # cafeNumber = PhoneNumberField(null=True, blank=True)

    # 가게 시작시간
    start = models.TimeField(null=True, blank=True, verbose_name='영업 시작시간')

    # 가게 종료시간
    end = models.TimeField(null=True, blank=True, verbose_name='영업 종료시간')
    
    # 주차장 유/무
    parkSite = models.BooleanField(default=False,null=True, blank=True)
    
    # 가게 주인 
    # FIXME: 어차피 카페를 내가 관리할거면 딱히 필요는 없을것 같음
    host = models.ForeignKey(userModel.User, on_delete=models.CASCADE)

    cafetype = models.ForeignKey(CafeType, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='커피 메뉴')

    # 카페 종류는 한 카페안에서도 같은 맥락 및 여러 메뉴를 갖을 수 있기 때문에 다대다관계로 사용한다.
    # 커스텀 용이하게 핸들링
    cafeMenu = models.ManyToManyField(Menu, blank=True)


    def __str__(self):
        return self.cafeName



class Photo(CoreModle.TimeStampedModel):
    '''
    * 카페 이미지 모델
    '''

    caption = models.CharField(max_length=80)
    file = models.ImageField()

    # 카페가 삭제되면 이미지도 삭제되야하므로, 연결해준다.
    room = models.ForeignKey(Cafe, on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
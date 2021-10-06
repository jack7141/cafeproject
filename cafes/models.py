from django.db import models
from core import models as CoreModle
from ConsVar import ConstVar
from users import models as userModel
from phonenumber_field.modelfields import PhoneNumberField

from django.urls import reverse

# 장고에서 HTML상의 코드를 방어하고 있는것을 안전하다고 인식시켜서 HTML코드를 사용하게 해준다.
from django.utils.html import mark_safe

class MenuItem(CoreModle.TimeStampedModel):
    '''
    * 다대다의 메뉴 관리 모델
    '''

    name = models.CharField(max_length=80, null=True, blank=True, verbose_name='메뉴')
    price = models.IntegerField(null=True, blank=True, verbose_name='가격')

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.name}, {self.price}'

class CafeType(CoreModle.AbstractItem):
    class Meta:
        verbose_name_plural = "카페 종류"

class Menu(MenuItem):
    class Meta:
        verbose_name_plural = "메뉴"


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
    # 역참조를 위해서 기존의 _set을 사용하기엔 너무 귀찮으니까 related_name을 사용한다.
    # 정참조는 상관없음
    # 정참조란 현재 Cafe를 바라보고 있는 host는 Cafe모델에서 cafe.host.요소 이런식으로 접근이 가능하다.
    # 반면 user쪽에서는 어떤 카페데이터를 가지고 있는지 알 수 없다.
    # 그렇기 때문에 만들어진게 related_name을 사용해서 역으로 user모델에서도 cafe를 알 수 있도록한다.
    # 즉, 특정 유저가 어떤 카페의 정보를 가지고 있는지 알 수 있게 된다.
    host = models.ForeignKey(userModel.User, on_delete=models.CASCADE, related_name='owner')

    cafetype = models.ForeignKey(CafeType, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='카페 타입', related_name='owner')

    # 카페 종류는 한 카페안에서도 같은 맥락 및 여러 메뉴를 갖을 수 있기 때문에 다대다관계로 사용한다.
    # 커스텀 용이하게 핸들링
    cafeMenu = models.ManyToManyField(Menu, blank=True, related_name='owner')


    def __str__(self):
        return self.cafeName

    # ------------------------------------------------------------------------------------------------------------------
    # override
    # ------------------------------------------------------------------------------------------------------------------
    def save(self, *args, **kwargs):
        '''
        * save를 오버라이드를 통해서 intercepting한다. 
        사용자가 저장하는것을 취향에 맞게 내가 알아서 변경해서 저장
        '''
        # super()를 이용하여 부모클래스에 접근할 수 있도록한다.
        # 현재 따로 수행하는 일이 없어서 주석해도 상관없음 
        # 단 override되고 있기 때문에, 함수 전체를 주석처리 해야함
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # admin 패널에서 해당 페이지로 넘길 수 있겠금, reverse함수를 사용한다.
        # 우리가 만든 viewDetail(cafes/View 함수)은 파라미터를 받아야하기 때문에 우리가 지정한 id와 맞춰서 id를 넘겨준다.
        return reverse('cafes:viewDetail', kwargs={'id':self.id})

    # ------------------------------------------------------------------------------------------------------------------
    # QUREYSET & MANAGE
    # ORM Qureyset 문서
    # https://docs.djangoproject.com/en/3.2/topics/db/queries/
    # 함수에서 obj를 읽어오는 기준은 Row를 기준으로 읽는다.
    # option : all(), count()
    # ------------------------------------------------------------------------------------------------------------------
    def count_cafeMenu(self):
        cafeMenuCount = self.cafeMenu.count()
        return cafeMenuCount

    def count_cafePhoto(self):
        cafePhotoCount = self.cafephotos.count()
        return cafePhotoCount

    def total_rating(self):
        # related_name='reviews' 리뷰 모델의 related키로 받고있기때문에 접근가능
        all_reviews = self.reviews.all()
        all_ratings = 0
        for review in all_reviews:
            all_ratings += review.rating_average()

        if all_ratings == 0:
            return all_ratings / 1
        else:
            return round(all_ratings / len(all_reviews),2)

    def first_photo(self):
        photo, = self.cafephotos.all()[:1]
        return photo.file.url

    def get_next_four_photos(self):
        photo = self.cafephotos.all()[1:5]
        return photo


class Photo(CoreModle.TimeStampedModel):
    '''
    * 카페 이미지 모델
    '''

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to='cafeImages')

    # 카페가 삭제되면 이미지도 삭제되야하므로, 연결해준다.
    room = models.ForeignKey(Cafe, on_delete=models.CASCADE, related_name='cafephotos')

    def __str__(self):
        return self.caption

    def get_thumbNali(self):
        '''
        * dir()을 통해서 property를 확인해서 필요한 정보를 가져옴
        print(self.file.url)
        print(self.file.size)
        print(self.file.width)
        print(self.file.height)
        '''
        return mark_safe(f'<img width="150px" src="{self.file.url}" />')





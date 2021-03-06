from django.contrib import admin
from .models import Cafe,CafeType,Menu, Photo, City, Country

@admin.register(CafeType, Menu)
class ItemAdmin(admin.ModelAdmin):
    '''
    * 카페 메뉴 패널
    '''
    list_display = ('name','used_by')
    def used_by(self, objects):
        return objects.owner.count()

class PhotoInline(admin.TabularInline):
    model = Photo

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    '''
    * 카페 메뉴 패널
    '''
    list_display = (
        'name',
    )


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    '''
    * 카페 메뉴 패널
    '''
    list_display = (
        'name',
    )
    fieldsets = (
        (
            "지역구 입력",
            {'fields': ('continent',)},
        ),
    )
    # 다대다 관계의 모델만 사용가능함
    filter_horizontal = ('continent',)


class PhotoInline(admin.TabularInline):
    model = Photo

@admin.register(Cafe)
class CafeAdmin(admin.ModelAdmin):

    # ------------------------------------------------------------------------------------------------------------------
    # DISPLAY 패널 요소 CUSTOM
    # ------------------------------------------------------------------------------------------------------------------
    list_display = (
        'cafeName',
        'city',
        'country',
        'start',
        'end',
        'parkSite',
        'count_cafeMenu',
        'count_cafePhoto',
        'total_rating',
    )

    # 내가 만든 모델 내부의 host가 외래키로 users.User를 가지고 있기 때문에,
    # host를 통해서 User클래스의 username을 가져올 수 있다.
    # 방법은 아래와 같이 --> 변수명__불러올값
    list_filter = (
        'host__gender',
        'parkSite',
        'city',
        'country',
        'cafetype'
    )

    search_fields = ('cafeName', '=city', '=country', 'host__username')

    # ------------------------------------------------------------------------------------------------------------------
    # CHANGE 패널요소 CUSTOM
    # ------------------------------------------------------------------------------------------------------------------
    fieldsets = (
        (
            "카페 정보",
            {'fields': ('cafeName','city','country','parkSite','website')},
        ),
        (
            '카페 운영 정보',
            {'fields':('start','end','cafetype','host')},
        ),
        (
            '메뉴 정보',
            {
                'fields': ('cafeMenu',),
                # classes 옵션을 통해서 패널을 접고 펴고 기능 및 다양한 기능을 할 수 있는것 같음
                # 'classes': ('collapse',),
            },
        ),

    )
    inlines = (PhotoInline,)

    # 다대다 관계의 모델만 사용가능함
    filter_horizontal = ('cafeMenu',)


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'get_thumbNali')
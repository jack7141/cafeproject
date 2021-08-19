from django.contrib import admin
from .models import Cafe,CafeType,Menu, Photo


@admin.register(CafeType, Menu)
class ItemAdmin(admin.ModelAdmin):
    '''
    * 카페 메뉴 패널
    '''
    pass

@admin.register(Cafe)
class RoomAdmin(admin.ModelAdmin):
    pass

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
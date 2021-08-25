'''
* 모델에 더미 데이터를 넣기 위해 만들어진 Command 파일
'''

# 커맨드 커스텀을 위해서 import
from django.core.management.base import BaseCommand
from cafes.models import Menu

class Command(BaseCommand):

    help = "Menu 입력 커멘드"
    '''
    def add_arguments(self, parser):
        parser.add_argument(
            "--times", help="How many times do you want me to tell you that I love you?"
        )
    def handle(self, *args, **options):
        times = options.get("times")
        for t in range(0, int(times)):
            self.stdout.write(self.style.SUCCESS("I love you"))
    '''

    def handle(self, *args, **options):
        menus = [
            ('자허토르테', 55000),
            ('원형 1단 (3호)', 85000),
            ('원형 1단 (5호)', 145000),
            ('프리미엄 카스텔라 (오리지널)', 30000),
            ('마카롱 (8구)', 31000),
            ('아메리카노', 4500),
            ('아메리카노', 4500),
            ('티', 4500),
            ('얼그레이 커피 타르트', 4500),
            ('마카롱(1ea)', 3000),
            ('마카롱(6ea)', 18000),
            ('듁스화이트', 4000),
            ('듁스블랙', 4000),
            ('파네토네(대)', 8000),
            ('식빵', 5800),
            ('BLT 샌드위치', 7300),
            ('프리미엄 파운드', 16000),
            ('오페라 (조각)', 7500),
            ('봉봉 15구 세트', 41000),
            ('봉봉 10구 세트', 28000),
            ('봉봉 6구 세트', 17500),
            ('봉봉 4구 세트', 12500),
            ('봉봉 2구 세트', 6500),
            ('블랙커피', 3800),
            ('화이트커피', 4500),
            ('핸드드립', 2500),
            ('플레인 베이글', 4500),
            ('포비 파운드', 4500),
        ]

        for a in menus:
            Menu.objects.create(name=a[0], price=a[1])

        self.stdout.write(self.style.SUCCESS('생성이 완료되었습니다.'))

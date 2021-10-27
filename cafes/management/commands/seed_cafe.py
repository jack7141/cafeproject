'''
* 모델에 더미 데이터를 넣기 위해 만들어진 Command 파일
'''

# 커맨드 커스텀을 위해서 import
from django.core.management.base import BaseCommand
from cafes.models import Cafe, CafeType, Photo, Menu
from users.models import User
from django_seed import Seed

from django.contrib.admin.utils import flatten
from ConsVar.ConstVar import CITY_CHOICES, COUNTRY_CHOICES_GANGNAM, COUNTRY_CHOICES_GANGBOK
import random

class Command(BaseCommand):

    help = "카페생성 입력 커멘드"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="몇개의 카페를 생성하시겠습니까?"
        )

    def handle(self, *args, **options):
        # number가 입력되지 않으면 기본적으로 1개를 생성

        number = options.get('number')
        seed = Seed.seeder()

        # 모델 인스턴스 생성
        allUser = User.objects.all()
        cafeTypes = CafeType.objects.all()
        cafeMenus = Menu.objects.all()

        RandomCity = random.choice(CITY_CHOICES)

        if RandomCity[0] == '서울-강북':
            RandomCountry = random.choice(COUNTRY_CHOICES_GANGBOK)
        elif RandomCity[0] == '서울-강남':
            RandomCountry = random.choice(COUNTRY_CHOICES_GANGNAM)

        seed.add_entity(Cafe, number, {
            'host': lambda x: random.choice(allUser),
            'cafetype': lambda x: random.choice(cafeTypes),
            'city' : RandomCity[0],
            'country' : RandomCountry[0],
        })

        createPhotos = seed.execute()
        flattenDatas = flatten(createPhotos.values())
        for id in flattenDatas:
            elementsCafes = Cafe.objects.get(id=id)

            for i in range(1, random.randint(6,7)):
                # Forien Key 추가 방법 Create함수 이용
                print(i)
                Photo.objects.create(
                    caption = seed.faker.sentence(),
                    file = f'cafeImages/{random.randint(1,9)}.jpg',
                    room = elementsCafes
                )

            for menu in cafeMenus:
                magicNumber = random.randint(0, 15)
                if magicNumber % 2  == 0:
                    # add 함수는 Class에서 바로 접근할 수 없어서 instance를 사용해서 접근해야함
                    elementsCafes.cafeMenu.add(menu)

        self.stdout.write(self.style.SUCCESS(f'{number}개 카페 생성 완료'))



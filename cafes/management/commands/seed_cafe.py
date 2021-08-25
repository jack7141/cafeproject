'''
* 모델에 더미 데이터를 넣기 위해 만들어진 Command 파일
'''

# 커맨드 커스텀을 위해서 import
from django.core.management.base import BaseCommand
from cafes.models import Cafe, CafeType
from users.models import User
from django_seed import Seed
from ConsVar.ConstVar import CITY_CHOICES
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
        allUser = User.objects.all()
        cafeTypes = CafeType.objects.all()
        print(cafeTypes)
        citychoice = CITY_CHOICES
        seed.add_entity(Cafe, number, {
            'host': lambda x: random.choice(allUser),
            'cafetype': lambda x: random.choice(cafeTypes),
        })

        seed.execute()
        self.stdout.write(self.style.SUCCESS(f'{number}개 카페 생성 완료'))
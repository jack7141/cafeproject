'''
* 모델에 더미 데이터를 넣기 위해 만들어진 Command 파일
'''

# 커맨드 커스텀을 위해서 import
from django.core.management.base import BaseCommand
from cafes.models import Cafe
from users.models import User
from django_seed import Seed
from reviews.models import Review
import random

class Command(BaseCommand):

    help = "카페생성 입력 커멘드"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="몇개의 리뷰를 생성하시겠습니까?"
        )

    def handle(self, *args, **options):
        # number가 입력되지 않으면 기본적으로 1개를 생성

        number = options.get('number')
        seed = Seed.seeder()
        user = User.objects.all()
        cafe = Cafe.objects.all()
        seed.add_entity(
            Review,
            number,
            {
                'user' : lambda x:random.choice(user),
                'cafe' : lambda x:random.choice(cafe),
                'location':lambda x:random.randint(0,6),
                'Interior':lambda x:random.randint(0,6),
                'starPoint':lambda x:random.randint(0,6),
                'cleanPoint':lambda x:random.randint(0,6),
            }
        )
        seed.execute()
        self.stdout.write(self.style.SUCCESS(f'{number}개 리뷰 생성 완료'))



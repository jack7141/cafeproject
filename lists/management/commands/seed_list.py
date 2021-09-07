'''
* 모델에 더미 데이터를 넣기 위해 만들어진 Command 파일
'''

# 커맨드 커스텀을 위해서 import
from django.core.management.base import BaseCommand
from cafes.models import Cafe
from users.models import User
from django_seed import Seed
from lists.models import List
import random
from django.contrib.admin.utils import flatten

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
            List,
            number,
            {
                'user' : lambda x:random.choice(user),
            }
        )
        create = seed.execute()
        clean = flatten(list(create.values()))
        for id in clean:
            list_model = List.objects.get(id=id)
            to_add = cafe[random.randint(0, 5): random.randint(6, 30)]
            # *로 array를 가져오면 요소만 가져올 수 있다.
            list_model.cafes.add(*to_add)
        self.stdout.write(self.style.SUCCESS(f'{number}개 리스트 생성 완료'))



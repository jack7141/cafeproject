'''
* 모델에 더미 데이터를 넣기 위해 만들어진 Command 파일
'''

# 커맨드 커스텀을 위해서 import
from django.core.management.base import BaseCommand
from users.models import User

from django_seed import Seed


class Command(BaseCommand):

    help = "계정생성 입력 커멘드"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="몇개의 계정을 생성하시겠습니까?"
        )

    def handle(self, *args, **options):
        # number가 입력되지 않으면 기본적으로 1개를 생성
        number = options.get('number')
        seed = Seed.seeder()
        seed.add_entity(User, number, {
            'is_staff':False,
            'is_superuser':False
        })
        seed.execute()
        self.stdout.write(self.style.SUCCESS(f'{number}명 유저 생성 완료'))
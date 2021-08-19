from django.db import models
from core import models as CoreModle

class Review(CoreModle.TimeStampedModel):
    '''
    * 리뷰 모델
    '''
    # 리뷰
    review = models.TextField()

    # 맛점수
    starPoint = models.IntegerField()

    # 인테리어 점수
    Interior = models.IntegerField()

    # 위치점수
    location = models.IntegerField()
    
    # 청결
    clean = models.IntegerField()

    # 리뷰 쓴 유저
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    # 카페
    cafe = models.ForeignKey('cafes.Cafe', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.cafe.cafeName} - {self.review}'

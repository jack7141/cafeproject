from django.db import models


class TimeStampedModel(models.Model):
    '''
    * 모델 생성 관리 모델
    '''
    # auto_now_add는 내가 새로 생성하면 그때 기록을해준다.
    created = models.DateTimeField(auto_now_add=True)
    # auto_now는 내가 생성할때마다 기록을해준다.
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class AbstractItem(TimeStampedModel):
    '''
    * 다대다의 Item 관리 모델
    '''

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
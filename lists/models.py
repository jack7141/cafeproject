from django.db import models
from core.models import TimeStampedModel

class List(TimeStampedModel):

    name = models.CharField(max_length=80)
    user = models.ForeignKey('users.User',on_delete=models.CASCADE)
    cafes = models.ManyToManyField('cafes.Cafe', blank=True)

    def __str__(self):
        return f'{self.name}'

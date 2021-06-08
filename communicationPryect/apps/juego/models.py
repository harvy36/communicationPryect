from django.db import models
from django.contrib.auth.models import User, Group
# Create your models here.


class Score(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    time = models.DurationField(blank=True, null=True)
    score = models.IntegerField(default=0)
    damage = models.IntegerField(default=0)
    win = models.BooleanField(default=False)
    datecreated = models.DateField(null=True, auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return str(self.score)


class Statistic(models.Model):
    maxScore  =  models.ForeignKey(
        Score, on_delete=models.CASCADE
    )
    user =  models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    countGames = models.IntegerField(default=0)

    def __str__(self):
        return str(self.score)

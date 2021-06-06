from rest_framework.serializers import ModelSerializer
from .models import (Score,Statistic)


class ScoreSerializer(ModelSerializer):
    class Meta:
        model = Score
        fields = ('__all__')

class StatisticSerializer(ModelSerializer):
    class Meta:
        model = Statistic
        fields = ('__all__')

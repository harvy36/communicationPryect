from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, GenericAPIView
# from django.core.serializers import serialize
from .serializers import (ScoreSerializer, StatisticSerializer)
# models
from .models import (Score, Statistic)

# score
class scoreCreateAPIView(CreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer


class scoreListAPIView(ListAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer


class scoreUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer


# statistic
class statisticCreateAPIView(CreateAPIView):
    queryset = Statistic.objects.all()
    serializer_class = StatisticSerializer

class statisticUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Statistic.objects.all()
    serializer_class = StatisticSerializer

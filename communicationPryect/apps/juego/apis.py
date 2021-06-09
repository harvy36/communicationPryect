from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, GenericAPIView
# from django.core.serializers import serialize
from .serializers import (ScoreSerializer, StatisticSerializer)
# models
from .models import (Score, Statistic)
from rest_framework.authtoken.models import Token

# score
class scoreCreateAPIView(CreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

    def perform_create(self, serializer):
        try:
            token = self.request.META['Authorization']
            token = token.split()
            tokenobject = Token.object.get(key= token[1])
            serializer.save(user=tokenobject.user)
        except:
            serializer.save()

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

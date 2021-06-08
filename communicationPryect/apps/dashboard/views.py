from django.shortcuts import render
from django.db.models import Avg, Max
from django.views.generic.base import TemplateView
from django.views.generic import (
  View,
  UpdateView,
  ListView
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin
)
from django.contrib.auth.forms import UserChangeForm

from apps.juego.models import Score
from django.contrib.auth.models import User
# Create your views here.

def handler404(request, exception):
  return render(request, '404.html')

class BaseView(TemplateView):
  template_name = 'dashboardTemplate.html'


class dashboardView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
      countGames = Score.objects.count()
      winGames = Score.objects.filter(win=True).count()
      loseGames = Score.objects.filter(win=False).count()
      scores_date = Score.objects.values_list('datecreated').distinct()
      dates = []
      scores_score = []
      for d in scores_date:
        dates.append(d)
        queryset= Score.objects.filter(datecreated=d).aggregate(score_avg=Avg('score'))
        scores_score.append(queryset[0].score_avg)
      highScores = Score.objects.all().order_by("-score")[:5]
      request_values = {
        "countGames":countGames,
        "winGames":winGames,
        "loseGames":loseGames,
        "scores_score":scores_score,
        "scores_date":dates,
        "highScores":highScores,
      }
      return render(request, "dashboardTemplate.html",request_values)


class userList(LoginRequiredMixin,ListView):
    model = User
    template_name='user-list.html'

    def get_queryset(self):
        queryset = User.objects.all().annotate(scoreMax=Max('score__score')).order_by("-scoreMax")
        print("get_queryset", queryset)
        return queryset
    

class userProfileView(LoginRequiredMixin,UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        countGames = Score.objects.filter(user=self.request.user).count()
        winGames = Score.objects.filter(win=True, user=self.request.user).count()
        loseGames = Score.objects.filter(win=False, user=self.request.user).count()
        context["countGames"] = countGames
        context["winGames"] = winGames
        context["loseGames"] = loseGames
        return context
    

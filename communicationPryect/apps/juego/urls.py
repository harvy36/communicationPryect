from django.conf.urls import url
from .apis import (
    scoreCreateAPIView,
    scoreUpdateAPIView,
    statisticCreateAPIView,
    statisticUpdateAPIView,
    scoreListAPIView
)
# from django.contrib.auth.decorators import login_required
app_name = 'juego'
urlpatterns = [
	url(r'^crearScore$', scoreCreateAPIView.as_view()),
	url(r'^modificarScore$', scoreUpdateAPIView.as_view()),
	url(r'^listarScore$', scoreListAPIView.as_view()),
    url(r'^crearStatistic$', statisticCreateAPIView.as_view()),
	url(r'^modificarStatistic$', statisticUpdateAPIView.as_view()),
]
from django.conf.urls import url
app_name = 'dashboard'
from .views import BaseView

urlpatterns = [
    url(r'^$', BaseView.as_view()),
]
from django.conf.urls import url
from django.urls import path
app_name = 'dashboard'
from .views import (
    dashboardView,
    userProfileView,
    userList
)

urlpatterns = [
    url(r'^$', dashboardView.as_view()),
    path(
        "profile/<pk>/", userProfileView.as_view(), name="profile"
    ),
    path(
        "userList/", userList.as_view(), name="userList"
    ),
    
]
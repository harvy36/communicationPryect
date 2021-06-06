# from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import (CreateView)
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = "index.html"

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    FormView,
    DetailView
)
# model
from .models import (Score, Statistic)

# Create your views here.

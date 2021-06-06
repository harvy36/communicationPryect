from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

def handler404(request, exception):
  return render(request, '404.html')

class BaseView(TemplateView):
  template_name = 'baseDasboard.html'

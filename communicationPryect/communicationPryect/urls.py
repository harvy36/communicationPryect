"""communicationPryect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path
from django.conf.urls import url
from apps.principal.views import ( IndexView, SignUpView )
from django.contrib.auth.views import LoginView


handler404 = 'apps.dashboard.views.handler404'

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', IndexView.as_view()),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^juego/', include('apps.juego.urls', namespace= "juego" )),
    url(r'^principal/', include('apps.principal.urls', namespace= "principal" )),
    url(r'^dashboard/', include('apps.dashboard.urls', namespace= "dashboard" )),
    # url(r'^usuarios/', include('apps.usuarios.urls', namespace= "usuarios" )),
    url(r'^login/', LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path

from . import views
from django.views.generic import TemplateView
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include

app_name = 'users'

urlpatterns = [
        path('auth/', include('dj_rest_auth.urls'))
]


from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('principal/',views.tablaCate,name='principal'),
]

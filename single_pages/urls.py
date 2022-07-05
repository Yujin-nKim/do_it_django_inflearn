from django.urls import path
from . import views #같은 폴더 내에 views.py import함

urlpatterns = [
    path('', views.landing),
    path('about_me/', views.about_me),
]

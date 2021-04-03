from django.urls import path
from . import views

urlpatterns = [
    path('challenges', views.index),
    path('calendar', views.calendar),
]

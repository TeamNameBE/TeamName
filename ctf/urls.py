from django.urls import path
from . import views

urlpatterns = [
    path('challenges', views.challenges),
    path('calendar', views.calendar),
]

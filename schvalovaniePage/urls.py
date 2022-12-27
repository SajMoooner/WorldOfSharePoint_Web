from django.urls import path
from . import views


urlpatterns = [
    path('', views.schvalovanie, name='schvalovanie'),
]

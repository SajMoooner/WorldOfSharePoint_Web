from django.urls import path
from . import views

urlpatterns = [ path('', views.UpravPage, name='uprav'), ]
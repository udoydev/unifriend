from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [path("home/",views.home, name="home")]
urlpatterns = [path("",views.home, name="home")]

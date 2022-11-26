from django.contrib import admin
from django.urls import path
from wtb.views import Main

urlpatterns = [
    path('', Main.as_view(), name='home')
]

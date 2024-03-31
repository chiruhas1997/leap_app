from django.contrib import admin
from django.urls import path,include

from .views import index,check,fetch,get_fact
urlpatterns = [
    path('', index, name='index'),
    path('health_check',check, name ='check'),
    path('fetch_fact',fetch,name='fetch'),
    path('get_fact',get_fact,name='get_fact'),
]
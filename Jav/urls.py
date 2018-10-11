from django.conf.urls import include, url
from django.contrib import admin

from Jav.views import main, search 

urlpatterns = [

    url('main', main),
    url('search', search),
]
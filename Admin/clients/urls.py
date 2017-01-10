from django.conf.urls import url,include
from django.contrib import admin
from .views import login,dashboard,logout,create

app_name = 'client'

urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^create/$', create, name='create'),

    ]
from django.conf.urls import url, include
from django.contrib import admin
from django.shortcuts import render

from rotns import views


urlpatterns = [
	url(r'^$', views.index, name='rotns'),
    url(r'^admin/', admin.site.urls),
]

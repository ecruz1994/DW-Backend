from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^category/(?P<category_id>\d+)/$', views.category),
]
from django.urls import re_path

from . import views

app_name = 'cookbook'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^(?P<page_id>[0-9]+)/$', views.page, name='page'),
]

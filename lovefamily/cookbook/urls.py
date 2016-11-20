from django.conf.urls import url

from . import views

app_name = 'cookbook'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<page_id>[0-9]+)/$', views.page, name='page'),
]

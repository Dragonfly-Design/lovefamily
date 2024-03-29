"""lovefamily URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import re_path, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from cookbook import views

urlpatterns = [
    re_path(r'^$', views.index, name='home'),
    re_path(r'^cookbook/', include('cookbook.urls')),
    re_path(r'^admin/', admin.site.urls),
]

#enable static files
urlpatterns += staticfiles_urlpatterns()
"""v1 URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^login',Login.as_view()),
    url(r'^logout', Logout.as_view(), name='log out'),
    #url(r'^admin/', admin.site.urls),
    url(r'attendance',Attendance.as_view(),name='attendance'),
    url(r'^admin', View_Courses.as_view(), name='admin'),
    url(r'^test/', include('quiz_app.test_urls')),
    url(r'^', Login.as_view()),
]

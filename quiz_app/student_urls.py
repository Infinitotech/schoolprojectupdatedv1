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
from .student_views import *


urlpatterns = [
    url(r'^test_intro/test questions/', TestQuestions.as_view(), name='test questions'),
    url(r'^test_intro/', TestIntro.as_view(), name='test_intro'),
    url(r'^student\sview\sgroup\stests', StudentViewGroupTests.as_view(), name='student view group tests'),
    url(r'^student\sview\smy\scourses', StudentViewMyCourses.as_view(), name='student view my courses'),

    url(r'^my\sdetails', MyDetails.as_view(), name='my details student'),
    url(r'', include('quiz_app.teacher_urls')),
]
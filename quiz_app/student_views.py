from v1.Database import StudentDataBase
from django.shortcuts import render,redirect
from django.views.generic import View
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.forms.utils import ErrorList
from django.utils.decorators import method_decorator
from pymongo import MongoClient
from v1.decorators import login_required
from quiz_app.Functions.student_functions import *


class StudentViewGroupTests(View):
    @login_required
    def get(self, request):
        test_names, test_score, test_duration, school_id, branch_id, counter, teacher_username = group_test_data(request)
        return render(request, 'student view group tests.html',{'names':zip(test_names,test_duration,test_score,school_id,branch_id,counter,teacher_username)})


class StudentViewMyCourses(View):
    @login_required
    def get(self, request):
        list, user, message = get_course_data(request)
        return render(request, 'student view my courses.html', {'list': list,'user': user,'message':message})


class MyDetails(View):
    @login_required
    def get(self, request):
        user = request.session['user']
        return HttpResponse("Nshaf")
       #return render(request,'my details.html',{'user': user})

    @login_required
    def post(self, request):
        user = ""
        if 'change_username' in request.POST:
            user = change_username(request)
        elif 'change_password' in request.POST:
            user = change_password(request)

        return render(request, 'my details.html', {'user': user})


class TestIntro(View):
     def get(self, request):
         context = get_test_intro(request)
         return render(request, 'test Introduction.html',context)


class TestQuestions(View):
    def get(self, request):
        bool, context = get_test_questions(request)
        if bool:
            return render(request, 'test questions.html', context)
        else:
            request.session.pop('test')
        return redirect ("/test/student%20view%20my%20courses?message=something went wrong")

    def post(self,request):
        context = get_test_results(request)
        return render(request, 'test Results.html',context)
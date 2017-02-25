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





class Student_View_Group_Tests(View):
    def get(self, request):
        test = request.GET.get('g_id')
        mongo = MongoClient()
        db = mongo['dummy_school_project_v1']
        tests = db.tests.find({'course.course_name':test})
        print(tests)
        test_names = []
        test_score = []
        test_duration = []
        count = 0
        dict = {}
        for i in tests:
            test_names.append(i['test_name'])
            test_score.append(i['maximum_score'])
            test_duration.append(i['duration'])
        return render(request, 'student view group tests.html', {'tests':tests,'test_names':test_names, 'test_score':test_score, 'test_duration':test_duration,'test':test})

class Student_View_My_Courses(View):
    def get(self, request):
        mongo = MongoClient()
        name = "azeemullah"
        s = "1"
        b = "1"
        db = mongo['dummy_school_project_v1']
        user = db.users.find_one({"name":"azeemullah", "school_id": 1, "branch_id": 1})

        courses = user['history']['courses']
        list = []
        for i in courses:
            print(i['status'])
            if i['status'] == "active":
                list.append(i['course_name'])

        return render(request, 'student view my courses.html', {'list':list})

class My_Details(View):
    def get(self, request):
        return render(request,'my details.html')
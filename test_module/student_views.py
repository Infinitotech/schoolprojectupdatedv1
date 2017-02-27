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


class Student_View_Group_Tests(View):
    @login_required
    def get(self, request):
        test = request.GET.get('g_id')
        mongo = MongoClient()
        db = mongo['dummy_school_project_v1']
        tests = db.tests.find({'course.course_name':test})
        print("Tests")
        print(tests)
        test_names = []
        test_score = []
        test_duration = []
        dict = {}
        for i in tests:
            test_names.append(i['test_name'])
            test_score.append(i['maximum_score'])
            test_duration.append(i['duration'])
        return render(request, 'student view group tests.html',{'names':zip(test_names,test_duration,test_score)})

class Student_View_My_Courses(View):
    @login_required
    def get(self, request):
        user = request.session['user']
        courses = user['history']['courses']
        list = []
        for i in courses:
            if i['status'] == "active":
                list.append(i['course_name'])
        return render(request, 'student view my courses.html', {'list': list,'user': user})


class My_Details(View):
    @login_required
    def get(self, request):
        user = request.session['user']
        return render(request,'admin_view_courses.html',{'user': user})

    @login_required
    def post(self, request):
        user = request.session['user']
        if 'change_username' in request.POST:
            old_user = user['username']
            new_username = request.POST['username']
            user['username'] = new_username
            StudentDataBase().change_username(new_username,old_user,user)
            request.session['user'] = user
        elif 'change_password' in request.POST:
            password = request.POST['pass2']
            user['password'] = password
            StudentDataBase().change_password(user, password)
            request.session['user'] = user
        return render(request, 'my details.html', {'user': user})


class Test_intro(View):
     def get(self, request):
         value = request.GET['course_name']
         mongo = MongoClient()
         db = mongo['dummy_school_project_v1']
         course = db.tests.find({'test_name':value})
         for i in course:
             question_len = str(len(i['questions']))
             context = {
                 'test_name': value,
                 'question_len': question_len,
                 'test_duration': i['duration'],
                 'type': i['type'],
             }
         print(question_len)
         print ("d")
         return render(request, 'test Introduction.html', context)


class Test_Questions(View):
    def get(self, request):
        test_name = request.GET['test_name']
        mongo = MongoClient()
        db = mongo['dummy_school_project_v1']
        course = db.tests.find_one({'test_name': test_name})
        questions = course['questions']
        options = course['options']
        return render(request, 'test questions.html', {'questions': questions,'options':options, 'test_name':test_name})

    def post(self,request):
        test_name = request.POST.get('test_name')
        mongo = MongoClient()
        db = mongo['dummy_school_project_v1']
        course = db.tests.find_one({'test_name': test_name})
        questions = course['questions']
        dict={}
        for q in questions:
            dict[q]=request.POST.get(q).split('+')[1]
        print (dict)
        return render(request, 'test questions.html')
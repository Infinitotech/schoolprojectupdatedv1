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
    def get(self, request):
        #for i in request.GET['user']:
         #   print (i)
        print ("sada");print(request.GET)
        mongo = MongoClient()
        name = "azeemullah"
        s = "1"

        b = "1"
        db = mongo['dummy_school_project_v1']
        user = request.session['user']
        for key in user:
            print (key,user[key])
        print ("printed")
        user = db.users.find_one({"name":"azeemullah", "school_id": 1, "branch_id": 1})

        courses = user['history']['courses']
        list = []
        for i in courses:
            print(i['status'])
            if i['status'] == "active":
                list.append(i['course_name'])
        print(list)
        return render(request, 'student view my courses.html', {'list':list,'user':user}  )


class My_Details(View):
    def get(self, request):
        user = request.session['user']
        return render(request,'my details.html',{'user': user})

    def post(self, request):
        print("In Post Method")
        mongo = MongoClient()
        db = mongo['dummy_school_project_v1']
        if 'change_username' in request.POST:
            user = request.session['user']
            old_user = user['username']
            new_username = request.POST['username']
            print(user['username'])
            user['username'] = new_username
            db.users.update({'username':old_user},
                            {
                                'username': new_username,
                                'name': user['name'],
                                'father_name': user['father_name'],
                                'password': user['password'],
                                'type': user['type'],
                                'dob': user['dob'],
                                'photo': user['photo'],
                                'nic': user['nic'],
                                'status': user['status'],
                                'school_id': user['school_id'],
                                'branch_id': user['branch_id']
                            })
            request.session['user'] = user

            return render(request, 'my details.html', {'user': user})

        elif 'change_password' in request.POST:
            password = request.POST['pass2']
            user = request.session['user']
            db.users.update({'username': user['username']},
                            {
                                'username': user['username'],
                                'name': user['name'],
                                'father_name': user['father_name'],
                                'password': password,
                                'type': user['type'],
                                'dob': user['dob'],
                                'photo': user['photo'],
                                'nic': user['nic'],
                                'status': user['status'],
                                'school_id': user['school_id'],
                                'branch_id': user['branch_id']
                            })
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
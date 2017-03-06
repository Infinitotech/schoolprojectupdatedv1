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
from datetime import datetime
import time as timeLib


class StudentViewGroupTests(View):
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
        school_id=[]
        branch_id=[]
        counter=[]
        teacher_username=[]
        dict = {}
        for i in tests:
            test_names.append(i['test_name'])
            test_score.append(i['maximum_score'])
            test_duration.append(i['duration'])
            school_id.append(i['school_id'])
            branch_id.append(i['branch_id'])
            counter.append(i['counter'])
            teacher_username.append(i['teacher_username'])
        return render(request, 'student view group tests.html',{'names':zip(test_names,test_duration,test_score,school_id,branch_id,counter,teacher_username)})


class StudentViewMyCourses(View):
    @login_required
    def get(self, request):
        message=request.GET['message']
        user = request.session['user']
        courses = user['history']['courses']
        list = []
        for i in courses:
            if i['status'] == "active":
                list.append(i['course_name'])
        return render(request, 'student view my courses.html', {'list': list,'user': user,'message':message})


class MyDetails(View):
    @login_required
    def get(self, request):
        user = request.session['user']
        return HttpResponse("Nshaf")
       #return render(request,'my details.html',{'user': user})

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


class TestIntro(View):
     def get(self, request):
         teacher_username = request.GET['teacher_username']
         print(teacher_username)
         school_id=request.GET['school_id']
         branch_id=request.GET['branch_id']
         counter=request.GET['counter']
         mongo = MongoClient()
         print('asdf')
         db = mongo['dummy_school_project_v1']
         course = db.tests.find_one({'teacher_username':teacher_username,'school_id':int(school_id),'branch_id':int(branch_id),'counter':int(counter)})
         context={}
         if course:
             question_len = str(len(course['questions']))
             context = {
                 'test_name': course['test_name'],
                 'question_len': question_len,
                 'test_duration': course['duration'],
                 'type': course['type'],
                 'teacher_username': teacher_username,
                 'school_id': int(school_id),
                 'branch_id': int(branch_id),
                 'counter': int(counter)
             }
             del course['_id']
             request.session['test']=course
         return render(request, 'test Introduction.html',context)


class TestQuestions(View):
    def get(self, request):
        course=request.session['test']
        test_name = course['test_name']
        questions = course['questions']
        options = course['options']
        teacher_usernameR = request.GET['teacher_username']
        school_id = int(request.GET['school_id'])
        branch_id = int(request.GET['branch_id'])
        counter = int(request.GET['counter'])
        duration=int(course['duration'])
        if 'test' in request.session:
            if counter==course['counter'] and teacher_usernameR==course['teacher_username'] and school_id==course['school_id'] and branch_id==course['branch_id']:
                return render(request, 'test questions.html', {'questions': questions,'options':options, 'test_name':test_name,'duration':duration})
            else:
                request.session.pop('test')
        return redirect ("/test/student%20view%20my%20courses?message=something went wrong")

    def post(self,request):
        test_name = request.POST.get('test_name')
        mongo = MongoClient()
        db = mongo['dummy_school_project_v1']
        test = db.tests.find_one({'test_name': test_name})
        questions = test['questions']
        solutions=test['solutions']
        user=request.session['user']
        counter = test['counter']
        max=test['maximum_score']
        user_name=user['username']
        course=test['course']
        course_name=course['course_name']
        options=test['options']
        dict={}
        wrong={}
        for q in questions:
            opt=request.POST.get(q)
            if opt:
                dict[q]=opt.split('+')[1]
            else:
                dict[q]="No option selected"
        score=0
        for key,item in dict.items():
            if solutions[key]==item:
                score+=10
            else:
                wrong[key]=item

        percentage=(score/max)*100
        timer=str(request.POST.get('timer')).split(':')
        time = int(timer[0]) * 60 + int(timer[1])
        time=(test['duration'] * 60 - time)
        duration=(timeLib.strftime("%H:%M:%S", timeLib.gmtime(time)))
        dateAndTime=datetime.utcnow()
        db.test_answer.insert({
            'test_counter': counter,
            'teacher_username': test['teacher_username'],
            'student_username': user['username'] ,
            'school_id': test['school_id'],
            'branch_id': test['branch_id'],
            'answers': dict,
            'result': score,
            'maximum_score':max,
            'duration': time,
            'date_given': dateAndTime,
            'solutions' : solutions,
            'questions':questions,
            'course':course
        })

        return render(request, 'test Results.html',{
            'questions': questions,
            'options':options,
            'answers':dict,
            'test_name':test_name,
            'duration':duration,
            'percentage':percentage,
            'user_name':user_name,
            'course':course_name,
            'duration':duration,
            'date':dateAndTime,
            'score':score,
            'max':max,
            'correct':solutions,
            'wrong':wrong
        })
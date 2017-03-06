from .Database import DataBase
from django.shortcuts import render,redirect
from django.views.generic import View
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.forms.utils import ErrorList
from django.utils.decorators import method_decorator
from pymongo import MongoClient
import json


class Logout(View):
    def get(self,request):
        print(' in log out function')
        keys = [key for key in request.session.keys()]
        for key in keys: del request.session[key]
        return redirect(to='/login')


class Login(View):
    def get(self,request):
        my_dict = DataBase.get_school_dict()
        try:
            type = request.session['user']['type']
            if type == 'teacher':
                return redirect('/test/Welcome')
            elif type == 'student':
                return redirect('/test/student%20view%20my%20courses?message=')
        except KeyError:
            pass
        return render(request,'login.html',{'schooldata': my_dict})

    def post(self,request):

        username = request.POST['username']
        password = request.POST['password']
        branchid = request.POST['branchid']
        school_id = request.POST['schoolname']
        request.session.set_expiry(0)
        user = DataBase().authenticate_and_get_user(username, password, school_id, branchid)
        if user:
            del user['_id']
            request.session['user'] = (user)
            request.session['user']['authenticate'] = True
            if user['type'] == 'teacher':
                return redirect('/test/Welcome')
            elif user['type'] == 'student':
                print('opening student homepage')
                return redirect('/test/student%20view%20my%20courses/?message=""')
        else:
            my_dict = DataBase.get_school_dict()
            return render(request, 'login.html', {'error': 'Invalid Credentials!', 'schooldata': my_dict})


class SignUp(View):
    def get(self,request):
        return render(request,'base.html')


class View_Courses(View):
    def get(self, request):
        mongo = MongoClient()
        db = mongo['dummy_school_project_v1']
        class_list = ['7-A', '6-B', '8-A']
        users = {}
        users = db.users.find({'class':'7-A'})

        return render(request,'admin_view_courses.html', {'users': users, 'class_name':'7-A'})

    def post(self, request):
        mongo = MongoClient()
        db = mongo['dummy_school_project_v1']
        class_name = request.POST.get('browser')
        users = db.users.find({'class':class_name})
        user = request.session['user']

        return render(request,'admin_view_courses.html',{'users':users, 'class_name': class_name, 'admin_name': user['name']})

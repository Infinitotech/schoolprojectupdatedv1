from .Database import DataBase
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
import json


class Login(View):
    def get(self,request):
        my_dict = DataBase.get_school_dict()
        try:
            type = request.session['user']['type']
            if type == 'teacher':
                return redirect('/test/Welcome')
            elif type == 'student':
                return redirect('/test/student%20view%20my%20courses')
        except KeyError:
            pass
        return render(request,'login.html',{'schooldata':my_dict})

    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        branchid = request.POST['branchid']
        school_id = request.POST['schoolname']
        request.session.set_expiry(0)
        user = DataBase().authenticate_and_get_user(username, password, school_id, branchid)
        print(user)
        if user:
            del user['_id']
            request.session['user'] = (user)
            if user['type'] == 'teacher':
                return redirect('/test/Welcome')
            elif user['type'] == 'student':
                return redirect('/test/student%20view%20my%20courses')
        else:
            my_dict = DataBase.get_school_dict()
            return render(request, 'login.html', {'error': 'Invalid Credentials!', 'schooldata': my_dict})


class SignUp(View):
    def get(self,request):
        return render(request,'base.html')

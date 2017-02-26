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
        return render(request,'login.html',{'schooldata':my_dict})

    def post(self,request):
        print("check_post_login_post")
        username = request.POST['username']
        password = request.POST['password']
        branchid = request.POST['branchid']
        school_id = request.POST['schoolname']
        request.session.set_expiry(0)
        user = DataBase().authenticate_and_get_user(username, password, school_id, branchid)
        if user:
            del user['_id']
            request.session['user'] = (user)
            return redirect('/test/student%20view%20my%20courses')
        else:
            mongo = MongoClient()
            print("InErrorLogin")
            db = mongo['dummy_school_project_v1']
            school = db.school.find()
            mydict = {}
            for s in school:
                mydict[s['id']] = s['school_name']
            return render(request, 'login.html', {'error': 'Invalid Credentials!', 'schooldata': mydict})


class SignUp(View):
    def get(self,request):
        return render(request,'base.html')

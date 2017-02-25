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


class Login(View):
    def get(self,request):
        mongo = MongoClient()
        db = mongo['dummy_school_project_v1']
        school = db.school.find()
        school_id = []
        school_name = []
        mydict={}
        for s in school:
          mydict[s['id']]=s['school_name']


        print(mydict)
        return render(request,'login.html',{'schooldata':mydict})

class SignUp(View):
    def get(self,request):
        return render(request,'base.html')

class check(View):
    def get(self,request):
        username = request.POST('username')
        password = request.POST('password')
        branchid = request.POST('branchid')
        id = request.POST('schoolname')

        print(username)
        print(id)
        return render(request,'welcome.html')



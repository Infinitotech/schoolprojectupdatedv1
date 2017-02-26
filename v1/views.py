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
        print("In post func")
        db = mongo['dummy_school_project_v1']
        school = db.school.find()
        mydict={}
        for s in school:
          mydict[s['id']]=s['school_name']
        print(mydict)
        return render(request,'login.html',{'schooldata':mydict})

class SignUp(View):
    def get(self,request):
        return render(request,'base.html')

class check(View):
    def authenticate(self, username, password,school_id,branchid):
        mongo = MongoClient()
        db = mongo['dummy_school_project_v1']
        user=db.users.find_one({'school_id': int(school_id), 'password': password, 'branch_id': int(branchid), 'username': username})
        if user:
            return user
        else:
            return None

    def post(self,request):
        print("check_post")
        username = request.POST['username']
        password = request.POST['password']
        branchid = request.POST['branchid']
        school_id = request.POST['schoolname']
        user = self.authenticate(username, password,school_id,branchid)
        if user :
            return redirect('test/student%20view%20my%20courses', user)
        else:
            mongo = MongoClient()
            print("InErrorLogin")
            db = mongo['dummy_school_project_v1']
            school = db.school.find()
            mydict = {}
            for s in school:
                mydict[s['id']] = s['school_name']
            return render(request, 'login.html', {'error': 'Invalid Credentials!', 'schooldata': mydict})


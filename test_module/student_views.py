from django.shortcuts import render,redirect
from django.views.generic import View
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.forms.utils import ErrorList
from django.utils.decorators import method_decorator






class Student_View_Group_Tests(View):
    def get(self, request):
        return render(request, 'student view group tests.html')

class Student_View_My_Courses(View):
    def get(self, request):
        return render(request, 'student view my courses.html')

class My_Details(View):
    def get(self, request):
        return render(request, 'my details.html')
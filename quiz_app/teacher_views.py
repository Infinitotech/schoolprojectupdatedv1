from v1.Database import QuizDataBase
from django.shortcuts import render,redirect
from django.views.generic import View
from quiz_app.Functions.teacher_functions import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.forms.utils import ErrorList
from django.utils.decorators import method_decorator
import random,json
from pymongo import MongoClient
from v1.decorators import login_required


class BasePage(View):
    def get(self,request):
        return render(request,'base.html')


class AccessLists(View):
    def get(self,request):
        return render(request,'Access Lists.html')


class AddNewRegisteredUserGroup(View):
    def get(self,request):
        return render(request,'Add new registered user group.html')


class AddNewTest(View):
    def get(self,request):
        return render(request,'Add new test.html')


class AddQuestion(View):
    def get(self,request, test_name, test_counter):
        return render(request,'Manage question.html',{'test_name':test_name,'test_counter':test_counter}) #this is the main thing

    def post(self, request, test_name, test_counter):
        test = QuizDataBase().get_test_dict(test_counter, request.session['user']['username'],
                                            request.session['user']['branch_id'], request.session['user']['school_id'])
        question_number = QuizDataBase.get_question_number(test)
        param_dict = get_parameters_from_request_for_each_question_teacher_creates(request=request)
        test = add_question_to_test_document(test, param_dict, question_number)
        QuizDataBase().update_test(test)
        return render(request, 'Manage question.html', {'test_name': test_name,'test_counter': test_counter})


class Assignteststep1(View):
    def get(self,request):
        print("sdafdf")
        mongo = MongoClient()
        user = request.session['user']
        db = mongo['dummy_school_project_v1']
        course_name = request.POST.get('test_id')
        tests = db.tests.find({"teacher_username": user['name']})

        return render(request,'Assign test step 1.html',{'course_name':course_name,'tests':tests,'user':user})

    def post(self,request):
        mongo = MongoClient()
        db = mongo['dummy_school_project_v1']
        user = request.session['user']
        tests = db.tests.find({"teacher_username": user['name']})
        course_name = request.POST.get('course_id')
        print("asfsfd")
        print(course_name)
        return render(request, 'Assign test step 1.html', {'course_name': course_name, 'tests': tests,'user':user})


class Assignteststep1b(View):
    def get(self,request):
        return render(request,'Assign test step 1b.html')


class Assignteststep2(View):
    def get(self,request):
        return render(request,'Assign test step 2.html',{'user':user})

    def post(self,request):
        user = request.session['user']
        test_name = request.POST.get('test_id')
        coursename = request.POST.get('cour')
        print(test_name)
        print(coursename)
        return render(request, 'Assign test step 2.html',{'test_name':test_name,'course_name':coursename,'user':user})


class Assignteststep3(View):

    def get(self,request):
        test_name = request.GET('test-name')
        coursename = request.GET('course-name')
        return render(request, 'Assign test step 3.html', {'test_name': test_name, 'course_name': coursename,'user':user})

    def post(self,request):
        test_name = request.POST.get('test-name')
        coursename = request.POST.get('course-name')
        user = request.session['user']
        return render(request, 'Assign test step 3.html', {'test_name': test_name, 'course_name': coursename,'user':user})



class Assignteststep3a(View):
    def get(self,request):
        return render(request,'Assign test step 3a.html')


class Assignteststep3b(View):
    def get(self,request):
        return render(request,'Assign test step 3b.html')


class Assistants(View):
    def get(self,request):
        return render(request,'Assistants.html')


class Base(View):
    def get(self,request):
        return render(request,'base.html')


class Categories(View):
    def get(self,request):
        return render(request,'Categories.html')


class Certificates(View):
    def get(self,request):
        return render(request,'Certificates.html')


class Community(View):
    def get(self,request):
        return render(request,'Community.html')


class ContactUsClassMarker(View):
    def get(self,request):
        return render(request,'Contact us ClassMarker.html')


class EditQuestionSettings(View):
    def get(self,request):
        return render(request,'Edit question settings.html')


class ExportResults(View):
    def get(self,request):
        return render(request,'Export results.html')


class Files(View):
    def get(self,request):
        return render(request,'Files.html')


class Group(View):
    def get(self,request):
        return render(request,'Group.html')


class Help(View):
    def get(self,request):
        return render(request,'Help.html')


class Introduction(View):
    def get(self,request):
        return render(request,'Introduction.html')


class Links(View):
    def get(self,request):
        return render(request,'links.html')


class ManageAccessList(View):
    def get(self,request):
        return render(request,'Manage Access List.html')


class ManageQuestionShow(View):
    def get(self,request):
        return render(request,'Manage question(show).html')


class ManageQuestion(View):
    def get(self,request, test_name, test_counter):
        return render(request,'Manage question.html',{'test_name':test_name,'test_counter':test_counter})


class ManageTestPost(View):
    def get(self,request):
        return render(request,'Manage test(post).html')


class ManageTest(View):
    @login_required
    def get(self,request):
        if request.session['user']['type'] == 'student':
            return redirect(to='quiz_app:my details student')
        test_name = (request.GET['test_name'])
        test_counter = QuizDataBase().create_test(test_name, request.session['user']['username'], request.session['user']['branch_id'],
                                                  request.session['user']['school_id'])
        return render(request,'Manage test.html',{'test_name':test_name,'test_counter':test_counter})


class MyAccount(View):
    def get(self,request):
        mongo =  MongoClient()
        db = mongo['dummy_school_project_v1']
        user = request.session['user']
        users = db.users.find_one({'name':user['name'], 'type':user['type']})
        for i in users:
            print(users[i])
        return render(request,'My Account.html',{'users': users})


class MyTests(View):
    def get(self,request):
        print("In tests")
        return render(request,'My tests.html')


class OnlineTestingFreeQuizMakerCreateTheBestWebBasedQuizzesClassMarker(View):
    def get(self,request):
        return render(request,'Online Testing Free Quiz Maker Create the Best web-based quizzes ClassMarker.html')


class OverallTestResultsByGroup(View):
    def get(self,request):
        return render(request,'Overall test results by group.html')


class OverallTestResultsByLink(View):
    def get(self,request):
        return render(request,'Overall test results by link.html')


class OverallTestResults(View):
    def get(self,request):
        return render(request,'Overall test results.html')


class Overview(View):
    def get(self,request):
        return render(request,'Overview.html')


class PrivacyClassMarker(View):
    def get(self,request):
        return render(request,'Privacy ClassMarker.html')


class QuestionBank(View):
    def get(self,request):
        return render(request,'Question bank.html')


class QuestionOrder(View):
    def get(self,request):
        return render(request,'Question order.html')


class QuizMakerStepByStepInstructionsClassMarker(View):
    def get(self,request):
        return render(request,'Quiz maker - Step by Step Instructions ClassMarker.html')


class RecentResultsLinks(View):
    def get(self,request):
        return render(request,'Recent results(links).html')


class RecentResults(View):
    def get(self,request):
        return render(request,'Recent results.html')


class Results(View):
    def get(self,request):
        return render(request,'Results.html')


class TermsAndConditionsClassMarker(View):
    def get(self,request):
        return render(request,'Terms and conditions ClassMarker.html')


class Test(View):
    def get(self,request):
        return render(request,'Test.html')


class Themes(View):
    def get(self,request):
        return render(request,'Themes.html')


class Upgrade(View):
    def get(self,request):
        return render(request,'Upgrade.html')


class VideoDemonstrations(View):
    def get(self,request):
        return render(request,'Video Demonstrations.html')


class WebBasedOnlineTestingServiceFreeQuizMakerClassMarker(View):
    def get(self,request):
        return render(request,'Web-based online testing service _ Free quiz maker ClassMarker.html')


class Welcome(View):
    def get(self,request):
        return render(request,'welcome.html', {'username':request.session['user']['name']})




class assign_test_group(View):
    def get(self,request):
        user = request.session['user']
        mongo = MongoClient()
        db = mongo['dummy_school_project_v1']


        cursor = db.courses.find({"current_year.teachers":{"$elemMatch":{ "username": user['name'] }}})


        return render(request, "assign test group.html", {'courses':cursor,'user':user})
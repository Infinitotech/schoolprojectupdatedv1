from v1.Database import QuizDataBase
from django.shortcuts import render,redirect
from django.views.generic import View
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.forms.utils import ErrorList
from django.utils.decorators import method_decorator
import random,json


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
        answers_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
        test = QuizDataBase().get_test_dict(test_counter, request.session['user']['username'],
                                            request.session['user']['branch_id'], request.session['user']['school_id'])
        print(test)
        question_number = QuizDataBase.get_question_number(test)
        test_name = request.POST.get('test_name')
        question = request.POST.get('question1')
        correct1 = request.POST.get('correct1')
        correct2 = request.POST.get('correct2')
        correct3 = request.POST.get('correct3')
        correct4 = request.POST.get('correct4')
        ans1 = request.POST['answer1']
        ans2 = request.POST.get('answer2')
        ans3 = request.POST.get('answer3')
        ans4 = request.POST.get('answer4')
        points = request.POST['points']
        randomize_answer = request.POST['random_a']
        if correct1 is not None:
            correct_answer = correct1
        elif correct2 is not None:
            correct_answer = correct2
        elif correct3 is not None:
            correct_answer = correct3
        else:
            correct_answer = correct4
        try:
            question_dict = test['questions']
            question_dict[question_number] = question
            test['questions'] = question_dict
            option_dict = test['options']
            option_dict[QuizDataBase.get_question_number(test, False)] = {
                'a': ans1,
                'b': ans2,
                'c': ans3,
                'd': ans4
            }
            test['options'] = option_dict
            solutions_dict = test['solutions']
            solutions_dict[question_number] = answers_dict[int(correct_answer)]
            test['solutions'] = solutions_dict
        except KeyError:
            test['questions'] = {question_number: question}
            test['options'] = {
                question_number: {
                    'a': ans1,
                    'b':  ans2,
                    'c': ans3,
                    'd': ans4
                }
            }
            test['solutions'] = {
                question_number: answers_dict[int(correct_answer)]
            }
        QuizDataBase().update_test(test)
        return render(request, 'Manage question.html',{'test_name':test_name,'test_counter':test_counter})


class AssignTestStep1(View):
    def get(self,request):
        return render(request,'Assign test step 1.html')


class AssignTestStep1B(View):
    def get(self,request):
        return render(request,'Assign test step 1b.html')


class AssignTestStep2(View):
    def get(self,request):
        return render(request,'Assign test step 2.html')


class AssignTestStep3(View):
    def get(self,request):
        return render(request,'Assign test step 3.html')


class AssignTestStep3A(View):
    def get(self,request):
        return render(request,'Assign test step 3a.html')


class AssignTestStep3B(View):
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
        print(test_name)
        print(test_counter)
        return render(request,'Manage question.html',{'test_name':test_name,'test_counter':test_counter})


class ManageTestPost(View):
    def get(self,request):
        return render(request,'Manage test(post).html')


class ManageTest(View):
    def get(self,request):
        test_name= (request.GET['test_name'])
        test_counter = QuizDataBase().create_test(test_name, request.session['user']['username'], request.session['user']['branch_id'],
                                                  request.session['user']['school_id'])
        return render(request,'Manage test.html',{'test_name':test_name,'test_counter':test_counter})


class MyAccount(View):
    def get(self,request):
        return render(request,'My Account.html')


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
        return render(request,'welcome.html',{'username':request.session['user']['name']})
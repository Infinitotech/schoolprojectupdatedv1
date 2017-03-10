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
        user = request.session['user']
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
        user = request.session['user']
        coursename = request.GET('course-name')
        return render(request, 'Assign test step 3.html', {'test_name': test_name, 'course_name': coursename,'user':user})

    def post(self,request):
        test_name = request.POST.get('test-name')
        coursename = request.POST.get('course-name')
        user = request.session['user']
        return render(request, 'Assign test step 3.html', {'test_name': test_name, 'course_name': coursename,'user':user})


class tt(View):
    def post(self,request):
        user = request.session['user']
        available = request.POST.get('available')

        fromdate = request.POST.get('show_from_date')
        lastdate = request.POST.get('show_until_date')
        user = request.session['user']

        fromhours = request.POST.get('show_from_h')
        fromminute = request.POST.get('show_from_m')
        fromampm = request.POST.get('show_from_ampm')

        untilhours = request.POST.get('show_until_h')
        untilminute = request.POST.get('show_until_m')
        untilampm = request.POST.get('show_until_ampm')

        attempt = request.POST.get('practice')

        resume = request.POST.get('save_finish_later')
        ''' RESUME WILL BE NONE OR 1'''

        QPP = request.POST.get('questions_displayed_per_page')
        points = request.POST.get('show_question_points_during_test')
        random = request.POST.get('random_q')
        MUSTSELECTANSWER = request.POST.get('must_select_answer')
        CORRECTTOCONTINUE = request.POST.get('correct_to_continue')
        question_grading_and_feedback_duringtest= request.POST.get('test_feedback_q')
        reveal_correct_answer_during_test = request.POST.get('test_feedback_qca')
        a=True

        allow_click_previous= request.POST.get('allow_click_previous')
        score = request.POST.get('score')

        if(available=='1'):
            available=True
        else:
            available=False

        if (points == '1'):
            points = True
        else:
            points = False

        if (random == '1'):
            random = True
        else:
            random = False

        if ( MUSTSELECTANSWER== '1'):
            MUSTSELECTANSWER = True
        else:
            MUSTSELECTANSWER = False

        if (CORRECTTOCONTINUE == '1'):
            CORRECTTOCONTINUE = True
        else:
            CORRECTTOCONTINUE = False

        if (question_grading_and_feedback_duringtest == '1'):
            question_grading_and_feedback_duringtest = True
        else:
            question_grading_and_feedback_duringtest = False

        if (reveal_correct_answer_during_test == '1'):
            reveal_correct_answer_during_test = True
        else:
            reveal_correct_answer_during_test = False

        if (allow_click_previous == '1'):
            allow_click_previous = True
        else:
            allow_click_previous = False

        if (attempt == '0'):
            attempt=0
        if (attempt == '2'):
            attempt=-1
        if (attempt == '1'):
            noa = request.POST.get('attempts_allowed')
            attempt=noa

        time = request.POST.get('time_limit')
        mongo = MongoClient()
        test_name = request.POST.get('test-name1')
        user = request.session['user']
        coursename = request.POST.get('course-name1')
        db = mongo['dummy_school_project_v1']

        tests = db.assigntest.find_one_and_update(
            {
                'teacher_username': user['name'],
                'school_id': user['school_id'],
                'branch_id': user['branch_id'],
                'test_name': test_name,
            },
        {
            '$push':{
            'course': {
                'course_name': coursename,
                'fromdate': fromdate,
                'deadline': lastdate,
                'maximum_score': score,
                'duration': time,
                'available': available,
                'showfromtime': fromdate,
                'showlasttime': lastdate,
                'noofattempts': attempt,
                'resume': resume,
                'questions_displayed_per_page': QPP,
                'show_question_points_during_test': points,
                'random': random,
                'must_select_answer': MUSTSELECTANSWER,
                #'correct_to_continue': CORRECTTOCONTINUE,
                'question_grading_and_feedback_duringtest': question_grading_and_feedback_duringtest,
                #'reveal_correct_answer_during_test': reveal_correct_answer_during_test,
                'allow_click_previous': allow_click_previous

            }

            }

        }
        )
        print(user['name'])
        print(user['school_id'])
        print(user['branch_id'])
        print(test_name)
        print(coursename)
        users = db.assigntest.find_one({'teacher_username': user['name'],
                'school_id': user['school_id'],
                'branch_id': user['branch_id']})
        print(users)
        mongo.close()



        print(allow_click_previous)

        print(reveal_correct_answer_during_test)
        print(question_grading_and_feedback_duringtest)
        print(MUSTSELECTANSWER)
        print(CORRECTTOCONTINUE)
        print(points)


        print(QPP)

        print(resume)



        print(time)


        print("dsafdsf")
        print(available)
        print(fromhours)
        print(fromminute)
        print(fromampm)

        print(untilhours)
        print(untilminute)
        print(untilampm)



        print(fromdate)
        print(lastdate)



        return render(request, 'assign test group.html')


class Assignteststepsetting(View):
    def get(self,request):
        return render(request,'Assistants.html')

    def post(self,request):
        '''available = request.POST.get('available')
        unavailable = request.POST.get('unavailable')
        fromdate = request.POST.get('show_from_date')
        lastdate = request.POST.get('show_until_date')
        user = request.session['user']
        test_name = request.POST.get('test-name')
        coursename = request.POST.get('course-name')

        print("dsafdsf")
        print(available)
        print(unavailable)
        print(fromdate)
        print(lastdate)'''
        print("sdfsdfsdf")
        user = request.session['user']
        return render(request, 'Assistants.html',{'test_name': "dfsdfs", 'course_name': "sdfsdfsdf", 'user': user})


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
        mongo = MongoClient()
        user = request.session['user']
        db = mongo['dummy_school_project_v1']
        course_name = request.POST.get('test_id')
        tests = db.tests.find({"teacher_username": user['name']})
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




class assigntestgroup(View):
    def get(self,request):
        user = request.session['user']
        mongo = MongoClient()
        db = mongo['dummy_school_project_v1']


        cursor = db.courses.find({"current_year.teachers":{"$elemMatch":{ "username": user['name'] }}})


        return render(request, "assign test group.html", {'courses':cursor,'user':user})
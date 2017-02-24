from django.shortcuts import render,redirect
from django.views.generic import View
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.forms.utils import ErrorList
from django.utils.decorators import method_decorator


class BasePage(View):
    def get(self,request):
        return render(request,'base.html')


class Access_Lists(View):
    def get(self,request):
        return render(request,'Access Lists.html')


class Add_new_registered_user_group(View):
    def get(self,request):
        return render(request,'Add new registered user group.html')

class Add_new_test(View):
    def get(self,request):
        return render(request,'Add new test.html')


class Assign_test_step_1(View):
	def get(self,request):
		return render(request,'Assign test step 1.html')


class Assign_test_step_1b(View):
	def get(self,request):
		return render(request,'Assign test step 1b.html')


class Assign_test_step_2(View):
	def get(self,request):
		return render(request,'Assign test step 2.html')


class Assign_test_step_3(View):
	def get(self,request):
		return render(request,'Assign test step 3.html')


class Assign_test_step_3a(View):
	def get(self,request):
		return render(request,'Assign test step 3a.html')


class Assign_test_step_3b(View):
	def get(self,request):
		return render(request,'Assign test step 3b.html')


class Assistants(View):
	def get(self,request):
		return render(request,'Assistants.html')


class base(View):
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


class Contact_us_ClassMarker(View):
	def get(self,request):
		return render(request,'Contact us ClassMarker.html')


class Edit_question_settings(View):
	def get(self,request):
		return render(request,'Edit question settings.html')


class Export_results(View):
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


class links(View):
	def get(self,request):
		return render(request,'links.html')


class Manage_Access_List(View):
	def get(self,request):
		return render(request,'Manage Access List.html')


class Manage_question_show(View):
	def get(self,request):
		return render(request,'Manage question(show).html')


class Manage_question(View):
	def get(self,request):
		test_name=request.GET['test_name']
		#return render(request,'Manage question.html')
		return render(request,'Manage question.html',{'test_name':test_name})
		#return render_to_response("Manage question.html", {'top_list': "nothing"},context_instance=RequestContext(request))


class Manage_test_post(View):
	def get(self,request):
		return render(request,'Manage test(post).html')


class Manage_test(View):
	def get(self,request):
		test_name= (request.GET['test_name'])
		return render(request,'Manage test.html',{'test_name':test_name})


class My_Account(View):
	def get(self,request):
		return render(request,'My Account.html')


class My_tests(View):
	def get(self,request):
		return render(request,'My tests.html')


class Online_Testing_Free_Quiz_Maker_Create_the_Best_web_based_quizzes_ClassMarker(View):
	def get(self,request):
		return render(request,'Online Testing Free Quiz Maker Create the Best web-based quizzes ClassMarker.html')


class Overall_test_results_by_group(View):
	def get(self,request):
		return render(request,'Overall test results by group.html')


class Overall_test_results_by_link(View):
	def get(self,request):
		return render(request,'Overall test results by link.html')


class Overall_test_results(View):
	def get(self,request):
		return render(request,'Overall test results.html')


class Overview(View):
	def get(self,request):
		return render(request,'Overview.html')


class Privacy_ClassMarker(View):
	def get(self,request):
		return render(request,'Privacy ClassMarker.html')


class Question_bank(View):
	def get(self,request):
		return render(request,'Question bank.html')


class Question_order(View):
	def get(self,request):
		return render(request,'Question order.html')


class Quiz_maker_Step_by_Step_Instructions_ClassMarker(View):
	def get(self,request):
		return render(request,'Quiz maker - Step by Step Instructions ClassMarker.html')


class Recent_results_links(View):
	def get(self,request):
		return render(request,'Recent results(links).html')


class Recent_results(View):
	def get(self,request):
		return render(request,'Recent results.html')


class Results(View):
	def get(self,request):
		return render(request,'Results.html')


class Terms_and_conditions_ClassMarker(View):
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


class Video_Demonstrations(View):
	def get(self,request):
		return render(request,'Video Demonstrations.html')


class Web_based_online_testing_service_Free_quiz_maker_ClassMarker(View):
	def get(self,request):
		return render(request,'Web-based online testing service _ Free quiz maker ClassMarker.html')


class welcome(View):
	def get(self,request):
	    return render(request,'welcome.html')
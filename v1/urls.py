"""v1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^student\sview\sgroup\stests', Student_View_Group_Tests.as_view()),
    url(r'^student\sview\smy\scourses', Student_View_My_Courses.as_view()),
    url(r'^my\sdetails', My_Details.as_view()),
    url(r'^.DS_Store',DS_Store.as_view()),
    url(r'^Access\sLists', Access_Lists.as_view()),
    url(r'^Add\snew\sregistered\suser\sgroup', Add_new_registered_user_group.as_view()),
    url(r'^Add\snew\stest', Add_new_test.as_view()),
    url(r'^Assign\stest\sstep\s1', Assign_test_step_1.as_view()),
    url(r'^Assign\stest\sstep\s1b', Assign_test_step_1b.as_view()),
    url(r'^Assign\stest\sstep\s2', Assign_test_step_2.as_view()),
    url(r'^Assign\stest\sstep\s3', Assign_test_step_3.as_view()),
    url(r'^Assign\stest\sstep\s3a', Assign_test_step_3a.as_view()),
    url(r'^Assign\stest\sstep\s3b', Assign_test_step_3b.as_view()),
    url(r'^Assistants', Assistants.as_view()),
    url(r'^base', base.as_view()),
    url(r'^Categories', Categories.as_view()),
    url(r'^Certificates', Certificates.as_view()),
    url(r'^Community', Community.as_view()),
    url(r'^Contact\sus\sClassMarker', Contact_us_ClassMarker.as_view()),
    url(r'^Edit\squestion\ssettings', Edit_question_settings.as_view()),
    url(r'^Export\sresults', Export_results.as_view()),
    url(r'^Files', Files.as_view()),
    url(r'^Group', Group.as_view()),
    url(r'^Help', Help.as_view()),
    url(r'^Introduction', Introduction.as_view()),
    url(r'^links', links.as_view()),
    url(r'^Manage\sAccess\sList', Manage_Access_List.as_view()),
    url(r'^Manage\squestion(show)', Manage_question_show.as_view()),
    url(r'^Manage\squestion', Manage_question.as_view()),
    url(r'^Manage\stest(post)', Manage_test_post.as_view()),
    url(r'^Manage\stest', Manage_test.as_view()),
    url(r'^My\sAccount', My_Account.as_view()),
    url(r'^My\stests', My_tests.as_view()),
    url(r'^Online\sTesting\sFree\sQuiz\sMaker\sCreate\sthe\sBest\sweb-based\squizzes\sClassMarker',Online_Testing_Free_Quiz_Maker_Create_the_Best_web_based_quizzes_ClassMarker.as_view()),
    url(r'^Overall\stest\sresults\sby\sgroup', Overall_test_results_by_group.as_view()),
    url(r'^Overall\stest\sresults\sby\slink', Overall_test_results_by_link.as_view()),
    url(r'^Overall\stest\sresults', Overall_test_results.as_view()),
    url(r'^Overview', Overview.as_view()),
    url(r'^Privacy\sClassMarker', Privacy_ClassMarker.as_view()),
    url(r'^Question\sbank', Question_bank.as_view()),
    url(r'^Question\sorder', Question_order.as_view()),
    url(r'^Quiz\smaker\s-\sStep\sby\sStep\sInstructions\sClassMarker',Quiz_maker_Step_by_Step_Instructions_ClassMarker.as_view()),
    url(r'^Recent\sresults(links)', Recent_results_links.as_view()),
    url(r'^Recent\sresults', Recent_results.as_view()),
    url(r'^Results', Results.as_view()),
    url(r'^Terms\sand\sconditions\sClassMarker', Terms_and_conditions_ClassMarker.as_view()),
    url(r'^Test', Test.as_view()),
    url(r'^Themes', Themes.as_view()),
    url(r'^Upgrade', Upgrade.as_view()),
    url(r'^Video\sDemonstrations', Video_Demonstrations.as_view()),
    url(r'^Web-based\sonline\stesting\sservice\s_\sFree\squiz\smaker\sClassMarker',Web_based_online_testing_service_Free_quiz_maker_ClassMarker.as_view()),
    url(r'^Welcome', welcome.as_view()),
    url(r'',BasePage.as_view()),
]

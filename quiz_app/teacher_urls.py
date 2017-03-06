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
from django.conf.urls import url,include
from .teacher_views import *


urlpatterns=[
    url(r'^assigntest', assigntestgroup.as_view()),
    url(r'^Access\sLists', AccessLists.as_view()),
    url(r'^Add\snew\sregistered\suser\sgroup', AddNewRegisteredUserGroup.as_view()),
    url(r'^Add\snew\stest', AddNewTest.as_view()),
    url(r'^addQuestion/(?P<test_name>.+)/(?P<test_counter>.+)', AddQuestion.as_view()),
    url(r'^tt',tt.as_view()),
    url(r'^Assign\stest\sstep\s1', Assignteststep1.as_view()),
    url(r'^Assign\stest\sstep\s1b', Assignteststep1b.as_view()),
    url(r'^Assign\stest\sstep\s2', Assignteststep2.as_view()),
    url(r'^Assign\stest\sstep\s3', Assignteststep3.as_view()),
    url(r'^Assign\stest\sstep\s3\setting', Assignteststepsetting.as_view()),
    url(r'^Assign\stest\sstep\s3b', Assignteststep3b.as_view()),
    url(r'^Assistants', Assistants.as_view()),
    url(r'^base', Base.as_view()),
    url(r'^Categories', Categories.as_view()),
    url(r'^Certificates', Certificates.as_view()),
    url(r'^Community', Community.as_view()),
    url(r'^Contact\sus\sClassMarker', ContactUsClassMarker.as_view()),
    url(r'^Edit\squestion\ssettings', EditQuestionSettings.as_view()),
    url(r'^Export\sresults', ExportResults.as_view()),
    url(r'^Files', Files.as_view()),
    url(r'^Group', Group.as_view()),
    url(r'^Help', Help.as_view()),
    url(r'^Introduction', Introduction.as_view()),
    url(r'^links', Links.as_view()),
    url(r'^Manage\sAccess\sList', ManageAccessList.as_view()),
    url(r'^Manage\squestion\sshow', ManageQuestionShow.as_view()),
    url(r'^Manage\squestion/(?P<test_name>.+)/(?P<test_counter>.+)', ManageQuestion.as_view()),
    url(r'^Manage\stest(post)', ManageTestPost.as_view()),
    url(r'^Manage\stest', ManageTest.as_view()),
    url(r'^My\sAccount', MyAccount.as_view()),
    url(r'^My\stests', MyTests.as_view()),
    url(r'^Online\sTesting\sFree\sQuiz\sMaker\sCreate\sthe\sBest\sweb-based\squizzes\sClassMarker',
        OnlineTestingFreeQuizMakerCreateTheBestWebBasedQuizzesClassMarker.as_view()),
    url(r'^Overall\stest\sresults\sby\sgroup', OverallTestResultsByGroup.as_view()),
    url(r'^Overall\stest\sresults\sby\slink', OverallTestResultsByLink.as_view()),
    url(r'^Overall\stest\sresults', OverallTestResults.as_view()),
    url(r'^Overview', Overview.as_view()),
    url(r'^Privacy\sClassMarker', PrivacyClassMarker.as_view()),
    url(r'^Question\sbank', QuestionBank.as_view()),
    url(r'^Question\sorder', QuestionOrder.as_view()),
    url(r'^Quiz\smaker\s-\sStep\sby\sStep\sInstructions\sClassMarker',
        QuizMakerStepByStepInstructionsClassMarker.as_view()),
    url(r'^Recent\sresults(links)', RecentResultsLinks.as_view()),
    url(r'^Recent\sresults', RecentResults.as_view()),
    url(r'^Results', Results.as_view()),
    url(r'^Terms\sand\sconditions\sClassMarker', TermsAndConditionsClassMarker.as_view()),
    url(r'^Test', Test.as_view()),
    url(r'^Themes', Themes.as_view()),
    url(r'^Upgrade', Upgrade.as_view()),
    url(r'^Video\sDemonstrations', VideoDemonstrations.as_view()),
    url(r'^Web-based\sonline\stesting\sservice\s_\sFree\squiz\smaker\sClassMarker',
        WebBasedOnlineTestingServiceFreeQuizMakerClassMarker.as_view()),
    url(r'^Welcome', Welcome.as_view()),
    url(r'', BasePage.as_view()),
]
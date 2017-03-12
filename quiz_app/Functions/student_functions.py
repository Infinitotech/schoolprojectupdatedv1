from pymongo import *
from v1.Database import StudentDataBase
from datetime import datetime
import time as timeLib


def group_test_data(request):
    courseName = request.GET.get('g_id')
    mongo = MongoClient()
    db = mongo['dummy_school_project_v1']
    user = request.session['user']
    school_id = user['school_id']
    branch_id = user['branch_id']
    tests =db.assigntest.find({'school_id':school_id,'branch_id':branch_id,'course.course_name': courseName})
    request.session['courseName']=courseName
    test_names = []
    test_score = []
    test_duration = []
    counter = []
    teacher_username = []
    for test in tests:
        for course in test['course']:
            if course['course_name'] == courseName:
                test_names.append(test['test_name'])
                test_score.append(course['maximum_score'])
                test_duration.append(course['duration'])
                counter.append(test['counter'])
                teacher_username.append(test['teacher_username'])

    return test_names, test_score, test_duration, school_id, branch_id, counter, teacher_username


def get_course_data(request):
    message = request.GET['message']
    user = request.session['user']
    courses = user['history']['courses']
    list = []
    for course in courses:
        if course['status'] == "active":
            list.append(course['course_name'])

    return list, user, message


def change_username(request):
    user = request.session['user']
    old_user = user['username']
    new_username = request.POST['username']
    user['username'] = new_username
    StudentDataBase().change_username(new_username, old_user, user)
    request.session['user'] = user
    return user


def change_password(request):
    user = request.session['user']
    password = request.POST['pass2']
    user['password'] = password
    StudentDataBase().change_password(user, password)
    request.session['user'] = user
    return user


def get_test_intro(request):
    teacher_username = request.GET['teacher_username']
    school_id = request.GET['school_id']
    branch_id = request.GET['branch_id']
    counter = request.GET['counter']
    mongo = MongoClient()
    db = mongo['dummy_school_project_v1']
    test = db.assigntest.find_one(
        {'teacher_username': teacher_username, 'school_id': int(school_id), 'branch_id': int(branch_id),
         'counter': int(counter)})
    context = {}
    courseName=request.session['courseName']
    courseIndex = [assigned for assigned,tests in enumerate(test['course']) if tests['course_name'] == courseName][0]
    print (courseIndex)

    if test:
        question_len = str(len(test['questions']))
        context = {
            'test_name': test['test_name'],
            'question_len': question_len,
            'test_duration': test['course'][courseIndex]['duration'],
            'type': test['type'],
            'teacher_username': teacher_username,
            'school_id': int(school_id),
            'branch_id': int(branch_id),
            'counter': int(counter)
        }
        del test['_id']
        request.session['test'] = test

    return context

def get_test_questions(request):
    test = request.session['test']
    courseName = request.session['courseName']
    courseIndex = [assigned for assigned, tests in enumerate(test['course']) if tests['course_name'] == courseName][0]

    context = {
        'test_name' : test['test_name'],
        'questions' : test['questions'],
        'options' : test['options'],
        'teacher_usernameR' : request.GET['teacher_username'],
        'school_id' : int(request.GET['school_id']),
        'branch_id' : int(request.GET['branch_id']),
        'counter' : int(request.GET['counter']),
        'duration' : int(test['course'][courseIndex]['duration'])
    }

    if 'test' in request.session:
        if context['counter'] == test['counter'] and context['teacher_usernameR'] == test['teacher_username'] and context['school_id'] == test[
            'school_id'] and context['branch_id'] == test['branch_id']:
             context = {'questions': context['questions'], 'options': context['options'], 'test_name': context['test_name'], 'duration': context['duration']}
             return True, context
        else:
            return False,None




def get_test_results(request):

    test_name = request.POST.get('test_name')

    test = request.session['test']
    user = request.session['user']
    courseName = request.session['courseName']
    courseIndex = [assigned for assigned, tests in enumerate(test['course']) if tests['course_name'] == courseName][0]

    mongo = MongoClient()
    db = mongo['dummy_school_project_v1']

    questions = test['questions']
    solutions = test['solutions']
    counter = test['counter']
    user_name = user['username']
    course = test['course']
    max = course[courseIndex]['maximum_score']
    options = test['options']

    selectedOptions = {}
    wrong = {}

    for question in questions:
        option = request.POST.get(question)
        if option:
            selectedOptions[question] = option.split('+')[1]
        else:
            selectedOptions[question] = "No option selected"

    score = 0

    for key, item in selectedOptions.items():
        if solutions[key] == item:
            score += 10
        else:
            wrong[key] = item

    percentage = (score / max) * 100

    timer = str(request.POST.get('timer')).split(':')
    time = int(timer[0]) * 60 + int(timer[1])
    time = (course[courseIndex]['duration'] * 60 - time)
    duration = (timeLib.strftime("%H:%M:%S", timeLib.gmtime(time)))

    dateAndTime = datetime.utcnow()

    db.test_answer.insert({
        'test_counter': counter,
        'teacher_username': test['teacher_username'],
        'student_username': user['username'],
        'school_id': test['school_id'],
        'branch_id': test['branch_id'],
        'answers': selectedOptions,
        'result': score,
        'maximum_score': max,
        'duration': time,
        'date_given': dateAndTime,
        'solutions': solutions,
        'questions': questions,
        'course': [course[courseIndex]]
    })
    context = {
        'questions': questions,
        'options': options,
        'answers': selectedOptions,
        'test_name': test_name,
        'percentage': percentage,
        'user_name': user_name,
        'course': courseName,
        'duration': duration,
        'date': dateAndTime,
        'score': score,
        'max': max,
        'correct': solutions,
        'wrong': wrong,
    }
    return context
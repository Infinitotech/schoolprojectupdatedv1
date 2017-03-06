from pymongo import *
from v1.Database import StudentDataBase
from datetime import datetime
import time as timeLib


def group_test_data(request):
    test = request.GET.get('g_id')
    mongo = MongoClient()
    db = mongo['dummy_school_project_v1']
    print(test)
    #tests = StudentDataBase.get_group_tests(test)
    tests = db.tests.find({'course.course_name': test})
    test_names = []
    test_score = []
    test_duration = []
    school_id = []
    branch_id = []
    counter = []
    teacher_username = []
    dict = {}
    for i in tests:
        test_names.append(i['test_name'])
        test_score.append(i['maximum_score'])
        test_duration.append(i['duration'])
        school_id.append(i['school_id'])
        branch_id.append(i['branch_id'])
        counter.append(i['counter'])
        teacher_username.append(i['teacher_username'])

    return test_names, test_score, test_duration, school_id, branch_id, counter, teacher_username


def get_course_data(request):
    message = request.GET['message']
    user = request.session['user']
    courses = user['history']['courses']
    list = []
    for i in courses:
        if i['status'] == "active":
            list.append(i['course_name'])

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
    print(teacher_username)
    school_id = request.GET['school_id']
    branch_id = request.GET['branch_id']
    counter = request.GET['counter']
    mongo = MongoClient()
    print('asdf')
    db = mongo['dummy_school_project_v1']
    course = db.tests.find_one(
        {'teacher_username': teacher_username, 'school_id': int(school_id), 'branch_id': int(branch_id),
         'counter': int(counter)})

    context = {}
    if course:
        question_len = str(len(course['questions']))
        context = {
            'test_name': course['test_name'],
            'question_len': question_len,
            'test_duration': course['duration'],
            'type': course['type'],
            'teacher_username': teacher_username,
            'school_id': int(school_id),
            'branch_id': int(branch_id),
            'counter': int(counter)
        }
        del course['_id']
        request.session['test'] = course

    return context

def get_test_questions(request):
    course = request.session['test']
    print("course_info")
    print(course)
    context = {
        'test_name' : course['test_name'],
        'questions' : course['questions'],
        'options' : course['options'],
        'teacher_usernameR' : request.GET['teacher_username'],
        'school_id' : int(request.GET['school_id']),
        'branch_id' : int(request.GET['branch_id']),
        'counter' : int(request.GET['counter']),
        'duration' : int(course['duration']),
    }
    if 'test' in request.session:
        if context['counter'] == course['counter'] and context['teacher_usernameR'] == course['teacher_username'] and context['school_id'] == course[
            'school_id'] and context['branch_id'] == course['branch_id']:
             context = {'questions': context['questions'], 'options': context['options'], 'test_name': context['test_name'], 'duration': context['duration']}
             return True, context
        else:
            return False



def get_test_results(request):
    test_name = request.POST.get('test_name')
    mongo = MongoClient()
    db = mongo['dummy_school_project_v1']
    test = db.tests.find_one({'test_name': test_name})
    questions = test['questions']
    solutions = test['solutions']
    user = request.session['user']
    counter = test['counter']
    max = test['maximum_score']
    user_name = user['username']
    course = test['course']
    course_name = course['course_name']
    options = test['options']
    dict = {}
    wrong = {}
    for q in questions:
        opt = request.POST.get(q)
        if opt:
            dict[q] = opt.split('+')[1]
        else:
            dict[q] = "No option selected"
    score = 0
    for key, item in dict.items():
        if solutions[key] == item:
            score += 10
        else:
            wrong[key] = item

    percentage = (score / max) * 100
    timer = str(request.POST.get('timer')).split(':')
    time = int(timer[0]) * 60 + int(timer[1])
    time = (test['duration'] * 60 - time)
    duration = (timeLib.strftime("%H:%M:%S", timeLib.gmtime(time)))
    dateAndTime = datetime.utcnow()
    db.test_answer.insert({
        'test_counter': counter,
        'teacher_username': test['teacher_username'],
        'student_username': user['username'],
        'school_id': test['school_id'],
        'branch_id': test['branch_id'],
        'answers': dict,
        'result': score,
        'maximum_score': max,
        'duration': time,
        'date_given': dateAndTime,
        'solutions': solutions,
        'questions': questions,
        'course': course
    })
    context = {
        'questions': questions,
        'options': options,
        'answers': dict,
        'test_name': test_name,
        'percentage': percentage,
        'user_name': user_name,
        'course': course_name,
        'duration': duration,
        'date': dateAndTime,
        'score': score,
        'max': max,
        'correct': solutions,
        'wrong': wrong,
    }
    return context
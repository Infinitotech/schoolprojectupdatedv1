from v1.Database import *


def get_parameters_from_request_for_each_question_teacher_creates(request):
    print('in asdf')
    answers_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
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
    return {
        'test_name': test_name,
        'question': question,
        'correct1': correct1,
        'correct2': correct2,
        'correct3': correct3,
        'correct4': correct4,
        'ans1': ans1,
        'ans2': ans2,
        'ans3': ans3,
        'ans4': ans4,
        'points': points,
        'randomize_answer': randomize_answer,
        'correct_answer': correct_answer,
        'answers_dict': answers_dict
    }


def add_question_to_test_document(test, param_dict, question_number):
    try:
        question_dict = test['questions']
        question_dict[question_number] = param_dict['question']
        test['questions'] = question_dict
        option_dict = test['options']
        option_dict[QuizDataBase.get_question_number(test, False)] = {
            'a': param_dict['ans1'],
            'b': param_dict['ans2'],
            'c': param_dict['ans3'],
            'd': param_dict['ans4']
        }
        test['options'] = option_dict
        solutions_dict = test['solutions']
        solutions_dict[question_number] = param_dict['answers_dict'][int(param_dict['correct_answer'])]
        test['solutions'] = solutions_dict
    except KeyError:
        test['questions'] = {question_number: param_dict['question']}
        test['options'] = {
            question_number: {
                'a': param_dict['ans1'],
                'b': param_dict['ans2'],
                'c': param_dict['ans3'],
                'd': param_dict['ans4']
            }
        }
        test['solutions'] = {
            question_number: param_dict['answers_dict'][int(param_dict['correct_answer'])]
        }
    return test
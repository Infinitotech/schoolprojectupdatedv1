def get_parameters_from_request_for_each_question_teacher_creates(request):
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
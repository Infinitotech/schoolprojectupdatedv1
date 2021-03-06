import datetime
from pymongo import MongoClient
from quiz_app.teacher_files.teacher import Teacher


class DataBase(object):
    mongo_db = MongoClient()['dummy_school_project_v1']

    def __init__(self):
        self.mongo = MongoClient()
        self.db = self.mongo['dummy_school_project_v1']

    def get_database(self):
        return self.db

    def __del__(self):
        try:
            self.mongo.close()
        except Exception:
            pass

    @staticmethod
    def get_school_dict():
        school = DataBase.mongo_db.school.find()
        mydict = {}
        for s in school:
            mydict[s['id']] = s['school_name']
        return mydict

    # This function must return a user -- only to be called if the user is logged in
    def get_user(self,username, school_id, branch_id):
        return self.db.users.find_one({"username": username, "school_id": school_id, "branch_id": branch_id})

    def authenticate_and_get_user(self,username, password,school_id,branchid):
        user = self.db.users.find_one(
            {'school_id': int(school_id), 'password': password, 'branch_id': int(branchid), 'username': username})
        if user:
            return user
        else:
            return None

class StudentDataBase(DataBase):
    def __init__(self):
        super().__init__()
        self.mongo = MongoClient()
        self.db = self.mongo['dummy_school_project_v1']

    def get_group_tests(self, course_name):
        return self.db.tests.find({'course.course_name': course_name})

    def get_test_data(self, teacher_username,school_id,branch_id,counter):
        return self.db.tests.find_one(
            {'teacher_username': teacher_username, 'school_id': int(school_id), 'branch_id': int(branch_id), 'counter': int(counter)})

    def change_username(self, new_username, old_user, user):
        self.db.users.update({'username': old_user},
                        {
                            'username': new_username,
                            'name': user['name'],
                            'father_name': user['father_name'],
                            'password': user['password'],
                            'type': user['type'],
                            'dob': user['dob'],
                            'photo': user['photo'],
                            'nic': user['nic'],
                            'status': user['status'],
                            'school_id': user['school_id'],
                            'branch_id': user['branch_id'],
                            'class': user['class'],
                            'history': user['history'],
                            'roll_num': user['roll_num']
                        })

    def change_password(self, user, password):
        self.db.users.update({'username': user['username']},
                        {
                            'username': user['username'],
                            'name': user['name'],
                            'father_name': user['father_name'],
                            'password': password,
                            'type': user['type'],
                            'dob': user['dob'],
                            'photo': user['photo'],
                            'nic': user['nic'],
                            'status': user['status'],
                            'school_id': user['school_id'],
                            'branch_id': user['branch_id'],
                            'class': user['class'],
                            'history': user['history'],
                            'roll_num': user['roll_num']
                        })


class QuizDataBase(DataBase):
    def __init__(self):
        super().__init__()

    def create_test(self,test_name, teacher_username, branch_id, school_id):
        creation_time = datetime.datetime.now()
        counter = self.update_teacher_document_and_set_counter_value(teacher_username, school_id, branch_id)
        test_dict = QuizDataBase.get_dict_for_creation_of_quiz(counter, teacher_username, school_id, branch_id,
                                                               test_name, creation_time)
        self.db.tests.insert(test_dict)
        return counter

    def get_test_dict(self, test_counter, username, branch_id, school_id):
        test = self.db.tests.find_one({'counter': int(test_counter),'teacher_username': username, 'branch_id': branch_id,
                                       'school_id': school_id})
        return test

    def update_test(self,new_test):
        self.db.tests.find_one_and_replace({'counter': new_test['counter'],
                                            'teacher_username': new_test['teacher_username'],
                                            'branch_id': new_test['branch_id'], 'school_id': new_test['school_id']},
                                           new_test
                                           )

    def update_teacher_document_and_set_counter_value(self, teacher_username, school_id, branch_id):
        counter = self.db.users.find_one(Teacher.get_teacher_id_dict(teacher_username, school_id, branch_id))['counter']
        self.db.users.update_one(Teacher.get_teacher_id_dict(teacher_username, school_id, branch_id),{
            '$inc': {
                'counter': 1
            }
        })
        return counter

    @staticmethod
    def get_question_number(test_doc, add_one=True):
        try:
            question_dict = test_doc['questions']
            import re
            max_num = 1
            for key in question_dict.keys():
                num = int(re.findall(r'\d+', key)[0])
                if max_num < num:
                    max_num = num
            if add_one:
                return 'q' + str(max_num + 1)
            else:
                return 'q' + str(max_num)
        except KeyError:
            return 'q1'

    @staticmethod
    def get_dict_for_creation_of_quiz(counter, teacher_username, school_id, branch_id, test_name, creation_time):
        return {
            'counter': counter,
            'teacher_username': teacher_username,
            'school_id': school_id,
            'branch_id': branch_id,
            'test_name': test_name,
            'creation_date': creation_time,
            'status': 'active',
        }

    def find_and_update_test(self,):
        self.db.tests.find_one_and_update(
            {'test'}
        )

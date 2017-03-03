import datetime
from quiz_app.teacher_files.teacher import Teacher


class Test(object):
    def __init__(self,db,teacher_username,school_id,branch_id,test_name):
        self.database = db
        self.db,self.teacher_username, self.school_id,self.branch_id, self.test_name = db['users'],teacher_username,school_id,\
                                                                                       branch_id,test_name
        self.creation_time = datetime.datetime.now()
        self.update_teacher_document_and_set_counter_value()

    def update_teacher_document_and_set_counter_value(self,):
        self.counter = self.db.find_one(Teacher.get_teacher_id_dict(self.teacher_username, self.school_id,
                                                                    self.branch_id))['counter']
        self.db.update_one(Teacher.get_teacher_id_dict(self.teacher_username, self.school_id, self.branch_id),{
            '$inc': {
                'counter':1
            }
        })

    def get_dict_for_creation_of_test(self):
        return {
            'counter': self.counter,
            'teacher_username': self.teacher_username,
            'school_id': self.school_id,
            'branch_id': self.branch_id,
            'test_name': self.test_name,
            'creation_date': self.creation_time,
            'status': 'active',
        }

    def create_test_document(self):
        self.database.tests.insert(self.get_dict_for_creation_of_test())
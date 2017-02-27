from pymongo import MongoClient


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


class TestDataBase(DataBase):
    def __init__(self):
        super().__init__()
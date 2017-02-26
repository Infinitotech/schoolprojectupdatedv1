from pymongo import MongoClient


class DataBase(object):
    mongo_db = MongoClient()['dummy_school_project_v1']

    def __init__(self):
        self.mongo = MongoClient()
        self.db = self.mongo['dummy_school_project_v1']

    def get_database(self):
        return self.db

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

    def __del__(self):
        self.mongo.close()
from pymongo import MongoClient


class DataBase(object):
    def __init__(self):
        self.mongo = MongoClient()
        self.db = self.mongo['dummy_school_project_v1']

    def get_database(self):
        return self.db

    def __del__(self):
        self.mongo.close()
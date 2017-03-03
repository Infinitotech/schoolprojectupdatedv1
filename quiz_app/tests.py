from django.test import TestCase

# Create your tests here.
from pymongo import MongoClient
mongo = MongoClient()
db = mongo['dummy_school_project_v1']

school = db.users.find_one({'school_id': 1, 'password': 'teacher1','branch_id':1, 'username': 'nishaf'})
if school:
    for values in school:
        print(values + "    ")
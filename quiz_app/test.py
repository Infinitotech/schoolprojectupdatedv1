from pymongo import MongoClient
from regex import *

mongo=MongoClient()
db=mongo['dummy_school_project_v1']
name="ENG 101"
#collecion = db.users.find_one({"name":"azeemullah", "school_id":1, "branch_id": 1})
collecction=db.assigntest.find_one({'course.course_name': name})
#for c in collecction:
#    for courses in c['course']:
#        if courses['course_name']=='ENG 102':
#            print(courses['available'])

#print([i for i,_ in enumerate(collecction) if _['course_name'] == 'name'][0])
#print(collecction['course'].index(filter(lambda n: n.get('course_name') == name, collecction)[0]))

print (collecction['course'])

L = [{'id':'1234','name':'Jason'},
{'id':'2345','name':'Tom'},
{'id':'3456','name':'Art'}]
print([i for i,_ in enumerate(collecction['course']) if _['course_name'] == "ENG 101"][0])

print(collecction['course'][0]['course_name'])
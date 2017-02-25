from pymongo import MongoClient


mongo=MongoClient()
db=mongo['dummy_school_project_v1']
collecion = db.users.find_one({"name":"azeemullah", "school_id":1, "branch_id": 1})

print(collecion['name'])
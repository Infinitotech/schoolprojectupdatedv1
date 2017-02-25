class Teacher(object):
    @staticmethod
    def get_teacher_id_dict(username, school_id, branch_id):
        return {
            'school_id': school_id,
            'branch_id': branch_id,
            'username': username
        }
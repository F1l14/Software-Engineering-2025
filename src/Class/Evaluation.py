from src.Class.DBManager import DBManager
class Evaluation:
    def __init__(self):
        None
    
    def getEmployeeEvaluations(self, username):
        db = DBManager()
        return db.queryPersonalEvaluations(username)
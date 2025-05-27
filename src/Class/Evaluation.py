from src.Class.DBManager import DBManager
from datetime import datetime
class Evaluation:
    def __init__(self, eval_type: str, start_date: datetime, end_date: datetime):
        self.eval_type = eval_type            # e.g. 'eval_for_managers' or 'eval_for_employees'
        self.start_date = start_date
        self.end_date = end_date
                             
    
    def getEmployeeEvaluations(self, username):
        db = DBManager()
        return db.queryPersonalEvaluations(username)
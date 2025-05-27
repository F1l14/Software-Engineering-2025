from src.Class.User import User
from src.Class.DBManager import DBManager
class Employee(User):
    def __init__(self, username):
        super().__init__(username)
        
    def completeTask(self, db, task_id):
        return db.completeTask(task_id)
    
    def getEmployeeProgress(self):
        db = DBManager()
        return db.queryEmployeeProgress(self.username)
    
    def getProjects(self, db):
        return db.queryProjects(self.username)
    
    def createTask(self, db, team_id, project_id, task_name, assigned_to=None):
        return db.createTask(team_id, project_id, task_name, assigned_to)
    
    def getTeams(self):
        db = DBManager()
        return db.queryTeams(self.username)

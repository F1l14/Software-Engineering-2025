from src.Class.User import User
from src.Class.DBManager import DBManager
class Employee(User):
    def __init__(self, username, firstname, lastname):
        super().__init__(username, firstname, lastname)
        
    def completeTask(self, db, task_id):
        return db.completeTask(task_id)
    # def __str__(self):
    #     return f"Employee({self.username}, {self.firstname}, {self.lastname})"

    # def getTeam(self, db):
    #     if self.__team is None:
    #         self.__team = db.queryTeam(self.username)
    #     return self.__team

    # def getDepartment(self, db):
    #     if self.__department is None:
    #         self.__department = db.queryDepartment(self.username)
    #     return self.__department
    
    def getEmployeeProgress(self):
        db = DBManager()
        return db.queryEmployeeProgress(self.username)
    
    def getProjects(self, db):
        return db.queryProjects(self.username)
    
    def createTask(self, db, team_id, project_id, task_name, assigned_to=None):
        new_task = db.createTask(team_id, project_id, task_name, assigned_to)
        return {"db_message": new_task}

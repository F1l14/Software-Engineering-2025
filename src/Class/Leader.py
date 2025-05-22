from src.Class import User, Task
class Leader(User):
    __task_list = []
    def __init__(self, username, firstname, lastname):
        super().__init__(username, firstname, lastname)
        self.__team = None
        self.__department = None
        self.__business = None

    def __str__(self):
        return f"Leader({self.username}, {self.firstname}, {self.lastname})"
    
    def getProjects(self, db):
        return db.queryProjects(self.username)
    
    def createTask(self, db, team_id, name, assigned_to=None):
        new_task = Task(name, assigned_to)
        self.__task_list.append(new_task)
        return {"db_message": db.createTask(team_id, name, assigned_to), "task": new_task}
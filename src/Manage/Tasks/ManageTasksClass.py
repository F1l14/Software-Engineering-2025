from src.Class.DBManager import DBManager
class ManageTasksClass:
    __db = None
    __user = None
    def __init__(self, user):
        # self.progress_screen = ProgressScreen()
        # self.progress_screen.manage = self
        # self.progress_screen.display()
        self.__db = DBManager()
        self.__user = user
        
    def getTasks(self):
        tasks = self.__user.getTasks(self.__db)
        print(tasks)

    def getProjects(self):
        projects = self.__user.getProjects(self.__db)
        print(projects)

    def createTask(self, team_id, name, assigned_to=None):
        task = self.__db.createTask(team_id, name, assigned_to)
        print(task.message)
from src.Class.DBManager import DBManager
class ManageTasksClass:
    __db = None
    __username = None
    def __init__(self, username):
        # self.progress_screen = ProgressScreen()
        # self.progress_screen.manage = self
        # self.progress_screen.display()
        self.__db = DBManager()
        self.__username = username
        
    def getTasks(self):
        tasks = self.__db.queryTasks(self.__username)
        print(tasks)

    def getProjects(self):
        projects = self.__db.queryProjects(self.__username)
        print(projects)
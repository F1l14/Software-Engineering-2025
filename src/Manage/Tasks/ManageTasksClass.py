from src.Class.DBManager import DBManager
class ManageTasksClass:
    """

    Create Tasks and Projects ???

    """
    __db = None
    __user = None
    __tasks_list = []
    __projects_list = []

    def __init__(self, user):
        # self.progress_screen = ProgressScreen()
        # self.progress_screen.manage = self
        # self.progress_screen.display()
        self.__db = DBManager()
        self.__user = user
        
    def getTasks(self):
        tasks = self.__user.getTasks(self.__db)
        self.__tasks_list.append(tasks)
        print(tasks)

    def getProjects(self):
        # user = leader
        if not self.checkLeader():
            print("You are not a leader")
            return
        projects = self.__user.getProjects(self.__db)
        self.__projects_list.append(projects)
        print(projects)

    def completeTask(self, task_id):
        # user = employee
        message = self.__user.completeTask(self.__db, task_id)
        print(message)

    def createTask(self, team_id, name, assigned_to=None):
        # user = leader
        if not self.checkLeader():
            print("You are not a leader")
            return
        task = self.__user.createTask(self.__db, team_id, name, assigned_to)
        print(task.message)

    def checkLeader(self):
        if self.__user.__class__.__name__ == "Leader":
            return True
        else:
            return False
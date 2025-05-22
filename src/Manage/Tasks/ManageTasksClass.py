from src.Class.DBManager import DBManager
from src.Screen.Tasks.TasksScreen import TasksScreen
from src.Class.TaskListWidget import TaskItem
from PyQt6.QtWidgets import QListWidgetItem
class ManageTasksClass:
    """

    Create Tasks and Projects ???

    """
    __db = None
    __user = None
    __tasks_list = {}
    __projects_list = []

    def __init__(self, user):
        self.tasks_screen = TasksScreen()

        self.__db = DBManager()
        self.__user = user
        
    def getTasks(self):
        tasks = self.__user.getTasks(self.__db)
        for task in tasks:
            if task["name"] in self.__tasks_list:
                self.__tasks_list[task["name"]].append(task)
            else:
                self.__tasks_list[task["name"]] = [task]
        return self.__tasks_list
        
    def displayTasks(self):
        for task in self.__tasks_list:
            self.addToList(task[3])

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

    def addToList(self, name):

        item = QListWidgetItem()
        task_text = name

        # Create the custom widget
        task_widget = TaskItem(task_text, self.tasks_screen.listWidget, item)
        item.setSizeHint(task_widget.sizeHint())

        # Add item to list and set the widget
        self.tasks_screen.listWidget.addItem(item)
        self.tasks_screen.listWidget.setItemWidget(item, task_widget)
        # self.tasks_screen.show()
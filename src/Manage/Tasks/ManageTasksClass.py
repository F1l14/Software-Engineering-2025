from src.Class.DBManager import DBManager
from src.Screen.Tasks.TasksScreen import TasksScreen
from src.Screen.Tasks.TaskCreationScreen import TaskCreationScreen
from src.Class.TaskListWidget import TaskItem
from PyQt6.QtWidgets import QListWidgetItem
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QTreeWidgetItem
class ManageTasksClass:
    __db = None
    __user = None
    __tasks_list = {}
    __projects_list = {}

    def __init__(self, user):
        self.tasks_screen = TasksScreen()

        self.__db = DBManager()
        self.__user = user

        self.getTasks()
        self.displayTasks()
        self.tasks_screen.create_button.clicked.connect(self.newCreateTaskScreen)
    

    def newCreateTaskScreen(self):
        self.create_task_screen = TaskCreationScreen()
        self.addProjectsToTree()
    
    def addProjectsToTree(self):
        self.create_task_screen.treeWidget.clear()
        self.getProjects()
        print(self.__projects_list)
        for project in self.__projects_list:
            parent = QTreeWidgetItem(self.create_task_screen.treeWidget, [project])
            for team in self.__projects_list[project]:
                team_item = QTreeWidgetItem(parent, [team])
                for member in self.__projects_list[project][team]:
                    member_item = QTreeWidgetItem(team_item, [member])
                    team_item.addChild(member_item)
            self.create_task_screen.treeWidget.addTopLevelItem(parent)

    def getTasks(self):
        tasks = self.__user.getTasks(self.__db)
        for task in tasks:
            if task["name"] in self.__tasks_list:
                self.__tasks_list[task["name"]].append(task)
            else:
                self.__tasks_list[task["name"]] = [task]
        return self.__tasks_list
        
    def displayTasks(self):
        
        self.tasks_screen.listWidget.clear()
        for project in self.__tasks_list:
            print(project)
            
            self.tasks_screen.listWidget.addItem(project)
            
            for task in self.__tasks_list[project]:
                self.addToList(task["task_name"], task["id"])
                

    def getProjects(self):
        projects = self.__user.getProjects(self.__db)
        for project in projects:
            project_name = project[0]
            team_name = project[1]
            member = project[2]

            # Ensure the project exists
            if project_name not in self.__projects_list:
                self.__projects_list[project_name] = {}

            # Ensure the team exists under the project
            if team_name not in self.__projects_list[project_name]:
                self.__projects_list[project_name][team_name] = []

            # Ensure the member exists under the team
            if member not in self.__projects_list[project_name][team_name]:
                self.__projects_list[project_name][team_name].append(member)

    def completeTask(self, task_id):
        message = self.__user.completeTask(self.__db, task_id)
        print(message)

    def createTask(self, team_id, name, assigned_to=None):
        task = self.__user.createTask(self.__db, team_id, name, assigned_to)
        print(task.message)


    def addToList(self, name, id):

        item = QListWidgetItem()
        task_text = name

        # Create the custom widget
        task_widget = TaskItem(task_text, self.tasks_screen.listWidget, item, id, self)
        item.setSizeHint(task_widget.sizeHint())

        # Add item to list and set the widget
        self.tasks_screen.listWidget.addItem(item)
        self.tasks_screen.listWidget.setItemWidget(item, task_widget)
        # self.tasks_screen.show()

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("You are not a Leader!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()
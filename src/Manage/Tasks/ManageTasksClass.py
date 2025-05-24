from src.Class.DBManager import DBManager
from src.Screen.Tasks.TasksScreen import TasksScreen
from src.Screen.Tasks.TaskCreationScreen import TaskCreationScreen
from src.Screen.Tasks.TaskAssignScreen import TaskAssignScreen
from src.Class.TaskListWidget import TaskItem
from PyQt6.QtWidgets import QListWidgetItem
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QTreeWidgetItem
from PyQt6.QtCore import Qt
class ManageTasksClass:
    __db = None
    __user = None
    __tasks_list = {}
    __projects_list = {}

    def __init__(self, user):
        self.tasks_screen = TasksScreen()

        self.__db = DBManager()
        self.__user = user

        self.getTasks("all")
        self.displayTasks()
        self.tasks_screen.create_button.clicked.connect(self.newCreateTaskScreen)
        self.tasks_screen.assign_task_button.clicked.connect(self.newAssignTaskScreen)
        self.tasks_screen.refresh_button.clicked.connect(lambda: (self.getTasks("all"), self.displayTasks()))
    
    def newAssignTaskScreen(self):
        self.assign_tasks_screen = TaskAssignScreen()
        self.getTasks("unassigned")
        self.displayTasks("unassigned")
        self.assign_tasks_screen.unassigned_list.itemSelectionChanged.connect(self.changeTaskSelection)
        self.assign_tasks_screen.submit_assign_button.clicked.connect(self.assignTask)

    def assignTask(self):
        selected_task = self.assign_tasks_screen.unassigned_list.selectedItems()[0]
        selected_member = self.assign_tasks_screen.members_list.selectedItems()[0]

        if not selected_task or not selected_member:
            self.show_popup("Please select a task and a member to assign the task.")
            return
        task_id = selected_task.data(Qt.ItemDataRole.UserRole)[0]["task_id"]
        member = selected_member.text()
        mesg=self.__db.assignTask(task_id, member)
        print(mesg)

        self.assign_tasks_screen.unassigned_list.takeItem(self.assign_tasks_screen.unassigned_list.row(selected_task))
        self.assign_tasks_screen.members_list.clear()

    def changeTaskSelection(self):
        selected_item = self.assign_tasks_screen.unassigned_list.selectedItems()[0]
        hidden_data = selected_item.data(Qt.ItemDataRole.UserRole)
        # print(hidden_data)
        members = self.__db.queryTeamMembers(hidden_data[0]["team_id"])
        # print(f"Members: {members}")
        self.displayMembers(members)

    def displayMembers(self, members):
        self.assign_tasks_screen.members_list.clear()
        for member in members:
            item = QListWidgetItem(member)
            self.assign_tasks_screen.members_list.addItem(item)
        self.assign_tasks_screen.show()

    def newCreateTaskScreen(self):
        self.create_task_screen = TaskCreationScreen()
        self.addProjectsToTree()
        self.create_task_screen.submit_button.clicked.connect(self.submitNewTask)
    

    def submitNewTask(self):
        error_message = "Please select a project, team, and member to create a task."
        selected_item = self.create_task_screen.treeWidget.selectedItems()
        if selected_item == []:
            self.show_popup("Please select a project and team to create a task.")
            return
        member = selected_item[0]
        if member.parent() is None or member.parent().parent() is None:
            self.show_popup(error_message)
            return
        else:
            team = member.parent()
            project = team.parent()
            # print(f"Selected project: {project.text(0)}, team: {team.text(0)}, member: {member.text(0)}")
            
            task_name = self.create_task_screen.task_name_field.toPlainText()
            if task_name == "":
                self.show_popup("Please enter a task name.")
                return
            
            mesg=self.__user.createTask(self.__db,
                member.data(0, Qt.ItemDataRole.UserRole)["team_id"],
                member.data(0, Qt.ItemDataRole.UserRole)["project_id"],
                task_name
            )
            # print(mesg["db_message"])
        
    def addProjectsToTree(self):
        self.create_task_screen.treeWidget.clear()
        self.getProjects()
        for project in self.__projects_list:
            parent = QTreeWidgetItem(self.create_task_screen.treeWidget, [project])
            for team in self.__projects_list[project]:
                team_item = QTreeWidgetItem(parent, [team])
                for member in self.__projects_list[project][team]:
                    member_item = QTreeWidgetItem(team_item, [member["name"]])
                    member_item.setData(0, Qt.ItemDataRole.UserRole, {"team_id":member["team_id"], "project_id":member["project_id"]}) 
                    
                    team_item.addChild(member_item)
            self.create_task_screen.treeWidget.addTopLevelItem(parent)

    def getTasks(self, option):
        self.__tasks_list = {}
        tasks = self.__user.getTasks(self.__db,option)
        # print(f"Tasks: {tasks}")
        if option == "unassigned":
            for task in tasks:
                if task["task_name"]  in self.__tasks_list:
                    self.__tasks_list[task["task_name"]].append(task)
                else:
                    self.__tasks_list[task["task_name"]] = [task]
                    # print(task)
        else:
            for task in tasks:
                if task["name"] in self.__tasks_list:
                    self.__tasks_list[task["name"]].append(task)
                else:
                    self.__tasks_list[task["name"]] = [task]
        return self.__tasks_list
        


    def displayTasks(self, option="all"):
        
        self.tasks_screen.listWidget.clear()

        if option == "all":
            for project in self.__tasks_list:
                self.tasks_screen.listWidget.addItem(project)
                for task in self.__tasks_list[project]:
                    self.addToList(task["task_name"], task["id"])
        else:
            # print("============================")
            # print(self.__tasks_list)
            for task_name, task_list in self.__tasks_list.items():
                for task in task_list:
                    # print(f"Task Name: {task_name}, Task ID: {task['task_id']}")
                    item = QListWidgetItem(task_name)
                    item.setData(Qt.ItemDataRole.UserRole, task_list)
                    self.assign_tasks_screen.unassigned_list.addItem(item)
                

    def getProjects(self):
        projects = self.__user.getProjects(self.__db)
        for project in projects:
            project_name = project[0]
            project_id = project[1]
            team_name = project[2]
            team_id = project[3]
            member = project[4]

           
            # Ensure the project exists
            if project_name not in self.__projects_list:
                self.__projects_list[project_name] = {}

            # Ensure the team exists under the project
            if team_name not in self.__projects_list[project_name]:
                self.__projects_list[project_name][team_name] = []

            # Ensure the member exists under the team
            if member not in self.__projects_list[project_name][team_name]:
                member_data = {
                    "name": member,
                    "team_id": team_id,
                    "project_id": project_id
                }
                self.__projects_list[project_name][team_name].append(member_data)

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

    def show_popup(self, text):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText(text)
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()
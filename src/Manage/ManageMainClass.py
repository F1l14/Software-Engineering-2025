from src.Screen.MainScreen import MainScreen
from src.Manage.Progress.ManageProgressClass import ManageProgressClass
from src.Manage.Team_Space.ManageTeamListClass import ManageTeamListClass
from src.Manage.Projects.ManageProjectClass import ManageProjectClass
from src.Manage.Salaries.ManageEmployeeListClass import ManageEmployeeListClass
from src.Manage.Evaluation.ManageEvalFormClass import ManageEvalFormClass
from src.Manage.Evaluation.ManageFormAnswerClass import ManageFormAnswerClass
from src.Manage.Leaves.ManageLeaveRequestsClass import ManageLeaveRequestsClass
from src.Manage.Leaves.ManageLeavesClass import ManageLeavesClass
from src.Class.DBManager import DBManager
from src.Class.Session import Session
from src.Manage.Tasks.ManageTasksClass import ManageTasksClass
from PyQt6.QtWidgets import QMessageBox

class ManageMainClass:
    def __init__(self):
        self.main_screen = MainScreen()
        self.main_screen.manage = self
        self.main_screen.display()
        
    def show_popup(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Icon.Information)  # or Warning, Critical, etc.
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()

    def progress(self):
        ManageProgressClass()
    
    def showTeamsScreen(self):
        ManageTeamListClass()
        
    def showProjectsScreen(self):
        ManageProjectClass(Session.getRole())

    def showEmployeeListScreen(self):
        ManageEmployeeListClass()        

    def salaries(self):
        ManageEmployeeListClass()        

    def showEvaluationFormatWindow(self):
        user_type = Session.getRole()
        

        if user_type == "admin":
            ManageEvalFormClass()
        else:
            if user_type == "employee" and DBManager().employeeHasAnswered(Session.getUser()):
                self.show_popup("Error", "You have already answered the evaluation form.")
                return
            else:
                ManageFormAnswerClass()

    def showTasksScreen(self):
        ManageTasksClass()

    def showLeavesMenu(self):
        user_type = Session.getRole()
        if user_type == "manager":
            ManageLeavesClass()
        else:
            ManageLeaveRequestsClass()
        
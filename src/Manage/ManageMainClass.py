from src.Screen.MainScreen import MainScreen
from src.Manage.Progress.ManageProgressClass import ManageProgressClass
from src.Manage.Team_Space.ManageTeamListClass import ManageTeamListClass
from src.Manage.Projects.ManageProjectClass import ManageProjectClass
from src.Manage.Salaries.ManageEmployeeListClass import ManageEmployeeListClass
from src.Manage.Evaluation.ManageEvalFormClass import ManageEvalFormClass
from src.Manage.Evaluation.ManageFormAnswerClass import ManageFormAnswerClass
from src.Class.DBManager import DBManager
from src.Manage.Tasks.ManageTasksClass import ManageTasksClass

class ManageMainClass:
    def __init__(self):
        self.main_screen = MainScreen()
        self.main_screen.manage = self
        self.main_screen.display()

    def progress(self):
        ManageProgressClass()
    
    def showTeamsScreen(self):
        ManageTeamListClass()
        
    def showProjectsScreen(self):
        ManageProjectClass()

    def salaries(self):
        ManageEmployeeListClass()        

    def evaluation(self):
        db = DBManager()
        user_type = db.queryUserType("current_user")
        if user_type == "admin":
            ManageEvalFormClass()
        else:
            ManageFormAnswerClass()

        ManageEmployeeListClass()
    
    def showTasksScreen(self):
        ManageTasksClass()

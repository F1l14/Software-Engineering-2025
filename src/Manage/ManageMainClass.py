from src.Screen.MainScreen import MainScreen
from src.Manage.Progress.ManageProgressClass import ManageProgressClass
from src.Manage.Projects.ManageProjectClass import ManageProjectClass
from src.Manage.Salaries.ManageEmployeeListClass import ManageEmployeeListClass
from src.Manage.Evaluation.ManageEvalFormClass import ManageEvalFormClass
from src.Manage.Evaluation.ManageFormAnswerClass import ManageFormAnswerClass
from src.Class.DBManager import DBManager
class ManageMainClass:
    def __init__(self):
        self.main_screen = MainScreen()
        self.main_screen.manage = self
        self.main_screen.display()

    def progress(self):
        ManageProgressClass()
        
    def projects(self):
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
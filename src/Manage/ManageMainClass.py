from src.Screen.MainScreen import MainScreen
from src.Manage.Progress.ManageProgressClass import ManageProgressClass
from src.Manage.Projects.ManageProjectClass import ManageProjectClass
from src.Manage.Salaries.ManageEmployeeListClass import ManageEmployeeListClass

class ManageMainClass:
    def __init__(self):
        self.main_screen = MainScreen()
        self.main_screen.manage = self
        self.main_screen.display()

    def progress(self):
        ManageProgressClass()
        
    def showProjectsScreen(self):
        ManageProjectClass()

    def salaries(self):
        ManageEmployeeListClass()        
from src.Screen.MainScreen import MainScreen
from src.Manage.Progress.ManageProgressClass import ManageProgressClass
from src.Manage.Team_Space.ManageTeamListClass import ManageTeamListClass
from src.Manage.Projects.ManageProjectClass import ManageProjectClass
from src.Manage.Salaries.ManageEmployeeListClass import ManageEmployeeListClass

from src.Manage.Messages.ManageMessagesClass import ManageMessagesClass
from src.Manage.Notices.ManageNoticeboardClass import ManageNoticeboardClass

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

    def showMessageScreen(self):
        ManageMessagesClass()
    
    def showTasksScreen(self):
        ManageTasksClass()

    def showNoticeboardScreen(self):
        ManageNoticeboardClass()
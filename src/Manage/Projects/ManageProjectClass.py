from src.Screen.Projects.ProjectScreen import ProjectScreen
from src.Screen.Projects.ProjectCreationScreen import ProjectCreationScreen
from src.Class.DBManager import DBManager

class ManageProjectClass:
    def __init__(self):
        self.project_screen = ProjectScreen()
        self.project_screen.manage = self
        self.project_screen.display()

    def getAllProjects(self):
        db = DBManager()
        projects = db.queryAllProjects()
        return projects

    
        projects = db.queryAllProjects()
        return projects

    def showProjectCreation(self):
        self.projectCreation_screen = ProjectCreationScreen()
        self.projectCreation_screen.manage = self
        self.projectCreation_screen.display()
    
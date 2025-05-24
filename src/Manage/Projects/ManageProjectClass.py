from src.Screen.Projects.ProjectScreen import ProjectScreen
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

    
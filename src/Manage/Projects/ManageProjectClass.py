from src.Screen.Projects.ProjectScreen import ProjectScreen

class ManageProjectClass:
    def __init__(self):
        self.project_screen = ProjectScreen()
        self.project_screen.manage = self
        self.project_screen.display()

    def getProjects(self):
        db = DBManager()
        projects = db.    
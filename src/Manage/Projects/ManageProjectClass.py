from PyQt6.QtWidgets import QMessageBox
from src.Screen.Projects.ProjectScreen import ProjectScreen
from src.Screen.Projects.ProjectCreationScreen import ProjectCreationScreen
from src.Screen.Projects.ProjectAssignScreen import ProjectAssignScreen
from src.Screen.Projects.ProjectEditScreen import ProjectEditScreen
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

    def getAllDepartments(self):
        db = DBManager()
        departments = db.queryAllDepartments()
        return departments
    
    def saveNewProject(self, selected_names, projectDetails):
        db = DBManager()
        message = db.createProject(selected_names, projectDetails)
        print(message)
        self.project_screen.showAllProjects()

    def updateProjectDetails(self, updated_data):
        db = DBManager()
        message = db.updateProject(updated_data)
        print(message)
        self.project_screen.showAllProjects()

    def showProjectCreation(self):
        self.projectCreation_screen = ProjectCreationScreen()
        self.projectCreation_screen.manage = self
        self.projectCreation_screen.display()

    def showAssignProjectScreen(self, projectDetails):
        self.projectAssign_screen = ProjectAssignScreen(projectDetails)
        self.projectAssign_screen.manage = self
        self.projectAssign_screen.display()

    def showProjectEditScreen(self, project_data):
        self.projectEdit_screen = ProjectEditScreen(project_data)
        self.projectEdit_screen.manage = self
        self.projectEdit_screen.display()

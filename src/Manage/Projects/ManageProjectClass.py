from PyQt6.QtWidgets import QMessageBox
from src.Screen.Projects.ProjectScreen import ProjectScreen
from src.Screen.Projects.ProjectCreationScreen import ProjectCreationScreen
from src.Screen.Projects.ProjectAssignScreen import ProjectAssignScreen
from src.Screen.Projects.ProjectEditScreen import ProjectEditScreen
from src.Screen.Projects.ManagerProjectScreen import ManagerProjectScreen
from src.Screen.Projects.ProjectTeamsScreen import ProjectTeamsScreen
from src.Screen.Projects.TeamCreationScreen import TeamCreationScreen
from src.Class.DBManager import DBManager

class ManageProjectClass:
    def __init__(self, user_type):
        self.user_type = user_type
        self.project_screen = ProjectScreen()
        self.project_screen.manage = self
        self.managerProject_screen = ManagerProjectScreen()
        self.managerProject_screen.manage = self

        if (user_type == "admin"):
            self.project_screen.display()
        elif (user_type == "manager"):
            self.managerProject_screen.display()

    def getAllProjects(self):
        db = DBManager()
        projects = db.queryAllProjects()
        return projects
    
    def getMyProjects(self, username):
        db = DBManager()
        projects = db.queryMyProjects(username)
        return projects
    
    def getProjectTeams(self, project_data, manager):
        db = DBManager()
        teams = db.queryProjectTeams(project_data, manager)
        return teams

    def getAllDepartments(self):
        db = DBManager()
        departments = db.queryAllDepartments()
        return departments
    
    def getAvailableEmployees(self):
        db = DBManager()
        employees = db.queryAvailableEmployees()
        return employees
    
    def saveNewProject(self, selected_names, projectDetails):
        db = DBManager()
        message = db.createProject(selected_names, projectDetails)
        print(message)
        self.project_screen.showAllProjects()

    def saveNewTeam(self, selected_members, selected_leader, name, username):
        db = DBManager()
        message = db.createTeam(selected_members, selected_leader, name, username)
        print(message)
        self.projectTeams_screen.showAllTeams()

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

    def showProjectTeamsScreen(self, project_data):
        self.projectTeams_screen = ProjectTeamsScreen(project_data)
        self.projectTeams_screen.manage = self
        self.projectTeams_screen.display()

    def showTeamCreationScreen(self):
        self.teamCreation_screen = TeamCreationScreen()
        self.teamCreation_screen.manage = self
        self.teamCreation_screen.display()

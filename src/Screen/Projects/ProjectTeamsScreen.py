from PyQt6.QtWidgets import QDialog, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt6 import uic
from src.Class.Session import Session

class ProjectTeamsScreen(QDialog):
    def __init__(self, project_data):
        self.project_data = project_data
        super().__init__()
    
    def display(self):
        uic.loadUi("ui/2_Projects/ProjectTeamsScreen.ui", self)
        self.teamsList = self.findChild(QTableWidget, "teamsList")
        self.showAllTeams()

        self.addTeamButton.clicked.connect(self.manage.showTeamCreationScreen)
        self.exec()

    def showAllTeams(self):
        manager = Session.getUser()
        self.teams = self.manage.getProjectTeams(self.project_data, manager)
        id = [item[0] for item in self.teams]
        name = [item[1] for item in self.teams]
        department = [item[2] for item in self.teams]
        leader = [item[3] for item in self.teams]

        self.teamsList.setRowCount(len(id))
        self.teamsList.setColumnCount(4)
        self.teamsList.setHorizontalHeaderLabels(['id', 'name', 'department', 'leader'])

        for row, (id, name, department, leader) in enumerate(zip(id, name, department, leader)):
            self.teamsList.setItem(row, 0, QTableWidgetItem(str(id)))
            self.teamsList.setItem(row, 1, QTableWidgetItem(str(name)))
            self.teamsList.setItem(row, 2, QTableWidgetItem(str(department)))
            self.teamsList.setItem(row, 3, QTableWidgetItem(str(leader)))
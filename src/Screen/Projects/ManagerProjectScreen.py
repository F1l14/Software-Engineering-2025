from PyQt6.QtWidgets import QDialog, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt6 import uic
from src.Class.Session import Session

class ManagerProjectScreen(QDialog):
    def __init__(self):
        super().__init__()
    
    def display(self):
        uic.loadUi("ui/2_Projects/ManagerProjectScreen.ui", self)
        self.projectList = self.findChild(QTableWidget, "projectList")
        self.showAllProjects()

        self.assignButton.clicked.connect(self.checkSelection)
        self.exec()

    def showAllProjects(self):
        username = Session.getUser()
        self.projects = self.manage.getMyProjects(username)
        id = [item[0] for item in self.projects]
        name = [item[1] for item in self.projects]
        description = [item[2] for item in self.projects]
        team_id = [item[3] for item in self.projects]
        created = [item[4] for item in self.projects]
        status = [item[5] for item in self.projects]
        completed_at = [item[6] for item in self.projects]
        deadline = [item[7] for item in self.projects]
        value = [item[8] for item in self.projects]

        self.projectList.setRowCount(len(id))
        self.projectList.setColumnCount(9)
        self.projectList.setHorizontalHeaderLabels(['id', 'name', 'description', 'team_id', 'created', 'status', 'completed_at', 'deadline', 'value'])

        for row, (id, name, description, team_id, created, status, completed_at, deadline, value) in enumerate(zip(id, name, description, team_id, created, status, completed_at, deadline, value)):
            self.projectList.setItem(row, 0, QTableWidgetItem(str(id)))
            self.projectList.setItem(row, 1, QTableWidgetItem(str(name)))
            self.projectList.setItem(row, 2, QTableWidgetItem(str(description)))
            self.projectList.setItem(row, 3, QTableWidgetItem(str(team_id)))
            self.projectList.setItem(row, 4, QTableWidgetItem(str(created)))
            self.projectList.setItem(row, 5, QTableWidgetItem(str(status)))
            self.projectList.setItem(row, 6, QTableWidgetItem(str(completed_at)))
            self.projectList.setItem(row, 7, QTableWidgetItem(str(deadline)))
            self.projectList.setItem(row, 8, QTableWidgetItem(str(value)))

    def checkSelection(self):
        selected_row = self.projectList.currentRow()
        if selected_row == -1:
            QMessageBox.information(self, "No Selection", "Please select a project.")
            return

        project_data = {
            "id": self.projectList.item(selected_row, 0).text(),
            "name": self.projectList.item(selected_row, 1).text(),
            "description": self.projectList.item(selected_row, 2).text(),
            "status": self.projectList.item(selected_row, 5).text(),
            "deadline": self.projectList.item(selected_row, 7).text(),
            "value": self.projectList.item(selected_row, 8).text(),
        }

        self.manage.showProjectTeamsScreen(project_data)
from PyQt6.QtWidgets import QDialog, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt6 import uic

class ProjectScreen(QDialog):
    def __init__(self):
        super().__init__()
    
    def display(self):
        uic.loadUi("ui/2_Projects/ProjectScreen.ui", self)
        self.projectList = self.findChild(QTableWidget, "projectList")
        self.showAllProjects()

        self.createProjectButton.clicked.connect(self.manage.showProjectCreation)
        self.editProjectButton.clicked.connect(self.checkSelection)
        self.exec()

    def showAllProjects(self):
        self.projects = self.manage.getAllProjects()
        id = [item[0] for item in self.projects]
        name = [item[1] for item in self.projects]
        description = [item[2] for item in self.projects]
        team_id = [item[3] for item in self.projects]
        created = [item[4] for item in self.projects]
        status = [item[5] for item in self.projects]
        completed_at = [item[6] for item in self.projects]
        deadline = [item[7] for item in self.projects]

        self.projectList.setRowCount(len(id))
        self.projectList.setColumnCount(8)
        self.projectList.setHorizontalHeaderLabels(['id', 'name', 'description', 'team_id', 'created', 'status', 'completed_at', 'deadline'])

        for row, (id, name, description, team_id, created, status, completed_at, deadline) in enumerate(zip(id, name, description, team_id, created, status, completed_at, deadline)):
            self.projectList.setItem(row, 0, QTableWidgetItem(str(id)))
            self.projectList.setItem(row, 1, QTableWidgetItem(str(name)))
            self.projectList.setItem(row, 2, QTableWidgetItem(str(description)))
            self.projectList.setItem(row, 3, QTableWidgetItem(str(team_id)))
            self.projectList.setItem(row, 4, QTableWidgetItem(str(created)))
            self.projectList.setItem(row, 5, QTableWidgetItem(str(status)))
            self.projectList.setItem(row, 6, QTableWidgetItem(str(completed_at)))
            self.projectList.setItem(row, 7, QTableWidgetItem(str(deadline)))

    def checkSelection(self):
        selected_row = self.projectList.currentRow()
        if selected_row == -1:
            QMessageBox.information(self, "No Selection", "Please select a project to edit.")
            return

        project_data = {
            "id": self.projectList.item(selected_row, 0).text(),
            "name": self.projectList.item(selected_row, 1).text(),
            "description": self.projectList.item(selected_row, 2).text(),
            "status": self.projectList.item(selected_row, 5).text(),
            "deadline": self.projectList.item(selected_row, 7).text(),
        }

        self.manage.showProjectEditScreen(project_data)
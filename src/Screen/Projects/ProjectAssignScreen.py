from PyQt6.QtWidgets import QDialog, QListWidget, QListWidgetItem, QMessageBox, QPushButton
from PyQt6 import uic
from datetime import datetime

class ProjectAssignScreen(QDialog):
    def __init__(self, projectDetails):
        super().__init__()
        self.projectDetails = projectDetails
    
    def display(self):
        uic.loadUi("ui/2_Projects/ProjectAssignScreen.ui", self)
        self.departmentsList = self.findChild(QListWidget, "departmentsList")
        self.saveButton = self.findChild(QPushButton, "saveButton")
        self.saveButton.clicked.connect(self.save)
        self.bac2Button = self.findChild(QPushButton, "backButton")
        self.back2Button.clicked.connect(self.back)
        self.showAllDepartments()
        self.exec()

    def showAllDepartments(self):
        self.departments = self.manage.getAllDepartments()
        self.departmentsList.clear()

        for dept in self.departments:
            item = QListWidgetItem(dept[0])  
            self.departmentsList.addItem(item)

    def save(self):
        selected_items = self.departmentsList.selectedItems()
        selected_names = [item.text() for item in selected_items]

        if not selected_names:
            QMessageBox.information(self, "No Selection", "Please select at least one member.")
        else:
            QMessageBox.information(self, "Selected Members", "\n".join(selected_names))
            self.manage.projectCreation_screen.accept()
            self.accept()
            self.manage.saveNewProject(selected_names, self.projectDetails)

    def back(self):
        self.reject()
        self.manage.projectCreation_screen.show()


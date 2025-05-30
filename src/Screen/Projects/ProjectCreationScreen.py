from PyQt6.QtWidgets import QDialog, QDateTimeEdit, QTextEdit, QLineEdit, QMessageBox, QPushButton
from PyQt6 import uic
from datetime import datetime

class ProjectCreationScreen(QDialog):
    def __init__(self):
        super().__init__()
    
    def display(self):
        uic.loadUi("ui/2_Projects/ProjectCreationScreen.ui", self)
        self.nameBox = self.findChild(QLineEdit, "nameBox")
        self.descriptionBox = self.findChild(QTextEdit, "descriptionBox")
        self.deadlineBox = self.findChild(QDateTimeEdit, "deadlineBox")
        self.valueBox = self.findChild(QLineEdit, "valueBox")
        self.nextButton = self.findChild(QPushButton, "nextButton")
        self.nextButton.clicked.connect(self.submitProjectDetails)
        self.backButton = self.findChild(QPushButton, "backButton")
        self.backButton.clicked.connect(self.back)
        self.exec()

    def submitProjectDetails(self):
        name = self.nameBox.text().strip()
        description = self.descriptionBox.toPlainText().strip()
        deadline = self.deadlineBox.dateTime().toPyDateTime()
        value = self.valueBox.text().strip()
        self.checkProjectDetails(name, description, deadline, value)

    def checkProjectDetails(self, name, description, deadline, value):
        projectDetails = [name, description, deadline, value]
        errors = []

        if not name:
            errors.append("Project name cannot be empty.")
        if not description:
            errors.append("Project description cannot be empty.")
        if deadline <= datetime.now():
            errors.append("Deadline must be a future date and time.")
        if not value:
            errors.append("Project value cannot be empty.")

        if errors:
            QMessageBox.warning(self, "Input Error", "\n".join(errors))
            return False
        
        self.close()
        self.manage.showAssignProjectScreen(projectDetails)
        return True

    def back(self):
        self.reject()
from PyQt6.QtWidgets import QDialog, QDateTimeEdit, QTextEdit, QLineEdit, QMessageBox, QPushButton
from PyQt6 import uic
from datetime import datetime

class ProjectEditScreen(QDialog):
    def __init__(self, project_data):
        super().__init__()
        self.project_data = project_data
    
    def display(self):
        uic.loadUi("ui/2_Projects/ProjectEditScreen.ui", self)
        self.nameBox = self.findChild(QLineEdit, "nameBox")
        self.descriptionBox = self.findChild(QTextEdit, "descriptionBox")
        self.deadlineBox = self.findChild(QDateTimeEdit, "deadlineBox")
        self.valueBox = self.findChild(QLineEdit, "valueBox")
        self.updateButton = self.findChild(QPushButton, "updateButton")
        self.updateButton.clicked.connect(self.update)
        self.cancelButton = self.findChild(QPushButton, "cancelButton")
        self.cancelButton.clicked.connect(self.cancel)

        self.showProjectDetals()
        self.exec()

    def showProjectDetals(self):
        self.nameBox.setText(self.project_data["name"])
        self.descriptionBox.setPlainText(self.project_data["description"])

        deadline_dt = datetime.strptime(self.project_data["deadline"], "%Y-%m-%d %H:%M:%S")
        self.deadlineBox.setDateTime(deadline_dt)

        self.valueBox.setText(self.project_data["value"])

    def update(self):
        name = self.nameBox.text().strip()
        description = self.descriptionBox.toPlainText().strip()
        deadline = self.deadlineBox.dateTime().toString("yyyy-MM-dd HH:mm:ss").strip()
        value = self.valueBox.text().strip()

        if not name or not description or not deadline or not value:
            QMessageBox.warning(self, "Validation Error", "All fields must be filled out.")
            return

        updated_data = {
            "id": self.project_data["id"],
            "name": name,
            "description": description,
            "deadline": deadline,
            "value": value
        }

        self.manage.updateProjectDetails(updated_data)
        self.accept() 

    def cancel(self):
        self.reject()
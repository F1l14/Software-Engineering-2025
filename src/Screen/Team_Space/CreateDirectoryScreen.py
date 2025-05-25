from PyQt6 import uic
from PyQt6.QtWidgets import QDialog


class CreateDirectoryScreen(QDialog):
    def __init__(self):
        super().__init__()
        
    def display(self):
        uic.loadUi("ui/6_Team_Space/CreateDirectoryScreen.ui", self)
        self.pushButton.clicked.connect(self.createDirectory)
        self.exec()

    def createDirectory(self):
        directory_name = self.lineEdit.text().strip()
        if not directory_name:
            self.errorLabel.setText("Directory name cannot be empty.")
            return
        
        return self.manageCreateDirectory.createDirectory(directory_name)
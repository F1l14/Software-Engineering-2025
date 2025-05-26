from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QMessageBox


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
            QMessageBox.information(self, "Error", "Directory name cannot be empty.")
            return
        return self.manageCreateDirectory.createDirectory(self.current_directory, directory_name)
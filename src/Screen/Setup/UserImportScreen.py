from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

class UserImportScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.file = None
    
    def display(self):
        uic.loadUi("ui/1_Setup/UserImportScreen.ui", self)
        self.upload_button.clicked.connect(self.handleFile)
        self.next_button.clicked.connect(lambda:self.manage.processUsers(self.file))
        self.skip_button.clicked.connect(lambda:self.manage.finishSetup("skip"))
        self.show()
    
    def handleFile(self):
        self.file = self.manage.importUsers()
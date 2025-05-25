from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

class UserImportScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.display()
    
    def display(self):
        uic.loadUi("ui/1_Setup/UserImportScreen.ui", self)
        self.upload_button.clicked.connect(self.manage.importUsers)
        self.next_button.clicked.connect(lambda:self.manage.processUsers(self.manage.__users_file))
        self.skip_button.clicked.connect(lambda:self.manage.mainScreenSetup(option="skip"))
        self.show()
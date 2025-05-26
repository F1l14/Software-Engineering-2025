from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

class UsersListScreen(QMainWindow):
    def __init__(self):
        super().__init__()
    
    def display(self):
        uic.loadUi("ui/1_Setup/UsersListScreen.ui", self)
        self.finish_button.clicked.connect(self.manage.saveUsers)
        self.show()
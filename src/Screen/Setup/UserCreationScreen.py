from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

class UserCreationScreen(QMainWindow):
    def __init__(self):
        super().__init__()
    
    def display(self):
        uic.loadUi("ui/1_Setup/UserCreationScreen.ui", self)
        self.next_button.clicked.connect(self.manage.createAdmin)
        self.show()
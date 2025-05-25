from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

class TaskAssignScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.display()
    
    def display(self):
        uic.loadUi("ui/1_Setup/DepartmentCreationScreen.ui", self)
        self.show()
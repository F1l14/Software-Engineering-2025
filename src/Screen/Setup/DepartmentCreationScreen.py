from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

class DepartmentCreationScreen(QMainWindow):
    def __init__(self):
        super().__init__()
    
    def display(self):
        uic.loadUi("ui/1_Setup/DepartmentCreationScreen.ui", self)
        self.create_button.clicked.connect(self.manage.createDepartment)
        self.next_button.clicked.connect(self.manage.checkDepartments)
        self.show()
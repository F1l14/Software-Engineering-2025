from PyQt6.QtWidgets import QDialog
from PyQt6 import uic

class EmployeeListScreen(QDialog):
    def __init__(self):
        super().__init__()
    
    def display(self):
        uic.loadUi("ui/7_Salaries/EmployeeListScreen.ui", self)
        self.exec()
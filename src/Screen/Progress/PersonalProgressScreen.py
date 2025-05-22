from PyQt6.QtWidgets import QDialog
from PyQt6 import uic

class PersonalProgressScreen(QDialog):
    def __init__(self):
        super().__init__()
    
    def display(self):
        uic.loadUi("ui/3_Progress/PersonalProgressScreen.ui", self)
        
        current_text1 = self.employeeFirstNameLabel.text()
        self.employeeFirstNameLabel.setText(current_text1 + ' ' + self.manage.first_name)
        
        current_text2 = self.employeeLastNameLabel.text()
        self.employeeLastNameLabel.setText(current_text2 + ' ' + self.manage.last_name)
        
        current_text3 = self.employeeDepartmentLabel.text()
        self.employeeDepartmentLabel.setText(current_text3 + ' ' + self.manage.department)
        
        self.exec()
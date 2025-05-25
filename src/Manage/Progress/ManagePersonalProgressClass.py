from src.Screen.Progress.PersonalProgressScreen import PersonalProgressScreen
from src.Class.Employee import Employee
from src.Class.Evaluation import Evaluation
from PyQt6.QtWidgets import QMessageBox
class ManagePersonalProgressClass:
    def __init__(self, username, first_name, last_name, department):

        self.employee = Employee(username)
        self.evalation = Evaluation()
        self.employee.firstname = first_name
        self.employee.lastname = last_name
        self.department = department
        
        self.personal_screen = PersonalProgressScreen()
        self.personal_screen.manage = self
        self.personal_screen.display()
        # self.personal_screen.showEvaluationData()

    def getData(self):
        return self.employee.getEmployeeProgress()
    
    def getEmployeeEvaluations(self):
        return self.evalation.getEmployeeEvaluations(self.employee.username)
    
    def export(self):
        self.personal_screen.createExportFile()
    
    def showSuccessScreen(self):
        QMessageBox.information(self.personal_screen, "Success", "Export successful!")
        self.personal_screen.accept()
    
from src.Screen.Progress.PersonalProgressScreen import PersonalProgressScreen
from src.Class.DBManager import DBManager
from src.Class.Employee import Employee
class ManagePersonalProgressClass:
    def __init__(self, username, first_name, last_name, department):

        self.employee = Employee(username, first_name, last_name)
        self.department = department
        
        self.personal_screen = PersonalProgressScreen()
        self.personal_screen.manage = self
        self.personal_screen.display()
        # self.personal_screen.showEvaluationData()

    def getData(self):
        return self.employee.getEmployeeProgress(self.employee.username)

    
    def getEmployeeEvaluations(self):
        return self.employee.getEmployeeEvaluations(self.employee.username)
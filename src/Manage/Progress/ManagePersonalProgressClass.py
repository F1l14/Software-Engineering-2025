from src.Screen.Progress.PersonalProgressScreen import PersonalProgressScreen
from src.Class.Employee import Employee
from src.Class.Evaluation import Evaluation
class ManagePersonalProgressClass:
    def __init__(self, username, first_name, last_name, department):

        self.employee = Employee(username, first_name, last_name)
        self.evalation = Evaluation()
        self.department = department
        
        self.personal_screen = PersonalProgressScreen()
        self.personal_screen.manage = self
        self.personal_screen.display()
        # self.personal_screen.showEvaluationData()

    def getData(self):
        return self.employee.getEmployeeProgress()
    
    def getEmployeeEvaluations(self):
        return self.evalation.getEmployeeEvaluations(self.employee.username)
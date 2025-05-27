from src.Screen.Salaries.EmployeeListScreen import EmployeeListScreen
from src.Manage.Salaries.ManageBonusClass import ManageBonusClass
from src.Class.DBManager import DBManager

class ManageEmployeeListClass:
    def __init__(self):
        self.employeeList_screen = EmployeeListScreen()
        self.employeeList_screen.manage = self
        self.employeeList_screen.display()

    def getEmployeeSalaries(self):
        db = DBManager()
        salaries = db.queryEmployeeSalaries()
        return salaries
    
    def showBonus(self):
        ManageBonusClass()
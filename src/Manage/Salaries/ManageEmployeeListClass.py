from src.Screen.Salaries.EmployeeListScreen import EmployeeListScreen

class ManageEmployeeListClass:
    def __init__(self):
        self.employeeList_screen = EmployeeListScreen()
        self.employeeList_screen.manage = self
        self.employeeList_screen.display()
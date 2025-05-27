from PyQt6.QtWidgets import QDialog, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt6 import uic

class EmployeeListScreen(QDialog):
    def __init__(self):
        super().__init__()
    
    def display(self):
        uic.loadUi("ui/7_Salaries/EmployeeListScreen.ui", self)
        self.salaryList = self.findChild(QTableWidget, "employeeSalaryList")
        self.showEmployeeSalariesList()
        self.exec()

    def showEmployeeSalariesList(self):
        self.salaries = self.manage.getEmployeeSalaries()
        username = [item[0] for item in self.salaries]
        salary = [item[1] for item in self.salaries]

        self.salaryList.setRowCount(len(username))
        self.salaryList.setColumnCount(2)
        self.salaryList.setHorizontalHeaderLabels(['username', 'salary'])

        for row, (username, salary) in enumerate(zip(username, salary)):
            self.salaryList.setItem(row, 0, QTableWidgetItem(str(username)))
            self.salaryList.setItem(row, 1, QTableWidgetItem(str(salary)))
            

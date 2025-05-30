from src.Class.DBManager import DBManager


from PyQt6.QtWidgets import QDialog, QHeaderView, QTableWidgetItem
from PyQt6.QtCore import Qt
from PyQt6 import uic

class ManagerEmployeeListScreen(QDialog):
    def __init__(self):
        super().__init__()
        

    def display(self):
        uic.loadUi("ui/5_Evaluation/ManagerEmployeeListScreen.ui", self)

        self.employeesTable.setColumnCount(2)
        self.employeesTable.setHorizontalHeaderLabels(["Employee", "Answered"])
        self.employeesTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.employeesTable.verticalHeader().setDefaultSectionSize(40)
        self.backButton.clicked.connect(self.manage.back)

        end_date = DBManager().getEvaluationEndDate()
        self.endDateLabel.setText(end_date.strftime("%d/%m/%Y %H:%M"))
        

        db = DBManager()
        self.employeesList = db.queryManagerEmployees(self.manage.user)
        if isinstance(self.employeesList, list) and not self.employeesList:
            self.manage.show_popup("Error", "No employees found for this manager.")
            return
        
        for employee in self.employeesList:
            self.employeesTable.insertRow(self.employeesTable.rowCount())
            self.employeesTable.setItem(self.employeesTable.rowCount()-1, 0, QTableWidgetItem(employee[0]))
            conn = db.conn
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM evaluation_answers WHERE eval_for = %s AND username = %s", (employee[0], self.manage.user))
            result = cursor.fetchone()
            self.employeesTable.setItem(self.employeesTable.rowCount()-1, 1, QTableWidgetItem("No" if not result else "Yes"))
            if not result:
                self.employeesTable.itemClicked.connect(self.manage.employee_evaluation_show)

        self.exec()
    
    

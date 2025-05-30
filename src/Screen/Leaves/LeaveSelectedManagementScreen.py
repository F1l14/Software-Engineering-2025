from PyQt6.QtWidgets import QDialog,QHeaderView,QTableWidgetItem
from PyQt6 import uic


class LeaveSelectedManagementScreen(QDialog):
    def __init__(self):
        super().__init__()
        
    def display(self, employee:str, start_date:str=None, end_date:str=None, reason:str=None):
        uic.loadUi("ui/9_Leaves/LeaveSelectedManagementScreen.ui", self)
        self.employeeName.setText(employee)
        self.startDate.setText(start_date)
        self.endDate.setText(end_date)
        self.leaveReason.setText(reason)

        self.backButton.clicked.connect(self.manage.leave_request_management_screen.display)
        self.acceptRequestButton.clicked.connect(lambda: self.manage.acceptRequest(employee, start_date, end_date))
        self.declineRequestButton.clicked.connect(self.manage.declineRequestReasonScreen)
        

        self.otherEmployeesList.setColumnCount(3)
        self.otherEmployeesList.setHorizontalHeaderLabels(["Employee", "Start Date", "End Date"])
        self.otherEmployeesList.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.otherEmployeesList.verticalHeader().setDefaultSectionSize(40)
        self.exec()
        
    def setOtherEmployees(self, other_employees:list):
        self.otherEmployeesList.setRowCount(0)
        self.otherEmployeesList.clearContents()
        for employee in other_employees:
            self.otherEmployeesList.insertRow(self.otherEmployeesList.rowCount())
            self.otherEmployeesList.setItem(self.otherEmployeesList.rowCount()-1, 0, QTableWidgetItem(employee[0]))
            self.otherEmployeesList.setItem(self.otherEmployeesList.rowCount()-1, 1, QTableWidgetItem(employee[1].strftime('%d/%m/%Y')))
            self.otherEmployeesList.setItem(self.otherEmployeesList.rowCount()-1, 2, QTableWidgetItem(employee[2].strftime('%d/%m/%Y')))

    
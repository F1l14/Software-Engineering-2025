from PyQt6.QtWidgets import QDialog, QHeaderView
from PyQt6 import uic
from src.Class.DBManager import DBManager
from PyQt6.QtWidgets import QTableWidgetItem
class LeaveRequestHistoryScreen(QDialog):
    def __init__(self):
        super().__init__()
    
    def display(self):
        uic.loadUi("ui/9_Leaves/LeaveRequestHistoryScreen.ui", self)
        self.backButton.clicked.connect(self.manage.cancel)
        self.newReqButton.clicked.connect(self.manage.showLeaveRequestForm)
        self.requestsTable.setColumnCount(4)
        self.requestsTable.setHorizontalHeaderLabels(["Request ID", "Start Date", "End Date", "Status"])
        self.requestsTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.requestsTable.verticalHeader().setDefaultSectionSize(40)
        self.manage.showLeaveRequestHistory()
        self.exec()

    def showRequestsList(self, requestsList):
        # Populate the table with leave requests
        self.requestsTable.setRowCount(0)
        self.requestsTable.clearContents()
        for request in requestsList:
            self.requestsTable.insertRow(self.requestsTable.rowCount())
            self.requestsTable.setItem(self.requestsTable.rowCount()-1, 0, QTableWidgetItem(str(request[0])))
            self.requestsTable.setItem(self.requestsTable.rowCount()-1, 1, QTableWidgetItem(request[1].strftime('%d/%m/%Y')))
            self.requestsTable.setItem(self.requestsTable.rowCount()-1, 2, QTableWidgetItem(request[2].strftime('%d/%m/%Y')))
            self.requestsTable.setItem(self.requestsTable.rowCount()-1, 3, QTableWidgetItem(str(request[3])))
        
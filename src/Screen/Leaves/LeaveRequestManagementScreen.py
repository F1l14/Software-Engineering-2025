from PyQt6.QtWidgets import QDialog,QTableWidgetItem,QHeaderView
from PyQt6 import uic


class LeaveRequestManagementScreen(QDialog):
    def __init__(self):
        super().__init__()
        

    def display(self):
        uic.loadUi("ui/9_Leaves/LeaveRequestManagementScreen.ui", self)
        self.newRequestsTable.itemClicked.connect(self.selectRequest)
        self.backButton.clicked.connect(self.close)
        self.newRequestsTable.setColumnCount(4)
        self.newRequestsTable.setHorizontalHeaderLabels(["Request ID","Employee", "Start Date", "End Date"])
        self.newRequestsTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.newRequestsTable.verticalHeader().setDefaultSectionSize(40)

        self.leavesTable.setColumnCount(3)
        self.leavesTable.setHorizontalHeaderLabels(["Employee", "Start Date", "End Date"])
        self.leavesTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.leavesTable.verticalHeader().setDefaultSectionSize(40)

        self.manage.searchRequests()
        self.manage.searchLeaves()
        self.exec()



    def showDepRequests(self, newRequestsList):
        self.newRequestsTable.setRowCount(0)
        self.newRequestsTable.clearContents()
        for request in newRequestsList:
            self.newRequestsTable.insertRow(self.newRequestsTable.rowCount())
            self.newRequestsTable.setItem(self.newRequestsTable.rowCount()-1, 0, QTableWidgetItem(str(request[0])))
            self.newRequestsTable.setItem(self.newRequestsTable.rowCount()-1, 1, QTableWidgetItem(str(request[1])))
            self.newRequestsTable.setItem(self.newRequestsTable.rowCount()-1, 2, QTableWidgetItem(request[2].strftime('%d/%m/%Y')))
            self.newRequestsTable.setItem(self.newRequestsTable.rowCount()-1, 3, QTableWidgetItem(request[3].strftime('%d/%m/%Y')))

    def showDepLeaves(self, leavesList):
        self.leavesTable.setRowCount(0)
        self.leavesTable.clearContents()
        for leave in leavesList:
            self.leavesTable.insertRow(self.leavesTable.rowCount())
            self.leavesTable.setItem(self.leavesTable.rowCount()-1, 0, QTableWidgetItem(leave[0]))
            self.leavesTable.setItem(self.leavesTable.rowCount()-1, 1, QTableWidgetItem(leave[1].strftime('%d/%m/%Y')))
            self.leavesTable.setItem(self.leavesTable.rowCount()-1, 2, QTableWidgetItem(leave[2].strftime('%d/%m/%Y')))
        
    def selectRequest(self, item):
        row = item.row()
        request_id = self.newRequestsTable.item(row, 0).text()
        self.manage.showRequestDetails(request_id)
        
    def reload(self):
        self.manage.searchRequests()
        self.manage.searchLeaves()
        self.newRequestsTable.clearSelection()
        self.leavesTable.clearSelection()
        
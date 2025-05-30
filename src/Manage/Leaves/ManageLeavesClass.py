from src.Screen.Leaves.LeaveRequestManagementScreen import LeaveRequestManagementScreen
from src.Screen.Leaves.LeaveSelectedManagementScreen import LeaveSelectedManagementScreen
from src.Screen.Leaves.LeaveRequestDeclinedScreen import LeaveRequestDeclinedScreen
from src.Class.DBManager import DBManager
from src.Class.Leave import Leave
from src.Class.Session import Session
from datetime import datetime
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem

class ManageLeavesClass:
    def __init__(self):
        self.user = Session.getUser()
        self.db = DBManager()
        self.leave_request_management_screen = LeaveRequestManagementScreen()
        self.leave_selected_management_screen = LeaveSelectedManagementScreen()
        self.leave_request_management_screen.manage = self
        self.leave_selected_management_screen.manage = self
        self.leave_request_management_screen.display()
    
    def show_popup(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Icon.Information)  # or Warning, Critical, etc.
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()

    

    def searchRequests(self):
        newRequestsList = self.db.queryDepartmentLeaveRequests(self.user)
        if newRequestsList:
            self.leave_request_management_screen.showDepRequests(newRequestsList)
        else:
            self.leave_request_management_screen.newRequestsTable.insertRow(0)
            self.leave_request_management_screen.newRequestsTable.setItem(0, 0, QTableWidgetItem("No new requests found."))
            return
        
    
    def searchLeaves(self):
        leavesList = self.db.queryDepartmentLeaves(self.user)
        if leavesList: 
            self.leave_request_management_screen.showDepLeaves(leavesList)
        else:
            self.leave_request_management_screen.leavesTable.insertRow(0)
            self.leave_request_management_screen.leavesTable.setItem(0, 0, QTableWidgetItem("No leaves found."))
            return  


    def showRequestDetails(self, request_id):
        leave_request = self.db.queryLeaveRequestById(request_id)
        if leave_request:
            employee = leave_request[0][0]
            start_date = leave_request[0][1].strftime('%d/%m/%Y')
            end_date = leave_request[0][2].strftime('%d/%m/%Y')
            reason = leave_request[0][3]
            self.leave_selected_management_screen.display(employee, start_date, end_date, reason)
            self.leave_request_management_screen.close()
            otherEmployees = self.db.checkSameDateRequests(employee, start_date, end_date)
            self.leave_selected_management_screen.showSameDateRequests(otherEmployees)
        else:
            self.show_popup("Error", "No leave request found for this employee.")
        
    def acceptRequest(self, employee, start_date, end_date):
        start_date_format = datetime.strptime(start_date, '%d/%m/%Y').date()
        end_date_format = datetime.strptime(end_date, '%d/%m/%Y').date()
        result = self.db.saveRequest(employee, start_date_format, end_date_format)
        if result:
            self.db.createNotification(
                employee, 
                "Leave Request Answer",
                f"Your leave request from {start_date} to {end_date} has been accepted by {self.user.name}."
            )
            Leave(employee, start_date, end_date)
            self.show_popup("Success", "Leave request accepted successfully.")
            self.leave_selected_management_screen.close()
            self.leave_request_management_screen.reload()
        else:
            self.show_popup("Error", "Failed to accept leave request.")

    def declineRequestReasonScreen(self):
        self.leave_request_declined_screen = LeaveRequestDeclinedScreen()
        self.leave_request_declined_screen.manage = self
        self.leave_request_declined_screen.show()

    def declineRequest(self, employee, start_date, end_date, decline_reason):
        start_date_format = datetime.strptime(start_date, '%d/%m/%Y').date()
        end_date_format = datetime.strptime(end_date, '%d/%m/%Y').date()
        result = self.db.saveDeclinedRequest(employee, start_date_format, end_date_format, decline_reason)
        if result:
            self.db.createNotification(
                employee, 
                "Leave Request Answer",
                f"Your leave request from {start_date} to {end_date} has been declined by {self.user.name}. Reason: {decline_reason}"
            )
            self.show_popup("Success", "Leave request declined successfully.")
            self.leave_request_declined_screen.close()
            self.leave_selected_management_screen.close()
            self.leave_request_management_screen.reload()
        else:
            self.show_popup("Error", "Failed to decline leave request.")
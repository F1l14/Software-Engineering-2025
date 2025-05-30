from src.Screen.Leaves.LeaveRequestHistoryScreen import LeaveRequestHistoryScreen
from src.Screen.Leaves.LeaveRequestFormScreen import LeaveRequestFormScreen
from src.Class.Session import Session
from src.Class.DBManager import DBManager
from src.Class.LeaveRequest import LeaveRequest
from datetime import datetime
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem

class ManageLeaveRequestsClass:
    def __init__(self):
        self.user = Session.getUser()  
        self.db = DBManager()
        self.leave_request_history_screen = LeaveRequestHistoryScreen()
        self.leave_request_history_screen.manage = self
        self.leave_request_history_screen.display()

    def show_popup(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Icon.Information)  # or Warning, Critical, etc.
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()

    def cancel(self):
        self.leave_request_history_screen.close()

    def back(self):
        self.leave_request_form_screen.close()
        self.leave_request_history_screen.display()

    def showLeaveRequestHistory(self):
        requestsList = self.db.queryUserLeaveRequests(self.user)
        if requestsList:
            self.leave_request_history_screen.showRequestsList(requestsList)
        else:
            self.leave_request_history_screen.requestsTable.insertRow(0)
            self.leave_request_history_screen.requestsTable.setItem(0, 0, QTableWidgetItem("No leave requests found."))
        

    def showLeaveRequestForm(self):
        if not DBManager().checkLeaveCapability(self.user):
            self.show_popup("Error", "You have already submitted a leave request. You cannot submit another one.")
            return
        else:
            self.leave_request_form_screen = LeaveRequestFormScreen()
            self.leave_request_form_screen.manage = self
            self.leave_request_form_screen.display()
            self.leave_request_history_screen.close()

    def submitLeaveRequest(self):
        db = DBManager()
        start_date = self.leave_request_form_screen.requestStartDate.date().toPyDate()
        end_date = self.leave_request_form_screen.requestEndDate.date().toPyDate()
        reason = self.leave_request_form_screen.requestText.toPlainText()
        if not start_date or not end_date or not reason:
            self.show_popup("Error", "Please fill in all fields.")
            return
        if start_date > end_date:
            self.show_popup("Error", "Start date cannot be after end date.")
            return
        if start_date < datetime.now().date() or end_date < datetime.now().date():
            self.show_popup("Error", "Leave dates cannot be in the past.")
            return
        if not db.insertLeaveRequest(self.user, start_date, end_date, reason):
            self.show_popup("Error", "Failed to submit leave request. Please try again.")
            return
        LeaveRequest(self.user, start_date, end_date, reason)
        manager = db.queryManager(self.user)
        db.createNotification(
            manager,
            "leave_request",
            f"New leave request from {self.user}: {start_date} to {end_date}"
        )
        self.show_popup("Success", "Leave request submitted successfully!")
        self.leave_request_form_screen.close()
        self.leave_request_history_screen.display()

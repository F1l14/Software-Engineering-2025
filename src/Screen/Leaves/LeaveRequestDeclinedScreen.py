from PyQt6.QtWidgets import QDialog
from PyQt6 import uic


class LeaveRequestDeclinedScreen(QDialog):
    def __init__(self):
        super().__init__()

    def display(self):
            uic.loadUi("ui/9_Leaves/LeaveRequestDeclinedScreen.ui", self)
            self.submitReasonButton.clicked.connect(self.submitDeclineRequest)
            self.backButton.clicked.connect(self.close)
            self.exec()

    def submitDeclineRequest(self):
            decline_reason = self.declineReason.toPlainText()
            if not decline_reason.strip():
                self.show_popup("Error", "Please provide a reason for declining the leave request.")
                return
            self.manage.declineRequest(self.manage.leave_selected_management_screen.employeeName.text(), self.manage.leave_selected_management_screen.startDate.text(), self.manage.leave_selected_management_screen.endDate.text(), decline_reason)
            self.close()

from PyQt6.QtWidgets import QDialog
from PyQt6 import uic

class LeaveRequestFormScreen(QDialog):
    def __init__(self):
        super().__init__()
    
    def display(self):
        uic.loadUi("ui/9_Leaves/LeaveRequestFormScreen.ui", self)
        self.backButton.clicked.connect(self.manage.back)
        self.sumbitRequestButton.clicked.connect(self.manage.submitLeaveRequest)
        self.exec()

   
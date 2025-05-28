from PyQt6.QtWidgets import QDialog, QHeaderView
from PyQt6 import uic

class ManagerEmployeeListScreen(QDialog):
    def __init__(self):
        super().__init__()
        

    def display(self):
        uic.loadUi("src/Screen/Evaluation/ui/ManagerEmployeeListScreen.ui", self)

        self.employeesTable.setColumnCount(2)
        self.employeesTable.setHorizontalHeaderLabels(["Employee", "Answered"])
        self.employeesTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.employeesTable.verticalHeader().setDefaultSectionSize(40)
        self.sumbitAnswersButton.setEnabled(False)
        self.cancelButton.clicked.connect(self.manage.cancel)
        self.sumbitAnswersButton.clicked.connect(self.manage.submit_answers_employee)
        self.exec()
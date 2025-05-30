from PyQt6.QtWidgets import QDialog
from PyQt6 import uic

class EvaluationFormatScreen(QDialog):
    def __init__(self):
        super().__init__()

    def display(self):
        uic.loadUi("ui/5_Evaluation/EvaluationFormatScreen.ui", self)
        self.cancelButton.clicked.connect(self.manage.cancel)
        self.EvalForManagerButton.clicked.connect(lambda:self.selectFormatType('manager'))
        self.EvalForEmployeeButton.clicked.connect(lambda:self.selectFormatType('employee'))
        self.exec()

    def selectFormatType(self, type: str):
        if type == "manager":
            eval_type_text = "Managers"
            self.manage.showEvaluationEditScreen(eval_type_text)
        elif type == "employee":
            eval_type_text = "Employees"
            self.manage.showEvaluationEditScreen(eval_type_text)
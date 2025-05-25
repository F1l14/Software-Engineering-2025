from PyQt6.QtWidgets import QDialog
from PyQt6 import uic

class EvaluationFormatScreen(QDialog):
    def __init__(self):
        super().__init__()

    def display(self):
        uic.loadUi("ui/5_Evaluation/EvaluationFormatScreen.ui", self)
        self.cancelButton.clicked.connect(self.manage.cancel)
        self.EvalForManagerButton.clicked.connect(self.manage.eval_for_manager)
        self.EvalForEmployeeButton.clicked.connect(self.manage.eval_for_employee)
        self.exec()
from PyQt6.QtWidgets import QDialog, QLabel
from PyQt6 import uic

class EvaluationEditScreen(QDialog):
    def __init__(self, eval_type_text):
        super().__init__()
        self.eval_type_text = eval_type_text

    def display(self):
        uic.loadUi("ui/5_Evaluation/EvaluationEditScreen.ui", self)

        label = self.findChild(QLabel, "evalTypeLabel")  # ✅ Use QLabel
        if label:
            label.setText(self.eval_type_text)
        else:
            print("❌ QLabel 'evalTypeLabel' not found in the .ui file")
        self.exec()
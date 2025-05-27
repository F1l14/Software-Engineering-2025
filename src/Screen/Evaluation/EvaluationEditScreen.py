from PyQt6.QtWidgets import QDialog, QLabel, QHeaderView
from PyQt6 import uic

class EvaluationEditScreen(QDialog):
    def __init__(self, eval_type_text):
        super().__init__()
        self.eval_type_text = eval_type_text

    def display(self):
        uic.loadUi("ui/5_Evaluation/EvaluationEditScreen.ui", self)

        self.findChild(QLabel, "evalTypeLabel").setText(self.eval_type_text)

        self.readyFormButton.setEnabled(False)
        self.editButton.setEnabled(False)
        self.deleteButton.setEnabled(False)
        self.addQuestionButton.clicked.connect(self.manage.add_question)
        self.questionsTable.setColumnCount(2)
        self.questionsTable.setHorizontalHeaderLabels(["Question", "Answers"])
        self.questionsTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.questionsTable.verticalHeader().setDefaultSectionSize(40)  # or any height in pixels
        self.editButton.clicked.connect(self.manage.edit_selected_question)
        
        self.exec()

    def reload(self):
        if self.questionsTable.rowCount() > 0:
            self.readyFormButton.setEnabled(True)
        else:
            self.readyFormButton.setEnabled(False)

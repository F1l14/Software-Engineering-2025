from PyQt6.QtWidgets import QDialog,QLineEdit, QVBoxLayout 
from PyQt6 import uic

class QuestionEditScreen(QDialog):
    def __init__(self):
        super().__init__()

    def display(self):
        uic.loadUi("ui/5_Evaluation/QuestionEditScreen.ui", self)
        self.backButton.clicked.connect(self.manage.cancel_question)

        self.answersLayout = QVBoxLayout(self.answersList)
        self.answersList.setLayout(self.answersLayout)

        self.addAnswerButton.clicked.connect(self.add_answer)
        self.saveQuestionButton.clicked.connect(self.manage.save_question)
        self.add_answer()  
        self.exec()

    def add_answer(self):
        answer_field = QLineEdit()
        self.answersLayout.addWidget(answer_field)

    def get_data(self):
        question = self.questionText.toPlainText().strip()
        answers = []
        for i in range(self.answersLayout.count()):
            widget = self.answersLayout.itemAt(i).widget()
            if isinstance(widget, QLineEdit):
                text = widget.text().strip()
                if text:
                    answers.append(text)
        return question, answers
    

def set_data(self, question_text: str, answers: list[str]):
    self.questionText.setPlainText(question_text)

    # Clear existing answer fields
    for i in reversed(range(self.answersLayout.count())):
        self.answersLayout.itemAt(i).widget().setParent(None)

    for ans in answers:
        field = QLineEdit()
        field.setText(ans)
        self.answersLayout.addWidget(field)

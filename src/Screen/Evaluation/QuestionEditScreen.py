from PyQt6.QtWidgets import QDialog,QLineEdit, QVBoxLayout 
from PyQt6 import uic

class QuestionEditScreen(QDialog):
    def __init__(self):
        super().__init__()
        

    def display(self, question_text="", answers=None):
        uic.loadUi("ui/5_Evaluation/QuestionEditScreen.ui", self)
        self.setWindowTitle("Question Edit")
        self.answersLayout = QVBoxLayout(self.answersList)
        self.answersList.setLayout(self.answersLayout)

        self.backButton.clicked.connect(self.manage.cancel_question)
        self.addAnswerButton.clicked.connect(self.add_answer)
        self.saveQuestionButton.clicked.connect(self.manage.save_question)

        if question_text:
            self.questionText.setText(question_text)
        if answers:
            for ans in answers:
                field = QLineEdit()
                field.setText(ans)
                self.answersLayout.addWidget(field)

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
    

   
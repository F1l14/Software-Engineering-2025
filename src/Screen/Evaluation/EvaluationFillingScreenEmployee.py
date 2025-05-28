from PyQt6.QtWidgets import QDialog, QVBoxLayout, QFrame, QLabel, QRadioButton, QButtonGroup
from PyQt6 import uic
from src.Class.DBManager import DBManager

class EvaluationFillingScreenEmployee(QDialog):
    def __init__(self):
        super().__init__()

    def display(self,type:str):
        uic.loadUi("ui/5_Evaluation/EvaluationFillingScreenEmployee.ui", self)

        self.submitAnswersButton.setEnabled(False)
        self.cancelButton.clicked.connect(self.manage.cancel)
        self.submitAnswersButton.clicked.connect(self.manage.submit_answers_manager)

        db = DBManager()
        questions_data = db.queryEvaluationForm("eval_for_managers")  
        form_id = questions_data[0][0] if questions_data else None
        if isinstance(questions_data, str):
            print("Error fetching questions:", questions_data)
            return


        for i in reversed(range(self.formToAnswer.layout().count())):
            item = self.formToAnswer.layout().itemAt(i)
            if item.widget():
                item.widget().deleteLater()

        layout = QVBoxLayout(self.formToAnswer)
        self.formToAnswer.setStyleSheet("background-color: white;")

        for row in questions_data:
            question_text = row[1]  # question_text
            answers_list = [a.strip() for a in row[2].split(",") if a.strip()]  # answers

            frame = QFrame()
            frame_layout = QVBoxLayout(frame)

            label = QLabel(question_text)
            label.setStyleSheet("font-weight: bold; font-size: 14px; color: black;")
            frame_layout.addWidget(label)

            button_group = QButtonGroup(frame)
            for answer in answers_list:
                radio = QRadioButton(answer)
                radio.setStyleSheet("""
                    QRadioButton {
                        color: black;
                        background-color: transparent;
                        border: none;
                    }
                    QRadioButton::indicator {
                        background-color: transparent;
                        border: 1px solid #555;
                        width: 12px;
                        height: 12px;
                        border-radius: 6px;
                    }
                    QRadioButton::indicator:checked {
                        background-color: #999;
                        border: 1px solid #333;
                    }
                """)
                frame_layout.addWidget(radio)
                button_group.addButton(radio)

            frame.setStyleSheet("""
                background-color: #f5f5f5;
                border: 1px solid #ccc;
                margin-bottom: 10px;
                padding: 8px;
            """)

            layout.addWidget(frame)

        layout.addStretch()
        self.questionsContainer.setLayout(layout)
        self.exec()

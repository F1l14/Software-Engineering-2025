from PyQt6.QtWidgets import QDialog, QVBoxLayout, QFrame, QLabel, QRadioButton, QButtonGroup
from PyQt6 import uic
from src.Class.DBManager import DBManager

class EvaluationFillingScreenEmployee(QDialog):
    def __init__(self):
        super().__init__()

    def display(self):
        uic.loadUi("ui/5_Evaluation/EvaluationFillingScreenEmployee.ui", self)

        #self.submitAnswersButton.setEnabled(False)
        self.cancelButton.clicked.connect(self.manage.cancel)
        self.submitAnswersButton.clicked.connect(self.manage.submit_answers_for_manager)

        db = DBManager()
        self.questions_data = db.queryEvaluationForm("eval_for_managers")  
        self.form_id = self.questions_data[0][0] if self.questions_data else None
        if isinstance(self.questions_data, str):
            self.manage.show_popup("Error", self.questions_data)
            return

        layout = QVBoxLayout(self.formToAnswer)
        self.formToAnswer.setStyleSheet("background-color: white;")

        for i in reversed(range(self.formToAnswer.layout().count())):
            item = self.formToAnswer.layout().itemAt(i)
            if item.widget():
                item.widget().deleteLater()

        

        for row in self.questions_data:
            question_text = row[2]  # question_text
            answers_list = [a.strip() for a in row[3].split(",") if a.strip()]  # answers

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
        self.formToAnswer.setLayout(layout)
        self.exec()

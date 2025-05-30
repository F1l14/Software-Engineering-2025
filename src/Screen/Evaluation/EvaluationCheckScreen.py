from PyQt6.QtWidgets import QDialog, QVBoxLayout, QFrame, QLabel, QRadioButton, QButtonGroup
from PyQt6 import uic

class EvaluationCheckScreen(QDialog):
    def __init__(self):
        super().__init__()
        
    def display(self, source_table):
        uic.loadUi("ui/5_Evaluation/EvaluationCheckScreen.ui", self)
        self.setWindowTitle("Evaluation Check")
        self.editFormButton.clicked.connect(self.manage.eval_edit_screen.show)
        self.editFormButton.clicked.connect(self.hide)

        self.publishFormButton.clicked.connect(self.manage.publish_form)
        

    
        self.questionsContainer.setStyleSheet("background-color: white;")
        layout = QVBoxLayout(self.questionsContainer)

        row_count = source_table.rowCount()
        for row in range(row_count):
            question_item = source_table.item(row, 0)
            answers_item = source_table.item(row, 1)
            

            if not question_item or not answers_item:
                continue

            question_text = question_item.text()
            answers_list = [a.strip() for a in answers_item.text().split(",") if a.strip()]

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
                        background-color: #999;  /* Change this to match the grey frame */
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

   
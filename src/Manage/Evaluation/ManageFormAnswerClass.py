from src.Screen.Evaluation.EvaluationFillingScreenEmployee import EvaluationFillingScreenEmployee
from src.Screen.Evaluation.ManagerEmployeeListScreen import ManagerEmployeeListScreen
from PyQt6.QtWidgets import  QRadioButton, QMessageBox
from src.Class.DBManager import DBManager
from src.Class.Session import Session
class ManageFormAnswerClass:
    def __init__(self):
        self.user = Session.getUser()
        db = DBManager()
        user_type = db.queryUserType(self.user)
        if user_type == "manager":
            self.eval_filling_screen = ManagerEmployeeListScreen()
            self.eval_filling_screen.manage = self
            self.eval_filling_screen.display("manager")
        elif user_type == "employee":
            self.eval_filling_screen = EvaluationFillingScreenEmployee()
            self.eval_filling_screen.manage = self
            self.eval_filling_screen.display()

    def show_popup(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Icon.Information)  # or Warning, Critical, etc.
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()

    def cancel(self):
        self.eval_filling_screen.close()

    def submit_answers_for_manager(self):
        db = DBManager()
        all_success = True  

        layout = self.eval_filling_screen.formToAnswer.layout()

        for i in range(layout.count()):
            item = layout.itemAt(i)
            if item.widget():
                radio_buttons = item.widget().findChildren(QRadioButton)
                selected_answer = None
                for radio in radio_buttons:
                    if radio.isChecked():
                        selected_answer = radio.text()
                        break

                if selected_answer:
                    question_id = self.eval_filling_screen.questions_data[i][1]  
                    result = db.saveEvaluationAnswer(
                        self.eval_filling_screen.form_id,
                        self.user,
                        question_id,
                        selected_answer
                    )
                    if isinstance(result, str) and result.startswith("Error"):
                        all_success = False

        if all_success:
            self.show_popup("Success", )
        else:
            self.show_popup("Error", result)


        # Close the screen after submission
        self.eval_filling_screen.close()

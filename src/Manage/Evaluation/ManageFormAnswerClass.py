from src.Screen.Evaluation.EvaluationFillingScreenEmployee import EvaluationFillingScreenEmployee
from src.Screen.Evaluation.ManagerEmployeeListScreen import ManagerEmployeeListScreen
from src.Manage.ManageWelcomeClass import ManageWelcomeClass
from PyQt6.QtWidgets import  QRadioButton, QMessageBox
from src.Class.DBManager import DBManager
class ManageFormAnswerClass:
    def __init__(self):
        db = DBManager()
        user_type = db.queryUserType("current_user")
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
        msg_box.setIcon(QMessageBox.Information)  # or Warning, Critical, etc.
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()

    def cancel(self):
        self.eval_filling_screen.close()

    def submit_answers_manager(self):

        # Collect answers from the form
        answers = []
        for i in range(self.eval_filling_screen.formToAnswer.layout().count()):
            item = self.eval_filling_screen.formToAnswer.layout().itemAt(i)
            if item.widget():
                radio_buttons = item.widget().findChildren(QRadioButton)
                for radio in radio_buttons:
                    if radio.isChecked():
                        answers.append(radio.text())
                        break
            answers_str = ", ".join(answers)
        db = DBManager()
        # Save answers to the database
        if db.saveEvaluationAnswers(self.eval_filling_screen.form_id, "current_user", answers_str):
            self.show_popup("Success", "Answers submitted successfully.")
        else:
            self.show_popup("Error", "Failed to submit answers.")

        
        # Close the screen after submission
        self.eval_filling_screen.close()

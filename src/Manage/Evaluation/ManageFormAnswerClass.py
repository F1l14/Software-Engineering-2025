from src.Screen.Evaluation.EvaluationFillingScreen import EvaluationFillingScreen
from src.Screen.Evaluation.ManagerEmployeeListScreen import ManagerEmployeeListScreen
from PyQt6.QtWidgets import  QRadioButton, QMessageBox
from src.Class.DBManager import DBManager
from src.Class.Session import Session
class ManageFormAnswerClass:
    def __init__(self):
        self.user = Session.getUser()
        user_type = Session.getRole()
        if user_type == "manager":
            self.eval_filling_screen = ManagerEmployeeListScreen()
            self.eval_filling_screen.manage = self
            self.eval_filling_screen.display()
        elif user_type == "employee":
            manager = DBManager().queryManager(self.user)
            self.eval_filling_screen = EvaluationFillingScreen(manager)
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

    def submit_answers(self):
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
                        if selected_answer:
                            question_id = int(self.eval_filling_screen.questions_data[i][1])

                            result = db.saveEvaluationAnswer(
                            self.eval_filling_screen.form_id,
                            self.user,
                            self.eval_filling_screen.evaluation_for,
                            question_id,
                            selected_answer
                            )
                        break
                if not selected_answer:
                    self.show_popup("Error", f"Please answer question {i + 1}.")
                    return

                if isinstance(result, str) and result.startswith("Error"):
                    all_success = False

        if all_success:
            self.show_popup("Success", "All answers submitted successfully.")
        else:
            self.show_popup("Error", result)


        # Close the screen after submission
        self.eval_filling_screen.close()

    def employee_evaluation_show(self,item):
        row = item.row()
        first_col_item = self.eval_filling_screen.employeesTable.item(row, 0)
        employee_name = first_col_item.text() if first_col_item else None
        if not employee_name:
            self.show_popup("Error", "No employee selected.")
            return
        self.eval_filling_screen = EvaluationFillingScreen(employee_name)
        self.eval_filling_screen.manage = self
        self.eval_filling_screen.display()

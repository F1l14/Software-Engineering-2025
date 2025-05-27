from src.Screen.Evaluation.EvaluationFormatScreen import EvaluationFormatScreen
from src.Screen.Evaluation.EvaluationEditScreen import EvaluationEditScreen
from src.Screen.Evaluation.QuestionEditScreen import QuestionEditScreen
from src.Screen.Evaluation.EvaluationCheckScreen import EvaluationCheckScreen
from src.Class.DBManager import DBManager
from src.Class.Evaluation import Evaluation
from src.Class.EvaluationQuestion import EvaluationQuestion
from PyQt6.QtWidgets import QTableWidgetItem,QMessageBox
class ManageEvalFormClass:
    def __init__(self):
        self.eval_form_screen = EvaluationFormatScreen()
        self.eval_form_screen.manage = self
        self.eval_form_screen.display()

    def show_popup(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Icon.Information)  # or Warning, Critical, etc.
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()

    def cancel(self):
        self.eval_form_screen.close()

    def selectFormatType(self, type: str):
        if type == "manager":
            eval_type_text = "Managers"
            self.eval_edit_screen = EvaluationEditScreen(eval_type_text)
            self.eval_edit_screen.manage = self
            self.eval_edit_screen.display()
            self.eval_form_screen.close()
        elif type == "employee":
            eval_type_text = "Employees"
            self.eval_edit_screen = EvaluationEditScreen(eval_type_text)
            self.eval_edit_screen.manage = self
            self.eval_edit_screen.display()
            self.eval_form_screen.close()
    

    def add_question(self):
        self.question_edit_screen = QuestionEditScreen()
        self.question_edit_screen.manage = self
        self.question_edit_screen.display()

    def cancel_question(self):
        self.question_edit_screen.close()
    
    def save_question(self):
        question_text, user_answers = self.question_edit_screen.get_data()
        if question_text and user_answers:
            if hasattr(self, "editing_row") and self.editing_row >= 0:
                
                self.eval_edit_screen.questionsTable.setItem(self.editing_row, 0, QTableWidgetItem(question_text))
                self.eval_edit_screen.questionsTable.setItem(self.editing_row, 1, QTableWidgetItem(", ".join(user_answers)))
                print(f"Updated row {self.editing_row}")
            else:
                
                row_position = self.eval_edit_screen.questionsTable.rowCount()
                self.eval_edit_screen.questionsTable.insertRow(row_position)

                self.eval_edit_screen.questionsTable.setItem(row_position, 0, QTableWidgetItem(question_text))
                self.eval_edit_screen.questionsTable.setItem(row_position, 1, QTableWidgetItem(", ".join(user_answers)))

            self.question_edit_screen.close()
            self.eval_edit_screen.reload()

            
            self.editing_row = -1
        else:
            self.show_popup("Error", "Please fill in both question and answers before saving.")


    def edit_selected_question(self):
        selected_row = self.eval_edit_screen.questionsTable.currentRow()
        self.editing_row = selected_row
        if selected_row < 0:
            self.show_popup("Error", "No row selected")
            return
        
        question_item = self.eval_edit_screen.questionsTable.item(selected_row, 0)
        answers_item = self.eval_edit_screen.questionsTable.item(selected_row, 1)

        question_text = question_item.text() if question_item else ""
        answers_text = answers_item.text() if answers_item else ""
        answers_list = [a.strip() for a in answers_text.split(",") if a.strip()]
       
        
        self.question_edit_screen = QuestionEditScreen()
        self.question_edit_screen.manage = self
        self.question_edit_screen.display(question_text, answers_list)
        
        

    def delete_selected_question(self):
        selected_row = self.eval_edit_screen.questionsTable.currentRow()
        if selected_row < 0:
            self.show_popup("Error", "No row selected")
            return
        
        self.eval_edit_screen.questionsTable.removeRow(selected_row)
        self.eval_edit_screen.reload()
    
    def cancelEvaluation(self):
        self.eval_edit_screen.close()
        self.eval_form_screen.close()
        self.eval_check_screen.close()

    def submitQuestionsList(self):
        self.eval_edit_screen.hide()
        self.eval_form_screen.close()
        self.eval_check_screen = EvaluationCheckScreen()
        self.eval_check_screen.manage = self
        self.eval_check_screen.display(self.eval_edit_screen.questionsTable)

    def publish_form(self):
        db = DBManager()
        start_date = self.eval_check_screen.startDateTime.dateTime().toPyDateTime()
        end_date = self.eval_check_screen.endDateTime.dateTime().toPyDateTime()

        if self.eval_edit_screen.eval_type_text == "Managers":
            _, eval_id  = db.saveEvaluationForm('eval_for_managers', start_date, end_date)
            eval_form = Evaluation('eval_for_managers', start_date, end_date)
            row_count = self.eval_edit_screen.questionsTable.rowCount()
            for row in range(row_count):
                question_item = self.eval_edit_screen.questionsTable.item(row, 0)
                answers_item = self.eval_edit_screen.questionsTable.item(row, 1)

                question_text = question_item.text() if question_item else ""
                answers = [a.strip() for a in answers_item.text().split(",")] if answers_item else []
                db.saveQuestion(eval_id, question_text, answers)
                evalQuestion = EvaluationQuestion(eval_form, question_text, answers)
            employees = db.queryAllEmployees()
            for employee in employees:
                username = employee[0]  
                db.createNotification(username, "Evaluation", "A new evaluation form has been published. Please check your evaluations section.")
        elif self.eval_edit_screen.eval_type_text == "Employees":
            __, eval_id = db.saveEvaluationForm('eval_for_employees', start_date, end_date)

            row_count = self.eval_edit_screen.questionsTable.rowCount()
            for row in range(row_count):
                question_item = self.eval_edit_screen.questionsTable.item(row, 0)
                answers_item = self.eval_edit_screen.questionsTable.item(row, 1)

                question_text = question_item.text() if question_item else ""
                answers = [a.strip() for a in answers_item.text().split(",")] if answers_item else []
                db.saveQuestion(eval_id, question_text, answers)
                evalQuestion = EvaluationQuestion(eval_form, question_text, answers)
            managers = db.queryAllManagers()
            for manager in managers:
                username = manager[0]
                db.createNotification(username, "Evaluation", "A new evaluation form has been published. Please check your evaluations section.")
        db.close()
        self.show_popup("Success", "Evaluation form published successfully.")
        self.eval_check_screen.close()
        self.eval_form_screen.close()
        self.eval_edit_screen.close()
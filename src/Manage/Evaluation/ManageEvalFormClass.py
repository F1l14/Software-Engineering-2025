from src.Screen.Evaluation.EvaluationFormatScreen import EvaluationFormatScreen
from src.Screen.Evaluation.EvaluationEditScreen import EvaluationEditScreen
from src.Screen.Evaluation.QuestionEditScreen import QuestionEditScreen
from PyQt6.QtWidgets import QTableWidgetItem
class ManageEvalFormClass:
    def __init__(self):
        self.eval_form_screen = EvaluationFormatScreen()
        self.eval_form_screen.manage = self
        self.eval_form_screen.display()
      

    def cancel(self):
        self.eval_form_screen.close()

    def eval_for_manager(self):
        eval_type_text = "Managers"
        self.eval_edit_screen = EvaluationEditScreen(eval_type_text)
        self.eval_edit_screen.manage = self
        self.eval_edit_screen.display()
        self.eval_form_screen.close()
        

    def eval_for_employee(self):
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
            table = self.eval_edit_screen.questionsTable  

            row_position = table.rowCount()
            table.insertRow(row_position)

            
            table.setItem(row_position, 0, QTableWidgetItem(question_text))

            
            answers_str = ", ".join(user_answers)
            table.setItem(row_position, 1, QTableWidgetItem(answers_str))

            self.question_edit_screen.close()
        else:
            print("Question or answers cannot be empty.")

    def edit_selected_question(self):
        selected_row = self.questionsTable.currentRow()
        if selected_row < 0:
            print("No row selected")
            return

        question_item = self.questionsTable.item(selected_row, 0)
        answers_item = self.questionsTable.item(selected_row, 1)

        question_text = question_item.text() if question_item else ""
        answers_text = answers_item.text() if answers_item else ""
        answers_list = [a.strip() for a in answers_text.split(",") if a.strip()]

        # Open the QuestionEditScreen with pre-filled data
        self.question_edit_screen = QuestionEditScreen()
        self.question_edit_screen.manage = self.manage  # Reuse your existing management
        self.question_edit_screen.set_data(question_text, answers_list)
        self.question_edit_screen.display()

        # Optionally store the row index to update it later
        self.editing_row = selected_row

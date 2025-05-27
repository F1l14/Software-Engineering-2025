from src.Screen.Evaluation.EvaluationFormatScreen import EvaluationFormatScreen
from src.Screen.Evaluation.EvaluationEditScreen import EvaluationEditScreen
from src.Screen.Evaluation.QuestionEditScreen import QuestionEditScreen
from src.Screen.Evaluation.EvaluationCheckScreen import EvaluationCheckScreen
from PyQt6.QtWidgets import QTableWidgetItem
class ManageEvalFormClass:
    def __init__(self):
        self.eval_form_screen = EvaluationFormatScreen()
        self.eval_form_screen.manage = self
        self.eval_form_screen.display()
      

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
            print("Question or answers cannot be empty.")


    def edit_selected_question(self):
        selected_row = self.eval_edit_screen.questionsTable.currentRow()
        self.editing_row = selected_row
        if selected_row < 0:
            print("No row selected")
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
            print("No row selected")
            return
        
        self.eval_edit_screen.questionsTable.removeRow(selected_row)
        self.eval_edit_screen.reload()
       
    def ready_form(self):
        self.eval_edit_screen.hide()
        self.eval_form_screen.close()
        self.eval_check_screen = EvaluationCheckScreen()
        self.eval_check_screen.manage = self
        self.eval_check_screen.display(self.eval_edit_screen.questionsTable)

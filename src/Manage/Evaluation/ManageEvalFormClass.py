from src.Screen.Evaluation.EvaluationFormatScreen import EvaluationFormatScreen
from src.Screen.Evaluation.EvaluationEditScreen import EvaluationEditScreen

class ManageEvalFormClass:
    def __init__(self):
        self.eval_form_screen = EvaluationFormatScreen()
        self.eval_form_screen.manage = self
        self.eval_form_screen.display()

    def cancel(self):
        self.eval_form_screen.close()

    def eval_for_manager(self):
        eval_type_text = "Manager"
        self.eval_edit_screen = EvaluationEditScreen(eval_type_text)
        self.eval_edit_screen.display()
        self.eval_form_screen.close()
        

    def eval_for_employee(self):
        eval_type_text = "Employee"
        self.eval_edit_screen = EvaluationEditScreen(eval_type_text)
        self.eval_edit_screen.display()
        self.eval_form_screen.close()
from src.Class.Evaluation import Evaluation
class EvaluationQuestion:
    def __init__(self, eval_form:Evaluation , question_text: str, answers: list[str]):
        self.eval_form = eval_form
        self.question_text = question_text
        self.answers = answers  # list of strings (answer options)
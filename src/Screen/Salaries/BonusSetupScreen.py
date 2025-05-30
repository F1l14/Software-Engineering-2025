from PyQt6.QtWidgets import QDialog, QPlainTextEdit, QMessageBox, QPushButton
from PyQt6 import uic

class BonusSetupScreen(QDialog):
    def __init__(self):
        super().__init__()
    
    def display(self):
        uic.loadUi("ui/7_Salaries/BonusSetupScreen.ui", self)
        self.badget = self.findChild(QPlainTextEdit, "badget")
        self.percentage1 = self.findChild(QPlainTextEdit, "percentage1")
        self.percentage2 = self.findChild(QPlainTextEdit, "percentage2")
        self.saveBonusButton = self.findChild(QPushButton, "saveBonusButton")
        self.saveBonusButton.clicked.connect(self.checkBonus)
        self.exec()

    def checkBonus(self):
        try:
            badget_values = [x.strip() for x in self.badget.toPlainText().split(',') if x.strip()]
            percentage1_values = [x.strip() for x in self.percentage1.toPlainText().split(',') if x.strip()]
            percentage2_values = [x.strip() for x in self.percentage2.toPlainText().split(',') if x.strip()]

            if not badget_values or not percentage1_values or not percentage2_values:
                QMessageBox.critical(self, "Error", "All fields must be filled.")
                return

            try:
                badget_numbers = [float(b) for b in badget_values]
            except ValueError:
                QMessageBox.critical(self, "Error", "Project value categories must be numbers.")
                return

            if badget_numbers != sorted(badget_numbers):
                QMessageBox.critical(self, "Error", "Project value categories must be in ascending order.")
                return

            def convert_percentages(p_list, label):
                result = []
                for p in p_list:
                    if p.endswith('%'):
                        p = p[:-1]
                    try:
                        result.append(float(p))
                    except ValueError:
                        QMessageBox.critical(self, "Error", f"Invalid percentage in {label}.")
                        return None
                return result

            perc1 = convert_percentages(percentage1_values, "Manager Bonus")
            perc2 = convert_percentages(percentage2_values, "Employee Bonus")

            if perc1 is None or perc2 is None:
                return

            if not (len(perc1) == len(badget_numbers) and len(perc2) == len(badget_numbers)):
                QMessageBox.critical(self, "Σφάλμα", "Οι λίστες ποσοστών bonus πρέπει να έχουν ίδιο αριθμό με τις κατηγορίες project.")
                return


            self.manage.saveBonusDetails(badget_numbers, perc1, perc2)
            self.accept()

        except Exception as e:
            import traceback
            traceback.print_exc()
            QMessageBox.critical(self, "Error", f"Unexpected error: {repr(e)}")




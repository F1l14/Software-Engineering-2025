from PyQt6.QtWidgets import QDialog, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt6 import uic

class BonusBoardScreen(QDialog):
    def __init__(self):
        super().__init__()
    
    def display(self):
        uic.loadUi("ui/7_Salaries/BonusBoardScreen.ui", self)
        self.bonusBoard = self.findChild(QTableWidget, "bonusBoard")
        self.bonusSetup = self.findChild(QTableWidget, "bonusSetup")
        self.showBonus()
        self.exec()

    def showBonus(self):
        results = self.manage.getBonusBoardDetails()

        if not results or not isinstance(results, tuple):
            QMessageBox.critical(self, "Error", f"Failed to get bonus details: {results}")
            return

        self.bonus_board_results, self.bonus_setup_results = results

        if self.bonus_board_results is None or self.bonus_setup_results is None:
            QMessageBox.critical(self, "Error", f"Failed to get bonus details: {self.bonus_setup_results}")
            return

        self.bonusBoard.setRowCount(len(self.bonus_board_results))
        self.bonusBoard.setColumnCount(2)
        self.bonusBoard.setHorizontalHeaderLabels(["Username", "Bonus ($)"])

        for row_idx, bonus_data in enumerate(self.bonus_board_results):
            username = bonus_data["username"]
            bonus_amount = bonus_data["bonus"]
            self.bonusBoard.setItem(row_idx, 0, QTableWidgetItem(username))
            self.bonusBoard.setItem(row_idx, 1, QTableWidgetItem(f"{bonus_amount:.2f}"))

        if not self.bonus_setup_results:
            QMessageBox.warning(self, "Warning", "No bonus setup found.")
            return

        category_values = [str(row["category_value"]) for row in self.bonus_setup_results]
        manager_percentages = [f"{row['manager_bonus_percentage']}%" for row in self.bonus_setup_results]
        employee_percentages = [f"{row['employee_bonus_percentage']}%" for row in self.bonus_setup_results]


        self.bonusSetup.setRowCount(2)
        self.bonusSetup.setColumnCount(len(category_values))
        self.bonusSetup.setHorizontalHeaderLabels(category_values)
        self.bonusSetup.setVerticalHeaderLabels(["Manager", "Employee"])

        for col_idx in range(len(category_values)):
            self.bonusSetup.setItem(0, col_idx, QTableWidgetItem(manager_percentages[col_idx]))
            self.bonusSetup.setItem(1, col_idx, QTableWidgetItem(employee_percentages[col_idx]))


       
        

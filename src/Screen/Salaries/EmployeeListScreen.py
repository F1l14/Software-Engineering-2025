from PyQt6.QtWidgets import QDialog, QTableWidget, QTableWidgetItem, QMessageBox, QFileDialog
from PyQt6 import uic
import csv

class EmployeeListScreen(QDialog):
    def __init__(self):
        super().__init__()
    
    def display(self):
        uic.loadUi("ui/7_Salaries/EmployeeListScreen.ui", self)
        self.salaryList = self.findChild(QTableWidget, "employeeSalaryList")
        self.showEmployeeSalariesList()
        self.bonusButton.clicked.connect(self.manage.showBonus)
        self.editButton.clicked.connect(self.checkChanges)
        self.exportButton.clicked.connect(self.exportData)
        self.exec()

    def showEmployeeSalariesList(self):
        self.salaries = self.manage.getEmployeeSalaries()
        username = [item[0] for item in self.salaries]
        salary = [item[1] for item in self.salaries]

        self.salaryList.setRowCount(len(username))
        self.salaryList.setColumnCount(2)
        self.salaryList.setHorizontalHeaderLabels(['username', 'salary'])

        for row, (username, salary) in enumerate(zip(username, salary)):
            self.salaryList.setItem(row, 0, QTableWidgetItem(str(username)))
            self.salaryList.setItem(row, 1, QTableWidgetItem(str(salary)))

    def checkChanges(self):
        updated_data = []

        for row in range(self.salaryList.rowCount()):
            username_item = self.salaryList.item(row, 0)
            salary_item = self.salaryList.item(row, 1)

            if username_item is None or salary_item is None:
                QMessageBox.warning(self, "Input Error", f"Missing data in row {row + 1}.")
                return

            username = username_item.text().strip()
            salary_text = salary_item.text().strip()

            if not username:
                QMessageBox.warning(self, "Input Error", f"Username in row {row + 1} is empty.")
                return

            try:
                salary = float(salary_text)
                if salary < 0:
                    raise ValueError()
            except ValueError:
                QMessageBox.warning(self, "Input Error", f"Invalid salary '{salary_text}' in row {row + 1}. Please enter a non-negative number.")
                return

            updated_data.append((username, salary))

        self.manage.editList(updated_data)
        QMessageBox.information(self, "Success", "Salaries updated successfully.")


    
    def exportData(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save File", "", "CSV Files (*.csv);;All Files (*)"
        )

        if not file_path:
            return 

        try:
            
            with open(file_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)

                headers = [self.salaryList.horizontalHeaderItem(i).text() for i in range(self.salaryList.columnCount())]
                writer.writerow(headers)

                for row in range(self.salaryList.rowCount()):
                    row_data = []
                    for col in range(self.salaryList.columnCount()):
                        item = self.salaryList.item(row, col)
                        row_data.append(item.text() if item else "")
                    writer.writerow(row_data)

            QMessageBox.information(self, "Export Successful", "Data exported successfully!")

        except Exception as e:
            QMessageBox.critical(self, "Export Failed", f"An error occurred: {e}")

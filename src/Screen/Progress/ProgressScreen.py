from PyQt6.QtWidgets import QDialog, QTableWidgetItem, QTableWidget, QLineEdit, QPushButton
from PyQt6 import uic
import matplotlib.pyplot as plt


class ProgressScreen(QDialog):
    def __init__(self):
        super().__init__()
    
    def display(self):
        uic.loadUi("ui/3_Progress/ProgressScreen.ui", self)
        self.employeeTable = self.findChild(QTableWidget, "employeeTable")
        self.searchBox = self.findChild(QLineEdit, "searchBox")
        self.createEmployeeList()
        
        if self.searchBox:
            self.searchBox.textChanged.connect(self.manage.filterTable)

        self.employeeTable.cellDoubleClicked.connect(self.onRowSelected)

        self.employeeDetailsButton.clicked.connect(self.onRowSelected)

        
        self.exec()
        
    def createBusinessGraph(self):
        self.graphData = self.manage.getData()

        # Unpack data
        months = [item[0] for item in self.graphData]
        project_counts = [item[1] for item in self.graphData]

        plt.figure(figsize=(8, 5))
        plt.bar(months, project_counts, color='skyblue')
        plt.xlabel('Month')
        plt.ylabel('Completed Projects')
        plt.title('Number of Completed Projects per Month')
        plt.tight_layout()
        plt.show()
        
    def createEmployeeList(self):
        self.employeeData = self.manage.getEmployeeData()
        usernames = [item[0] for item in self.employeeData]
        first_names = [item[1] for item in self.employeeData]
        last_names = [item[2] for item in self.employeeData]
        departments = [item[3] for item in self.employeeData]

        self.employeeTable.setRowCount(len(usernames))
        self.employeeTable.setColumnCount(4)
        self.employeeTable.setHorizontalHeaderLabels(['Όνομα Χρήστη', 'Όνομα', 'Επώνυμο', 'Τμήμα'])

        for row, (username, first_name, last_name, department) in enumerate(zip(usernames, first_names, last_names, departments)):
            self.employeeTable.setItem(row, 0, QTableWidgetItem(str(username)))
            self.employeeTable.setItem(row, 1, QTableWidgetItem(str(first_name)))
            self.employeeTable.setItem(row, 2, QTableWidgetItem(str(last_name)))
            self.employeeTable.setItem(row, 3, QTableWidgetItem(str(department)))


    def onRowSelected(self, row):
        # Get data from the selected row
        username = self.employeeTable.item(row, 0).text()
        first_name = self.employeeTable.item(row, 1).text()
        last_name = self.employeeTable.item(row, 2).text()
        department = self.employeeTable.item(row, 3).text()
        # Proceed to another window, e.g.:
        self.showPersonalProgress(username, first_name, last_name, department)

    def showPersonalProgress(self, username, first_name, last_name, department):
        self.manage.showPersonalProgress(username, first_name, last_name, department)

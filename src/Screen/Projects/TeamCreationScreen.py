from PyQt6.QtWidgets import QDialog, QLineEdit, QListWidget, QListWidgetItem, QMessageBox, QPushButton
from PyQt6 import uic
from src.Class.Session import Session

class TeamCreationScreen(QDialog):
    def __init__(self):
        super().__init__()
    
    def display(self):
        uic.loadUi("ui/2_Projects/TeamCreationScreen.ui", self)
        self.employeesList = self.findChild(QListWidget, "employeesList")
        self.employeesList2 = self.findChild(QListWidget, "employeesList2")
        self.saveButton = self.findChild(QPushButton, "saveButton")
        self.saveButton.clicked.connect(self.save)
        self.nameBox = self.findChild(QLineEdit, "nameBox")
        self.showAvailableEmployees()
        self.exec()

    def showAvailableEmployees(self):
        self.employees = self.manage.getAvailableEmployees()
        self.employeesList.clear()
        self.employeesList2.clear()

        for empl in self.employees:
            item = QListWidgetItem(empl[0])  
            self.employeesList.addItem(item)

        for empl2 in self.employees:
            item = QListWidgetItem(empl2[0])  
            self.employeesList2.addItem(item)

    def save(self):
        username = Session.getUser()
        name = self.nameBox.text().strip()

        selected_items = self.employeesList.selectedItems()
        selected_members = [item.text() for item in selected_items]

        leader_items = self.employeesList2.selectedItems()
        if not leader_items:
            QMessageBox.information(self, "No Selection", "Please select a team leader.")
            return
        selected_leader = leader_items[0].text()  

        if not name:
            QMessageBox.information(self, "No Selection", "Please type a team name.")
            return

        if not selected_members:
            QMessageBox.information(self, "No Selection", "Please select at least one member.")
            return
 
        if selected_leader in selected_members:
            QMessageBox.warning(self, "Invalid Selection", "Leader cannot also be a team member.")
            return
            
        
        self.manage.saveNewTeam(selected_members, selected_leader, name, username)
        self.accept()

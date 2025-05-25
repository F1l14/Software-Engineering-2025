from PyQt6.QtWidgets import QDialog, QTableWidget, QTableWidgetItem
from PyQt6 import uic

class TeamListScreen(QDialog):
    def __init__(self):
        super().__init__()
    
    def display(self):
        uic.loadUi("ui/6_Team_Space/TeamListScreen.ui", self)
        self.exec()
from PyQt6.QtWidgets import QDialog, QTextEdit, QMessageBox, QPushButton
from PyQt6 import uic

class BonusSetupScreen(QDialog):
    def __init__(self):
        super().__init__()
    
    def display(self):
        uic.loadUi("ui/7_Salaries/BonusSetupScreen.ui", self)
        self.badget = self.findChild(QTextEdit, "badget")
        self.percentage1 = self.findChild(QTextEdit, "percentage1")
        self.percentage2 = self.findChild(QTextEdit, "percentage2")
        self.saveBonusButton = self.findChild(QPushButton, "saveBonusButton")
        self.saveBonusButton.clicked.connect(self.checkBonus)
        self.exec()

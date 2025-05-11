from PyQt6.QtWidgets import QDialog
from PyQt6 import uic

class WelcomeScreen(QDialog):
    def __init__(self):
        super().__init__()
    
    def display(self):
        uic.loadUi("ui/WelcomeScreen.ui", self)
        self.loginButton.clicked.connect(self.handler.handle_login)
        self.exec()
from PyQt6.QtWidgets import QDialog
from PyQt6 import uic

class WelcomeScreen(QDialog):
    def __init__(self):
        super().__init__()
    
    def display(self):
        uic.loadUi("ui/WelcomeScreen.ui", self)
        self.loginButton.clicked.connect(self.manage.handle_login)
        self.registerButton.clicked.connect(self.manage.handle_register)
        self.exec()
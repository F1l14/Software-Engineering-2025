from PyQt6.QtWidgets import QDialog
from PyQt6 import uic

class MainScreen(QDialog):
    def __init__(self):
        super().__init__()
    
    def display(self):
        uic.loadUi("ui/MainScreen.ui", self)
        self.pushButton.clicked.connect(self.handler.progress)
        self.exec()
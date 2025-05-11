from PyQt6.QtWidgets import QDialog
from PyQt6 import uic

class ProgressScreen(QDialog):
    def __init__(self):
        super().__init__()
    
    def display(self):
        uic.loadUi("ui/ProgressScreen.ui", self)
        self.exec()
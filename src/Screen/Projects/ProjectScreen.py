from PyQt6.QtWidgets import QDialog
from PyQt6 import uic

class ProjectScreen(QDialog):
    def __init__(self):
        super().__init__()
    
    def display(self):
        uic.loadUi("ui/2_Projects/ProjectScreen.ui", self)
        self.exec()
from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

class TasksScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.display()
    
    def display(self):
        uic.loadUi("ui/MainScreen.ui", self)
        self.show()
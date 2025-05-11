from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

class MainScreen(QMainWindow):
    def __init__(self):
        super().__init__()
    
    def display(self):
        uic.loadUi("ui/MainScreen.ui", self)
        self.pushButton.clicked.connect(self.manage.progress)
        self.show()
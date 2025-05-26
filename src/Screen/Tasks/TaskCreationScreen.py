from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

class TaskCreationScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        
    
    def display(self):
        uic.loadUi("ui/8_Tasks/TaskCreationScreen.ui", self)
        self.submit_button.clicked.connect(self.manage.submitNewTask)
        self.show()
        self.setWindowTitle("Create New Task")
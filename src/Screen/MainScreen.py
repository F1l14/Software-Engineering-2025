from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

class MainScreen(QMainWindow):
    def __init__(self):
        super().__init__()
    
    def display(self):
        uic.loadUi("ui/MainScreen.ui", self)
        self.projectsButton.clicked.connect(self.manage.projects)
        self.pushButton.clicked.connect(self.manage.progress)
        self.salariesButton.clicked.connect(self.manage.salaries)
        self.evaluationButton.clicked.connect(self.manage.evaluation)
        self.show()
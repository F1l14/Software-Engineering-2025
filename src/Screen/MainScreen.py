from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic
from src.Class.Session import Session

class MainScreen(QMainWindow):
    def __init__(self):
        super().__init__()
    
    def display(self):
        uic.loadUi("ui/MainScreen.ui", self)
        self.projectsButton.clicked.connect(self.manage.showProjectsScreen)
        self.salariesButton.clicked.connect(self.manage.showEmployeeListScreen)
        self.progressButton.clicked.connect(self.manage.progress)
        self.teamsButton.clicked.connect(self.manage.showTeamsScreen)
        self.salariesButton.clicked.connect(self.manage.salaries)
        self.evaluationButton.clicked.connect(self.manage.evaluation)
        self.tasksButton.clicked.connect(self.manage.showTasksScreen)
        
        if Session.getRole() != "admin":
            self.progressButton.setVisible(False)
        
        if Session.getRole() == "employee":
            self.projectsButton.setVisible(False)

        self.show()
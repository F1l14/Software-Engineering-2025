from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic
from src.Class.Session import Session
from src.Class.DBManager import DBManager

class MainScreen(QMainWindow):
    def __init__(self):
        super().__init__()
    
    def display(self):
        uic.loadUi("ui/MainScreen.ui", self)
        self.projectsButton.clicked.connect(self.manage.showProjectsScreen)
        self.progressButton.clicked.connect(self.manage.progress)
        self.teamsButton.clicked.connect(self.manage.showTeamsScreen)
        self.salariesButton.clicked.connect(self.manage.salaries)
        self.evaluationButton.clicked.connect(self.manage.evaluation)
        self.tasksButton.clicked.connect(self.manage.showTasksScreen)
        
        if Session.getRole() != "admin":
            self.progressButton.setVisible(False)
        
        if Session.getRole() == "employee":
            self.projectsButton.setVisible(False)
        if Session.getRole() == "admin":
            self.evaluationButton.setEnabled(True)
        else: 
            if DBManager().isEvaluationActive(Session.getRole()):
                self.evaluationButton.setEnabled(True)
            else:
                self.evaluationButton.setEnabled(False)
                self.evaluationButton.setToolTip("No evaluation period is currently active.")
        self.show()
    
    
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
        self.salariesButton.clicked.connect(self.manage.showEmployeeListScreen)
        self.progressButton.clicked.connect(self.manage.progress)
        self.teamsButton.clicked.connect(self.manage.showTeamsScreen)
        self.salariesButton.clicked.connect(self.manage.salaries)
        self.messageSelect.clicked.connect(self.manage.showMessageScreen)
        self.noticeSelect.clicked.connect(self.manage.showNoticeboardScreen)
        self.evaluationButton.clicked.connect(self.manage.showEvaluationFormatWindow)
        self.tasksButton.clicked.connect(self.manage.showTasksScreen)
        self.leavesButton.clicked.connect(self.manage.showLeavesMenu)
        
        if Session.getRole() == "employee": # Hide the projects button for employees
            self.projectsButton.setVisible(False)
        
        if Session.getRole() != "admin":   # Hide the evaluation and salaries button for employees and managers
            self.progressButton.setVisible(False)
            self.salariesButton.setVisible(False)
        
        
        if Session.getRole() != "employee": # Hide the tasks and teams button for admin and managers
            self.tasksButton.setVisible(False)
            self.teamsButton.setVisible(False)
            

        if Session.getRole() == "admin":
            self.evaluationButton.setEnabled(True)
            self.leavesButton.setVisible(False)
        else: 
            if DBManager().isEvaluationActive(Session.getRole()):
                self.evaluationButton.setEnabled(True)
            else:
                self.evaluationButton.setEnabled(False)
                self.evaluationButton.setToolTip("No evaluation period is currently active.")
        
        self.show()
    
    
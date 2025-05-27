from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

class MainScreen(QMainWindow):
    def __init__(self):
        super().__init__()
    
    def display(self):
        uic.loadUi("ui/MainScreen.ui", self)
        self.projectsButton.clicked.connect(self.manage.showProjectsScreen)
        self.salariesButton.clicked.connect(self.manage.showEmployeeListScreen)
        self.progressButton.clicked.connect(self.manage.progress)
        self.teamsButton.clicked.connect(self.manage.showTeamsScreen)
        self.tasksButton.clicked.connect(self.manage.showTasksScreen)

        self.show()
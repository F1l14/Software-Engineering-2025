from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

class MainScreen(QMainWindow):
    def __init__(self):
        super().__init__()
    
    def display(self):
        uic.loadUi("ui/MainScreen.ui", self)
        self.projectsButton.clicked.connect(self.manage.showProjectsScreen)
        self.progressButton.clicked.connect(self.manage.progress)
        self.teamsButton.clicked.connect(self.manage.showTeamsScreen)
        self.salariesButton.clicked.connect(self.manage.salaries)

        self.messageSelect.clicked.connect(self.manage.showMessageScreen)
        self.noticeSelect.clicked.connect(self.manage.showNoticeboardScreen)
        
        self.tasksButton.clicked.connect(self.manage.showTasksScreen)

        self.show()
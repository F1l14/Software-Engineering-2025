from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

class TasksScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        
    
    def display(self):
        uic.loadUi("ui/8_Tasks/TasksScreen.ui", self)
        self.create_button.clicked.connect(self.manage.newCreateTaskScreen)
        self.assign_task_button.clicked.connect(self.manage.newAssignTaskScreen)
        self.refresh_button.clicked.connect(lambda: (self.manage.getTasks("all"), self.manage.displayTasks()))
        self.show()
        self.setWindowTitle("Tasks")
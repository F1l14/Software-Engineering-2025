from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

class TaskAssignScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        
    
    def display(self):
        uic.loadUi("ui/8_Tasks/TaskAssignScreen.ui", self)
        self.unassigned_list.itemSelectionChanged.connect(self.manage.changeTaskSelection)
        self.submit_assign_button.clicked.connect(self.manage.assignTask)
        self.show()
        self.setWindowTitle("Assign Task")
from PyQt6.QtWidgets import QDialog, QTableWidgetItem
from PyQt6 import uic

class TeamSpaceScreen(QDialog):
    def __init__(self):
        super().__init__()
    
    def display(self, tasks):
        uic.loadUi("ui/6_Team_Space/TeamSpaceScreen.ui", self)
        
        self.pushButton.clicked.connect(self.showFileSharing)
        
        tasks_ids = [item[0] for item in tasks]
        tasks_names = [item[1] for item in tasks]
        tasks_assigned_to = [item[2] for item in tasks]
        tasks_states = [item[3] for item in tasks]
        # self.tasksTableWidget = self.findChild(QtasksTableWidget, "tasksTableWidget")


        self.tasksTableWidget.setRowCount(len(tasks_ids))
        self.tasksTableWidget.setColumnCount(4)
        self.tasksTableWidget.setHorizontalHeaderLabels(['Αναγνωριστικό', 'Όνομα', 'Ανατεθειμένο σε', 'Κατάσταση'])

        for row, (task_id, task_name, task_assigned_to, task_state) in enumerate(zip(tasks_ids, tasks_names, tasks_assigned_to, tasks_states)):
            self.tasksTableWidget.setItem(row, 0, QTableWidgetItem(str(task_id)))
            self.tasksTableWidget.setItem(row, 1, QTableWidgetItem(str(task_name)))
            self.tasksTableWidget.setItem(row, 2, QTableWidgetItem(str(task_assigned_to)))
            self.tasksTableWidget.setItem(row, 3, QTableWidgetItem(str(task_state)))

        self.exec()

    def showFileSharing(self):
        self.manage.showFileSharingScreen()

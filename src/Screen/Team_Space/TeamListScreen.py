from PyQt6.QtWidgets import QDialog, QTableWidgetItem
from PyQt6 import uic
from src.Manage.Team_Space.ManageTeamSpaceClass import ManageTeamSpaceClass

class TeamListScreen(QDialog):
    def __init__(self):
        super().__init__()
    
    def display(self, teams):
        uic.loadUi("ui/6_Team_Space/TeamListScreen.ui", self)
        self.showTeamSpaceButton.clicked.connect(self.manage.showTeamSpace)
        
        team_ids = [item[0] for item in teams]
        team_names = [item[1] for item in teams]
        # self.tableWidget = self.findChild(QTableWidget, "tableWidget")


        self.tableWidget.setRowCount(len(team_ids))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(['Αναγνωριστικό', 'Όνομα'])

        for row, (team_id, team_name) in enumerate(zip(team_ids, team_names)):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(team_id)))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(str(team_name)))

        self.exec()
        
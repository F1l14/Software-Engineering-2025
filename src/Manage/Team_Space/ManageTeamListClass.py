from src.Screen.Team_Space.TeamListScreen import TeamListScreen
from src.Class.Session import Session
from src.Class.Employee import Employee
from src.Manage.Team_Space.ManageTeamSpaceClass import ManageTeamSpaceClass

class ManageTeamListClass:
    def __init__(self):
        self.team_screen = TeamListScreen()
        self.team_screen.manage = self
        self.employee = Employee(Session.getUser())
        teams = self.employee.getTeams()
        self.team_screen.display(teams)

    def showTeamSpace(self):
        selected_row = self.team_screen.tableWidget.currentRow()
        if selected_row >= 0:
            team_id = self.team_screen.tableWidget.item(selected_row, 0).text()
            ManageTeamSpaceClass(team_id)
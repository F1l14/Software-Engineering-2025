from src.Screen.Team_Space.TeamListScreen import TeamListScreen
from src.Class.Session import Session
from src.Class.Employee import Employee
from src.Class.DBManager import DBManager

class ManageTeamListClass:
    def __init__(self):
        self.team_screen = TeamListScreen()
        self.team_screen.manage = self
        self.employee = Employee(Session.getUser())
        teams = self.employee.getTeams()
        self.team_screen.display(teams)

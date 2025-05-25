from src.Screen.Team_Space.TeamListScreen import TeamListScreen
from src.Class.DBManager import DBManager

class ManageTeamListClass:
    def __init__(self):
        self.team_screen = TeamListScreen()
        self.team_screen.manage = self
        self.team_screen.display()

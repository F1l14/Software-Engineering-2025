from src.Class.Team import Team
from src.Screen.Team_Space.FileShareScreen import FileShareScreen
class ManageFileShareClass:
    def __init__(self, team_space_id):
        self.team_space_id = team_space_id
        self.team = Team(team_space_id)
        self.team_directory = self.team.getTeamDirectory()
        
        self.file_share_screen = FileShareScreen()
        self.file_share_screen.display(self.team_directory)
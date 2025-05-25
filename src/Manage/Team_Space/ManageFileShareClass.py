from src.Class.Team import Team
from src.Screen.Team_Space.FileShareScreen import FileShareScreen
from src.Screen.Team_Space.CreateDirectoryScreen import CreateDirectoryScreen
class ManageFileShareClass:
    def __init__(self, team_space_id):
        self.team_space_id = team_space_id
        self.team = Team(team_space_id)
        self.team_directory = self.team.getTeamDirectory()
        
        self.file_share_screen = FileShareScreen()
        self.file_share_screen.manageFileShare = self
        self.file_share_screen.display(self.team_directory)
        
    def createDirectoryScreen(self):
        self.create_directory_screen = CreateDirectoryScreen()
        self.create_directory_screen.manageCreateDirectory = self
        self.create_directory_screen.display()
        
    def createDirectory(self, directory_name):
        from src.Class.FileSystem import FileSystem
        FileSystem().createDirectory(self.team_space_id, directory_name)
        self.create_directory_screen.close()
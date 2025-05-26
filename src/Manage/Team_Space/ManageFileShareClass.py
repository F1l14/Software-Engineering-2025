from src.Class.Team import Team
from src.Screen.Team_Space.FileShareScreen import FileShareScreen
from src.Screen.Team_Space.CreateDirectoryScreen import CreateDirectoryScreen
from src.Screen.Team_Space.UploadFileScreen import UploadFileScreen
from src.Class.FileSystem import FileSystem
class ManageFileShareClass:
    def __init__(self, team_space_id):
        self.team_space_id = team_space_id
        self.team = Team(team_space_id)
        self.current_directory = self.team.getTeamDirectory()
        
        self.file_share_screen = FileShareScreen()
        self.file_share_screen.manageFileShare = self
        self.file_share_screen.current_directory = self.current_directory
        self.file_share_screen.display(self.current_directory)
        
    def createDirectoryScreen(self, directory=None):
        self.create_directory_screen = CreateDirectoryScreen()
        self.create_directory_screen.manageCreateDirectory = self
        self.create_directory_screen.current_directory = directory
        self.create_directory_screen.display()
        
    def createDirectory(self, current_directory, directory_name):
        FileSystem().createDirectory(current_directory, directory_name)
        self.create_directory_screen.close()

    def showUploadWindow(self, directory=None):
        self.upload_file_screen = UploadFileScreen(directory)
        self.upload_file_screen.manageUploadFile = self
        self.upload_file_screen.current_directory = directory
        self.upload_file_screen.display()
        
    def upload(self, file_path, directory=None):
        from src.Class.FileSystem import FileSystem
        FileSystem().upload(self.team_space_id, file_path, directory)
        self.upload_file_screen.close()
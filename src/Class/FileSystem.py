from pathlib import Path

class FileSystem:
    def __init__(self):
        pass

    def queryTeamDirectory(self, team_id):
        dir_path = Path("FileSystem/TeamDirectories") / str(team_id)
        dir_path.mkdir(parents=True, exist_ok=True)  # Create directory if it doesn't exist
        return str(dir_path) + "/"
    
    def createDirectory(self, team_id, directory_name):
        team_directory = self.queryTeamDirectory(team_id)
        new_directory_path = Path(team_directory) / directory_name
        new_directory_path.mkdir(parents=True, exist_ok=True)
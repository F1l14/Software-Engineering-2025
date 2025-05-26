from pathlib import Path

class FileSystem:
    def __init__(self):
        pass

    def queryTeamDirectory(self, team_id):
        dir_path = Path("FileSystem/TeamDirectories") / str(team_id)
        dir_path.mkdir(parents=True, exist_ok=True)  # Create directory if it doesn't exist
        return str(dir_path) + "/"
    
    def createDirectory(self, current_directory, directory_name):
        new_directory_path = Path(current_directory) / directory_name
        new_directory_path.mkdir(parents=True, exist_ok=True)
        
    def upload(self, team_id, file_path, directory=None):
        from shutil import copy2
        
        team_directory = self.queryTeamDirectory(team_id)
        if directory:
            target_directory = Path(team_directory) / directory
        else:
            target_directory = Path(team_directory)
        
        target_directory.mkdir(parents=True, exist_ok=True)
        destination_path = target_directory / Path(file_path).name
        copy2(file_path, destination_path)
from pathlib import Path
from PyQt6.QtWidgets import QFileDialog
import os
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
        
    def download(self, file_path):
        # Prompt user to select a directory
        directory = QFileDialog.getExistingDirectory(None, "Select Download Directory")

        if directory:
            # Example: copy file to selected directory
            import shutil
            destination = os.path.join(directory, os.path.basename(file_path))
            shutil.copy(file_path, destination)
            print(f"File downloaded to: {destination}")
        else:
            print("No directory selected.")
            
    def rename(self, file_path):
        new_name, _ = QFileDialog.getSaveFileName(None, "Rename File", file_path)

        if new_name:
            os.rename(file_path, new_name)
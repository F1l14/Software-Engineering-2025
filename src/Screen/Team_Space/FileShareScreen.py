import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QDialog
from PyQt6.QtGui import QFileSystemModel
from PyQt6.QtCore import QDir
from pathlib import Path

class FileShareScreen(QDialog):
    def __init__(self):
        super().__init__()
        
    def display(self, team_space_directory=None):
        uic.loadUi("ui/6_Team_Space/FileShareScreen.ui", self)

        # Dynamically determine the workspace root
        workspace_root = Path(__file__).resolve().parents[3]  # Adjust the number if needed
        # Default to a 'team_files' folder in the workspace if not provided
        if team_space_directory is None:
            team_space_directory = workspace_root / "team_files"
        else:
            team_space_directory = Path(team_space_directory)

        model = QFileSystemModel()
        model.setRootPath(str(team_space_directory))

        self.treeView.setModel(model)
        self.treeView.setRootIndex(model.index(str(team_space_directory)))
        self.exec()

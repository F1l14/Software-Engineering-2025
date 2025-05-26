import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QDialog
from PyQt6.QtGui import QFileSystemModel
from pathlib import Path

class FileShareScreen(QDialog):
    def __init__(self):
        super().__init__()
        
    def display(self, team_space_directory=None):
        uic.loadUi("ui/6_Team_Space/FileShareScreen.ui", self)

        self.createDirectoryButton.clicked.connect(self.showCreateDirectory)
        self.uploadButton.clicked.connect(self.showUpload)
        self.treeView.clicked.connect(self.onRowClicked)
        self.downloadButton.clicked.connect(self.downloadFile)

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
        
    def onRowClicked(self, index):
        self.selected_path = self.treeView.model().filePath(index)
    
    def showCreateDirectory(self):
        self.manageFileShare.createDirectoryScreen(self.selected_path if hasattr(self, 'selected_path') else self.current_directory)
        
    def showUpload(self):
        self.manageFileShare.showUploadWindow(self.selected_path if hasattr(self, 'selected_path') else self.current_directory)
    
    def downloadFile(self):
        if hasattr(self, 'selected_path'):
            self.manageFileShare.download(self.selected_path)
        else:
            print("No file selected for download.")
        

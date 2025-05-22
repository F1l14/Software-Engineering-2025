from src.Screen.Progress.ProgressScreen import ProgressScreen

class ManageProgressClass:
    def __init__(self):
        self.progress_screen = ProgressScreen()
        self.progress_screen.manage = self
        self.progress_screen.display()
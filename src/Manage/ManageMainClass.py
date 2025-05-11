from src.Screen.MainScreen import MainScreen
from src.Manage.ManageProgressClass import ManageProgressClass
class ManageMainClass:
    def __init__(self):
        self.main_screen = MainScreen()
        self.main_screen.handler = self
        self.main_screen.display()

    def progress(self):
        self.progress_screen = ManageProgressClass()        
        
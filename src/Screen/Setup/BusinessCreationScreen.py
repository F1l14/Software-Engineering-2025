from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

class BusinessCreationScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.display()
    
    def display(self):
        uic.loadUi("ui/1_Setup/BusinessCreationScreen.ui", self)
        self.next_button.clicked.connect(self.manage.createBusiness)
        self.upload_button.clicked.connect(self.manage.getLogo)
        self.show()
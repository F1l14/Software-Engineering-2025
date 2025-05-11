import sys
from PyQt6.QtWidgets import QApplication
from src.Manage.ManageWelcomeClass import ManageWelcomeClass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ManageWelcomeClass()
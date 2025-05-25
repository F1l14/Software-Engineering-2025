import sys
from PyQt6.QtWidgets import QApplication
from src.Manage.ManageWelcomeClass import ManageWelcomeClass
from src.Manage.ManageMainClass import ManageMainClass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Uncomment the line below to run the welcome screen
    # ManageWelcomeClass()
    ManageWelcomeClass()
    sys.exit(app.exec())
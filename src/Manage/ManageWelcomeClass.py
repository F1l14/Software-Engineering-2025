import mysql.connector
from src.Class.DBManager import DBManager
from src.Screen.WelcomeScreen import WelcomeScreen
from src.Manage.ManageMainClass import ManageMainClass
from PyQt6.QtWidgets import QMessageBox
from src.Manage.Setup.ManageSetupClass import ManageSetupClass
class ManageWelcomeClass:
    def __init__(self):
        self.welcome_screen = WelcomeScreen()
        self.welcome_screen.manage = self
        self.welcome_screen.display()
        
    def handle_login(self):
        username = self.welcome_screen.usernameLineEdit.text()
        password = self.welcome_screen.passwordLineEdit.text()
        
        try:
            db = DBManager()
            conn = db.conn
            cursor = conn.cursor()
            cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
            result = cursor.fetchone()

            if result and result[0] == password:
                QMessageBox.information(self.welcome_screen, "Success", "Login successful!")
                self.welcome_screen.accept()
                ManageMainClass()
            else:
                self.welcome_screen.statusLabel.setText("Invalid username or password.")

        except mysql.connector.Error as err:
            self.welcome_screen.statusLabel.setText(f"Database error: {err}")
        finally:
            if 'cursor' in locals() and cursor:
                cursor.close()
            if 'conn' in locals() and conn.is_connected():
                conn.close()
        
    def handle_register(self):
        self.welcome_screen.hide()
        self.managesetup = ManageSetupClass()

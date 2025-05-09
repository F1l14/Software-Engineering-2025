import sys
import mysql.connector
from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
from src.GUI.WelcomeScreen import Ui_Welcome  # The converted UI file
from src.GUI.MainScreen import Ui_Main  # The converted UI file

class LoginWindow(QDialog, Ui_Welcome):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loginButton.clicked.connect(self.handle_login)

    def handle_login(self):
        username = self.usernameLineEdit.text()
        password = self.passwordLineEdit.text()
        
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pythonDB"
            )
            cursor = conn.cursor()
            cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
            result = cursor.fetchone()

            if result and result[0] == password:
                QMessageBox.information(self, "Success", "Login successful!")
                self.accept()
            else:
                self.statusLabel.setText("Invalid username or password.")

        except mysql.connector.Error as err:
            self.statusLabel.setText(f"Database error: {err}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

class MainWindow(QDialog, Ui_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # connect signals or modify widgets here
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LoginWindow()
    if login.exec():
        print("Login accepted!")
        main_window = MainWindow()
        main_window.exec()
    else:
        print("Login rejected!")
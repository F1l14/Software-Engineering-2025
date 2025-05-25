from src.Screen.Setup.UserCreationScreen import UserCreationScreen
from src.Class.DBManager import DBManager
from src.Class.Admin import Admin
from src.Screen.Setup.BusinessCreationScreen import BusinessCreationScreen
from src.Screen.Setup.DepartmentCreationScreen import DepartmentCreationScreen
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QFileDialog

class ManageSetupClass:
    def __init__(self):
        self.user_creation_screen = UserCreationScreen()
        self.__db = DBManager()
        self.user_creation_screen.next_button.clicked.connect(self.createAdmin)
    
    def createAdmin(self):
        firstname = self.user_creation_screen.firstname_field.toPlainText()
        lastname = self.user_creation_screen.lastname_field.toPlainText()
        username = self.user_creation_screen.username_field.toPlainText()
        password = self.user_creation_screen.password_field.toPlainText()
        if not firstname or not lastname or not username or not password:
            self.show_popup("All fields are required.")
            return

        self.admin = Admin(username, firstname, lastname)
        msg = self.__db.createUser(username, password, firstname, lastname)
        if msg != "OK":
            self.show_popup(msg)
        else:
            self.user_creation_screen.hide()
            self.businessSetup()
            self.user_creation_screen.close()
            # Here you can redirect to the main application screen or perform other actions
            # For example, you might want to instantiate and show the main application class
            # ManageMainClass()  # Uncomment this line if you have a main class to show

    def businessSetup(self):
        self.business_creation_screen = BusinessCreationScreen()
        self.business_creation_screen.next_button.clicked.connect(self.createBusiness)
        self.business_creation_screen.upload_button.clicked.connect(self.getLogo)

    def createBusiness(self):
        name = self.business_creation_screen.business_field.toPlainText()
        owner = self.admin.username
        msg = self.admin.createBusiness(self.__db, name, owner, self.file_data)
        if msg != "OK":
            self.show_popup(msg)
            return
        self.departmentSetup()

    def getLogo(self):
        filename = QFileDialog.getOpenFileName(self.business_creation_screen, "Select Logo", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)")
        if filename[0]:
            self.business_creation_screen.logo_field.setText(filename[0])
            with open(filename[0], 'rb') as f:
                self.file_data = f.read()
        else:
            self.show_popup("No file selected.")
        
    
    def departmentSetup(self):
        self.business_creation_screen.hide()
        self.department_creation_screen = DepartmentCreationScreen()
        self.business_creation_screen.close()

    def show_popup(self, text):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText(text)
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

        

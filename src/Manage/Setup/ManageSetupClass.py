from src.Screen.Setup.UserCreationScreen import UserCreationScreen
from src.Class.DBManager import DBManager
from src.Class.Admin import Admin
from src.Screen.Setup.BusinessCreationScreen import BusinessCreationScreen
from src.Screen.Setup.DepartmentCreationScreen import DepartmentCreationScreen
from src.Screen.Setup.UserImportScreen import UserImportScreen
from src.Screen.Setup.UsersListScreen import UsersListScreen
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QFileDialog
import json

class ManageSetupClass:
    def __init__(self):
        self.user_creation_screen = UserCreationScreen()
        self.__db = DBManager()
        self.user_creation_screen.next_button.clicked.connect(self.createAdmin)
        self.__users_file=None
        self.__logo_data = None
    
    def createAdmin(self):
        firstname = self.user_creation_screen.firstname_field.toPlainText()
        lastname = self.user_creation_screen.lastname_field.toPlainText()
        username = self.user_creation_screen.username_field.toPlainText()
        password = self.user_creation_screen.password_field.toPlainText()
        if not firstname or not lastname or not username or not password:
            self.show_popup("All fields are required.")
            return

        self.admin = Admin(username)
        msg = self.__db.createUser(username, password, firstname, lastname)
        if msg != "OK":
            self.show_popup(msg)
        else:
            self.user_creation_screen.hide()
            self.businessSetup()
            self.user_creation_screen.close()
            
    def businessSetup(self):
        self.business_creation_screen = BusinessCreationScreen()
        self.business_creation_screen.next_button.clicked.connect(self.createBusiness)
        self.business_creation_screen.upload_button.clicked.connect(self.getLogo)

    def createBusiness(self):
        name = self.business_creation_screen.business_field.toPlainText()
        owner = self.admin.username
        msg = self.admin.createBusiness(self.__db, name, owner, self.__logo_data)
        if msg != "OK":
            self.show_popup(msg)
            return
        self.departmentSetup()

    def getLogo(self):
        filename = QFileDialog.getOpenFileName(self.business_creation_screen, "Select Logo", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)")
        if filename[0]:
            self.business_creation_screen.logo_field.setText(filename[0])
            with open(filename[0], 'rb') as f:
                self.__logo_data = f.read()
        else:
            self.show_popup("No file selected.")
            self.business_creation_screen.logo_field.clear()
        
    
    def departmentSetup(self):
        self.business_creation_screen.hide()
        self.department_creation_screen = DepartmentCreationScreen()
        self.business_creation_screen.close()

        self.department_creation_screen.create_button.clicked.connect(self.createDepartment)
        self.department_creation_screen.next_button.clicked.connect(self.checkDepartments)

    def createDepartment(self):
        name = self.department_creation_screen.department_field.toPlainText()
        if not name:
            self.show_popup("Department name is required.")
            return
        msg = self.__db.createDepartment(name)
        if msg != "OK":
            self.show_popup(msg)
            return
        
        self.department_creation_screen.departments_list.addItem(name)
        self.department_creation_screen.department_field.clear()

    def checkDepartments(self):
        if self.department_creation_screen.departments_list.count() == 0:
            self.show_popup("At least one department is required.")
            return
        self.userImportSetup()
    
    def userImportSetup(self):
        self.department_creation_screen.hide()
        self.user_import_screen = UserImportScreen()
        self.department_creation_screen.close()

        self.user_import_screen.upload_button.clicked.connect(self.importUsers)
        self.user_import_screen.next_button.clicked.connect(lambda:self.processUsers(self.__users_file))
        self.user_import_screen.skip_button.clicked.connect(lambda:self.mainScreenSetup(option="skip"))

    def importUsers(self):
        filename = QFileDialog.getOpenFileName(self.business_creation_screen, "Select JSON", "", "JSON Files (*.json)")
        if filename[0]:
            self.user_import_screen.file_label.setText(filename[0])
            self.__users_file = filename[0]
        else:
            self.show_popup("No file selected.")
            self.user_import_screen.file_label.clear()

    def processUsers(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                
                data = json.load(f) 
                self.usersListSetup()
               

        except json.JSONDecodeError as e:
            self.show_popup(f"Invalid JSON: {str(e)}")
        except Exception as e:
            self.show_popup(f"Error reading file: {str(e)}")


    def usersListSetup(self):
        self.user_import_screen.hide()
        self.users_list_screen = UsersListScreen()
        self.user_import_screen.close()

    def mainScreenSetup(self, option=None):
        print("todo")

    def show_popup(self, text):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText(text)
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

        

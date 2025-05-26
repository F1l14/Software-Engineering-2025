from src.Screen.Setup.UserCreationScreen import UserCreationScreen
from src.Class.DBManager import DBManager
from src.Class.Admin import Admin
from src.Screen.Setup.BusinessCreationScreen import BusinessCreationScreen
from src.Screen.Setup.DepartmentCreationScreen import DepartmentCreationScreen
from src.Screen.Setup.UserImportScreen import UserImportScreen
from src.Screen.Setup.UsersListScreen import UsersListScreen
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtWidgets import QCheckBox
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidgetItem, QComboBox

import json

class ManageSetupClass:
    def __init__(self):
        self.user_creation_screen = UserCreationScreen()
        self.user_creation_screen.manage = self
        self.user_creation_screen.display()

        self.__db = DBManager()
        
        self.__users_file = None
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
        self.business_creation_screen.manage = self
        self.business_creation_screen.display()

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
        self.department_creation_screen.manage = self
        self.department_creation_screen.display()
        self.business_creation_screen.close()

        

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
        self.user_import_screen.manage = self
        self.user_import_screen.display()
        self.department_creation_screen.close()

        

    def importUsers(self):
        filename = QFileDialog.getOpenFileName(self.business_creation_screen, "Select JSON", "", "JSON Files (*.json)")
        if filename[0]:
            self.user_import_screen.file_label.setText(filename[0])
            return filename[0]
        else:
            self.show_popup("No file selected.")
            self.user_import_screen.file_label.clear()

    def processUsers(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                
                data = json.load(f) 
                self.usersListSetup()
                self.populateList(data)

        except json.JSONDecodeError as e:
            self.show_popup(f"Invalid JSON: {str(e)}")
        except Exception as e:
            self.show_popup(f"Error reading file: {str(e)}")


    def usersListSetup(self):
        self.user_import_screen.hide()
        self.users_list_screen = UsersListScreen()
        self.users_list_screen.manage = self
        self.users_list_screen.display()
        self.user_import_screen.close()


    def populateList(self, data):
        departments = self.__db.queryDepartments()
        
        
        if departments == "Error":
            self.show_popup("DB ERROR")
            return
        flat_departments = [item[0] for item in departments]
        # print(flat_departments)

        self.users_list_screen.tableWidget.setRowCount(len(data))
        self.users_list_screen.tableWidget.setColumnCount(5)
        self.users_list_screen.tableWidget.setHorizontalHeaderLabels(["First Name", "Last Name", "Username", "Department", "Manager"])



        for i, user in enumerate(data):
            # Username (read-only)

            firstname = QTableWidgetItem(user["firstname"])
            firstname.setFlags(firstname.flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.users_list_screen.tableWidget.setItem(i, 0, firstname)

            lastname = QTableWidgetItem(user["lastname"])
            lastname.setFlags(lastname.flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.users_list_screen.tableWidget.setItem(i, 1, lastname)

            username = QTableWidgetItem(user["username"])
            username.setFlags(username.flags() & ~Qt.ItemFlag.ItemIsEditable)
            username.setData(Qt.ItemDataRole.UserRole, user["password"])
            self.users_list_screen.tableWidget.setItem(i, 2, username)

            # Role combobox
            combo = QComboBox()
            combo.addItems(flat_departments)
            self.users_list_screen.tableWidget.setCellWidget(i, 3, combo)


            
            role = QCheckBox()
            self.users_list_screen.tableWidget.setCellWidget(i, 4, role)

    def saveUsers(self):
        role = None
        for row in range(self.users_list_screen.tableWidget.rowCount()):
            firstname = self.users_list_screen.tableWidget.item(row, 0).text()
            lastname = self.users_list_screen.tableWidget.item(row, 1).text()
            username = self.users_list_screen.tableWidget.item(row, 2).text()
            password = self.users_list_screen.tableWidget.item(row, 2).data(Qt.ItemDataRole.UserRole)
            department = self.users_list_screen.tableWidget.cellWidget(row, 3).currentText()
            is_manager = self.users_list_screen.tableWidget.cellWidget(row, 4).isChecked()

            if not firstname or not lastname or not username:
                self.show_popup("All fields are required.")
                return

           
            if is_manager:
                role = "manager"
            else:
                role = "employee"

            print(f"Saving user: {firstname} {lastname}, Username: {username}, Department: {department}, Role: {role}")
            msg = self.__db.createUser(username, password, firstname, lastname, role, department)
            if msg != "OK":
                self.show_popup(msg)
                return
        
        self.show_popup("Users saved successfully.")
        self.finishSetup()


    def finishSetup(self):
        import sys
        from PyQt6.QtWidgets import QApplication
        from src.Manage.ManageWelcomeClass import ManageWelcomeClass
        self.users_list_screen.hide()
        self.users_list_screen.close()
        # self.welcome_class = ManageWelcomeClass()

    def show_popup(self, text):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText(text)
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

        

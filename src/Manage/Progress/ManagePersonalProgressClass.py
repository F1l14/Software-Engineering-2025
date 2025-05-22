from src.Screen.Progress.PersonalProgressScreen import PersonalProgressScreen
from src.Class.DBManager import DBManager
class ManagePersonalProgressClass:
    def __init__(self, username, first_name, last_name, department):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        
        self.personal_screen = PersonalProgressScreen()
        self.personal_screen.manage = self
        self.personal_screen.display()

    def getData(self):
        db = DBManager()
        data = db.queryEmployeeProgress(self.username)
        return data
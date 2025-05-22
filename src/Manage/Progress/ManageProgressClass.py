from src.Screen.Progress.ProgressScreen import ProgressScreen
from src.Class.DBManager import DBManager
class ManageProgressClass:
    def __init__(self):
        self.progress_screen = ProgressScreen()
        self.progress_screen.manage = self
        self.progress_screen.createBusinessGraph()
        self.progress_screen.display()
        
    def getData(self):
        db = DBManager()
        data = db.queryBusinessData()
        return data
    
    def getEmployeeData(self):
        db = DBManager()
        data = db.queryAllEmployees()
        return data
    
    def filterTable(self, text):
        table = self.progress_screen.employeeTable
        for row in range(table.rowCount()):
            match = False
            for col in range(table.columnCount()):
                item = table.item(row, col)
                if item and text.lower() in item.text().lower():
                    match = True
                    break
            table.setRowHidden(row, not match)

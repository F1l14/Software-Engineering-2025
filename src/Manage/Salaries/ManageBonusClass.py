#from src.Screen.Salaries.EmployeePercentScreen import EmployeePercentScreen
from src.Screen.Salaries.BonusSetupScreen import BonusSetupScreen
#from src.Screen.Salaries.BonusBoardScreen import BonusBoardScreen
from src.Class.DBManager import DBManager

class ManageBonusClass:
    def __init__(self):
        #self.employeePercent_screen = EmployeePercentScreen()
        self.bonusSetup_screen = BonusSetupScreen()
        #self.bonusBoard_screen = BonusBoardScreen()
        self.employeePercent_screen.manage = self
        self.bonusSetup_screen.manage = self
        self.bonusBoard_screen.manage = self

        BonusState = self.getBonusState()
        if BonusState == "active" :
            self.bonusBoard_screen.display()
        else :
            self.bonusSetup_screen.display()

    def getBonusState(self):
        db = DBManager()
        BonusState = db.checkBonusState()
        return BonusState
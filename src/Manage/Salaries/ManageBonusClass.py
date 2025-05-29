from PyQt6.QtWidgets import QMessageBox
from src.Screen.Salaries.BonusSetupScreen import BonusSetupScreen
from src.Screen.Salaries.BonusBoardScreen import BonusBoardScreen
from src.Class.DBManager import DBManager

class ManageBonusClass:
    def __init__(self):
        self.bonusSetup_screen = BonusSetupScreen()
        self.bonusBoard_screen = BonusBoardScreen()
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
    
    def saveBonusDetails(self, badget_numbers, perc1, perc2):
        db = DBManager()
        message = db.createBonusDetails(badget_numbers, perc1, perc2)
        print(message)
        try:
            self.bonusBoard_screen.display()
        except Exception as e:
            import traceback
            traceback.print_exc()
            QMessageBox.critical(None, "Error", f"Error during display: {repr(e)}")


    def getBonusBoardDetails(self):
        db = DBManager()
        return db.queryBonusBoardDetails()
        
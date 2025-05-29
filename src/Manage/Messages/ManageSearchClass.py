from src.Screen.Messages.SearchReceiverScreen import SearchReceiverScreen
from src.Class.DBManager import DBManager

class ManageSearchClass:
    def __init__(self):
        self.search_screen = SearchReceiverScreen()
        self.search_screen.manageSearch = self

    def display(self):
        self.search_screen.show()

    def searchReceiver(self):
        if self.search_screen.nameRadioButton.isChecked():
            keyword = self.search_screen.searchBar.text().strip()
            db = DBManager()  # Δημιουργία αντικειμένου
            results = db.queryReceiver(keyword)  # Σωστή κλήση instance method

        elif self.search_screen.tagRadioButton.isChecked():
            tag = self.search_screen.filterComboBox.currentText()
            results = DBManager.queryReceiverTag(tag)

        self.search_screen.showReceiver(results)

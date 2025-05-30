from src.Screen.Messages.SearchReceiverScreen import SearchReceiverScreen
from src.Class.DBManager import DBManager
from src.Manage.Messages.ManageChatClass import ManageChatClass
from src.Class.Session import Session

class ManageSearchClass:
    def __init__(self):
        self.search_screen = SearchReceiverScreen()
        self.search_screen.manageSearch = self

    def display(self):
        self.search_screen.show()

    def searchReceiver(self):
        if self.search_screen.nameRadioButton.isChecked():
            keyword = self.search_screen.searchBar.text().strip()
            results = DBManager().queryReceiver(keyword) 

        elif self.search_screen.tagRadioButton.isChecked():
            tag = self.search_screen.filterComboBox.currentText()
            results = DBManager().queryReceiverTag(tag)
        self.search_screen.showReceiver(results)

    def showChat(self):
        selected_item = self.search_screen.showResultList.currentItem()
        if not selected_item:
            return

        username = selected_item.text().split('(')[-1][:-1]  # Παίρνει το username από το (username)

        user_info = DBManager().get_user_by_username(username) 
        if user_info:
            current_user = Session.getUser()
            self.chat_manager = ManageChatClass(current_user, user_info)
            self.chat_manager.display()
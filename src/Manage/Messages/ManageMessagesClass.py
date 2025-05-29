from src.Screen.Messages.MessagesScreen import MessagesScreen
from src.Class.DBManager import DBManager
from src.Class.Session import Session
from src.Manage.Messages.ManageSearchClass import ManageSearchClass


class ManageMessagesClass:
    def __init__(self):
        self.message_screen = MessagesScreen()
        self.message_screen.manage = self  # Ανάθεση ελέγχου

        self.message_screen.display()

    def getMessages(self):
        db = DBManager()
        self.username = Session.getUser()
        return db.queryMessages(self.username)

    def newChat(self):
        self.search_manager = ManageSearchClass()
        self.search_manager.display()
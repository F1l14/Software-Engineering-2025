from src.Screen.Messages.MessagesScreen import MessagesScreen
from src.Class.DBManager import DBManager

class ManageMessagesClass:
    def __init__(self):
        self.message_screen = MessagesScreen()
        self.message_screen.manage = self  # Ανάθεση ελέγχου

        self.message_screen.display()

    def getUserChats(self):
        db = DBManager()
        user_email = "user@example.com"  #θα αλλάζει ανά session
        return db.queryUserChats(user_email)

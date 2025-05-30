from src.Screen.Messages.ChatScreen import ChatScreen
from src.Class.DBManager import DBManager
from datetime import datetime

class ManageChatClass:
    def __init__(self, current_user, receiver):
        self.current_user = current_user
        self.receiver = receiver
        self.db = DBManager()
        self.chat_screen = ChatScreen()
        self.chat_screen.manageChat = self

        self.chat_screen.setReceiverInfo(f"{receiver['firstname']} {receiver['lastname']}")
        self.chat_id = self.get_or_create_chat()
        self.loadMessages()

    def display(self):
        self.chat_screen.show()

    def get_or_create_chat(self):
        chat_id = self.db.get_chat_id(self.current_user, self.receiver['username'])
        if chat_id:
            return chat_id
        name = f"Συνομιλία {self.current_user} και {self.receiver['username']}"
        return self.db.create_chat(name, self.current_user, self.receiver['username'])

    def loadMessages(self):
        history = self.db.get_chat_history(self.chat_id)
        for msg in history:
            self.chat_screen.appendMessage(msg['message'], msg['from'])

    def createMessage(self, text):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        new_msg = {
            "from": self.current_user,
            "to": self.receiver['username'],
            "message": text,
            "timestamp": timestamp
        }
        self.db.insert_message(self.chat_id, new_msg)
        self.chat_screen.appendMessage(text, self.current_user)
        self.chat_screen.clearInput()

from PyQt6.QtWidgets import QMainWindow, QListWidget, QPushButton, QLabel
from PyQt6 import uic
from src.Class.Session import Session

class MessagesScreen(QMainWindow):
    def __init__(self):
        super().__init__()

    def display(self):
        uic.loadUi("ui/4_Messages/MessagesScreen.ui", self)

        # Σύνδεση UI αντικειμένων
        self.messagesList = self.findChild(QListWidget, "messagesList")
        self.newChatButton = self.findChild(QPushButton, "newChatButton")
        self.messagesLabel = self.findChild(QLabel, "messagesLabel")

        self.newChatButton.clicked.connect(self.newChat)

        # Δημιουργεί δυναμική λίστα συνομιλιών
        self.showMessages()

        self.show()

    def newChat(self):
        self.manage.newChat()

    def showMessages(self):
        messages = self.manage.getMessages()  #σύνδεση με DBManager
        current_user = Session.getUser()
        self.messagesList.clear()

        for chat in messages:
            other_user = chat["user_2"] if chat["user_1"] == current_user else chat["user_1"]
            display_name = f"{chat['name']} ({other_user})"
            self.messagesList.addItem(display_name)

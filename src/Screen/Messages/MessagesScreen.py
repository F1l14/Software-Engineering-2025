from PyQt6.QtWidgets import QDialog, QListWidget, QPushButton, QLabel
from PyQt6 import uic

class MessagesScreen(QDialog):
    def __init__(self):
        super().__init__()

    def display(self):
        uic.loadUi("src/ui/4_Messages/MessagesScreen.ui", self)

        # Σύνδεση UI αντικειμένων
        self.messagesList = self.findChild(QListWidget, "messagesList")
        self.newChatButton = self.findChild(QPushButton, "newChatButton")
        self.messagesLabel = self.findChild(QLabel, "messagesLabel")

        self.newChatButton.clicked.connect(self.handleNewChat)

        # Δημιουργεί δυναμική λίστα συνομιλιών
        self.showMessages()

        self.exec()

    def handleNewChat(self): #newChatSelect(self)
        print("Ο χρήστης πάτησε 'Νέα Συνομιλία'")
        # Εδώ μπορεί να ανοίξει νέο παράθυρο για δημιουργία συνομιλίας

    def showMessages(self):
        messages = self.manage.getUserChats()  #σύνδεση με DBManager
        self.messagesList.clear()

        for chat in messages:
            display_name = f"{chat['name']} ({chat['user_1']} - {chat['user_2']})"
            self.messagesList.addItem(display_name)

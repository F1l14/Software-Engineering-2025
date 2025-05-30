from PyQt6.QtWidgets import QMainWindow, QLabel, QTextBrowser, QTextEdit, QPushButton
from PyQt6 import uic

class ChatScreen(QMainWindow):
    def __init__(self):
        super().__init__()

    def display(self):
        uic.loadUi("ui/4_Messages/ChatScreen.ui", self)

        self.receiverNameLabel = self.findChild(QLabel, "receiverNameLabel2")
        self.chatHistoryWidget = self.findChild(QTextBrowser, "chatHistoryTextBrowser")
        self.messageTextEdit = self.findChild(QTextEdit, "messageTextEdit")
        self.sendButton = self.findChild(QPushButton, "sendButton")

        self.sendButton.clicked.connect(self.onSendClicked)

        self.manageChat = None  

    def setReceiverInfo(self, full_name):
        self.receiverNameLabel.setText(full_name)

    def appendMessage(self, message, sender):
        self.chatHistoryWidget.append(f"<b>{sender}:</b> {message}<br>")

    def clearInput(self):
        self.messageTextEdit.clear()

    def onSendClicked(self):
        text = self.messageTextEdit.toPlainText().strip()
        if text and self.manageChat:
            self.manageChat.createMessage(text)
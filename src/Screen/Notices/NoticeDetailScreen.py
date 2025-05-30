from PyQt6.QtWidgets import QMainWindow, QLabel
from PyQt6 import uic
from src.Class.DBManager import DBManager

class NoticeDetailScreen(QMainWindow):
    def __init__(self, notice_id):
        super().__init__()
        self.notice_id = notice_id

    def display(self):
        uic.loadUi("ui/10_Notices/NoticeDetailScreen.ui", self)

        self.titleLabel = self.findChild(QLabel, "titleLabel")
        self.typeLabel = self.findChild(QLabel, "typeLabel")
        self.createdLabel = self.findChild(QLabel, "createdLabel")
        self.bodyLabel = self.findChild(QLabel, "bodyLabel")

        self.loadNotice()
        self.show()

    def loadNotice(self):
        db = DBManager()
        cursor = db.conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT title, type, created, body FROM notices WHERE id = %s", (self.notice_id,))
            notice = cursor.fetchone()
            if notice:
                self.titleLabel.setText(notice["title"])
                self.typeLabel.setText(notice["type"])
                self.createdLabel.setText(notice["created"].strftime("%Y-%m-%d %H:%M"))
                self.bodyLabel.setText(notice["body"])
        finally:
            cursor.close()

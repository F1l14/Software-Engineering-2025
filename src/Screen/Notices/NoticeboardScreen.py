from PyQt6.QtWidgets import QMainWindow, QListWidget, QPushButton, QLabel, QListWidgetItem
from PyQt6.QtCore import Qt
from PyQt6 import uic

class NoticeboardScreen(QMainWindow):
    def __init__(self):
        super().__init__()

    def display(self):
        uic.loadUi("ui/10_Notices/NoticeboardScreen.ui", self)

        # Σύνδεση UI αντικειμένων
        self.noticeboardListWidget = self.findChild(QListWidget, "noticeboardListWidget")
        self.newNoticeButton = self.findChild(QPushButton, "newNoticeButton")
        self.noticeboardLabel = self.findChild(QLabel, "noticeboardLabel")
        #self.item = self.findChild(QLabel, "noticeboardLabel")


        self.newNoticeButton.clicked.connect(self.postNewNotice)

        # Δημιουργεί δυναμική λίστα συνομιλιών
        self.showAvailableNotices()
        self.noticeboardListWidget.itemClicked.connect(self.openNoticeDetail)

        self.show()

    def postNewNotice(self):
        self.manage.postNewNotice()

    def showAvailableNotices(self):
        notices = self.manage.getNotices()
        self.noticeboardListWidget.clear()

        for notice in notices:
            title = notice["title"]
            notice_type = notice["type"]
            created = notice["created"].strftime("%Y-%m-%d %H:%M")
            notice_id = notice["id"]

            display_text = f"[{notice_type}] {title} — {created}"

            item = QListWidgetItem(display_text)
            item.setData(Qt.ItemDataRole.UserRole, notice_id)  # Αποθήκευση id μέσα στο item
            self.noticeboardListWidget.addItem(item)


    def openNoticeDetail(self, item):
        notice_id = item.data(Qt.ItemDataRole.UserRole)
        self.manage.openNoticeDetail(notice_id)


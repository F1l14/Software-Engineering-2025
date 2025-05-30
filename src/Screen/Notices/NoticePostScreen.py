from PyQt6.QtWidgets import QMainWindow, QTextEdit, QPushButton, QLabel, QMessageBox, QComboBox
from PyQt6 import uic
from src.Class.DBManager import DBManager

class NoticePostScreen(QMainWindow):
    def __init__(self):
        super().__init__()

    def display(self):
        uic.loadUi("ui/10_Notices/NoticePostScreen.ui", self)

        # Σύνδεση UI αντικειμένων
        self.postNoticeTextEdit = self.findChild(QTextEdit, "postNoticeTextEdit")
        self.postNoticeButton = self.findChild(QPushButton, "postNoticeButton")
        self.postNoticeLabel = self.findChild(QLabel, "postNoticeLabel")
        self.noticeboardListWidget = self.findChild(QTextEdit, "noticeboardListWidget")
        self.titleTextEdit = self.findChild(QTextEdit, "titleTextEdit")
        self.bodyTextEdit = self.findChild(QTextEdit, "bodyTextEdit")
        self.typeComboBox = self.findChild(QComboBox, "typeComboBox")
        self.titleLabel = self.findChild(QLabel, "titleLabel")
        self.typeLabel = self.findChild(QLabel, "typeLabel")
        self.bodyLabel = self.findChild(QLabel, "bodyLabel")

        self.postNoticeButton.clicked.connect(self.createNotice)

        self.show()

    def createNotice(self):
        title = self.titleTextEdit.toPlainText().strip()
        body = self.bodyTextEdit.toPlainText().strip()
        notice_type = self.typeComboBox.currentText().strip()  # 'business', 'department', 'team'

        if not title or not body or not notice_type:
            QMessageBox.warning(self, "Σφάλμα", "Συμπληρώστε όλα τα πεδία.")
            return

        db = DBManager()
        try:
            db.insertNotice(notice_type, title, body)
            QMessageBox.information(self, "Επιτυχία", "Η ανακοίνωση αναρτήθηκε με επιτυχία.")
            self.close()
            self.manage.notice_screen.showAvailableNotices()
        except Exception as e:
            QMessageBox.critical(self, "Σφάλμα", f"Απέτυχε η ανάρτηση: {e}")

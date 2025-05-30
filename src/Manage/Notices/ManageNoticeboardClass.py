from src.Screen.Notices.NoticeboardScreen import NoticeboardScreen
from src.Class.DBManager import DBManager
from src.Screen.Notices.NoticePostScreen import NoticePostScreen


class ManageNoticeboardClass:
    def __init__(self):
        self.notice_screen = NoticeboardScreen()
        self.notice_screen.manage = self  # Ανάθεση ελέγχου

        self.notice_screen.display()

    def getNotices(self):
        db = DBManager()
        return db.queryAvailableNotices()

    def postNewNotice(self):
        self.notice_post_screen = NoticePostScreen()
        self.notice_post_screen.manage = self
        self.notice_post_screen.display()

    def openNoticeDetail(self, notice_id):
        from src.Screen.Notices.NoticeDetailScreen import NoticeDetailScreen

        # Δημιουργία και προβολή οθόνης λεπτομερειών
        self.notice_detail_screen = NoticeDetailScreen(notice_id)
        self.notice_detail_screen.display()

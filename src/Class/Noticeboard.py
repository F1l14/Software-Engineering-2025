class Noticeboard:
    def __init__(self):
        pass
    def getNoticeboard(self, team_space_id):
        from src.Class.DBManager import DBManager
        db = DBManager()
        return db.queryNoticeboard(team_space_id)
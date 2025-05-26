from src.Class.DBManager import DBManager
class Calendar:
    def __init__(self):
        pass
    def getCalendar(self, team_space_id):
        db = DBManager()
        db.queryEvents(team_space_id)
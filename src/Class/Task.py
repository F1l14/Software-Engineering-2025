from src.Class.DBManager import DBManager
class Task:
    def __init__(self, name=None, assigned_to=None):
        self.__name = name
        self.__assigned_to = assigned_to
        self.__state = "pending"
    
    def getTasks(self, team_space_id):
        db = DBManager()
        return db.queryTasksOfTeam(team_space_id)
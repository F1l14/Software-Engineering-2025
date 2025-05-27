from src.Class.DBManager import DBManager

class Session:
    _user = None
    _role = None

    @classmethod
    def setUser(cls, username):
        cls._user = username
        cls.classifyUser()

    @classmethod

    def getUser(cls):
        return cls._user

    @classmethod
    def clear(cls):
        cls._user = None
        
    @classmethod
    def classifyUser(cls):
        if cls._user is None:
            return
        db = DBManager()
        cls._role = db.classifyUser(cls._user)
        print(f"User {cls._user} classified as {cls._role}")
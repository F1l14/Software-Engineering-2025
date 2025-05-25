from src.Class.User import User

class Session:
    _user = None

    @classmethod
    def setUser(cls, username):
        cls._user = username

    @classmethod
    def getUser(cls) -> User:
        return cls._user

    @classmethod
    def clear(cls):
        cls._user = None
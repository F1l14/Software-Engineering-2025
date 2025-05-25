from src.Class.User import User
class Admin(User):
    def __init__(self, username, firstname, lastname):
        super().__init__(username, firstname, lastname)
    
    def createUser(self, db, username, password, firstname, lastname):
        return db.createUser(username, password, firstname, lastname)

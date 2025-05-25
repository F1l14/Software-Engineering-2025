from src.Class.User import User
class Admin(User):
    def __init__(self, username, firstname, lastname):
        super().__init__(username, firstname, lastname)

    def createBusiness(self, db, name, owner, logo):
        return db.createBusiness(name, owner, logo)
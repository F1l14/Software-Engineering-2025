from src.Class.User import User
class Admin(User):
    def __init__(self, username):
        super().__init__(username)

    def createBusiness(self, db, name, owner, logo):
        return db.createBusiness(name, owner, logo)

    def createDepartment(self, db, name):
        return db.createDepartment(name)
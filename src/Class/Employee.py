from src.Class import User
class Employee(User):
    def __init__(self, username, firstname, lastname):
        super().__init__(username, firstname, lastname)
        self.__team = None
        self.__department = None
        self.__business = None

    def __str__(self):
        return f"Employee({self.username}, {self.firstname}, {self.lastname})"

    def getTeam(self, db):
        if self.__team is None:
            self.__team = db.queryTeam(self.username)
        return self.__team

    def getDepartment(self, db):
        if self.__department is None:
            self.__department = db.queryDepartment(self.username)
        return self.__department
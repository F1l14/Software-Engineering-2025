from src.Class import User
class Leader(User):
    def __init__(self, username, firstname, lastname):
        super().__init__(username, firstname, lastname)
        self.__team = None
        self.__department = None
        self.__business = None

    def __str__(self):
        return f"Leader({self.username}, {self.firstname}, {self.lastname})"
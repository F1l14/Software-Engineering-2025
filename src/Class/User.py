class User:
    def __init__(self, username, firstname, lastname):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname

    # def __str__(self):
    #     return f"User({self.username}, {self.firstname}, {self.lastname})"
    
    def getTasks(self, db, option):
        return db.queryTasks(employee=self.username, option=option)
        
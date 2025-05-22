class Task:
    def __init__(self, name, assigned_to=None):
        self.__name = name
        self.__assigned_to = assigned_to
        self.__state = "pending"
    
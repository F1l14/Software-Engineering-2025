from src.Class.FileSystem import FileSystem
class Team:
    def __init__(self, team_id):
        self.team_id = team_id
    
    def getTeamDirectory(self):
        return FileSystem().queryTeamDirectory(self.team_id)

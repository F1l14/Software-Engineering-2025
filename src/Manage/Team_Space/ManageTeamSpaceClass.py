from src.Screen.Team_Space.TeamSpaceScreen import TeamSpaceScreen
from src.Class.Task import Task
# from src.Class.Calendar import Calendar
# from src.Class.Noticeboard import Noticeboard
from src.Manage.Team_Space.ManageFileShareClass import ManageFileShareClass
class ManageTeamSpaceClass:
    def __init__(self, team_space_id):
        self.team_space_id = team_space_id
        team_space_screen = TeamSpaceScreen()
        team_space_screen.manage = self
        task = Task()
        # calendar = Calendar()
        # noticeboard = Noticeboard()
        
        # noticeboardData = task.getNoticeboard(team_space_id)
        # calendarData = task.getCalendar(team_space_id)

        self.taskData = task.getTasks(team_space_id)
        
        team_space_screen.display(self.taskData)
        
    def showFileSharingScreen(self):
        ManageFileShareClass(self.team_space_id)

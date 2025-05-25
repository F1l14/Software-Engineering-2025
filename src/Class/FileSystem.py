from pathlib import Path

class FileSystem:
    def __init__(self):
        pass

    def queryTeamDirectory(self, team_id):
        dir_path = Path("FileSystem/TeamDirectories") / str(team_id)
        dir_path.mkdir(parents=True, exist_ok=True)  # Create directory if it doesn't exist
        return str(dir_path) + "/"
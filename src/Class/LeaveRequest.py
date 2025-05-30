class LeaveRequest:
    def __init__(self, username, start_date, end_date, reason):
        self.username = username
        self.start_date = start_date
        self.end_date = end_date
        self.reason = reason
        self.status = "Pending"
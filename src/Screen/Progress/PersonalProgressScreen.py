from PyQt6.QtWidgets import QDialog
from PyQt6 import uic

class PersonalProgressScreen(QDialog):
    def __init__(self):
        super().__init__()
    
    def display(self):
        uic.loadUi("ui/3_Progress/PersonalProgressScreen.ui", self)
        
        current_text1 = self.employeeFirstNameLabel.text()
        self.employeeFirstNameLabel.setText(current_text1 + ' ' + self.manage.employee.firstname)
        
        current_text2 = self.employeeLastNameLabel.text()
        self.employeeLastNameLabel.setText(current_text2 + ' ' + self.manage.employee.lastname)
        
        current_text3 = self.employeeDepartmentLabel.text()
        self.employeeDepartmentLabel.setText(current_text3 + ' ' + self.manage.department)
        
        self.progressData = self.manage.getData()
        self.showEmployeeProgress()
        
        self.exec()
        
    def showEmployeeProgress(self):        
        # Get project and task progress lists
        project_progress = self.progressData["projects"]
        task_progress = self.progressData["tasks"]

        # Initialize counts to 0 in case a status is missing
        projects_assigned_count = 0
        projects_completed_count = 0
        tasks_pending_count = 0
        tasks_completed_count = 0

        # Count projects by status
        for entry in project_progress:
            if entry['status'] == 'assigned':
                projects_assigned_count = entry['project_count']
            elif entry['status'] == 'completed':
                projects_completed_count = entry['project_count']

        # Count tasks by status
        for entry in task_progress:
            if entry['state'] == 'pending':
                tasks_pending_count = entry['task_count']
            elif entry['state'] == 'completed':
                tasks_completed_count = entry['task_count']

        # Update labels with the counts
        self.assignedProjectsLabel.setText(f"Assigned Projects: {projects_assigned_count}")
        self.completedProjectsLabel.setText(f"Completed Projects: {projects_completed_count}")
        self.assignedTasksLabel.setText(f"Assigned Tasks: {tasks_pending_count}")
        self.completedTasksLabel.setText(f"Completed Tasks: {tasks_completed_count}")
        
        
    def showEvaluationData(self):
        self.evaluationData = self.manage.getEmployeeEvaluations()
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
        
        self.exportButton.clicked.connect(self.exportButtonPushed)
        
        self.exec()
        
    def showEmployeeProgress(self):        
        # Get project and task progress lists
        project_progress = self.progressData["projects"]
        task_progress = self.progressData["tasks"]

        # Initialize counts to 0 in case a status is missing
        self.projects_assigned_count = 0
        self.projects_completed_count = 0
        self.tasks_pending_count = 0
        self.tasks_completed_count = 0

        # Count projects by status
        for entry in project_progress:
            if entry['status'] == 'assigned':
                self.projects_assigned_count = entry['project_count']
            elif entry['status'] == 'completed':
                self.projects_completed_count = entry['project_count']

        # Count tasks by status
        for entry in task_progress:
            if entry['state'] == 'pending':
                self.tasks_pending_count = entry['task_count']
            elif entry['state'] == 'completed':
                self.tasks_completed_count = entry['task_count']

        # Update labels with the counts
        self.assignedProjectsLabel.setText(f"Ολοκληρωμένα Project: {self.projects_assigned_count}")
        self.completedProjectsLabel.setText(f"Ανοιχτά Project: {self.projects_completed_count}")
        self.completedTasksLabel.setText(f"Ολοκληρωμένα Tasks: {self.tasks_completed_count}")
        self.assignedTasksLabel.setText(f"Ανοιχτά Tasks: {self.tasks_pending_count}")
        
        
    def showEvaluationData(self):
        self.evaluationData = self.manage.getEmployeeEvaluations()
        
    def exportButtonPushed(self):
        self.manage.export()
        
        
    def createExportFile(self):
        # Create a CSV file with the employee's progress data
        with open(f"{self.manage.employee.username}_progress.csv", "w") as file:
            file.write("Completed Projects, Pending Projects, Completed Tasks, Pending Tasks\n")
            file.write(f"{self.projects_completed_count}, {self.projects_assigned_count}, {self.tasks_completed_count}, {self.tasks_pending_count}\n")
                
        self.manage.showSuccessScreen()
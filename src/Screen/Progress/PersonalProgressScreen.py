from PyQt6.QtWidgets import QDialog
from PyQt6 import uic

class PersonalProgressScreen(QDialog):
    def __init__(self):
        super().__init__()
    
    def display(self):
        uic.loadUi("ui/3_Progress/PersonalProgressScreen.ui", self)
        
        current_text1 = self.employeeFirstNameLabel.text()
        self.employeeFirstNameLabel.setText(current_text1 + ' ' + self.manage.first_name)
        
        current_text2 = self.employeeLastNameLabel.text()
        self.employeeLastNameLabel.setText(current_text2 + ' ' + self.manage.last_name)
        
        current_text3 = self.employeeDepartmentLabel.text()
        self.employeeDepartmentLabel.setText(current_text3 + ' ' + self.manage.department)
        
        self.progressData = self.manage.getData()
        self.showEmployeeProgress()
        
        self.exec()
        
    def showEmployeeProgress(self):        
        # Initialize counts to 0 in case a status is missing
        assigned_count = 0
        completed_count = 0

        for entry in self.progressData:
            if entry['status'] == 'assigned':
                assigned_count = entry['project_count']
            elif entry['status'] == 'completed':
                completed_count = entry['project_count']

        # Update labels with the counts
        current_text1 = self.assignedProjectsLabel.text()
        current_text2 = self.completedProjectsLabel.text()
        self.assignedProjectsLabel.setText(current_text1 + ' ' + str(assigned_count))
        self.completedProjectsLabel.setText(current_text2 + ' ' + str(completed_count))
        
    def showEvaluationData(self):
        self.evaluationData = self.manage.getEmployeeEvaluations()
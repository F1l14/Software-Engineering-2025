from PyQt6.QtWidgets import QDialog
from PyQt6 import uic
import matplotlib.pyplot as plt

class ProgressScreen(QDialog):
    def __init__(self):
        super().__init__()
    
    def display(self):
        uic.loadUi("ui/3_Progress/ProgressScreen.ui", self)
        self.exec()
        
    def createBusinessGraph(self):
        self.graphData = self.manage.getData()

        # Unpack data
        months = [item[0] for item in self.graphData]
        project_counts = [item[1] for item in self.graphData]

        plt.figure(figsize=(8, 5))
        plt.bar(months, project_counts, color='skyblue')
        plt.xlabel('Month')
        plt.ylabel('Completed Projects')
        plt.title('Number of Completed Projects per Month')
        plt.tight_layout()
        plt.show()
from PyQt6.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout,
    QListWidget, QListWidgetItem, QPushButton, QLabel
)
import sys

class TaskItem(QWidget):
    def __init__(self, text, parent_list, list_item, task_id, user):
        super().__init__()

        self.parent_list = parent_list
        self.list_item = list_item
        self.task_id = task_id
        self.user = user

        # Layout for the custom task item
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        # Task text
        self.label = QLabel(text)
        layout.addWidget(self.label)

        # Delete button
        self.delete_btn = QPushButton("ok")
        self.delete_btn.clicked.connect(self.remove_item)
        layout.addWidget(self.delete_btn)

        self.setLayout(layout)

    def remove_item(self):
        current_row = self.parent_list.row(self.list_item)
        self.parent_list.takeItem(self.parent_list.row(self.list_item))
        self.user.completeTask(self.task_id)

        above_item = self.parent_list.item(current_row - 1)
        print(f"Above item: {above_item.__class__.__name__}")
        if above_item.__class__.__name__ != "TaskItem":
            self.parent_list.takeItem(current_row - 1)
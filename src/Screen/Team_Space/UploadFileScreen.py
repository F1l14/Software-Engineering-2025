from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QMessageBox


class UploadFileScreen(QDialog):
    def __init__(self, directory=None):
        super().__init__()
        self.directory = directory
        
    def display(self):
        uic.loadUi("ui/6_Team_Space/UploadFileScreen.ui", self)
        self.pushButton.clicked.connect(self.upload)
        self.toolButton.clicked.connect(self.selectFile)
        self.exec()

    def upload(self):
        file_path = self.lineEdit.text().strip()
        if not file_path:
            QMessageBox.information(self, "Error", "File path cannot be empty.")
            return
        
        self.manageUploadFile.upload(file_path, self.directory)
        self.close()

    def selectFile(self):
        from PyQt6.QtWidgets import QFileDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*)")
        if file_name:
            self.lineEdit.setText(file_name)
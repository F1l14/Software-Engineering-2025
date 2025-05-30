from PyQt6.QtWidgets import QMainWindow, QPushButton, QRadioButton, QLineEdit, QComboBox, QListWidget, QMessageBox
from PyQt6 import uic

class SearchReceiverScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/4_Messages/SearchReceiverScreen.ui", self)

        # Σύνδεση με τα widgets
        self.nameRadioButton = self.findChild(QRadioButton, "nameRadioButton")
        self.tagRadioButton = self.findChild(QRadioButton, "tagRadioButton")
        self.searchBar = self.findChild(QLineEdit, "searchBar")
        self.filterComboBox = self.findChild(QComboBox, "filterComboBox")
        self.searchButton = self.findChild(QPushButton, "searchButton")
        self.showResultList = self.findChild(QListWidget, "showResultList")
        self.createButton = self.findChild(QPushButton, "createButton")

        # Σύνδεση ενεργειών
        self.nameRadioButton.toggled.connect(self.updateInputFields)
        self.tagRadioButton.toggled.connect(self.updateInputFields)
        self.searchButton.clicked.connect(self.onSearchClicked)
        self.createButton.clicked.connect(self.onCreateClicked)

        # Αρχικές ρυθμίσεις
        self.searchBar.setEnabled(False)
        self.filterComboBox.setEnabled(False)
        self.createButton.setEnabled(False)

        self.manageSearch = None  

    def updateInputFields(self):
        if self.nameRadioButton.isChecked():
            self.searchBar.setEnabled(True)
            self.filterComboBox.setEnabled(False)
        elif self.tagRadioButton.isChecked():
            self.filterComboBox.setEnabled(True)
            self.searchBar.setEnabled(False)

    def onSearchClicked(self):
        if self.nameRadioButton.isChecked() and not self.searchBar.text().strip():
            QMessageBox.warning(self, "Σφάλμα", "Πληκτρολογήστε όνομα.")
            return
        if self.tagRadioButton.isChecked() and self.filterComboBox.currentIndex() == 0:
            QMessageBox.warning(self, "Σφάλμα", "Επιλέξτε tag.")
            return

        if self.manageSearch:
            self.manageSearch.searchReceiver()

    def showReceiver(self, results):
        self.showResultList.clear()

        if not results:
            self.showResultList.addItem("Ο χρήστης που αναζητείτε δεν βρέθηκε!")
            self.createButton.setEnabled(False)
            return

        for user in results:
            full_name = f"{user['firstname']} {user['lastname']}"
            username = user['username']
            item_text = f"{full_name} ({username})"
            self.showResultList.addItem(item_text)
        self.createButton.setEnabled(True)

    def onCreateClicked(self):
        if self.manageSearch:
            self.manageSearch.showChat()     

        



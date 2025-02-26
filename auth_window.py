from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QSizePolicy


class auth_window(QWidget):
    def __init__(self, cursor, db):
        super().__init__()
        self.setWindowTitle("User Authentication")
        self.resize(500, 700)

        self.username_label = QLabel("Username")
        self.password_label = QLabel("Password")
        self.username_box = QLineEdit()
        self.password_box = QLineEdit()
        self.password_box.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton("Login")
        self.register_button = QPushButton("Register")

        master_layout = QVBoxLayout()
        first_row = QHBoxLayout()
        first_col = QVBoxLayout()
        first_col.addWidget(self.username_label)
        first_col.addWidget(self.username_box)
        first_row.addLayout(first_col)

        second_row = QHBoxLayout()
        second_col = QVBoxLayout()
        second_col.addWidget(self.password_label)
        second_col.addWidget(self.password_box)
        second_row.addLayout(second_col)

        third_row = QHBoxLayout()
        third_col = QVBoxLayout()
        third_col.addWidget(self.login_button)
        third_col.addWidget(self.register_button)
        third_row.addLayout(third_col)

        master_layout.addLayout(first_row)
        master_layout.addLayout(second_row)
        master_layout.addLayout(third_row)
        master_layout.setContentsMargins(25, 25, 25, 25)
        master_layout.setSpacing(10)

        # ==============================================================================
        # This design should probably be done in a separate css file
        self.username_box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.password_box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.login_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.register_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.username_label.setMaximumHeight(30)
        self.password_label.setMaximumHeight(30)
        self.username_box.setMaximumHeight(30)
        self.password_box.setMaximumHeight(30)
        self.login_button.setMaximumHeight(40)
        self.register_button.setMaximumHeight(40)
        # ==============================================================================

        self.setLayout(master_layout)

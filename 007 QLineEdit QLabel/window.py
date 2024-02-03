from PySide6.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QPushButton, QLabel, QLineEdit, QFormLayout
from PySide6.QtCore import QSize

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # self.setFixedSize(QSize(500, 500))

        centralWidget = QWidget()
        layout = QVBoxLayout()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

        # add content to layout
        formLayout = QFormLayout()
        self.usernameEdit = QLineEdit()
        # self.usernameEdit.textChanged.connect(self.textChangedHandler)
        self.usernameEdit.editingFinished.connect(self.editingFinishedHandler)
        formLayout.addRow("User Name", self.usernameEdit)

        button = QPushButton("Press Me!")
        button.setMinimumHeight(50)

        self.feedbackLabel = QLabel()

        layout.addLayout(formLayout)
        layout.addWidget(button)
        layout.addWidget(self.feedbackLabel)
        
    
    def textChangedHandler(self, text):
        self.feedbackLabel.setText(text)

    def editingFinishedHandler(self):
        text = self.usernameEdit.text()
        self.feedbackLabel.setText(text)
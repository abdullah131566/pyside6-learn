from PySide6.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QPushButton
from PySide6.QtCore import QSize

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(QSize(500, 500))

        centralWidget = QWidget()
        layout = QVBoxLayout()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

        # add content to layout
        button = QPushButton("Press Me!")
        button.setMinimumHeight(50)
        layout.addWidget(button)
        
from PySide6.QtWidgets import QWidget, QMainWindow, QGridLayout, QVBoxLayout, QPushButton, QTextEdit, QSizePolicy
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
        gridLayout = QGridLayout()
        layout.addLayout(gridLayout)

        # some content for the grid
        textEdit = QTextEdit()
        textEdit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button1 = QPushButton("Button 1")
        button1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button2 = QPushButton("Button 2")
        button2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button3 = QPushButton("Button 3")
        button3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button3.setMaximumHeight(50)
        button4 = QPushButton("Button 4")
        button4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button4.setMaximumHeight(50)
        button5 = QPushButton("Button 5")
        button5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button5.setMaximumHeight(50)
        button6 = QPushButton("Button 6")
        button6.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button6.setMaximumHeight(50)

        # add content to grid
        gridLayout.addWidget(textEdit, 0, 0, 2, 3)
        gridLayout.addWidget(button1, 0, 3)
        gridLayout.addWidget(button2, 1, 3)
        gridLayout.addWidget(button3, 2, 0)
        gridLayout.addWidget(button4, 2, 1)
        gridLayout.addWidget(button5, 2, 2)
        gridLayout.addWidget(button6, 2, 3)
        
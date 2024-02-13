from PySide6.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QPushButton, QLabel
from PySide6.QtGui import QMouseEvent, QPixmap, QPainter, QColor, QPen, QFont
from PySide6.QtCore import QSize, Qt

import random as rd

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(QSize(500, 500))

        centralWidget = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

        # add content to layout
        self.pixmapHolder = QLabel()
        canvas = QPixmap(QSize(400, 350))
        canvas.fill(QColor("white"))
        self.pixmapHolder.setPixmap(canvas)
        layout.addWidget(self.pixmapHolder)

        self.drawButton = QPushButton("Draw")
        # self.drawButton.clicked.connect(self.drawSomething)
        self.drawButton.clicked.connect(self.drawText)
        layout.addWidget(self.drawButton)

        # self.drawSomething()

    def drawSomething(self):
        canvas = self.pixmapHolder.pixmap()
        painter = QPainter(canvas)
        pen = QPen(QColor(255, 0, 80), 1.5)
        painter.setPen(pen)
        # painter.drawLine(0, 0, 400, 350)
        # painter.drawPoint(50, 100)
        for i in range(0, 10000):
            x = rd.randrange(-199, 200) + 200
            y = rd.randrange(-174, 175) + 175
            painter.drawPoint(x, y)
        painter.end()
        self.pixmapHolder.setPixmap(canvas)
        # self.pixmapHolder.update()

    def drawText(self):
        canvas = self.pixmapHolder.pixmap()
        painter = QPainter(canvas)
        
        pen = QPen(QColor(150, 200, 10), 1.5)
        painter.setPen(pen)

        font = QFont("Robotto", 28, 200)
        font.setBold(True)
        painter.setFont(font)

        painter.drawText(70, 28, "Hello World!")
        painter.end()
        self.pixmapHolder.setPixmap(canvas)

    # def mouseMoveEvent(self, event: QMouseEvent) -> None:
    #     canvas = self.pixmapHolder.pixmap()
    #     painter = QPainter(canvas)
    #     painter.drawPoint(event.position())
    #     painter.end()
    #     self.pixmapHolder.setPixmap(canvas)
    #     return super().mouseMoveEvent(event)

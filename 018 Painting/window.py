from PySide6.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QPushButton, QLabel
from PySide6.QtGui import QMouseEvent, QPixmap, QPainter, QColor, QPen, QFont
from PySide6.QtCore import QSize, Qt, Property

import random as rd

class PixmapCanvas(QLabel):
    def __init__(self, mouseMoveCb = None, width = 400, height = 400):
        super().__init__()
        pixmap = QPixmap(QSize(width, height))
        pixmap.fill(QColor("white"))
        self.setPixmap(pixmap)
        self.setFixedSize(QSize(width, height)) # for exact mouse capturing
        self.mouseMoveCb = mouseMoveCb if mouseMoveCb else lambda: None

    def mouseMoveEvent(self, ev: QMouseEvent) -> None:
        self.mouseMoveCb(ev)
        return super().mouseMoveEvent(ev)
    

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(QSize(500, 500))

        centralWidget = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

        self.lastX, self.lastY = None, None

        # add content to layout
        self.pixmapHolder = PixmapCanvas(self.drawOnMouse)
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

    def drawOnMouse(self, event: QMouseEvent) -> None:
        if not self.lastX:
            self.lastX = event.position().x()
            self.lastY = event.position().y()
            return
        
        canvas = self.pixmapHolder.pixmap()
        painter = QPainter(canvas)
        # painter.drawPoint(event.position())
        painter.drawLine(self.lastX, self.lastY, event.position().x(), event.position().y())
        painter.end()
        self.pixmapHolder.setPixmap(canvas)

        self.lastX = event.position().x()
        self.lastY = event.position().y()


    def mouseReleaseEvent(self, ev: QMouseEvent) -> None:
        self.lastX = None
        self.lastY = None
        return super().mouseReleaseEvent(ev)

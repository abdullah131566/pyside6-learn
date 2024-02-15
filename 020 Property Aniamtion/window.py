from PySide6.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QPushButton, QSizePolicy
from PySide6.QtCore import QSize, QPropertyAnimation, QPoint, QEasingCurve, QTimer

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(QSize(500, 500))

        centralWidget = QWidget()
        layout = QVBoxLayout()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

        # add content to layout
        self.box = QWidget()
        self.box.setFixedSize(50, 50)
        self.box.setStyleSheet("background-color:red;border-radius:15px;")
        layout.addWidget(self.box)
        
        self.box2 = QWidget()
        self.box2.resize(50, 50)
        self.box2.setStyleSheet("background-color:red;border-radius:15px;")
        layout.addWidget(self.box2)

        self.anim = QPropertyAnimation(self.box, b"pos")
        # self.anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.anim.setEasingCurve(QEasingCurve.Type.OutBounce)
        self.anim.setStartValue(QPoint(350, 0))
        self.anim.setEndValue(QPoint(350, 400))
        self.anim.setDuration(1500)
        
        self.anim2 = QPropertyAnimation(self.box2, b"podssas")
        # self.anim2.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.anim2.setEasingCurve(QEasingCurve.Type.OutBounce)
        self.anim2.setStartValue(QPoint(150, 0))
        self.anim2.setEndValue(QPoint(150, 400))
        self.anim2.setDuration(1500)
        
        self.anim3 = QPropertyAnimation(self.box2, b"size")
        # self.anim3.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.anim3.setEasingCurve(QEasingCurve.Type.InQuad)
        self.anim3.setStartValue(QSize(25, 25))
        self.anim3.setEndValue(QSize(75, 75))
        self.anim3.setDuration(300)

        self.timer = QTimer()
        self.timer.setInterval(2000)
        self.timer.timeout.connect(self.anim.start)
        self.timer.timeout.connect(self.anim2.start)
        self.timer.timeout.connect(self.anim3.start)
        self.timer.start()
        
        
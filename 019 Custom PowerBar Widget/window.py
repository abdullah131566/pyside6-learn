from PySide6.QtGui import QPaintEvent, QPainter, QColor
from PySide6.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QPushButton
from PySide6.QtCore import QSize, Qt, QRect
from powerbar_ui import Ui_Window
    

class Powerbar(QWidget, Ui_Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dialValueDisplay.setText(str(self.dial.value()))

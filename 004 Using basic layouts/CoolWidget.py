from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QPushButton, QSlider, QHBoxLayout, QVBoxLayout, QSizePolicy

class CoolWidget(QWidget):
  def __init__(self):
    super().__init__()

    button1 = QPushButton()
    button1.setText("&Press Me!")
    button1.setCheckable(True)
    button1.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
    
    button2 = QPushButton()
    button2.setText("&Press Me Too!")

    layout1 = QHBoxLayout()
    layout1.addWidget(button1, 2)
    layout1.addWidget(button2, 1)

    slider1 = QSlider()
    slider1.setOrientation(Qt.Vertical)
    slider1.setMinimum(0)
    slider1.setMaximum(100)
    slider1.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))

    slider2 = QSlider()
    slider2.setOrientation(Qt.Vertical)
    slider2.setMinimum(0)
    slider2.setMaximum(20)

    layout2 = QVBoxLayout()
    layout2.addWidget(slider1)
    layout2.addWidget(slider2, 2)

    layout3 = QVBoxLayout()
    layout3.addLayout(layout1)
    layout3.addLayout(layout2)

    self.setLayout(layout3)

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QPushButton, QSlider, QGridLayout

class ButtonHolder(QMainWindow):
  def __init__(self):
    super().__init__()

    window = super()
    
    button = QPushButton()
    button.setText("&Press Me!")
    button.setCheckable(True)
    button.clicked.connect(self.click_handler)

    slider = QSlider()
    slider.setOrientation(Qt.Horizontal)
    slider.setMinimum(0)
    slider.setMaximum(1)
    slider.setTickInterval(25)
    slider.setSingleStep(2)
    slider.valueChanged.connect(self.slider_change_handler)
    
    # window.setCentralWidget(button)
    window.setCentralWidget(slider)
  
  def click_handler(self, data):
    print("Handler ran with data, ", data)

  def slider_change_handler(self, data):
    print("Slider Changed, ", data)
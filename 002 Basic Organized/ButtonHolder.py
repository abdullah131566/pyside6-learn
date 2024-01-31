from PySide6.QtWidgets import QMainWindow, QPushButton

class ButtonHolder(QMainWindow):
  def __init__(self):
    super().__init__()

    window = super()
    
    button = QPushButton()
    button.setText("&Press Me!")
    window.setCentralWidget(button)
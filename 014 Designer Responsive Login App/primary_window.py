from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt, QSize

class MyPrimaryWindow(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My Application")
    self.setMinimumSize(QSize(900, 500))

    mainVLayout = QVBoxLayout()
    self.setLayout(mainVLayout)

    centralHeading = QLabel("The application")
    centralHeading.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
    mainVLayout.addWidget(centralHeading)
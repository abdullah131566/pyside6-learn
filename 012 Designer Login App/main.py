# main.py
from PySide6.QtWidgets import QApplication
import sys
from window import MyWindow

app = QApplication(sys.argv)

window = MyWindow()
window.show()

app.exec()
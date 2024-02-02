from PySide6.QtWidgets import QApplication
import sys

from window import MyWindow

app = QApplication(sys.argv)

window = MyWindow(app=app)
window.show()

app.exec()
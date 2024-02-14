from PySide6.QtWidgets import QApplication
import sys
from window import Powerbar

app = QApplication(sys.argv)

window = Powerbar()
window.show()

app.exec()
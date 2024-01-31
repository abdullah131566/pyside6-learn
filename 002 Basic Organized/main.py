from PySide6.QtWidgets import QApplication
from ButtonHolder import ButtonHolder

import sys

app = QApplication(sys.argv)

window = ButtonHolder()
window.show()

app.exec()
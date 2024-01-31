from PySide6.QtWidgets import QApplication
import sys
from CoolWidget import CoolWidget

app = QApplication(sys.argv)

window = CoolWidget()
window.show()

app.exec()
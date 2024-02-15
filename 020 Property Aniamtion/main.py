from PySide6.QtWidgets import QApplication
import sys
from window import MyWindow
from Switch import Switch

app = QApplication(sys.argv)

# window = MyWindow()
# window.show()
switch = Switch()
switch.show()

app.exec()

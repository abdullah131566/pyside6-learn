from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton
import sys

app = QApplication(sys.argv)

window = QMainWindow()

button = QPushButton()
button.setText("&Press Me!")
window.setCentralWidget(button)

window.show()
app.exec()
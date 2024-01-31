from PySide6.QtWidgets import QMainWindow, QMenu

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My Window")

    menubar = self.menuBar()

    fileMenu = menubar.addMenu("&File")
    quitAction = fileMenu.addAction("Quit")
    quitAction.triggered.connect(self.close)

    editMenu = menubar.addMenu("&Edit")
    editMenu.addAction("Copy")
    editMenu.addAction("Paste")
    editMenu.addAction("Delete")
    editMenu.addAction("Select")

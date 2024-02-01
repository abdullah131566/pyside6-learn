from PySide6.QtWidgets import QMainWindow, QApplication, QToolBar, QPushButton
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QAction

class MainWindow(QMainWindow):
  def __init__(self, app: QApplication):
    super().__init__()
    self.app = app

    self.setFixedSize(QSize(500, 500))
    self.setWindowTitle("My Window")

    menubar = self.menuBar()

    fileMenu = menubar.addMenu("&File")

    quitAction = QAction("Quit", self)
    quitAction.setStatusTip("Quit the Application")
    quitAction.triggered.connect(self.app.quit)
    fileMenu.addAction(quitAction)

    editMenu = menubar.addMenu("&Edit")
    editMenu.addAction("Copy")
    editMenu.addAction("Paste")
    editMenu.addAction("Delete")
    editMenu.addAction("Select")

    windowMenu = menubar.addMenu("&Window")
    searchMenu = menubar.addMenu("&Search")
    helpMenu = menubar.addMenu("&Help")
    
    toolbar = QToolBar()
    toolbar.setIconSize(QSize(15, 15))
    toolbar.setMovable(False)
    self.addToolBar(toolbar)
    toolbar.addAction(quitAction)

    cursorIcon = QIcon("C:/Users/User/Documents/DEV/python/001pyside6/005 QMainWindow Advance/cursor.png")
    cursorAction = toolbar.addAction(cursorIcon, "Cursor")
    cursorAction.setStatusTip("Cursor tool")
    cursorAction.setCheckable(True)
    cursorAction.triggered.connect(self.cursorSelection)

    toolbar.addSeparator()
    playButton = QPushButton(QIcon("C:/Users/User/Documents/DEV/python/001pyside6/005 QMainWindow Advance/play.webp"), "&Play")
    toolbar.addWidget(playButton)

  def cursorSelection(self):
    print("Cursor Selected")

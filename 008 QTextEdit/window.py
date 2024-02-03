from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox, QToolBar, QVBoxLayout, QPushButton, QTextEdit
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize

class MyWindow(QMainWindow):
    def __init__(self, app: QApplication):
        super().__init__()
        self.app = app
        self.textEdit = QTextEdit()

        # self.setFixedSize(QSize(500, 500))

        centralWidget = QWidget()
        centralWidgetLayout = QVBoxLayout()
        centralWidget.setLayout(centralWidgetLayout)
        self.setCentralWidget(centralWidget)

        # toolbar
        toolBar = QToolBar()
        toolBar.setMovable(False)
        self.addToolBar(toolBar)

        # add actions to toolbar
        copyButton = QPushButton("Copy")
        copyButton.setMinimumHeight(30)
        copyButton.clicked.connect(self.textEdit.copy)
        toolBar.addWidget(copyButton)

        cutButton = QPushButton("Cut")
        cutButton.setMinimumHeight(30)
        cutButton.clicked.connect(self.textEdit.cut)
        toolBar.addWidget(cutButton)

        pasteButton = QPushButton("Paste")
        pasteButton.setMinimumHeight(30)
        pasteButton.clicked.connect(self.textEdit.paste)
        toolBar.addWidget(pasteButton)

        undoButton = QPushButton("Undo")
        undoButton.setMinimumHeight(30)
        undoButton.clicked.connect(self.textEdit.undo)
        toolBar.addWidget(undoButton)

        redoButton = QPushButton("Redo")
        redoButton.setMinimumHeight(30)
        redoButton.clicked.connect(self.textEdit.redo)
        toolBar.addWidget(redoButton)

        clearButton = QPushButton("Clear")
        clearButton.setMinimumHeight(30)
        clearButton.clicked.connect(self.textEdit.clear)
        toolBar.addWidget(clearButton)

        closeButton = QPushButton(QIcon("C:/Users/Engineer Computers/Documents/dev/pyside6-learn/008 QTextEdit/cross.png"), " Close")
        closeButton.setIconSize(QSize(10, 10))
        closeButton.setMinimumHeight(30)
        closeButton.clicked.connect(self.confirmAndQuit)
        toolBar.addWidget(closeButton)
        
        # QTextEdit in the centre
        centralWidgetLayout.addWidget(self.textEdit)
    
    def confirmAndQuit(self):
        ret = QMessageBox.question(self, "Confirm Quit", "Are you sure you want to quit?",
                                   QMessageBox.Yes | QMessageBox.No,
                                   QMessageBox.Yes)
        if ret == QMessageBox.Yes:
            self.app.quit()

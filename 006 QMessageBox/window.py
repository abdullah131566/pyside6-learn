from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout, QMessageBox
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize

class MyWindow(QMainWindow):
    def __init__(self, app: QApplication):
        super().__init__()

        self.app = app

        # set window size
        self.setFixedSize(QSize(500, 500))

        # Initialize pushbuttons
        normalButton = QPushButton("Normal Way!")
        normalButton.setMinimumHeight(50)

        criticalButton = QPushButton("Critical")
        criticalButton.setMinimumHeight(50)

        warningButton = QPushButton("Warning")
        warningButton.setMinimumHeight(50)

        questionButton = QPushButton("Question")
        questionButton.setMinimumHeight(50)

        infoButton =QPushButton("Information")
        infoButton.setMinimumHeight(50)

        aboutButton = QPushButton("About")
        aboutButton.setMinimumHeight(50)

        closeButton = QPushButton(QIcon("C:/Users/Engineer Computers/Documents/dev/pyside6-learn/006 QMessageBox/cross.png"), " Close")
        closeButton.setIconSize(QSize(10, 10))
        closeButton.setMinimumHeight(50)

        # attach clicked signals to slots
        normalButton.clicked.connect(self.customMessageBox)
        criticalButton.clicked.connect(self.criticalMessageBox)
        warningButton.clicked.connect(self.warningMessageBox)
        questionButton.clicked.connect(self.questionMessageBox)
        infoButton.clicked.connect(self.informationMessageBox)
        aboutButton.clicked.connect(self.aboutMessageBox)
        closeButton.clicked.connect(self.closeConfirmationMessageBox)

        # Add buttons to a layout
        layout = QVBoxLayout()
        layout.addWidget(normalButton)
        layout.addWidget(criticalButton)
        layout.addWidget(warningButton)
        layout.addWidget(questionButton)
        layout.addWidget(infoButton)
        layout.addWidget(aboutButton)
        layout.addWidget(closeButton)

        # set the main-window central widget's layout to be this layout
        placeholderWidget = QWidget()
        placeholderWidget.setLayout(layout)
        self.setCentralWidget(placeholderWidget)


    def customMessageBox(self):
        messageBox = QMessageBox()
        messageBox.setMinimumSize(QSize(400, 200))
        messageBox.setWindowTitle("Custom Message Box")
        messageBox.setText("Made by Abdullah")
        messageBox.setInformativeText("This message box was made manually by Abdullah. The text, this information, icon and buttons were all set manually.")
        messageBox.setIcon(QMessageBox.Critical)
        messageBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Close)
        messageBox.setDefaultButton(QMessageBox.Ok)

        ret = messageBox.exec()
        if ret == QMessageBox.Ok:
            print("Ok pressed")
        else:
            print("Close pressed")

    def criticalMessageBox(self):
        ret = QMessageBox.critical(self, "My Application", "A critical message",
                             QMessageBox.Ok | QMessageBox.Cancel, 
                             QMessageBox.Ok)
        if ret == QMessageBox.Ok:
            print("Ok pressed")
        else:
            print("Close pressed")


    def warningMessageBox(self):
        ret = QMessageBox.warning(self, "My Application", "You are gonna die soon!",
                                  QMessageBox.Ok | QMessageBox.Ignore,
                                  QMessageBox.Ignore)
        if ret == QMessageBox.Ok:
            print("Ok pressed")
        else:
            print("Close pressed")
        

    def questionMessageBox(self):
        ret = QMessageBox.question(self, "MY Application", "Are you good?",
                             QMessageBox.Yes | QMessageBox.No,
                             QMessageBox.Yes)
        if ret == QMessageBox.Yes:
            print("Yes pressed")
        else:
            print("No pressed")
        
    
    def informationMessageBox(self):
        ret = QMessageBox.information(self, "My Application", "This is an information Message box",
                                      QMessageBox.Yes | QMessageBox.No,
                                      QMessageBox.Yes)
        if ret == QMessageBox.Yes:
            print("Yes pressed")
        else:
            print("No pressed")


    def aboutMessageBox(self):
        ret = QMessageBox.about(self, "My Application", "Hi! My name is Abdullah.")


    def closeConfirmationMessageBox(self):
        ret = QMessageBox.question(self, "My Application", "Are you sure you want to quit?",
                                   QMessageBox.Yes | QMessageBox.No,
                                   QMessageBox.Yes)
        if ret == QMessageBox.Yes:
            print("Yes pressed")
            self.app.quit()
        else:
            print("No pressed")
        
        
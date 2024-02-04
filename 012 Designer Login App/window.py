from PySide6.QtCore import QObject, QFile
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()

class MyWindow(QObject):
    def __init__(self):
        super().__init__()
        
        uiFile = QFile("C:/Users/Engineer Computers/Documents/dev/pyside6-learn/012 Designer Login App/loginform.ui")
        uiFile.open(QFile.ReadOnly)
        self.ui = loader.load(uiFile, None)
        uiFile.close()
        
        self.ui.loginButton.clicked.connect(self.loginHandler)


    def show(self):
        self.ui.show()

    
    def loginHandler(self):
        username = self.ui.usernameEdit.text()
        password = self.ui.passwordEdit.text()

        print("User Name:", username)
        print("Password:", password)
        
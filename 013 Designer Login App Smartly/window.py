from PySide6.QtWidgets import QWidget
from loginform_ui import Ui_Widget

class MyWindow(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.loginButton.clicked.connect(self.loginHandler)

    
    def loginHandler(self):
        username = self.usernameEdit.text()
        password = self.passwordEdit.text()

        print("User Name:", username)
        print("Password:", password)
        
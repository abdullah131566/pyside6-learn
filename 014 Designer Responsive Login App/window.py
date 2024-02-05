from PySide6.QtWidgets import QMainWindow, QDialog
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression

from interface_ui import Ui_MainWindow
from loading_dialog_ui import Ui_LoadingDialog
import time

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        userNameValidator = QRegularExpressionValidator()
        userNameValidator.setRegularExpression(QRegularExpression("[a-zA-Z]+"))
        self.usernameEdit.setValidator(userNameValidator)

        passwordValidator = QRegularExpressionValidator()
        passwordValidator.setRegularExpression(QRegularExpression("[a-zA-Z]+"))
        self.passwordEdit.setValidator(passwordValidator)

        self.usernameEdit.textChanged.connect(self.validateAndEnableLoginButton)
        self.passwordEdit.textChanged.connect(self.validateAndEnableLoginButton)

        self.loginButton.clicked.connect(self.login)
    
    # private function for checking if the username and password are valid
    def inputsAreValid(self):
        return self.usernameEdit.hasAcceptableInput() and self.passwordEdit.hasAcceptableInput()

    def validateAndEnableLoginButton(self):
        if self.inputsAreValid():
            self.loginButton.setEnabled(True)
        else:
            self.loginButton.setEnabled(False)


    def login(self):
        if not self.inputsAreValid():
            return
        
        # dialog = QDialog()
        # loadingDialog = Ui_LoadingDialog()
        # loadingDialog.setupUi(dialog)
        # dialog.show()
        # dialog.exec()
        print("Username: ", self.usernameEdit.text())
        print("Password: ", self.passwordEdit.text())
        # self.loginButton.setEnabled(False)
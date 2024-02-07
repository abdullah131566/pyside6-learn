from PySide6.QtWidgets import QMainWindow, QDialog, QMessageBox
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression

from primary_window import MyPrimaryWindow
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
        username = self.usernameEdit.text()
        password = self.passwordEdit.text()

        acceptedUsernames = ["abdullah", "admin", "superuser"]
        acceptedPasswords = ["123", "admin"]

        if username in acceptedUsernames and password in acceptedPasswords:
            self.primaryWindow = MyPrimaryWindow()
            self.primaryWindow.show()
            self.close()
        else:
            ret = QMessageBox.warning(self, "Invalid Credentials",
                                "Username or password is invalid.\nRetry with valid credentials.",
                                QMessageBox.Retry | QMessageBox.Close,
                                QMessageBox.Retry)
            if ret == QMessageBox.Close:
                self.close()
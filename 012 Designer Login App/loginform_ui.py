# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginform.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(400, 113)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.usernameLabel = QLabel(Widget)
        self.usernameLabel.setObjectName(u"usernameLabel")

        self.horizontalLayout.addWidget(self.usernameLabel)

        self.usernameEdit = QLineEdit(Widget)
        self.usernameEdit.setObjectName(u"usernameEdit")

        self.horizontalLayout.addWidget(self.usernameEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.passwordLabel = QLabel(Widget)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.horizontalLayout_2.addWidget(self.passwordLabel)

        self.passwordEdit = QLineEdit(Widget)
        self.passwordEdit.setObjectName(u"passwordEdit")

        self.horizontalLayout_2.addWidget(self.passwordEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.loginButton = QPushButton(Widget)
        self.loginButton.setObjectName(u"loginButton")

        self.verticalLayout.addWidget(self.loginButton)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Login - My Application", None))
        self.usernameLabel.setText(QCoreApplication.translate("Widget", u"User Name", None))
        self.passwordLabel.setText(QCoreApplication.translate("Widget", u"Password", None))
        self.loginButton.setText(QCoreApplication.translate("Widget", u"Login", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(600, 600)
        MainWindow.setMinimumSize(QSize(600, 600))
        MainWindow.setMaximumSize(QSize(600, 600))
        font = QFont()
        font.setFamilies([u"DejaVu Sans"])
        MainWindow.setFont(font)
        icon = QIcon(QIcon.fromTheme(u"address-book-new"))
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionClear = QAction(MainWindow)
        self.actionClear.setObjectName(u"actionClear")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(False)
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 2, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(25, 15, 25, 40)
        self.titleLabel = QLabel(self.widget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Black"])
        font1.setPointSize(24)
        font1.setBold(True)
        self.titleLabel.setFont(font1)
        self.titleLabel.setFrameShape(QFrame.NoFrame)
        self.titleLabel.setFrameShadow(QFrame.Plain)
        self.titleLabel.setScaledContents(False)
        self.titleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.titleLabel)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(12)
        self.usernameLabel = QLabel(self.widget)
        self.usernameLabel.setObjectName(u"usernameLabel")
        self.usernameLabel.setFocusPolicy(Qt.NoFocus)
        self.usernameLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.usernameLabel.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.gridLayout.addWidget(self.usernameLabel, 0, 0, 1, 1)

        self.usernameEdit = QLineEdit(self.widget)
        self.usernameEdit.setObjectName(u"usernameEdit")
        self.usernameEdit.setMinimumSize(QSize(200, 0))
        self.usernameEdit.setFocusPolicy(Qt.WheelFocus)
        self.usernameEdit.setMaxLength(100)

        self.gridLayout.addWidget(self.usernameEdit, 0, 1, 1, 1)

        self.passwordLabel = QLabel(self.widget)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.passwordLabel, 1, 0, 1, 1)

        self.passwordEdit = QLineEdit(self.widget)
        self.passwordEdit.setObjectName(u"passwordEdit")
        self.passwordEdit.setMinimumSize(QSize(200, 0))
        self.passwordEdit.setMaxLength(500)
        self.passwordEdit.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.passwordEdit, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.loginButton = QPushButton(self.widget)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setMinimumSize(QSize(0, 35))

        self.verticalLayout.addWidget(self.loginButton)


        self.gridLayout_2.addLayout(self.verticalLayout, 1, 1, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 117, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 0, 1, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(149, 276, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(251, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 1, 1, 2)

        self.horizontalSpacer = QSpacerItem(150, 276, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
        self.usernameLabel.setBuddy(self.usernameEdit)
        self.passwordLabel.setBuddy(self.passwordEdit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.usernameEdit, self.passwordEdit)
        QWidget.setTabOrder(self.passwordEdit, self.loginButton)

        self.retranslateUi(MainWindow)
        self.passwordEdit.returnPressed.connect(self.loginButton.click)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Login", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionClear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"Dashboard Login", None))
        self.usernameLabel.setText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.passwordLabel.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.loginButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi


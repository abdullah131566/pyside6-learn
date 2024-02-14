# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'powerbar.ui'
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
from PySide6.QtWidgets import (QApplication, QDial, QGridLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

from Bar import _Bar

class Ui_Window(object):
    def setupUi(self, Window):
        if not Window.objectName():
            Window.setObjectName(u"Window")
        Window.resize(177, 356)
        self.gridLayout = QGridLayout(Window)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dialValueDisplay = QLabel(Window)
        self.dialValueDisplay.setObjectName(u"dialValueDisplay")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setKerning(True)
        self.dialValueDisplay.setFont(font)
        self.dialValueDisplay.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.dialValueDisplay)

        self.powerbarWidget = _Bar(Window)
        self.powerbarWidget.setObjectName(u"powerbarWidget")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.powerbarWidget.sizePolicy().hasHeightForWidth())
        self.powerbarWidget.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.powerbarWidget)

        self.dial = QDial(Window)
        self.dial.setObjectName(u"dial")
        self.dial.setMaximum(100)
        self.dial.setValue(27)

        self.verticalLayout.addWidget(self.dial)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Window)
        self.dial.valueChanged.connect(self.dialValueDisplay.setNum)
        self.dial.valueChanged.connect(self.powerbarWidget.update)

        QMetaObject.connectSlotsByName(Window)
    # setupUi

    def retranslateUi(self, Window):
        Window.setWindowTitle(QCoreApplication.translate("Window", u"Form", None))
        self.dialValueDisplay.setText(QCoreApplication.translate("Window", u"0", None))
    # retranslateUi


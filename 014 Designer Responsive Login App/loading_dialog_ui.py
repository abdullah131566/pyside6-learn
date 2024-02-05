# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loading_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QWidget)
import resource_rc

class Ui_LoadingDialog(object):
    def setupUi(self, LoadingDialog):
        if not LoadingDialog.objectName():
            LoadingDialog.setObjectName(u"LoadingDialog")
        LoadingDialog.resize(300, 120)
        LoadingDialog.setMinimumSize(QSize(300, 120))
        LoadingDialog.setMaximumSize(QSize(300, 120))
        self.gridLayout = QGridLayout(LoadingDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label = QLabel(LoadingDialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"DejaVu Sans Mono"])
        font.setPointSize(10)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.retranslateUi(LoadingDialog)

        QMetaObject.connectSlotsByName(LoadingDialog)
    # setupUi

    def retranslateUi(self, LoadingDialog):
        LoadingDialog.setWindowTitle(QCoreApplication.translate("LoadingDialog", u"Please Wait", None))
        self.label.setText(QCoreApplication.translate("LoadingDialog", u"Logging in...", None))
    # retranslateUi


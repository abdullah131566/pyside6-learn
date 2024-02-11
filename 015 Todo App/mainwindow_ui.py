# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLineEdit,
    QListView, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_TodoWindow(object):
    def setupUi(self, TodoWindow):
        if not TodoWindow.objectName():
            TodoWindow.setObjectName(u"TodoWindow")
        TodoWindow.resize(500, 500)
        TodoWindow.setMinimumSize(QSize(500, 500))
        TodoWindow.setMaximumSize(QSize(500, 500))
        self.gridLayout = QGridLayout(TodoWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.todoView = QListView(TodoWindow)
        self.todoView.setObjectName(u"todoView")
        self.todoView.setLayoutMode(QListView.Batched)
        self.todoView.setSpacing(2)
        self.todoView.setBatchSize(3)

        self.verticalLayout_2.addWidget(self.todoView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.markDoneTodoButton = QPushButton(TodoWindow)
        self.markDoneTodoButton.setObjectName(u"markDoneTodoButton")
        self.markDoneTodoButton.setMinimumSize(QSize(0, 35))
        icon = QIcon()
        icon.addFile(u":/icon/tick", QSize(), QIcon.Normal, QIcon.Off)
        self.markDoneTodoButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.markDoneTodoButton)

        self.deleteTodoButton = QPushButton(TodoWindow)
        self.deleteTodoButton.setObjectName(u"deleteTodoButton")
        self.deleteTodoButton.setMinimumSize(QSize(0, 35))
        self.deleteTodoButton.setAutoFillBackground(False)
        self.deleteTodoButton.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.deleteTodoButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.todoEdit = QLineEdit(TodoWindow)
        self.todoEdit.setObjectName(u"todoEdit")
        self.todoEdit.setMinimumSize(QSize(0, 30))
        self.todoEdit.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.todoEdit)

        self.addTodoButton = QPushButton(TodoWindow)
        self.addTodoButton.setObjectName(u"addTodoButton")
        self.addTodoButton.setMinimumSize(QSize(0, 35))

        self.verticalLayout.addWidget(self.addTodoButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        QWidget.setTabOrder(self.markDoneTodoButton, self.deleteTodoButton)
        QWidget.setTabOrder(self.deleteTodoButton, self.todoEdit)
        QWidget.setTabOrder(self.todoEdit, self.addTodoButton)
        QWidget.setTabOrder(self.addTodoButton, self.todoView)

        self.retranslateUi(TodoWindow)
        self.todoEdit.returnPressed.connect(self.addTodoButton.click)

        QMetaObject.connectSlotsByName(TodoWindow)
    # setupUi

    def retranslateUi(self, TodoWindow):
        TodoWindow.setWindowTitle(QCoreApplication.translate("TodoWindow", u"Form", None))
        self.markDoneTodoButton.setText(QCoreApplication.translate("TodoWindow", u"Mark Done", None))
        self.deleteTodoButton.setText(QCoreApplication.translate("TodoWindow", u"Delete Current", None))
        self.todoEdit.setPlaceholderText(QCoreApplication.translate("TodoWindow", u"Add your new todo", None))
        self.addTodoButton.setText(QCoreApplication.translate("TodoWindow", u"Add todo", None))
    # retranslateUi


from PySide6.QtWidgets import QWidget, QMainWindow, QSizePolicy, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QListWidgetItem
from PySide6.QtCore import QSize

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # self.setFixedSize(QSize(500, 500))

        centralWidget = QWidget()
        centralLayout = QVBoxLayout()
        centralWidget.setLayout(centralLayout)
        self.setCentralWidget(centralWidget)

        # add content to centralLayout
        hLayout = QHBoxLayout()
        centralLayout.addLayout(hLayout)
        
        self.newItemEdit = QLineEdit()
        self.newItemEdit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        addItemButton = QPushButton("Add Item")
        addItemButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        addItemButton.clicked.connect(self.addItemToListWidget)
        addItemLayout = QHBoxLayout()
        addItemLayout.addWidget(self.newItemEdit)
        addItemLayout.addWidget(addItemButton, 0)
        addItemWidget = QWidget()
        addItemWidget.setLayout(addItemLayout)
        addItemWidget.setMinimumHeight(50)
        addItemWidget.setMaximumHeight(70)

        deleteItemButton = QPushButton("Delete Button")
        deleteItemButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        deleteItemButton.clicked.connect(self.deleteItemFromListWidget)

        vButtonLayout = QVBoxLayout()
        vButtonLayout.addWidget(addItemWidget)
        vButtonLayout.addWidget(deleteItemButton)

        self.listWidget = QListWidget()
        self.totalItemsLabel = QLabel("Number of items: " + str(self.listWidget.count()))
        vListLayout = QVBoxLayout()
        vListLayout.addWidget(self.listWidget)
        vListLayout.addWidget(self.totalItemsLabel)

        hLayout.addLayout(vButtonLayout)
        hLayout.addLayout(vListLayout)

    
    def addItemToListWidget(self):
        self.newItemEdit.setFocus()
        if self.newItemEdit.text().__len__() == 0:
            return
        listWidgetItem = QListWidgetItem(self.newItemEdit.text())
        self.listWidget.addItem(listWidgetItem)
        self.newItemEdit.clear()
        self.newItemEdit.setFocus()
        self.updateCountLabel()
    

    def deleteItemFromListWidget(self):
        currentRow = self.listWidget.currentRow()
        self.listWidget.takeItem(currentRow)
        self.updateCountLabel()


    def updateCountLabel(self):
        count = self.listWidget.count()
        self.totalItemsLabel.setText("Number of items: " + str(count))
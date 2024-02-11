from PySide6.QtWidgets import QWidget
from spreadsheet_ui import Ui_Window
from models.TableModel import TableModel
from datetime import datetime

class MyWindow(QWidget, Ui_Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        testData = [
            [7, 2, 3, 4, 5, -1],
            [-5, 4, 3.1274, 4, False, 6],
            [1, 0, 3, 75, 5, 6],
            [datetime(2001, 2, 27), 2, 3, 4, "Hello", 6],
            [1, 10, True, 4, 5, 6],
        ]
        self.tableModel = TableModel(testData)
        self.tableView.setModel(self.tableModel)
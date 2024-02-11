from PySide6.QtCore import QAbstractListModel, Qt
from PySide6.QtGui import QPixmap


class TodoModel(QAbstractListModel):
    def __init__(self, todos = None) -> None:
        super().__init__()

        self.todos = todos or []

    
    def data(self, index, role):
        if role == Qt.DisplayRole:
            _, text = self.todos[index.row()]
            return text
        
        if role == Qt.DecorationRole:
            status, text = self.todos[index.row()]
            if status:
                # return "DONE" # Displays nothing except a space
                return QPixmap(":/icon/tick")


    def rowCount(self, index):
        return len(self.todos)
    
from typing import Any
from PySide6.QtCore import QAbstractTableModel, QModelIndex, QPersistentModelIndex, Qt
from PySide6.QtGui import QColor
from datetime import datetime

class TableModel(QAbstractTableModel):
    def __init__(self, _data):
        super().__init__()
        self._data = _data

    
    def data(self, index: QModelIndex | QPersistentModelIndex, role: int = ...) -> Any:
        dataPoint = self._data[index.row()][index.column()]
        if role == Qt.DisplayRole:
            if isinstance(dataPoint, float):
                return "%.2f" % dataPoint
            if isinstance(dataPoint, str):
                return '"%s"' % dataPoint
            if isinstance(dataPoint, datetime):
                return dataPoint.strftime("%d/%b/%Y")
            return dataPoint
        
        if role == Qt.ForegroundRole:
            if isinstance(dataPoint, (float, int)) and dataPoint <= 0:
                return QColor("red")
        
        if role == Qt.BackgroundRole:
            if isinstance(dataPoint, (float, int)):
                value = int(dataPoint)
                value = max(0, value)  # cut from lower
                value = min(10,  value)  # cut from upper
                value = 11 - value  # invert
                valueStrength = (int) (value)/11    # percentage
                return QColor(valueStrength*255, 175, 195)
        
        if role == Qt.TextAlignmentRole:
            if isinstance(dataPoint, (float, int)):
                return Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight
    

    def rowCount(self, parent: QModelIndex | QPersistentModelIndex = ...) -> int:
        return len(self._data)
    

    def columnCount(self, parent: QModelIndex | QPersistentModelIndex = ...) -> int:
        return len(self._data[0])

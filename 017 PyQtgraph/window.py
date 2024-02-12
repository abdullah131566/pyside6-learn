from PySide6.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QPushButton
from PySide6.QtCore import QSize, Qt, QTimer
from PySide6.QtGui import QColor, QPen, QBrush, QPalette
import pyqtgraph as pg
import random as rd

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # self.setFixedSize(QSize(500, 500))

        centralWidget = QWidget()
        layout = QVBoxLayout()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

        # add content to layout
        self.plotWidget = pg.PlotWidget()
        self.plotWidget.setBackground(self.palette().color(QPalette.Window))
        self.plotWidget.setTitle("Random Values Plot")
        self.plotWidget.addLegend()
        self.plotWidget.showGrid(x=True, y=True)
        layout.addWidget(self.plotWidget)

        self.dynamicPlotWidget = pg.PlotWidget()
        self.dynamicPlotWidget.setBackground(self.palette().color(QPalette.Window))
        self.dynamicPlotWidget.setTitle("Random Values Plot")
        self.dynamicPlotWidget.addLegend()
        self.dynamicPlotWidget.showGrid(x=True, y=True)
        self.dynamicPlotWidget.setYRange(-20, 20)
        layout.addWidget(self.dynamicPlotWidget)


        # plotting here
        time = [i for i in range(0, 10)]
        yValues = [rd.randrange(0, 100) for _ in range(0, 10)]
        # self.pen = pg.mkPen(color=QColor(200, 0, 80), width=5)
        self.pen = QPen(QColor(200, 0, 80), 3, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        self.pen.setCosmetic(True)
        self.plotWidget.plot(time, yValues, name="Random", pen=self.pen, symbol="o", symbolSize=8, symbolBrush=QBrush(QColor("gray")))
        self.plotWidget.setLabel("bottom", "time")
        self.plotWidget.setLabel("left", "Number of people")

        self.dynamicTime = [i for i in range(0, 30)]
        self.dynamicYValues = [rd.randrange(-20, 20) for _ in range(0, 30)]
        self.dynamicPlotItem = self.dynamicPlotWidget.plot(self.dynamicTime, self.dynamicYValues, name="Dynamic", pen=self.pen)

        self.timer = QTimer()
        self.timer.setInterval(150)
        self.timer.timeout.connect(self.updateDynamicPlot)
        self.timer.start()

    def updateDynamicPlot(self):
        self.dynamicTime = self.dynamicTime[1:]
        self.dynamicTime.append(self.dynamicTime[-1] + 1)

        self.dynamicYValues = self.dynamicYValues[1:]
        self.dynamicYValues.append(rd.randrange(-20, 20))

        self.dynamicPlotItem.setData(self.dynamicTime, self.dynamicYValues)

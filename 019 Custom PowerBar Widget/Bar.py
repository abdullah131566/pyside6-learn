from PySide6.QtWidgets import QWidget, QDial
from PySide6.QtGui import QMouseEvent, QPainter, QPaintEvent, QPen, QBrush, QColor, QFont
from PySide6.QtCore import QRect, QSize, Qt


class _Bar(QWidget):
    def __init__(self, parent: QWidget | None = ..., f: Qt.WindowType = ...) -> None:
        super().__init__()
        self.numberOfBars = 5
        self.xPadding = 5
        self.yPadding = 5
        self.relativeBarSpacerHeight = 0.3

    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter(self)

        # Background
        brush = QBrush(QColor("#000"))
        rectangle = QRect(0, 0, painter.device().width(), painter.device().height())
        painter.fillRect(rectangle, brush)

        # Foreground
        dial : QDial = self.parent().dial
        dialMin = dial.minimum()
        dialMax = dial.maximum()
        dialCurrentVal = dial.value()

        pen = QPen(QColor("red"))
        painter.setPen(pen)

        # # V1 (Test) Foreground
        # # text = "{} : {} : {}".format(dialMin, dialCurrentVal, dialMax)

        # font = QFont("Robotto", 28, 200)
        # painter.setFont(font)
        # painter.drawText(10, 35, text)
        # painter.end()

        # V2 Foreground
        brush = QBrush(QColor("blue"))
        painter.setBrush(brush)

        singleContainerWidth = painter.device().width() - self.xPadding * 2
        singleContainerHeight = (painter.device().height() - self.yPadding * 2) / self.numberOfBars
        singleContainerHeightSpacing = singleContainerHeight * self.relativeBarSpacerHeight

        dialValInPercent = (dialCurrentVal - dialMin) / (dialMax - dialMin)
        numberOfBarsToDraw = int(dialValInPercent * self.numberOfBars)
        for i in range(numberOfBarsToDraw):
            bar = QRect(
                self.xPadding,
                self.yPadding + (self.numberOfBars - i - 1) * singleContainerHeight + singleContainerHeightSpacing / 2,
                singleContainerWidth,
                singleContainerHeight - singleContainerHeightSpacing
            )
            painter.fillRect(bar, brush)

        painter.end()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        percentClicked = 0.1 + (self.height() - event.y()) / self.height()
        dialMax = self.parent().dial.maximum()
        self.parent().dial.setValue(percentClicked * dialMax)
        self.update()

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        percentClicked = 0.05 + (self.height() - event.y()) / self.height()
        dialMax = self.parent().dial.maximum()
        self.parent().dial.setValue(percentClicked * dialMax)
        self.update()



    def sizeHint(self) -> QSize:
        return QSize(50, 120)

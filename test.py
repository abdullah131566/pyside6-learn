from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QMainWindow, QApplication
from PySide6.QtCore import QRunnable, QThreadPool, Slot, QObject, Signal

import sys
import time

class WorkerSignals(QObject):
    finished = Signal()
    result = Signal(object)
    error = Signal(tuple)
    

class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.
    '''
    def __init__(self, fn, *args, **kwargs) -> None:
        super().__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
    
    @Slot()
    def run(self) -> None:
        res = self.fn(*self.args, **self.kwargs)
        self.signals.result.emit(res)
        self.signals.finished.emit()

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.threadPool = QThreadPool()
        print("Maximum thread count", self.threadPool.maxThreadCount())
        self.counter = 0

        layout = QVBoxLayout()

        self.l = QLabel("Start")
        b = QPushButton("DANGER!")
        b.pressed.connect(self.oh_no)

        c = QPushButton("?")
        c.pressed.connect(self.change_message)

        layout.addWidget(self.l)
        layout.addWidget(b)

        layout.addWidget(c)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

        self.show()

    def change_message(self):
        self.message = "OH NO"

    def oh_no(self):
        self.message = "Pressed"
        worker = Worker(self.aLongTask, 5)
        worker.signals.result.connect(lambda x: print("result", x))
        self.threadPool.start(worker)
        self.l.setText(self.message)

    def aLongTask(self, _time):
        print("Long task started...", _time)
        time.sleep(_time)
        print("...Long task finished")
        return 10
        
app = QApplication(sys.argv)
window = MainWindow()
app.exec()
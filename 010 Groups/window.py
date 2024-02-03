from PySide6.QtWidgets import QWidget, QMainWindow, QHBoxLayout, QVBoxLayout, QPushButton, QCheckBox, QRadioButton, QGroupBox, QButtonGroup
from PySide6.QtCore import QSize

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # self.setFixedSize(QSize(500, 500))

        centralWidget = QWidget()
        mainLayout = QVBoxLayout()
        centralWidget.setLayout(mainLayout)
        self.setCentralWidget(centralWidget)

        h_layout = QHBoxLayout()
        mainLayout.addLayout(h_layout)

        # add non-exclusive group box to layout
        osGroupBox = QGroupBox("Operating System")
        h_layout.addWidget(osGroupBox)
        
        windowCheckBox = QCheckBox("MS Windows")
        linuxCheckBox = QCheckBox("Linux")
        macCheckBox = QCheckBox("Mac OS")
        osLayout = QVBoxLayout()
        osLayout.addWidget(windowCheckBox)
        osLayout.addWidget(linuxCheckBox)
        osLayout.addWidget(macCheckBox)
        osGroupBox.setLayout(osLayout)
        
        # add exclusive button-group group box to layout
        travelMeanGroupBox = QGroupBox("Travel Mean")
        h_layout.addWidget(travelMeanGroupBox)

        walkCheckBox = QCheckBox("Walk")
        bikeCheckBox = QCheckBox("Bike")
        carCheckBox = QCheckBox("Car")
        travelMeanButtonGroup = QButtonGroup(travelMeanGroupBox)
        travelMeanButtonGroup.addButton(walkCheckBox)
        travelMeanButtonGroup.addButton(bikeCheckBox)
        travelMeanButtonGroup.addButton(carCheckBox)
        travelMeanButtonGroup.setExclusive(True)
        travelMeanLayout = QVBoxLayout()
        travelMeanLayout.addWidget(walkCheckBox)
        travelMeanLayout.addWidget(bikeCheckBox)
        travelMeanLayout.addWidget(carCheckBox)
        travelMeanGroupBox.setLayout(travelMeanLayout)

        # add radio button group box to layout
        sleepTimeGroupBox = QGroupBox("Time of sleep")
        mainLayout.addWidget(sleepTimeGroupBox)

        eightPM = QRadioButton("8:00 PM")
        ninePM = QRadioButton("9:00 PM")
        afterTenPM = QRadioButton("After 10:00 PM")
        sleepTimeLayout = QVBoxLayout()
        sleepTimeLayout.addWidget(eightPM)
        sleepTimeLayout.addWidget(ninePM)
        sleepTimeLayout.addWidget(afterTenPM)
        sleepTimeGroupBox.setLayout(sleepTimeLayout)

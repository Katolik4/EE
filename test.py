import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QRect, QStringListModel, QDir, Qt
from RpiHardware import Rpi
from Przekazniki import przyckiskiWidget

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 tabs - pythonspot.com'
        self.left = 0
        self.top = 30
        self.width = 1000
        self.height = 600

        self.rpi_hardware = Rpi()
        self.setWindowTitle(self.title)

        self.setGeometry(self.left, self.top, self.width, self.height)
        #self.showFullScreen()


        self.centralWindow = 0
        self.centralWindowLayout = QGroupBox()

        #self.table_widget = MyTableWidget(self)
        #self.setCentralWidget(self.table_widget)

        self.main_widget = oknoWidget(self)
        self.setCentralWidget(self.main_widget)

       # self.mainLayout()

        self.initMenu()


        self.show()

    def initMenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        viewMenu = mainMenu.addMenu('View')
        searchMenu = mainMenu.addMenu('Search')
        toolsMenu = mainMenu.addMenu('Tools')
        helpMenu = mainMenu.addMenu('Help')

        exitButton = QAction(QIcon('.\pic\icon.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

    def mainLayout(self):
        layout = QHBoxLayout()
       # tabs = MyTableWidget(self)
        layout.addWidget(self.mainGrid())
        layout.addWidget(self.mainGrid())
        self.setLayout(layout)

    def test(self):
        print('Rpi hardware main: {}'.format(self.rpi_hardware))



class MyMainWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.rpi_hardware = parent.rpi_hardware


        self.table_widget = MyHButtonWidget(self)
        self.layout.addWidget(self.table_widget)

        self.grid_widget = przyckiskiWidget(self)
        self.layout.addWidget(self.grid_widget)

        #self.button_widget = MyButtonWidget(self)
        #self.layout.addWidget(self.button_widget)
        self.setLayout(self.layout)

class oknoWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.rpi_hardware = parent.rpi_hardware

        self.topleft = QSplitter(Qt.Horizontal)

        self.okno = QTextEdit()

        self.topleft.addWidget(MyHButtonWidget(self))
        self.topleft.addWidget(self.okno)
        self.layout.addWidget(self.topleft)

        # self.table_widget = MyHButtonWidget(self)
        # self.layout.addWidget(self.table_widget)
        #
        # self.grid_widget = przyckiskiWidget(self)
        # self.layout.addWidget(self.grid_widget)

        #self.button_widget = MyButtonWidget(self)
        #self.layout.addWidget(self.button_widget)
        self.setLayout(self.layout)

class MyHButtonWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.rpi_hardware = parent.rpi_hardware
        #self.layout = QVBoxLayout(self)
        self.initButtons()
        #self.setMaximumHeight(50)
        #self.kolor_tla()




    def initButtons(self):

        layout = QHBoxLayout()
        self.button = QPushButton('PyQt5 button', self)
        self.button.setToolTip('This is an example button')
        self.button.clicked.connect(self.on_click)

        self.button1 = QPushButton('Testowy', self)
        self.button1.setObjectName('piotr')
        self.button1.setToolTip('przycisk do testu')
        self.button1.setCheckable(True)
        self.button1.clicked.connect(self.on_click1)

        self.button2 = QPushButton('PyQt5 button', self)
        self.button2.setToolTip('This is an example button')
        self.button2.clicked.connect(self.on_click)

        layout.addWidget(self.button)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)

        self.setLayout(layout)

    def kolor_tla(self):
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.darkBlue)
        self.setPalette(p)

    @pyqtSlot()
    def on_click(self):
        self.rpi_hardware.gpio1()

    @pyqtSlot()
    def on_click1(self):
        if self.button1.isChecked():
            self.rpi_hardware.gpio(1, 'on')
        else:
            self.rpi_hardware.gpio(1, 'off')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    ex = App()
    ex.test()

    sys.exit(app.exec_())
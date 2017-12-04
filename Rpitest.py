import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QLabel, QLineEdit, QTextEdit, QGridLayout, QFileSystemModel, QTreeView
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QRect, QStringListModel, QDir, Qt

from RpiHardware import Rpi


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

        self.main_widget = MyMainWidget(self,self.rpi_hardware)
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

class MyHButtonWidget(QWidget):
    def __init__(self, parent, rpi_hardware):
        super(QWidget, self).__init__(parent)
        #self.layout = QVBoxLayout(self)
        self.rpi_hardware = rpi_hardware
        self.initButtons()
        self.setMaximumHeight(50)
        #self.kolor_tla()


    def initButtons(self):

        layout = QHBoxLayout()
        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.clicked.connect(self.on_click)

        button1 = QPushButton('Testowy', self)
        button1.setToolTip('przycisk do testu')
        button1.clicked.connect(self.on_click1)

        button2 = QPushButton('PyQt5 button', self)
        button2.setToolTip('This is an example button')
        button2.clicked.connect(self.on_click)

        layout.addWidget(button)
        layout.addWidget(button1)
        layout.addWidget(button2)

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
        print("Wcisnieto przycisk testowy")

class MyVButtonWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        #self.layout = QVBoxLayout(self)

        self.initButtons()



    def initButtons(self):

        layout = QVBoxLayout()
        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.clicked.connect(self.on_click)

        button1 = QPushButton('Testowy', self)
        button1.setToolTip('przycisk do testu')
        button1.clicked.connect(self.on_click1)

        button2 = QPushButton('PyQt5 button', self)
        button2.setToolTip('This is an example button')
        button2.clicked.connect(self.on_click)

        layout.addWidget(button)
        layout.addWidget(button1)
        layout.addWidget(button2)

        self.setLayout(layout)

    @pyqtSlot()
    def on_click(self):
        print("Wcisnieto przycisk")

    @pyqtSlot()
    def on_click1(self):
        print("Wcisnieto przycisk testowy")

class MyGridTestWidget(QWidget):
    def __init__(self, parent, rpi_hardware):
        super(QWidget, self).__init__(parent)

        self.rpi = rpi_hardware
        MainGridLayout = QGroupBox()
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')
        review.setMaximumHeight(20)
        opcje = QLabel('Opcje')
        button = QPushButton('ok', self)
        button.setMaximumHeight(20)
        button.clicked.connect(self.on_click)

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 3, 1)

        grid.addWidget(button, 4, 0)

        buttons = MyHButtonWidget(self,self.rpi)
        grid.addWidget(opcje, 6, 0)
        grid.addWidget(buttons, 6, 1)


        MainGridLayout.setLayout(grid)
        self.setLayout(grid)


    @pyqtSlot()
    def on_click(self):
        self.rpi.uart_TX('wcisnieto przyciks grid test')

class MyMainWidget(QWidget):
    def __init__(self, parent, rpi_hardware):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.table_widget = MyGridTestWidget(self,rpi_hardware)
        self.layout.addWidget(self.table_widget)


        self.grid_widget = MyHButtonWidget(self,rpi_hardware)
        self.grid_widget.resize(10,1000)
        self.layout.addWidget(self.grid_widget)

        #self.button_widget = MyButtonWidget(self)
        #self.layout.addWidget(self.button_widget)
        self.setLayout(self.layout)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
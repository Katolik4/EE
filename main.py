import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from RpiHardware import Rpi
from Przekazniki import *


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.width = 1000
        self.height = 600

        self.rpi_hardware = Rpi()
        self.dane = dane_studentow()

        self.initMenu()
        self.initUI()



        self.show()



    def initUI(self):
        #self.setGeometry(10, 30, self.width, self.height)
        self.showFullScreen()
        self.setWindowTitle('Program Główny')
        self.setWindowIcon(QIcon('.\pic\icon.png'))
        #self.initButtons()
        #self.initTopBar()

        self.setCentralWidget(MainWidget(self))
        self.setStyleSheet(open("style.qss", "r").read())
        self.setAutoFillBackground(True)

    def initMenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        viewMenu = mainMenu.addMenu('View')
        searchMenu = mainMenu.addMenu('Search')
        toolsMenu = mainMenu.addMenu('Tools')
        helpMenu = mainMenu.addMenu('Help')
        exitMenu = mainMenu.addMenu('Exit')

        exitButton = QAction(QIcon('.\pic\icon.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        exitMenu.addAction(exitButton)

        daneButton = QAction(QIcon('.\pic\icon.png'), 'Dane', self)
        daneButton.setStatusTip('Dane studentow')
        daneButton.triggered.connect(self.dane.show)
        fileMenu.addAction(daneButton)

    def MainGrid(self):

        MainGridLayout = QGroupBox()
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

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
        grid.addWidget(reviewEdit, 3, 1, 2, 1)

        MainGridLayout.setLayout(grid)
        return MainGridLayout

    def initButtons(self):
        self.centralGroupBox = QGroupBox()
        layout = QHBoxLayout()

        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.clicked.connect(self.on_click)

        button1 = QPushButton('Testowy', self)
        button1.setToolTip('This is an example button')
        button1.clicked.connect(self.on_click1)

        button2 = QPushButton('PyQt5 button', self)
        button2.setToolTip('This is an example button')
        button2.clicked.connect(self.on_click)

        layout.addWidget(button)
        layout.addWidget(button1)
        layout.addWidget(button2)

        self.centralGroupBox.setLayout(layout)

    def initTopBar(self):
        self.horizontalGroupBox = QGroupBox()
        layout = QHBoxLayout()
        layout.setGeometry(QRect(300,400,200,50))

        buttonBlue = QPushButton('Blue', self)
        buttonBlue.clicked.connect(self.on_click)
        layout.addWidget(buttonBlue)

        buttonRed = QPushButton('Red', self)
        buttonRed.clicked.connect(self.on_click)
        layout.addWidget(buttonRed)

        buttonGreen = QPushButton('Green', self)
        buttonGreen.clicked.connect(self.on_click)
        layout.addWidget(buttonGreen)

        self.horizontalGroupBox.setLayout(layout)

    @pyqtSlot()
    def on_click(self):
        print("Wcisnieto przycisk")

    @pyqtSlot()
    def on_click1(self):

        self.zmiana_okna()

    def zmiana_okna(self):
        self.centralWindow += 1
        if self.centralWindow > 3:
            self.centralWindow = 0
        print(self.centralWindow)

class MainWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.rpi_hardware = parent.rpi_hardware

        self.glowne = QSplitter(Qt.Vertical)

        self.initokno()
        #self.okno = QTextEdit()
        self.przekaznikiwidget = przyckiskiWidget(self)
        self.przekaznikiwidget.setObjectName('BottomBar')

        self.glowne.addWidget(self.okno)
        self.glowne.addWidget(self.przekaznikiwidget)
        self.layout.addWidget(self.glowne)

        self.setLayout(self.layout)

    def initokno(self):
        self.okno = QSplitter(Qt.Horizontal)
        self.oknoprawe = wyswietl_dane_studentow(self)
        self.oknolewe = QTextEdit()

        self.okno.addWidget(self.oknolewe)
        self.okno.addWidget(self.oknoprawe)


# class Serial(QWidget)
#     def __init__(self, parent=None):
#         super(QWidget, self).__init__(parent)
#         self.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
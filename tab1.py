import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QLabel, QLineEdit, QTextEdit, QGridLayout, QFileSystemModel, QTreeView
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QRect, QStringListModel, QDir

from RpiHardware import Rpi


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 tabs - pythonspot.com'
        self.left = 0
        self.top = 30
        self.width = 1000
        self.height = 600
        self.setWindowTitle(self.title)

        self.setGeometry(self.left, self.top, self.width, self.height)
        #self.showFullScreen()
        self.centralWindow = 0
        self.centralWindowLayout = QGroupBox()

        #self.table_widget = MyTableWidget(self)
        #self.setCentralWidget(self.table_widget)

        self.main_widget = MyMainWidget(self)
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


class MyMainWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QHBoxLayout(self)

        self.table_widget = MyTableWidget(self)
        self.layout.addWidget(self.table_widget)


        self.grid_widget = MyGridWidget(self)
        self.layout.addWidget(self.grid_widget)

        #self.button_widget = MyButtonWidget(self)
        #self.layout.addWidget(self.button_widget)
        self.setLayout(self.layout)

class MyHButtonWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        #self.layout = QVBoxLayout(self)

        self.initButtons()



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

    @pyqtSlot()
    def on_click(self):
        print("Wcisnieto przycisk")

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


class MyGridWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        MainGridLayout = QGroupBox()
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')
        opcje = QLabel('Opcje')

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

        buttons = MyHButtonWidget(self)
        grid.addWidget(opcje, 6, 0)
        grid.addWidget(buttons, 6, 1)


        MainGridLayout.setLayout(grid)
        self.setLayout(grid)

class MyGridTestWidget(QWidget):
    def __init__(self, parent, Rpi):
        super(QWidget, self).__init__(parent)

        self.rpi = Rpi()
        MainGridLayout = QGroupBox()
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')
        opcje = QLabel('Opcje')
        button = QPushButton('ok', self)
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

        buttons = MyHButtonWidget(self)
        grid.addWidget(opcje, 6, 0)
        grid.addWidget(buttons, 6, 1)


        MainGridLayout.setLayout(grid)
        self.setLayout(grid)

    @pyqtSlot()
    def on_click(self):
        self.rpi.uart_TX('wcisnieto przyciks grid test')

class MyGridFilesWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        start_dir = QStringListModel()
        start_dir = 'C:/ROBOCZY'


        self.model = QFileSystemModel()
        self.model.setFilter(QDir.AllDirs | QDir.NoDotAndDotDot | QDir.AllEntries)
        self.model.setNameFilters()
        self.model.setNameFilterDisables(0)
        #self.model.setRootPath(start_dir)

        #self.model.setRootPath(start_dir)
        self.tree = QTreeView()
        self.tree.setRootIndex(self.model.index(start_dir))
        self.tree.setModel(self.model)

        self.tree.setAnimated(False)
        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)

        self.tree.setWindowTitle("Dir View")
        self.tree.resize(640, 480)

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.tree)
        self.setLayout(windowLayout)

class MyTableWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(300, 200)

        # Add tabs
        self.tabs.addTab(self.tab1, "Tab 1")
        self.tabs.addTab(self.tab2, "Tab 2")

        # Create first tab
        self.tab1.layout = QVBoxLayout(self)
       # self.pushButton1 = QPushButton("PyQt5 button")
        #self.tab1.layout.addWidget(self.pushButton1)
        self.tab1.layout.addWidget(MyVButtonWidget(self))
        self.tab1.setLayout(self.tab1.layout)

        # Create 2 tab
        self.tab2.layout = QVBoxLayout(self)

        #self.tab2.layout.addWidget(MyGridWidget(self))
        #self.tab2.setLayout(self.tab2.layout)

        #self.tab2.layout.addWidget(MyGridFilesWidget(self))
        #self.tab2.setLayout(self.tab2.layout)

        self.tab2.layout.addWidget(MyGridTestWidget(self))
        self.tab2.setLayout(self.tab2.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

class MyStatusWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.initButtons()



    def initButtons(self):

        layout = QVBoxLayout()
        button.setToolTip('This is an example button')
        button.clicked.connect(self.on_click)
        button.resize(20,20)

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
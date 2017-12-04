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

        self.testowany_widget = wyswietl_dane_studentow(self)

        self.setCentralWidget(self.testowany_widget)

        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
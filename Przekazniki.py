from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from db import Db
import _json


class przyckiskiWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.rpi_hardware = parent.rpi_hardware
        # self.setObjectName('BottomBar')
        # self.setStyleSheet(open('style_przekazniki.qss', 'r').read())
        # self.layout = QVBoxLayout(self)
        self.initButtons()
        self.setMaximumHeight(120)
        # self.kolor_tla()

    def initButtons(self):

        layout = QHBoxLayout()

        self.button = QPushButton('Obiekt 1', self)
        self.button.setObjectName('piotr')
        self.button.setToolTip('przycisk do testu')
        self.button.setCheckable(True)
        self.button.clicked.connect(self.on_click)

        self.button1 = QPushButton('Obiekt 2', self)
        self.button1.setObjectName('piotr')
        self.button1.setToolTip('przycisk do testu')
        self.button1.setCheckable(True)
        self.button1.clicked.connect(self.on_click1)

        self.button2 = QPushButton('Obiekt 3', self)
        self.button2.setObjectName('piotr')
        self.button2.setToolTip('przycisk do testu')
        self.button2.setCheckable(True)
        self.button2.clicked.connect(self.on_click2)

        self.button3 = QPushButton('Stycznik 4', self)
        self.button3.setObjectName('piotr')
        self.button3.setToolTip('przycisk do testu')
        self.button3.setCheckable(True)
        self.button3.clicked.connect(self.on_click3)

        layout.addWidget(self.button)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)

        self.setLayout(layout)

    def kolor_tla(self):
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.darkBlue)
        self.setPalette(p)

    @pyqtSlot()
    def on_click(self):
        if self.button.isChecked():
            self.rpi_hardware.gpio(1, 'on')
        else:
            self.rpi_hardware.gpio(1, 'off')

    @pyqtSlot()
    def on_click1(self):
        if self.button1.isChecked():
            self.rpi_hardware.gpio(2, 'on')
        else:
            self.rpi_hardware.gpio(2, 'off')

    @pyqtSlot()
    def on_click2(self):
        if self.button2.isChecked():
            self.rpi_hardware.gpio(3, 'on')
        else:
            self.rpi_hardware.gpio(3, 'off')

    @pyqtSlot()
    def on_click3(self):
        if self.button3.isChecked():
            self.rpi_hardware.gpio(4, 'on')
        else:
            self.rpi_hardware.gpio(4, 'off')


class dane_studentow(QDialog):
    def __init__(self):
        super().__init__()
        self.width = 500
        self.height = 600

        self.initForm()
        self.initButtonBox()

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(self.przyciski)

        self.setLayout(mainLayout)

    def initForm(self):
        self.formGroupBox = QGroupBox('Podaj dane')
        layout = QFormLayout()
        self.Calendar = QCalendarWidget()
        self.grupa = QLineEdit()
        self.imiona = QTextEdit()
        layout.addRow(QLabel("Data:"), self.Calendar)
        layout.addRow(QLabel("Grupa:"), self.grupa)
        layout.addRow(QLabel("Imiona:"), self.imiona)
        self.formGroupBox.setLayout(layout)

    def initButtonBox(self):
        self.przyciski = QGroupBox()
        layout = QHBoxLayout()

        buttonZapisz = QPushButton('Zapisz', self)
        buttonZapisz.setToolTip('Zapisz dane')
        buttonZapisz.clicked.connect(self.zapisz)

        buttonExit = QPushButton('Wyjdz', self)
        buttonExit.setToolTip('Wyjdz')
        buttonExit.clicked.connect(self.Exit)

        layout.addWidget(buttonZapisz)
        layout.addWidget(buttonExit)

        self.przyciski.setLayout(layout)

    @pyqtSlot()
    def zapisz(self):
        imiona = self.imiona.toPlainText()
        imiona = "IMIONA: \n" + imiona + "\n"
        print(imiona)
        grupa = self.grupa.text()
        grupa = "GRUPA: \n" + grupa + "\n"
        # dane = [self.Calendar.text(), self.grupa.text()]

        plik = open('test.txt', 'w')
        plik.write(grupa)
        plik.write(imiona)
        plik.close()

        self.close()

    @pyqtSlot()
    def Exit(self):
        self.close()


class wyswietl_dane_studentow(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.width = 500
        self.height = 600

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.addtekst())
        mainLayout.addWidget(QLabel("test"))
        self.setLayout(mainLayout)
        self.show()

    def testgrupa(self):
        self.grupa = QLabel
        plik = open('test.txt', 'r')
        try:
            tekst = plik.read
        finally:
            plik.close()

        self.grupa.setText(tekst)

    def addtekst(self):
        layout = QVBoxLayout()
        self.grupa = QLabel()
        tekst = "Dupa Dupa"
        self.grupa.setText("dupa dupa")
        layout.addWidget(self.grupa)
        self.setLayout(layout)
        # self.show()

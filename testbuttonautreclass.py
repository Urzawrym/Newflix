import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

class WindowInhalt(QWidget):
    def label(self):
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("Überschrift mit namen des text adventure")
        self.label1.setStyleSheet("font-size: 18px;color: black;")
        self.label1.setGeometry(50, 50, 400, 100)
        self.label1.move(350, 50)
        self.label1.show()

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("Spielen")
        self.label2.setStyleSheet("font-size: 18px;color: black;")
        self.label2.setGeometry(50, 50, 400, 100)
        self.label2.move(450, 120)
        self.label2.mousePressEvent = self.spielen
        self.label2.show()

        self.label3 = QtWidgets.QLabel(self)
        self.label3.setText("Settings")
        self.label3.setStyleSheet("font-size: 18px;color: black;")
        self.label3.setGeometry(50, 50, 400, 100)
        self.label3.move(450, 200)
        self.label3.mousePressEvent = self.settings
        self.label3.show()

        self.label4 = QtWidgets.QLabel(self)
        self.label4.setText("Credits")
        self.label4.setStyleSheet("font-size: 18px;color: black;")
        self.label4.setGeometry(50, 50, 400, 100)
        self.label4.move(450, 280)
        self.label4.mousePressEvent = self.credits
        self.label4.show()

    def button(self):
        QToolTip.setFont(QFont("Arial", 10))
        self.button = QPushButton("Spiel beenden", self)
        self.button.setGeometry(50, 50, 150, 50)
        self.button.setFont(QFont("Arial", 12))
        self.button.move(820, 420)
        self.button.setToolTip("<b>Button lel</b>")
        self.button.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.button.clicked.connect(self.gedruekt)
        self.button.setStyleSheet("background-color: white;")
        self.button.show()


class Window(WindowInhalt):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        self.label()
        self.button()
        self.setGeometry(50,50,1000,500)
        self.setWindowTitle("Gui lalal einhorn")
        self.setWindowIcon(QIcon("cookie.png"))
        self.setAutoFillBackground(True)
        self.setStyleSheet("background-color: lightblue;")
        self.move(500, 250)
        self.show()

    def spielen(self, event,):
        print("spielen")
        self.label1.hide()

    def settings(self, event):
        print("settings")

    def credits(self, event):
        print("credits")

    def gedruekt(self, event):
        print("Er hats getan ;(")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())
else:
    print("Gui not created, because script used at liabary")
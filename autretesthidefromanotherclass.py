import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

class Mainwindow(QWidget):
    def setup(self):
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("Disparait si on clic")
        self.label1.setStyleSheet("font-size: 18px;color: black;")
        self.label1.setGeometry(50, 50, 400, 100)
        self.label1.move(350, 50)
        self.label1.show()

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("Click me")
        self.label2.setStyleSheet("font-size: 18px;color: black;")
        self.label2.setGeometry(50, 50, 400, 100)
        self.label2.move(450, 120)
        self.label2.mousePressEvent = self.cacher
        self.label2.show()

class Window(Mainwindow):
    def __init__(self):
        super().__init__()
        self.initMe()


    def initMe(self):
        self.setup()
        self.setGeometry(50,50,1000,500)
        self.setWindowTitle("Fenetre test")
        self.setWindowIcon(QIcon("cookie.png"))
        self.setAutoFillBackground(True)
        self.setStyleSheet("background-color: lightblue;")
        self.move(500, 250)
        self.show()

    def cacher(self, event):
        print("ca marche")
        self.label1.hide()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())

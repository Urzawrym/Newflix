from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Main(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Main, self).__init__(parent)

        # main button
        self.addButton = QtWidgets.QPushButton('button to add other widgets')
        self.addButton.clicked.connect(self.addWidget)

        #self.removing=Test()
        self.kod = []
        self.removeButton = QtWidgets.QPushButton("remove widget")
        self.removeButton.clicked.connect(self.remove_widget)

        # scroll area widget contents - layout
        self.scrollLayout = QtWidgets.QFormLayout()

        # scroll area widget contents
        self.scrollWidget = QtWidgets.QWidget()
        self.scrollWidget.setLayout(self.scrollLayout)

        # scroll area
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.scrollWidget)

        # main layout
        self.mainLayout = QtWidgets.QVBoxLayout()

        # add all main to the main vLayout
        self.mainLayout.addWidget(self.addButton)
        self.mainLayout.addWidget(self.removeButton)
        self.mainLayout.addWidget(self.scrollArea)

        # central widget
        self.centralWidget = QtWidgets.QWidget()
        self.centralWidget.setLayout(self.mainLayout)

        # set central widget
        self.setCentralWidget(self.centralWidget)

    def addWidget(self):
        temp = Test()
        self.kod.append(temp)
        self.scrollLayout.addRow(temp)

    def remove_widget(self):
        self.kod.pop().deleteLater()


class Test(QtWidgets.QWidget):
  def __init__( self, parent=None):
      super(Test, self).__init__(parent)

      self.lineEdit = QtWidgets.QLineEdit('I am a Test widget')

      layout = QtWidgets.QHBoxLayout()
      layout.addWidget(self.lineEdit)
      self.setLayout(layout)






app = QtWidgets.QApplication(sys.argv)
myWidget = Main()
myWidget.show()
app.exec_()
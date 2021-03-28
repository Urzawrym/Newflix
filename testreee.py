from PyQt5 import QtGui, QtCore, QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.tree = QtWidgets.QTreeWidget(self)
        parent = QtWidgets.QTreeWidgetItem(self.tree, ['rigname1'])
        QtWidgets.QTreeWidgetItem(parent, ['light01'])
        parent = QtWidgets.QTreeWidgetItem(parent, ['light02'])
        QtWidgets.QTreeWidgetItem(parent, ['object02'])
        self.tree.expandAll()
        self.button = QtWidgets.QPushButton('Print', self)
        #self.button.clicked.connect(self.handleButton)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.tree)
        layout.addWidget(self.button)

    """def handleButton(self):
        iterator = QtWidgets.QTreeWidgetItemIterator(self.tree)
        while iterator.value():
            item = iterator.value()
            print
            (item.text(0)
            iterator += 1)"""


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.resize(300, 200)
    window.show()
    sys.exit(app.exec_())
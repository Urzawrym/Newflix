from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import sys


data_for_tree = {"tomato":{"color":"red","amount":"10", "note":"a note for tomato"},"banana":{"color":"yellow","amount":"1", "note":"b note for banana"}, "some fruit":{"color":"unknown","amount":"100", "note":"some text"}}

"""class TreeModel(QAbstractItemModel):

    def data(self, index, role=Qt.DisplayRole):
        #...
        if role == Qt.ToolTipRole:
            return 'ToolTip'

    def flags(self, index):
        if not index.isValid():
            return Qt.NoItemFlags # 0
        return Qt.ItemIsSelectable # or Qt.ItemIsEnabled

class ProxyModel(QSortFilterProxyModel):

    def __init__(self, parent=None):
        super(ProxyModel, self).__init__(parent)

    def lessThan(self, left, right):
        leftData = self.sourceModel().data(left)
        rightData = self.sourceModel().data(right)
        try:
            return float(leftData) < float(rightData)
        except ValueError:
            return leftData < rightData"""

class MainFrame(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.MyTreeView = QTreeView()
        self.MyTreeViewModel = QStandardItemModel()
        self.MyTreeView.setModel(self.MyTreeViewModel)
        self.most_used_cat_header = ['Name', "amount", "color"]
        self.MyTreeViewModel.setHorizontalHeaderLabels(self.most_used_cat_header)
        self.MyTreeView.setSortingEnabled(True)
        self.MyTreeView_Fill()

        MainWindow = QHBoxLayout(self)
        MainWindow.addWidget(self.MyTreeView)
        self.setLayout(MainWindow)

    def MyTreeView_Fill(self):
        for k in data_for_tree:
            name = QStandardItem(k)
            amount = QStandardItem(data_for_tree[k]["amount"])
            note = QStandardItem(data_for_tree[k]["color"])
            tooltip = data_for_tree[k]["note"]
            name.setToolTip(tooltip)
            amount.setToolTip(tooltip)
            note.setToolTip(tooltip)
            item = (name, amount, note)
            self.MyTreeViewModel.appendRow(item)
        #self.MyTreeView.sortByColumn(1, Qt.DescendingOrder)


        c = 0
        while c < len(self.most_used_cat_header):
            self.MyTreeView.resizeColumnToContents(c)
            c=c+1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainFrame()
    main.show()
    main.move(app.desktop().screen().rect().center() - main.rect().center())
sys.exit(app.exec_())
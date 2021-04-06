from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import types

class MainFrame(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        tree = {'root': {"1": ["A", "B", "C"],"2": {"2-1": ["G", "H", "I"],"2-2": ["J", "K", "L"]},"3": ["D", "E", "F"]}}

        self.tree = QtWidgets.QTreeView(self)
        layout = QtWidgets.QHBoxLayout(self)
        layout.addWidget(self.tree)

        root_model = QtGui.QStandardItemModel()
        self.tree.setModel(root_model)
        self._populateTree(tree, root_model.invisibleRootItem())

    def _populateTree(self, children, parent):
        for child in sorted(children):
            child_item = QtGui.QStandardItem(child)
            parent.appendRow(child_item)
            if isinstance(children, types.DictType):
                self._populateTree(children[child], child_item)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MainFrame()
    main.show()
    sys.exit(app.exec_())
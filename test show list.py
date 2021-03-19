from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from PyQt5.QtWidgets import *

class TableWidget(QWidget):
    def __init__(self):
        super().__init__()

        spisok = [{'some': 'any 1',  'some2': 'any 2',  'some3': 'any 3'},
                  {'some': 'any 1a', 'some2': 'any 2a', 'some3': 'any 3a'},
                  {'some': 'any 1b', 'some2': 'any 2b', 'some3': 'any 3b'}
                 ]

        table = QTableWidget()
        table.setRowCount(3)
        table.setColumnCount(3)

        vbox = QVBoxLayout(self)
        vbox.addWidget(table)

        for row, item_list in enumerate(spisok):
            for col, key in enumerate(item_list):
                newitem = QTableWidgetItem(item_list[key])
                table.setItem(row, col, newitem)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = TableWidget()
    w.show()
    sys.exit(app.exec_())
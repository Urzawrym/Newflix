from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from PyQt5.QtWidgets import *
from PyQt5.uic.properties import QtWidgets


class TableWidget(QWidget):
    def __init__(self):
        super().__init__()

        spisok = [{'some': 'any 1',  'some2': 'any 2',  'some3': 'any 3'},
                  {'some': 'any 1a', 'some2': 'any 2a', 'some3': 'any 3a'},
                  {'some': 'any 1b', 'some2': 'any 2b', 'some3': 'any 3b'}
                 ]

        table = QTableWidget()

        vbox = QVBoxLayout(self)
        vbox.addWidget(table)
        row_count = (len(spisok))
        column_count = (len(spisok[0]))

        table.setColumnCount(column_count)
        table.setRowCount(row_count)
        table.setHorizontalHeaderLabels((list(spisok[0].keys())))


        for row in range(row_count):  # add items from array to QTableWidget
            for column in range(column_count):
                item = (list(spisok[row].values())[column])
                table.setItem(row, column, QTableWidgetItem(item))



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = TableWidget()
    w.show()
    sys.exit(app.exec_())
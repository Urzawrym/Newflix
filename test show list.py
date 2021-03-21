from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from PyQt5.QtWidgets import *
from PyQt5.uic.properties import QtWidgets


class TableWidget(QWidget):
    def __init__(self):
        super().__init__()

        users = [{'Prenom': 'Claude',  'Nom': 'Belanger',  'Ville': 'Levis'},
                  {'Prenom': 'Francis', 'Nom': 'Gariepy', 'Ville': 'Quebec'},
                  {'Prenom': 'Nicolas', 'Nom': 'Mercier', 'Ville': 'Levis'}
                 ]

        table = QTableWidget()

        vbox = QVBoxLayout(self)
        vbox.addWidget(table)
        row_count = (len(users))
        column_count = (len(users[0]))

        table.setColumnCount(column_count)
        table.setRowCount(row_count)
        table.setHorizontalHeaderLabels((list(users[0].keys())))


        for row in range(row_count):  # add items from array to QTableWidget
            for column in range(column_count):
                item = (list(users[row].values())[column])
                table.setItem(row, column, QTableWidgetItem(item))



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = TableWidget()
    w.show()
    sys.exit(app.exec_())
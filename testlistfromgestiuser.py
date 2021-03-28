from gestionusers import *
from PyQt5 import QtCore, QtGui, QtWidgets

class GestUser(QtWidgets.QDialog, Ui_GestiUser): #Initialise gestionusers.py. Fenêtre de gestion des employés
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)

class Testlist():

    def testtable(self):
        self.tree = GestUser()
        users = [{'Prenom': 'Claude', 'Nom': 'Belanger', 'Ville': 'Levis'},
                 {'Prenom': 'Francis', 'Nom': 'Gariepy', 'Ville': 'Quebec'},
                 {'Prenom': 'Nicolas', 'Nom': 'Mercier', 'Ville': 'Levis'}
                 ]
        row_count = (len(users))
        column_count = (len(users[0]))


        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(
            ['Nom', 'Prenom', 'Sexe', 'Date Embauche', 'Code Usager', 'Mot de passe', 'Type Acces'])
        self.tree.treeView.header().setDefaultSectionSize(150)
        self.tree.treeView.setModel(self.model)


        def createModel(self):

            self.model = QtGui.QStandardItemModel()
            self.model.setHorizontalHeaderLabels(
                ['Nom', 'Prenom', 'Sexe', 'Date Embauche', 'Code Usager', 'Mot de passe', 'Type Acces'])
            self.treeView.header().setDefaultSectionSize(150)
            self.tree.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            self.treeView.setModel(self.model)


        self.tree.tableWidget.setColumnCount(column_count)
        self.tree.tableWidget.setRowCount(row_count)
        self.tree.tableWidget.setHorizontalHeaderLabels((list(users[0].keys())))
        self.tree.model.setHeaderData()

        for row in range(row_count):  # add items from array to QTableWidget
            for column in range(column_count):
                item = (list(users[row].values())[column])
                self.tree.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(item))
        self.tree.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    controller = Testlist()
    controller.testtable()
    sys.exit(app.exec_())
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import sys


data_for_tree = {"tomato":{"color":"red","amount":"10", "note":"a note for tomato"},"banana":{"color":"yellow","amount":"1", "note":"b note for banana"}, "some fruit":{"color":"unknown","amount":"100", "note":"some text"}}
datatest = [{"nom": "Administrateur", "prenom": "Admin", "sexe": "Masculin", "dateinscription": "01-01-0000", "courriel": "admin", "password": "admin123", "cartes": [{"numero": "12345678", "expiration": "12/04/03", "codecarte": "005"}]}]

class MainFrame(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.MyTreeView = QTreeView()
        self.MyTreeViewModel = QStandardItemModel()
        self.MyTreeView.setModel(self.MyTreeViewModel)
        self.most_used_cat_header = ['Nom', "Prénom", "Sexe", "Date Inscription", "Courriel Client", "Mot de passe"]
        self.MyTreeViewModel.setHorizontalHeaderLabels(self.most_used_cat_header)
        self.MyTreeView.setSortingEnabled(True)
        #self.MyTreeView_Fill()
        self.Testdata()

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

    def Testdata(self):
        for k in datatest:
            nom = QStandardItem(k["nom"])
            prenom = QStandardItem(k["prenom"])
            sexe = QStandardItem(k["sexe"])
            date = QStandardItem(k["dateinscription"])
            courriel = QStandardItem(k["courriel"])
            password = QStandardItem(k["password"])
            #cartes = QStandardItem(k["cartes"])
            tooltip = datatest(k["cartes"])
            nom.setToolTip(tooltip)
            prenom.setToolTip(tooltip)
            sexe.setToolTip(tooltip)
            date.setToolTip(tooltip)
            courriel.setToolTip(tooltip)
            password.setToolTip(tooltip)
            item = (nom, prenom, sexe, date, courriel, password)
            self.MyTreeViewModel.appendRow(item)


        """c = 0
        while c < len(self.most_used_cat_header):
            self.MyTreeView.resizeColumnToContents(c)
            c=c+1"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainFrame()
    main.show()
    main.move(app.desktop().screen().rect().center() - main.rect().center())
sys.exit(app.exec_())
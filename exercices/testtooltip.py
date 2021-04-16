from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import json

import sys


data_for_tree = {"tomato":{"color":"red","amount":"10", "note":"a note for tomato"},"banana":{"color":"yellow","amount":"1", "note":"b note for banana"}, "some fruit":{"color":"unknown","amount":"100", "note":"some text"}}
#datatest = [{"nom": "Belanger", "prenom": "Claude", "sexe": "Masculin", "dateinscription": "01-01-0000", "courriel": "admin", "motdepasse": "admin123", "cartes": [{"numero": "12345678", "expiration": "12/04/03", "codecarte": "005"}, {"numero": "987654321", "expiration": "12/05/06", "codecarte": "003"}]},{"nom": "Ouellet", "prenom": "Marie-Eve", "sexe": "Féminin", "dateinscription": "01-01-0000", "courriel": "admin", "motdepasse": "admin123", "cartes": [{"numero": "12345678", "expiration": "12/04/03", "codecarte": "005"}, {"numero": "1435345345", "expiration": "11/01/01", "codecarte": "001"}]}]

class MainFrame(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.MyTreeView = QTreeView()
        self.MyTreeViewModel = QStandardItemModel()
        self.MyTreeView.setModel(self.MyTreeViewModel)
        #self.header = ['Nom', "Prénom", "Sexe", "Date Inscription", "Courriel Client", "Mot de passe", "Numero de Carte", "Expiration", "Code secret"]
        self.headerfilm = ["Nom", "Durée", "Description", "Catégories", "Description Catégorie", "Nom de l'acteur",
                           "Prénom de l'acteur", "Sexe", "Nom du personnage", "Début de l'emploi", "Fin de l'emploi", "Cachet"]
        self.MyTreeViewModel.setHorizontalHeaderLabels(self.headerfilm)
        self.MyTreeView.setSortingEnabled(True)
        self.MyTreeView.setAlternatingRowColors(True)

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
        with open("../clients.json", "r") as f:
            datatest = json.load(f)
        with open("../films.json", "r") as f:
            datafilm = json.load(f)

            for g in datafilm:
                nom = QStandardItem(g["nom"])
                duree = QStandardItem(g["duree"])
                description = QStandardItem(g["description"])
                item = (nom, duree, description)
                self.MyTreeViewModel.appendRow(item)

                for dict in g["categories"]:
                    vide = QStandardItem("*****")
                    vide1 = QStandardItem("*****")
                    vide2 = QStandardItem("*****")
                    nomcat = QStandardItem(dict["nom"])
                    descripcat = QStandardItem(dict["description"])
                    childitem = (vide, vide1, vide2, nomcat, descripcat)
                    nom.appendRow(childitem)
                for dictact in g["acteurs"]:
                    text1 = QStandardItem("*****")
                    text2 = QStandardItem("*****")
                    text3 = QStandardItem("*****")
                    text4 = QStandardItem("*****")
                    text5 = QStandardItem("*****")
                    nomacteur = QStandardItem(dictact["nom"])
                    prenomacteur = QStandardItem(dictact["prenom"])
                    sexeacteur = QStandardItem(dictact["sexe"])
                    personnage = QStandardItem(dictact["nompersonnage"])
                    debutemploi = QStandardItem(dictact["debutemploi"])
                    finemploi = QStandardItem(dictact["finemploi"])
                    cachet = QStandardItem(dictact["cachet"])
                    childfilm = (text1, text2, text3, text4, text5, nomacteur, prenomacteur, sexeacteur, personnage, debutemploi, finemploi, cachet)
                    vide.appendRow(childfilm)


        """for k in datatest:
            nom = QStandardItem(k["nom"])
            prenom = QStandardItem(k["prenom"])
            sexe = QStandardItem(k["sexe"])
            date = QStandardItem(k["dateinscription"])
            courriel = QStandardItem(k["courriel"])
            password = QStandardItem(k["motdepasse"])
            item = (nom, prenom, sexe, date, courriel, password)
            self.MyTreeViewModel.appendRow(item)
            for dict in k["cartes"]:
                vide1 = QStandardItem("**")
                vide2 = QStandardItem("**")
                vide3 = QStandardItem("**")
                vide4 = QStandardItem("**")
                vide5 = QStandardItem("**")
                vide6 = QStandardItem("**")
                numero = QStandardItem(dict["numero"])
                expiration = QStandardItem(dict["expiration"])
                codecarte = QStandardItem(dict["codecarte"])
                childitem = (vide1, vide2, vide3, vide4,vide5, vide6, numero, expiration, codecarte)
                nom.appendRow(childitem)
                #tooltip = "Numéro de carte: {}, Date d'expiration: {}, Code secret: {}".format(numero.data(), expiration.data(), codecarte.data())
                #print(tooltip)
                #nom.setToolTip(tooltip)
                #for carte in k["cartes"] :
                    #tooltip = "Numéro de carte: {}, Date d'expiration: {}, Code secret: {}".format(carte["numero"], carte["expiration"], carte["codecarte"])
                    #nom.setToolTip(tooltip)"""




        """numero = QStandardItem("Numero")
        expiration = QStandardItem("Expiration")
        codecarte = QStandardItem("Code")
        childitem = (numero, expiration, codecarte)
        cartes.appendRow(childitem)"""

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
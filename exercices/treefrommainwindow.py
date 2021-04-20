from exercices.mainwindow import *
from PyQt5 import QtGui, QtWidgets
import json

class FenPrinci(QtWidgets.QMainWindow, Ui_MainWindow): #Initialise mainwindow.py. Fenêtre principale du logiciel.
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)


class controller:

    def loadclient(self):                   # Ouvre la liste de dictionnaires contenant les informations des clients
        try:
            with open("clients.json", "r") as f:
                self.dictclient = json.load(f)
        except Exception:
            pass

    def saveclient(self):                   # Sauvegarde le dictionnaire des usagers dans le fichier .json des clients
        try:
            with open("clients.json", "w") as f:
                data2 = json.dump(self.dictclient, f)
        except Exception:
            pass

    def mainwindow(self):
        self.loadclient()
        self.mainw = FenPrinci()
        self.mainw.show()
        self.treeViewModel = QtGui.QStandardItemModel()
        self.mainw.treeView.setModel(self.treeViewModel)
        self.header = ['Nom', "Prénom", "Sexe", "Date Inscription", "Courriel Client", "Mot de passe",
                                     "Numero de Carte", "Expiration", "Code secret"]
        self.treeViewModel.setHorizontalHeaderLabels(self.header)
        self.mainw.treeView.setSortingEnabled(True)
        self.mainw.treeView.setAlternatingRowColors(True)
        for k in self.dictclient:
            nom = QtGui.QStandardItem(k["nom"])
            prenom = QtGui.QStandardItem(k["prenom"])
            sexe = QtGui.QStandardItem(k["sexe"])
            date = QtGui.QStandardItem(k["dateinscription"])
            courriel = QtGui.QStandardItem(k["courriel"])
            password = QtGui.QStandardItem(k["motdepasse"])
            item = (nom, prenom, sexe, date, courriel, password)
            self.treeViewModel.appendRow(item)
            for dict in k["cartes"]:
                vide1 = QtGui.QStandardItem("*****")
                vide2 = QtGui.QStandardItem("*****")
                vide3 = QtGui.QStandardItem("*****")
                vide4 = QtGui.QStandardItem("*****")
                vide5 = QtGui.QStandardItem("*****")
                vide6 = QtGui.QStandardItem("*****")
                numero = QtGui.QStandardItem(dict["numero"])
                expiration = QtGui.QStandardItem(dict["expiration"])
                codecarte = QtGui.QStandardItem(dict["codecarte"])
                childitem = (vide1, vide2, vide3, vide4, vide5, vide6, numero, expiration, codecarte)
                nom.appendRow(childitem)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    controller = controller()
    controller.mainwindow()
    sys.exit(app.exec_())
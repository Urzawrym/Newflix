from gestionusers import *
from PyQt5 import QtCore, QtGui, QtWidgets

class GestUser(QtWidgets.QDialog, Ui_GestiUser): #Initialise gestionusers.py. Fenêtre de gestion des employés
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)

class Testlist():

    def testtable(self):
        self.tree = GestUser()
        users = [{"nom": "Administrateur", "prenom": "Admin", "sexe": "Masculin", "dateembauche": "01/01/00", "codeutilisateur": "admin", "password": "admin123", "acces": "Admin"}, {"nom": "", "prenom": "", "sexe": "Masculin", "dateembauche": "01/01/00", "codeutilisateur": "user1", "password": "password1", "acces": "Lecture"}, {"nom": "Claude", "prenom": "Belanger", "sexe": "Masculin", "dateembauche": "18/05/83", "codeutilisateur": "claude", "password": "1234", "acces": "Lecture"}, {"nom": "Mathieu", "prenom": "Royer", "sexe": "Masculin", "dateembauche": "17/12/84", "codeutilisateur": "mathieu", "password": "royer", "acces": "Modification"}, {"nom": "Meo", "prenom": "Ouellet", "sexe": "Feminin", "dateembauche": "17/12/84", "codeutilisateur": "meo", "password": "0987", "acces": "Modification"}, {"nom": "Meo", "prenom": "Ouellet", "sexe": "Feminin", "dateembauche": "1984-05-13", "codeutilisateur": "franky", "password": "0987", "acces": "Lecture"}, {"nom": "", "prenom": "", "sexe": "Masculin", "dateembauche": "2000-01-01", "codeutilisateur": "test", "password": "1234", "acces": "Lecture"}, {"nom": "", "prenom": "", "sexe": "Masculin", "dateembauche": "2000-01-01", "codeutilisateur": "meo2", "password": "1234", "acces": "Lecture"}, {"nom": "d", "prenom": "d", "sexe": "Masculin", "dateembauche": "2000-01-01", "codeutilisateur": "d", "password": "1234", "acces": "Lecture"}]
        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(
            ['Nom', 'Prenom', 'Sexe', 'Date Embauche', 'Code Usager', 'Mot de passe', 'Type Acces'])
        self.tree.treeView.header().setDefaultSectionSize(150)
        self.tree.treeView.setModel(self.model)
        self.tree.show()
        self.tree.pushButton_2.clicked.connect(self.onClickedRow)


        #self.model.setrowCount(0)


        root = self.model.invisibleRootItem()

        parent = root

        for a in (users):
            parent.appendRow([QtGui.QStandardItem(a['nom']), QtGui.QStandardItem(a['prenom']),
                              QtGui.QStandardItem(a['sexe']), QtGui.QStandardItem(a['dateembauche']),
                              QtGui.QStandardItem(a['codeutilisateur']), QtGui.QStandardItem(a['password']),
                              QtGui.QStandardItem(a['acces'])])

    def onClickedRow(self, index):



        for ix in self.tree.treeView.selectedIndexes():
            if ix.column() == 1:
                text1 = ix.data()
                print(text1)
            elif ix.column() == 2:
                text2 = ix.data()
                print(text2)






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    controller = Testlist()
    controller.testtable()
    sys.exit(app.exec_())
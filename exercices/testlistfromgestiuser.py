from gestionusers import *
from popupuser import *
from PyQt5 import QtCore, QtGui, QtWidgets

class GestUser(QtWidgets.QDialog, Ui_GestiUser): #Initialise gestionusers.py. Fenêtre de gestion des employés
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)

class FormUser(QtWidgets.QDialog, Ui_FormUser): #Initialise popupuser.py. Formulaire pour créer/modifier un employé
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)

class Testlist():

    def testtable(self):
        self.tree = GestUser()
        users = [{"nom": "Administrateur", "prenom": "Admin", "sexe": "Masculin", "dateembauche": "01-01-0000", "codeutilisateur": "admin", "password": "admin123", "acces": "Admin"}, {"nom": "", "prenom": "", "sexe": "Masculin", "dateembauche": "01-01-0000", "codeutilisateur": "user1", "password": "password1", "acces": "Lecture"}, {"nom": "Claude", "prenom": "Belanger", "sexe": "Masculin", "dateembauche": "18-05-1983", "codeutilisateur": "claude", "password": "1234", "acces": "Lecture"}, {"nom": "Royer", "prenom": "Mathieu", "sexe": "Masculin", "dateembauche": "17-12-1984", "codeutilisateur": "mathieu", "password": "royer", "acces": "Modification"}, {"nom": "Meo", "prenom": "Ouellet", "sexe": "F\u00e9minin", "dateembauche": "17-12-1984", "codeutilisateur": "meo", "password": "0987", "acces": "Modification"}, {"nom": "Meo", "prenom": "Ouellet", "sexe": "F\u00e9minin", "dateembauche": "13-05-1984", "codeutilisateur": "franky", "password": "0987", "acces": "Lecture"}, {"nom": "", "prenom": "", "sexe": "Masculin", "dateembauche": "01-01-2000", "codeutilisateur": "test", "password": "1234", "acces": "Lecture"}, {"nom": "", "prenom": "", "sexe": "Masculin", "dateembauche": "01-01-2000", "codeutilisateur": "meo2", "password": "1234", "acces": "Lecture"}, {"nom": "d", "prenom": "d", "sexe": "Masculin", "dateembauche": "01-01-2000", "codeutilisateur": "d", "password": "1234", "acces": "Lecture"}]
        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(
            ['Nom', 'Prenom', 'Sexe', 'Date Embauche', 'Code Usager', 'Mot de passe', 'Type Acces'])
        self.tree.treeView.header().setDefaultSectionSize(150)
        self.tree.treeView.setModel(self.model)
        self.tree.show()
        self.tree.pushButton_2.clicked.connect(self.onClickedRow)

        root = self.model.invisibleRootItem()
        parent = root
        for a in (users):
            parent.appendRow([QtGui.QStandardItem(a['nom']), QtGui.QStandardItem(a['prenom']),
                              QtGui.QStandardItem(a['sexe']), QtGui.QStandardItem(a['dateembauche']),
                              QtGui.QStandardItem(a['codeutilisateur']), QtGui.QStandardItem(a['password']),
                              QtGui.QStandardItem(a['acces'])])



    def onClickedRow(self):
        self.showpopusager = FormUser()
        self.showpopusager.show()

        donnees = [a.data() for a in self.tree.treeView.selectedIndexes()] #Créé une liste avec les infos de la ligne
        self.showpopusager.lineEdit.setText(donnees[0])
        self.showpopusager.lineEdit_2.setText(donnees[1])

        date = QtCore.QDate.fromString(donnees[3], "dd-MM-yyyy")
        self.showpopusager.dateEdit.setDate(date)
        index = self.showpopusager.comboBox.findText(donnees[2], QtCore.Qt.MatchFlag.MatchFixedString)
        self.showpopusager.comboBox.setCurrentIndex(index)

        #print(type(index))







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    controller = Testlist()
    controller.testtable()
    sys.exit(app.exec_())
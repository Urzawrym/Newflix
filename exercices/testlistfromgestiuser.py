from gestionusers import *
from popupuser import *
from PyQt5 import QtCore, QtGui, QtWidgets
from classes import *

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
        self.users = [{"nom": "Administrateur", "prenom": "Admin", "sexe": "Masculin", "dateembauche": "01-01-0000", "codeutilisateur": "admin", "password": "admin123", "acces": "Admin"}, {"nom": "", "prenom": "", "sexe": "Masculin", "dateembauche": "01-01-0000", "codeutilisateur": "user1", "password": "password1", "acces": "Lecture"}, {"nom": "Claude", "prenom": "Belanger", "sexe": "Masculin", "dateembauche": "18-05-1983", "codeutilisateur": "claude", "password": "1234", "acces": "Lecture"}, {"nom": "Royer", "prenom": "Mathieu", "sexe": "Masculin", "dateembauche": "17-12-1984", "codeutilisateur": "mathieu", "password": "royer", "acces": "Modification"}, {"nom": "Meo", "prenom": "Ouellet", "sexe": "F\u00e9minin", "dateembauche": "17-12-1984", "codeutilisateur": "meo", "password": "0987", "acces": "Modification"}, {"nom": "Meo", "prenom": "Ouellet", "sexe": "F\u00e9minin", "dateembauche": "13-05-1984", "codeutilisateur": "franky", "password": "0987", "acces": "Lecture"}, {"nom": "", "prenom": "", "sexe": "Masculin", "dateembauche": "01-01-2000", "codeutilisateur": "test", "password": "1234", "acces": "Lecture"}, {"nom": "", "prenom": "", "sexe": "Masculin", "dateembauche": "01-01-2000", "codeutilisateur": "meo2", "password": "1234", "acces": "Lecture"}, {"nom": "d", "prenom": "d", "sexe": "Masculin", "dateembauche": "01-01-2000", "codeutilisateur": "d", "password": "1234", "acces": "Lecture"}]
        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(
            ['Nom', 'Prenom', 'Sexe', 'Date Embauche', 'Code Usager', 'Mot de passe', 'Type Acces'])
        self.tree.treeView.header().setDefaultSectionSize(150)
        self.tree.treeView.setModel(self.model)
        self.tree.show()
        self.tree.pushButton_2.clicked.connect(self.modifpopup)
        self.tree.pushButton.clicked.connect(self.showpopuser)
        self.tree.pushButton_3.clicked.connect(self.deleteuser)

        root = self.model.invisibleRootItem()
        self.parent = root
        for a in (self.users):
            self.parent.appendRow([QtGui.QStandardItem(a['nom']), QtGui.QStandardItem(a['prenom']),
                              QtGui.QStandardItem(a['sexe']), QtGui.QStandardItem(a['dateembauche']),
                              QtGui.QStandardItem(a['codeutilisateur']), QtGui.QStandardItem(a['password']),
                              QtGui.QStandardItem(a['acces'])])

    def showpopuser(self): #Ouvre le formulaire pour créer un nouvel employé ou le modifier
        self.showpopusager = FormUser()  #Importe la fenêtre de formulaire de l'usager
        self.showpopusager.show()        #L'affiche
        self.showpopusager.pushButton.clicked.connect(self.saveuser) #Active le test de sauvegarde si bouton utilisé
        self.showpopusager.pushButton_2.clicked.connect(self.showpopusager.close) #Ferme la fenêtre sans sauvegarder

    def saveuser(self):

        #Ici j'utilise la classe Employe héritée de la classe Personne pour inscrire les données du formulaire dans
        #une liste de dictionnaire. Chaque dict = 1 usager. La liste est ensuite enregistrée dans un fichier json crypté
        employee=Employe(self.showpopusager.lineEdit.text(), self.showpopusager.lineEdit_2.text(),
                         self.showpopusager.comboBox.currentText(), self.showpopusager.dateEdit.text(),
                         self.showpopusager.lineEdit_3.text(), self.showpopusager.lineEdit_5.text(),
                         self.showpopusager.comboBox_2.currentText())
        dictemployee=vars(employee)
        if self.showpopusager.lineEdit.text() == "" or self.showpopusager.lineEdit_2.text() == "" or \
                    self.showpopusager.lineEdit_3.text() == "" or self.showpopusager.lineEdit_5.text() == "":
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Veuillez compléter les informations manquantes")
            msg.setInformativeText('')
            msg.setWindowTitle("Erreur")
            msg.exec_()
        elif any(d["codeutilisateur"] == self.showpopusager.lineEdit_3.text() for d in self.users):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Code utilisateur déjà utilisé")
            msg.setInformativeText('')
            msg.setWindowTitle("Erreur")
            msg.exec_()
        else:
            self.parent.appendRow([QtGui.QStandardItem(dictemployee['nom']), QtGui.QStandardItem(dictemployee['prenom']),
                              QtGui.QStandardItem(dictemployee['sexe']), QtGui.QStandardItem(dictemployee['dateembauche']),
                              QtGui.QStandardItem(dictemployee['codeutilisateur']), QtGui.QStandardItem(dictemployee['password']),
                              QtGui.QStandardItem(dictemployee['acces'])])


    def modifpopup(self):
        self.showpopusager = FormUser()
        self.showpopusager.show()
        self.showpopusager.pushButton.clicked.connect(self.modifusager)
        self.showpopusager.pushButton_2.clicked.connect(self.showpopusager.close)
        donnees = [a.data() for a in self.tree.treeView.selectedIndexes()] #Créé une liste avec les infos de la ligne
        self.showpopusager.lineEdit.setText(donnees[0])
        self.showpopusager.lineEdit_2.setText(donnees[1])
        index = self.showpopusager.comboBox.findText(donnees[2], QtCore.Qt.MatchFlag.MatchFixedString)
        self.showpopusager.comboBox.setCurrentIndex(index)  # Converti le format texte de l'item en index de la boite
        date = QtCore.QDate.fromString(donnees[3], "dd-MM-yyyy") #Converti le texte de la date en format Date
        self.showpopusager.dateEdit.setDate(date)
        self.showpopusager.lineEdit_3.setText(donnees[4])
        self.showpopusager.lineEdit_3.setEnabled(False)
        self.showpopusager.lineEdit_5.setText(donnees[5])
        index2 = self.showpopusager.comboBox_2.findText(donnees[6], QtCore.Qt.MatchFlag.MatchFixedString)
        self.showpopusager.comboBox_2.setCurrentIndex(index2)  # Converti le format texte de l'item en index de la boite

    def modifusager(self):
        indexes = self.tree.treeView.selectedIndexes()


    def deleteuser(self):
       indexes = self.tree.treeView.selectedIndexes()
       if indexes:
        index = indexes[0] #L'idndex correspond à la liste des items de la rangée
        self.model.removeRow(index.row()) #Enlève l'item







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    controller = Testlist()
    controller.testtable()
    sys.exit(app.exec_())
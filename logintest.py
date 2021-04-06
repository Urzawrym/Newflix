from PyQt5 import QtCore, QtGui, QtWidgets
import json
import sys
from mainwindow import *        #Importe l'affichage de la fenêtre principale
from gestionusers import *      #Importe l'affichage de la fenêtre gestion usager
from popupuser import *         #Importe le formulaire de création/modification d'usager
from popupcustomer import *     #Importe le formulaire de création/modification de client
from logindialog import *       #Importe la fenêtre de connexion du démarrage du logiciel
from classes import *            #Importe les classes Personnes, Employés, Clients, Cartes crédits, films, Categorie
                                 #avec toute la gestion des héritages entre les classes, tel que demandé dans la mise
                                 #en situation

#from cryptography.fernet import Fernet

"""key = Fernet.generate_key()
file = open('key.key','wb')
file.write(key)
file.close()

file = open('key.key','rb')
key = file.read()
file.close()"""
################## Aucune classe provenant de QT Designer n'est modifiée. Ici on créé les classes ##################
################## localement qui importent et initialisent les classes provenant de QT Designer. ##################

class FenPrinci(QtWidgets.QMainWindow, Ui_MainWindow): #Initialise mainwindow.py. Fenêtre principale du logiciel.
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

class GestUser(QtWidgets.QDialog, Ui_GestiUser): #Initialise gestionusers.py. Fenêtre de gestion des employés
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)

class FormUser(QtWidgets.QDialog, Ui_FormUser): #Initialise popupuser.py. Formulaire pour créer/modifier un employé
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)

class Connexion(QtWidgets.QDialog, Ui_Connexion): #Initialise logindialog.py. Fenêtre de connexion au démarrage
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)

class Controller: #C'est dans cette classe que l'action se passe, toutes les modifications visuelles et les
                  #les interactions avec l'utilisateur vont se faire à partir d'ici.

    def loaduser(self):
        try:
            with open("testuser.json","r") as f:  # Ouvre la liste de dictionnaires contenant les identifiants des
                self.dictuser = json.load(f)           # usagers. 3 données sont utilisées: user,password,type d'acces
        except Exception:
            pass

    def saveuser(self):
        try:
            with open("testuser.json", "w") as f:  # Ouvre la liste de dictionnaires contenant les identifiants des
                data = json.dump(self.dictuser,f)
        except Exception:
            pass

    def showlogin(self):
        self.connex = Connexion() #Importe la classe  Connexion
        self.connex.pushButton.clicked.connect(self.testconnex) #Le bouton activera la fonction de tester la connex.
        self.connex.show() #Affichage la fenêtre de connexion

    def testconnex(self):
        self.loaduser()
        logged_in = False                 #par défaut la connexion est fausse avant le démarrer la boucle
        self.mesgexcept = ""   #Va servir pour l'exception du try
        try:   #Défini un try avant de démarrer la boucle
            while not logged_in:                  #Démarre la boucle.
                for a in (self.dictuser): # Dans toute la liste, vérifie chaque dict. pour retrouver les 3 mêmes paramètres
                    if a['codeutilisateur'] == self.connex.lineEdit.text() and \
                            a['password'] == self.connex.lineEdit_2.text() and a["acces"] == "Admin":
                        self.adminwindow()
                        #Si les 3 inputs de l'usager correspond à un dict. avec accès admin, active modifwindow
                        logged_in = True   #Le "true" met fin à la boucle.
                    elif a['codeutilisateur'] == self.connex.lineEdit.text() and \
                            a['password'] == self.connex.lineEdit_2.text() and a["acces"] == "Modification":
                        self.modifwindow()
                        #Si les 3 inputs de l'usager correspond à un dict. avec accès modif, active modifwindow
                        logged_in = True #Ferme la boucle
                    elif a['codeutilisateur'] == self.connex.lineEdit.text() and \
                            a['password'] == self.connex.lineEdit_2.text() and a["acces"] == "Lecture":
                        self.viewwindow()
                        #Si les 3 inputs de l'usager correspond à un dict. avec accès lecture, active modifwindow
                        logged_in = True #Ferme la boucle
                if logged_in is not True: #Si la boucle n'est toujours pas fermée après les 3 premiers tests, fait
                    msg = QtWidgets.QMessageBox() #Affiche une fenêtre qui mentionne que les identifiants sont erronés
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setText("Identifiants erronés")
                    msg.setInformativeText('')
                    msg.setWindowTitle("Erreur")
                    msg.exec_()
                    self.connex.lineEdit.setFocus() #Remet le focus du clavier sur la ligne de l'usager
                    break #Casse la boucle car aucun identifiant n'a fonctionné
        except Exception: #Si la boucle n'a pas fonctionné
            pass

    def adminwindow(self):
        self.admin = FenPrinci()        #Importe la fenêtre principale
        self.admin.show()               #L'affiche la fenêtre principale
        self.connex.lineEdit.clear()    #Vide la ligne usager de la fenêtre de connexion
        self.connex.lineEdit_2.clear()  #Vide la ligne mot de passe de la fenêtre de connexion
        self.connex.lineEdit.setFocus() #Met le focus sur la ligne usager de la fenêtre de connexion
        self.connex.hide()              #Cache la fenêtre de connexion
        self.admin.actionGestion.triggered.connect(self.showgestuser) #Dans la fen. principale, trigger la gestion users
        self.admin.actionDeconnexion.triggered.connect(self.logout) #Trigger la déconnexion du logiciel
        self.admin.actionQuitter.triggered.connect(self.closeall) #Trigger la fermeture du logiciel

    def modifwindow(self):
        self.modif = FenPrinci()                       #Fait la même chose que la fonction précédente
        self.modif.actionGestion.setVisible(False)     #Cache le bouton Gestion Usagés du menu principal
        self.modif.show()
        self.connex.lineEdit.clear()
        self.connex.lineEdit_2.clear()
        self.connex.lineEdit.setFocus()
        self.connex.hide()
        self.modif.actionDeconnexion.triggered.connect(self.logout)
        self.modif.actionQuitter.triggered.connect(self.closeall)

    def viewwindow(self):
        self.view = FenPrinci()                        #Fait la même chose que la fonction précédente
        self.view.actionGestion.setVisible(False)
        self.view.pushButton.hide()                    #Cache les 6 boutons ajouter/modifier/supprimer de la
        self.view.pushButton_2.hide()                  #fenêtre principale pour permettre un accès en lecture
        self.view.pushButton_3.hide()                  #seulement des listes de clients et de films.
        self.view.pushButton_4.hide()
        self.view.pushButton_5.hide()
        self.view.pushButton_6.hide()
        self.view.show()
        self.connex.lineEdit.clear()
        self.connex.lineEdit_2.clear()
        self.connex.lineEdit.setFocus()
        self.connex.hide()
        self.view.actionDeconnexion.triggered.connect(self.logout)
        self.view.actionQuitter.triggered.connect(self.closeall)

    def showgestuser(self):
        self.showgest = GestUser()  #Importe la fenêtre de gestion des usagers
        self.showgest.pushButton.clicked.connect(self.showpopuser) #Ouvre le formulaire d'usager si on appuie
        self.showgest.pushButton_2.clicked.connect(self.modifpopup) #Ouvre le formulaire pour modifier l'usager
        self.showgest.pushButton_3.clicked.connect(self.deleteuser) #Envoie vers la fonction supprimer usager
        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Nom', 'Prenom', 'Sexe', 'Date Embauche', 'Code Usager',
                                              'Mot de passe', 'Type Acces'])
        self.showgest.treeView.setModel(self.model)  # Active le modèle
        self.showgest.show()  # Affiche le tableau

        self.mesgexcept = ""  # Va servir pour l'exception du try
        root = self.model.invisibleRootItem()  # Sert à rendre invisible l'entête "parent" de l'arbre
        self.parent = root
        try:  # Défini un try avant de démarrer la boucle
            for a in (self.dictuser):  # Pour chaque dictionnaire dans la liste, on créé une ligne avec les informations ci bas
                self.parent.appendRow([QtGui.QStandardItem(a['nom']), QtGui.QStandardItem(a['prenom']),
                                  QtGui.QStandardItem(a['sexe']), QtGui.QStandardItem(a['dateembauche']),
                                  QtGui.QStandardItem(a['codeutilisateur']), QtGui.QStandardItem(a['password']),
                                  QtGui.QStandardItem(a['acces'])])     #Ajoute chaque information dans les colonnes.
        except Exception:  #Si la boucle n'a pas fonctionné, stop la boucle
            pass

    def logout(self):

        app.closeAllWindows()       #Ferme toutes les fenêtres et l'application
        self.connex.show()          #Démarre l'affichage de la fenêtre de connexion

    def closeall(self):
        app.closeAllWindows()       #Ferme toutes les fenêtres et l'application

    def showpopuser(self): #Ouvre le formulaire pour créer un nouvel employé ou le modifier
        self.showpopusager = FormUser()  #Importe la fenêtre de formulaire de l'usager
        self.showpopusager.show()        #L'affiche
        self.showpopusager.pushButton.clicked.connect(self.savinguser) #Active le test de sauvegarde si bouton utilisé
        self.showpopusager.pushButton_2.clicked.connect(self.showpopusager.close) #Ferme la fenêtre sans sauvegarder


    def savinguser(self):
        #Ici j'utilise la classe Employe héritée de la classe Personne pour inscrire les données du formulaire dans
        #une liste de dictionnaire. Chaque dict = 1 usager. La liste est ensuite enregistrée dans un fichier json crypté
        employee=Employe(self.showpopusager.lineEdit.text(), self.showpopusager.lineEdit_2.text(),
                         self.showpopusager.comboBox.currentText(), self.showpopusager.dateEdit.text(),
                         self.showpopusager.lineEdit_3.text(), self.showpopusager.lineEdit_5.text(),
                         self.showpopusager.comboBox_2.currentText())
        self.dictemployee=vars(employee)
        if self.showpopusager.lineEdit.text() == "" or self.showpopusager.lineEdit_2.text() == "" or \
                    self.showpopusager.lineEdit_3.text() == "" or self.showpopusager.lineEdit_5.text() == "":
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Veuillez compléter les informations manquantes")
            msg.setInformativeText('')
            msg.setWindowTitle("Erreur")
            msg.exec_()
        elif any(d["codeutilisateur"] == self.showpopusager.lineEdit_3.text() for d in self.dictuser):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Code utilisateur déjà utilisé")
            msg.setInformativeText('')
            msg.setWindowTitle("Erreur")
            msg.exec_()

        else:
            self.parent.appendRow(
                    [QtGui.QStandardItem(self.dictemployee['nom']),
                     QtGui.QStandardItem(self.dictemployee['prenom']),
                     QtGui.QStandardItem(self.dictemployee['sexe']),
                     QtGui.QStandardItem(self.dictemployee['dateembauche']),
                     QtGui.QStandardItem(self.dictemployee['codeutilisateur']),
                     QtGui.QStandardItem(self.dictemployee['password']),
                     QtGui.QStandardItem(self.dictemployee['acces'])])
            self.dictuser.append(self.dictemployee)
            self.saveuser()
            self.showpopusager.close()

    def modifpopup(self):
        self.donnees = [a.data() for a in self.showgest.treeView.selectedIndexes()] #Créé une liste des données sélectionées
        if self.donnees == [] :
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Veuillez choisir un usager à modifier")
            msg.setInformativeText('')
            msg.setWindowTitle("Erreur")
            msg.exec_()
        elif self.donnees[4] == "admin":
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("L'administrateur système ne peut être modifié")
            msg.setInformativeText('')
            msg.setWindowTitle("Erreur")
            msg.exec_()
        else:
            self.showpopusager = FormUser()
            self.showpopusager.show()
            self.showpopusager.pushButton.clicked.connect(self.modifuser)
            self.showpopusager.pushButton_2.clicked.connect(self.showpopusager.close)
            index = self.showpopusager.comboBox.findText(self.donnees[2],QtCore.Qt.MatchFlag.MatchFixedString)  # Converti en int
            date = QtCore.QDate.fromString(self.donnees[3], "dd-MM-yyyy")  # Converti le texte de la date en format Date
            index2 = self.showpopusager.comboBox_2.findText(self.donnees[6],QtCore.Qt.MatchFlag.MatchFixedString)  # Conv. en int
            self.showpopusager.lineEdit_3.setEnabled(False)
            self.updateduser=Employe(
            self.showpopusager.lineEdit.setText(self.donnees[0]),          #Affiche la donnée de la colonne 0 dans la lineedit
            self.showpopusager.lineEdit_2.setText(self.donnees[1]),        #Affiche la donnée de la colonne 1 dans la lineedit_2
            self.showpopusager.comboBox.setCurrentIndex(index),       #Affiche l'index correspondant au int
            self.showpopusager.dateEdit.setDate(date),                #Affiche la date sélectionnée
            self.showpopusager.lineEdit_3.setText(self.donnees[4]),        #Affiche le nom d'utilisateur provenant de la colonne4
            self.showpopusager.lineEdit_5.setText(self.donnees[5]),        #Affiche le mot de passe provenant de la colonne5
            self.showpopusager.comboBox_2.setCurrentIndex(index2))  #Affiche l'index correspondant au int

    def modifuser(self):

        changeusager = next(
            item for item in self.dictuser if item['codeutilisateur'] == self.showpopusager.lineEdit_3.text())
        changeusager['nom'] = self.showpopusager.lineEdit.text()
        changeusager['prenom'] = self.showpopusager.lineEdit_2.text()
        changeusager['sexe'] = self.showpopusager.comboBox.currentText()
        changeusager['dateembauche'] = self.showpopusager.dateEdit.text()
        changeusager['password'] = self.showpopusager.lineEdit_5.text()
        changeusager['acces'] = self.showpopusager.comboBox_2.currentText()
        #self.model.endResetModel()
        self.showgestuser()
        #self.showgest.treeView.

        self.showpopusager.close()
        #self.model.dataChanged(QtCore.QModelIndex(), QtCore.QModelIndex())
        self.saveuser()


    def deleteuser(self):
        donnees = [a.data() for a in self.showgest.treeView.selectedIndexes()]  # Créé une liste des données sélectionées
        if donnees[4] == "admin":
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("L'administrateur système ne peut être supprimé")
            msg.setInformativeText('')
            msg.setWindowTitle("Erreur")
            msg.exec_()
        else: self.testdelete()

    def testdelete(self):
        box = QtWidgets.QMessageBox()
        box.setIcon(QtWidgets.QMessageBox.Question)
        box.setWindowTitle('Confirmation')
        box.setText('Êtes vous sûr de vouloir supprimer cet utilisateur?')
        box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        buttonY = box.button(QtWidgets.QMessageBox.Yes)
        buttonY.setText('Oui')
        buttonN = box.button(QtWidgets.QMessageBox.No)
        buttonN.setText('Non')
        box.exec_()

        if box.clickedButton() == buttonY:
            self.yesdelete()
        elif box.clickedButton() == buttonN:
            pass

    def yesdelete(self):
        indexes = self.showgest.treeView.selectedIndexes()
        donnees = [a.data() for a in self.showgest.treeView.selectedIndexes()]
        if indexes:
            index = indexes[0]  # L'index correspond à la liste des items de la rangée
            self.model.removeRow(index.row())  # Enlève l'item
            self.dictuser = [element for element in self.dictuser if element.get('codeutilisateur', '') != donnees[4]]
            self.saveuser()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.showlogin()
    sys.exit(app.exec_())
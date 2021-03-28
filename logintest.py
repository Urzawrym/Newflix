from PyQt5 import QtCore, QtGui, QtWidgets
import json
import sys
from mainwindow import *
from gestionusers import *
from popupuser import *
from popupcustomer import *
from logindialog import *
from classes import *

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

    def showlogin(self):
        self.connex = Connexion() #Importe la classe  Connexion
        self.connex.pushButton.clicked.connect(self.testconnex) #Le bouton activera la fonction de tester la connex.
        self.connex.show() #Affichage la fenêtre de connexion

    def testconnex(self):
        with open("testuser.json", "r") as f: #Ouvre la liste de dictionnaires contenant les identifiants des
            dicto = json.load(f)              #usagers. 3 données sont utilisées: user,password,type d'acces
            logged_in = False                 #par défaut la connexion est fausse avant le démarrer la boucle
            self.mesgexcept = ""   #Va servir pour l'exception du try
        try:   #Défini un try avant de démarrer la boucle
            while not logged_in:                  #Démarre la boucle.
                for a in (dicto): # Dans toute la liste, vérifie chaque dict. pour retrouver les 3 mêmes paramètres
                    if self.connex.lineEdit.text() == "admin" and self.connex.lineEdit_2.text() == "admin123":
                        self.adminwindow() #Si les 2 inputs de l'usager sont les mêmes, activer la fonction adminwindow
                        logged_in = True   #Le "true" met fin à la boucle.
                    elif a['codeutilisateur'] == self.connex.lineEdit.text() and \
                            a['password'] == self.connex.lineEdit_2.text() and a["acces"] == "Modification":
                        self.modifwindow() #Si les 3 inputs de l'usager correspond à un dict., active modifwindow
                        logged_in = True #Ferme la boucle
                    elif a['codeutilisateur'] == self.connex.lineEdit.text() and \
                            a['password'] == self.connex.lineEdit_2.text() and a["acces"] == "Lecture":
                        self.viewwindow() #Si les 3 inputs de l'usager correspond à un dict., active viewwindow
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
        except Exception as e: #Si la boucle n'a pas fonctionné, affiche ce message
            self.mesgexcept = "Une erreur est survenue" +e

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
        self.showgest.pushButton.clicked.connect(self.showpopuser) #Ouvre le formulaire
        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Nom', 'Prenom', 'Sexe', 'Date Embauche', 'Code Usager',
                                              'Mot de passe', 'Type Acces'])
        self.showgest.treeView.header().setDefaultSectionSize(150)  # Défini la largeur des colonnes
        self.showgest.treeView.setModel(self.model)  # Active le modèle
        self.showgest.show()  # Affiche le tableau

        with open("testuser.json", "r") as f:  # Ouvre la liste de dictionnaires contenant les informations des
            dicto = json.load(f)  # usagers.
            self.mesgexcept = ""  # Va servir pour l'exception du try

        root = self.model.invisibleRootItem()  # Sert à rendre invisible l'entête "parent" de l'arbre
        parent = root
        try:  # Défini un try avant de démarrer la boucle
            for a in (dicto):  # Pour chaque dictionnaire dans la liste, on créé une ligne avec les informations ci bas
                parent.appendRow([QtGui.QStandardItem(a['nom']), QtGui.QStandardItem(a['prenom']),
                                  QtGui.QStandardItem(a['sexe']), QtGui.QStandardItem(a['dateembauche']),
                                  QtGui.QStandardItem(a['codeutilisateur']), QtGui.QStandardItem(a['password']),
                                  QtGui.QStandardItem(a['acces'])])
        except Exception as e:  # Si la boucle n'a pas fonctionné, affiche ce message
            self.mesgexcept = "Une erreur est survenue" + e

    def logout(self):
        app.closeAllWindows()       #Ferme toutes les fenêtres et l'application
        self.connex.show()          #Démarrer l'affichage de la fenêtre de connexion

    def closeall(self):
        app.closeAllWindows()       #Ferme toutes les fenêtres et l'application

    """def showlistuser(self):  # Va servir à afficher les usagers dans la fenêtre de la liste
        self.tree = GestUser() #J'importe la fenêtre des usagers. Je vais préparer l'arbre ci bas plutôt que dans l'UI
        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Nom', 'Prenom', 'Sexe', 'Date Embauche', 'Code Usager',
                                              'Mot de passe', 'Type Acces'])
        self.tree.treeView.header().setDefaultSectionSize(150) #Défini la largeur des colonnes
        self.tree.treeView.setModel(self.model)                #Active le modèle
        #self.tree.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers) #Empêche les usagers de modifie le tableau
        self.tree.show()                                       #Affiche le tableau

        with open("testuser.json", "r") as f:   # Ouvre la liste de dictionnaires contenant les informations des
            dicto = json.load(f)                # usagers.
            self.mesgexcept = ""  # Va servir pour l'exception du try


        root = self.model.invisibleRootItem()       #Sert à rendre invisible l'entête "parent" de l'arbre
        parent = root
        try:                                            #Défini un try avant de démarrer la boucle
            for a in (dicto): #Pour chaque dictionnaire dans la liste, on créé une ligne avec les informations ci bas
                parent.appendRow([QtGui.QStandardItem(a['nom']), QtGui.QStandardItem(a['prenom']),
                                  QtGui.QStandardItem(a['sexe']), QtGui.QStandardItem(a['dateembauche']),
                                  QtGui.QStandardItem(a['codeutilisateur']), QtGui.QStandardItem(a['password']),
                                  QtGui.QStandardItem(a['acces'])])
        except Exception as e:    #Si la boucle n'a pas fonctionné, affiche ce message
            self.mesgexcept = "Une erreur est survenue" + e"""

    def showpopuser(self): #Ouvre le formulaire pour créer un nouvel employé ou le modifier
        self.showpopusager = FormUser()  #Importe la fenêtre de formulaire de l'usager
        self.showpopusager.show()        #L'affiche
        self.showpopusager.pushButton.clicked.connect(self.saveuser) #Active le test de sauvegarde si bouton utilisé
        self.showpopusager.pushButton_2.clicked.connect(self.showpopusager.close) #Ferme la fenêtre sans sauvegarder


    def saveuser(self):
        employee=Employe(self.showpopusager.lineEdit.text(), self.showpopusager.lineEdit_2.text(),
                         self.showpopusager.comboBox.currentText(), self.showpopusager.dateEdit.text(),
                         self.showpopusager.lineEdit_3.text(), self.showpopusager.lineEdit_5.text(),
                         self.showpopusager.comboBox_2.currentText())
        dictemployee=vars(employee)
        with open("testuser.json", "r") as f:
            dic = json.load(f)
            if self.showpopusager.lineEdit.text() == "" or self.showpopusager.lineEdit_2.text() == "" or \
                    self.showpopusager.lineEdit_3.text() == "" or self.showpopusager.lineEdit_5.text() == "":
               msg = QtWidgets.QMessageBox()
               msg.setIcon(QtWidgets.QMessageBox.Warning)
               msg.setText("Veuillez compléter les informations manquantes")
               msg.setInformativeText('')
               msg.setWindowTitle("Erreur")
               msg.exec_()
            elif any(d["codeutilisateur"] == self.showpopusager.lineEdit_3.text() for d in dic):
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Code utilisateur déjà utilisé")
                msg.setInformativeText('')
                msg.setWindowTitle("Erreur")
                msg.exec_()
            else:
                with open("testuser.json", "w") as outfile:
                    dic.append(dictemployee)
                    print(dic)
                    json.dump(dic,outfile)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.showlogin()
    sys.exit(app.exec_())
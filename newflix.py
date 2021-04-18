import json
import sys
from cryptography.fernet import Fernet
from ast import literal_eval
from mainwindow import *                #Importe l'affichage de la fenêtre principale
from gestionusers import *              #Importe l'affichage de la fenêtre gestion usager
from popupuser import *                 #Importe le formulaire de création/modification d'usager
from popupcustomer import *             #Importe le formulaire de création/modification de client
from exercices.logindialog import *               #Importe la fenêtre de connexion du démarrage du logiciel
from classes import *                   #Importe les classes Personnes, Employés, Clients, Cartes crédits, Films,
from popcard import *                   #Categorie avec toute la gestion des héritages entre les classes, tel que
from popupacteur import *               #demandé dans la mise en situation
from popupcat import *
from popupmovie import *

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

class FormUsager(QtWidgets.QDialog, Ui_FormUser): #Initialise popupuser.py. Formulaire pour créer/modifier un employé
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)

class Connexion(QtWidgets.QDialog, Ui_Connexion): #Initialise logindialog.py. Fenêtre de connexion au démarrage
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)

class FormClient(QtWidgets.QDialog, Ui_FormCustomer): #Init. popupcostumer.py. Fenêtre pour créer/modifier un client
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)

class Popcarte(QtWidgets.QDialog, Ui_Carte):  #Init. popupcarte.py. Fenêtre pour ajouter une carte de crédit
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)

class Popfilm(QtWidgets.QDialog, Ui_Film): #Init. popupmovie.py. Fenêtre pour créer/modifier un film
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)

class Popcategorie(QtWidgets.QDialog, Ui_Cat): #Init. popupcat.py. Fenêtre pour ajouter une catégorie
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)

class Popacteur(QtWidgets.QDialog, Ui_Acteur): #Init. popupacteur.py. Fenêtre pour ajouter un acteur
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)

################## C'est dans cette classe que l'action se passe, toutes les modifications visuelles ##################
################## et les interactions avec l'utilisateur vont se faire à partir d'ici.              ##################

class Controller: #C'est dans cette classe que l'action se passe, toutes les modifications visuelles et les
                  #les interactions avec l'utilisateur vont se faire à partir d'ici.
    def load_key(self):
        file = open('key.key', 'rb')
        self.key = file.read()
        file.close()
        self.fernet = Fernet(self.key)

    def loaduser(self):                     # Ouvre la liste de dictionnaires contenant les identifiants usagers
        try:
            with open("userscrypt.json", "rb") as file:
                file_user = file.read()
                usercrypt = self.fernet.decrypt(file_user)
                self.dictuser = literal_eval(usercrypt.decode('utf8'))

        except Exception:
            pass

    def saveuser(self):                     # Sauvegarde le dictionnaire des usagers dans le fichier .json des usagers
        try:
            with open("userscrypt.json", "wb") as file:
                newdictuser = str(self.dictuser)
                usercrypt = newdictuser.encode('utf8')
                encrypted_user = self.fernet.encrypt(usercrypt)
                file.write(encrypted_user)
        except Exception:
            pass

    def loadclient(self):                   # Ouvre la liste de dictionnaires contenant les informations des clients
        try:
            with open("clientscrypt.json","rb") as file:
                file_client = file.read()
                customercrypt = self.fernet.decrypt(file_client)
                self.dictclient = literal_eval(customercrypt.decode('utf8'))
        except Exception:
            pass

    def saveclient(self):                   # Sauvegarde le dictionnaire des usagers dans le fichier .json des clients
        try:
            with open("clientscrypt.json", "wb") as file:
                newdictcustomer = str(self.dictclient)
                customercrypt = newdictcustomer.encode('utf8')
                encrypted_customer = self.fernet.encrypt(customercrypt)
                file.write(encrypted_customer)
        except Exception:
            pass

    def loadfilm(self):                     # Ouvre la liste de dictionnaires contenant les informations des films
        try:
            with open("filmscrypt.json", "rb") as file:
                file_film = file.read()
                moviescrypt = self.fernet.decrypt(file_film)
                self.dictmovie = literal_eval(moviescrypt.decode('utf8'))
        except Exception:
            pass

    def savefilm(self):                      # Sauvegarde le dictionnaire des usagers dans le fichier .json des films
        try:
            with open("filmscrypt.json", "wb") as file:
                newdictmovie = str(self.dictmovie)
                moviecrypt = newdictmovie.encode('utf8')
                encrypted_movies = self.fernet.encrypt(moviecrypt)
                file.write(encrypted_movies)
        except Exception:
            pass

    def showlogin(self):
        self.connex = Connexion()   #Importe la classe  Connexion
        self.connex.pushButton.clicked.connect(self.testconnex) #Le bouton activera la fonction de tester la connex.
        self.connex.show()          #Affiche la fenêtre de connexion

    def testconnex(self):
        self.load_key()     #Charge la clé pour décrypter et encrypter les données dans les fichiers json
        self.loaduser()     #Charge la liste des utilisateurs provenant du fichier json dans la variable self.dictuser
        self.loadfilm()     #Charge la liste des films provenant du fichier json dans la variable self.dictmovie
        self.loadclient()   #Charge la liste des client provenant du fichier json dans la variable self.dictclient

        logged_in = False                 #par défaut la connexion est fausse avant le démarrer la boucle
        self.mesgexcept = ""   #Va servir pour l'exception du try
        try:   #Défini un try avant de démarrer la boucle
            while not logged_in:                  #Démarre la boucle.
                for a in (self.dictuser): # Dans toute la liste, vérifie chaque dict. pour retrouver les 3 mêmes paramètres
                    if a['codeutilisateur'] == self.connex.lineEdit.text() and \
                            a['password'] == self.connex.lineEdit_2.text() and a["acces"] == "Admin":
                        self.mainwindow()
                        self.statutlogin = "admin"
                        #Si les 3 inputs de l'usager correspond à un dict. avec accès admin, active modifwindow
                        logged_in = True   #Le "true" met fin à la boucle.
                    elif a['codeutilisateur'] == self.connex.lineEdit.text() and \
                            a['password'] == self.connex.lineEdit_2.text() and a["acces"] == "Modification":
                        self.modifwindow()
                        self.statutlogin = "modif"
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

    def mainwindow(self):
        self.connex.lineEdit.clear()  # Vide la ligne usager de la fenêtre de connexion
        self.connex.lineEdit_2.clear()  # Vide la ligne mot de passe de la fenêtre de connexion
        self.connex.lineEdit.setFocus()  # Met le focus sur la ligne usager de la fenêtre de connexion
        self.connex.hide()  # Cache la fenêtre de connexion
        self.mainw = FenPrinci()
        self.mainw.show()
        self.mainw.setWindowTitle("Newflix")
        self.mainw.actionGestion.triggered.connect(self.showgestuser)  # Dans la fen. principale, trigger la gestion users
        self.mainw.actionDeconnexion.triggered.connect(self.logout)  # Trigger la fonction déconnexion du logiciel
        self.mainw.actionQuitter.triggered.connect(self.closeall)  # Trigger la fonction fermeture du logiciel
        self.mainw.pushButton.clicked.connect(self.popupclient)
        self.mainw.pushButton_2.clicked.connect(self.modifcustomer)
        self.mainw.pushButton_3.clicked.connect(self.suppclient)
        self.mainw.pushButton_4.clicked.connect(self.popupfilm)
        self.mainw.pushButton_5.clicked.connect(self.modiffilm)
        self.mainw.pushButton_6.clicked.connect(self.suppfilm)
        self.model1()
        self.model2()

    def model1(self):
        self.treeViewModel = QtGui.QStandardItemModel()
        self.mainw.treeView.setModel(self.treeViewModel)
        self.mainw.treeView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.header = ['ID', 'Nom', "Prénom", "Sexe", "Date Inscription", "Courriel Client", "Mot de passe",
                                     "Numero de Carte", "Expiration", "Code secret"]
        self.treeViewModel.setHorizontalHeaderLabels(self.header)
        self.mainw.treeView.setSortingEnabled(True)
        self.mainw.treeView.setAlternatingRowColors(True)

        for b in self.dictclient:
            identifiant = QtGui.QStandardItem(str(b["identifiant"]))
            nom = QtGui.QStandardItem(b["nom"])
            prenom = QtGui.QStandardItem(b["prenom"])
            sexe = QtGui.QStandardItem(b["sexe"])
            date = QtGui.QStandardItem(b["dateinscription"])
            courriel = QtGui.QStandardItem(b["courriel"])
            password = QtGui.QStandardItem(b["motdepasse"])
            item = (identifiant, nom, prenom, sexe, date, courriel, password)
            self.treeViewModel.appendRow(item)
            self.mainw.treeView.setCurrentIndex(self.treeViewModel.index(0, 0))
            for dict in b["cartes"]:
                vide1 = QtGui.QStandardItem("*****")
                vide2 = QtGui.QStandardItem("*****")
                vide3 = QtGui.QStandardItem("*****")
                vide4 = QtGui.QStandardItem("*****")
                vide5 = QtGui.QStandardItem("*****")
                vide6 = QtGui.QStandardItem("*****")
                vide7 = QtGui.QStandardItem("*****")
                numero = QtGui.QStandardItem(dict["noCarte"])
                expiration = QtGui.QStandardItem(dict["expiration"])
                codecarte = QtGui.QStandardItem(dict["codecarte"])
                childitem = (vide1, vide2, vide3, vide4, vide5, vide6, vide7, numero, expiration, codecarte)
                identifiant.appendRow(childitem)

    def model2(self):
        self.treeViewModel2 = QtGui.QStandardItemModel()
        self.mainw.treeView_2.setModel(self.treeViewModel2)
        self.mainw.treeView_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.header2 = ["Nom", "Durée", "Description", "Catégories", "Description Catégorie", "Nom de l'acteur",
                        "Prénom de l'acteur", "Sexe", "Nom du personnage", "Début de l'emploi", "Fin de l'emploi",
                        "Cachet"]
        self.treeViewModel2.setHorizontalHeaderLabels(self.header2)
        self.mainw.treeView_2.setSortingEnabled(True)
        self.mainw.treeView_2.setAlternatingRowColors(True)

        for g in self.dictmovie:
            nom2 = QtGui.QStandardItem(g["nom"])
            duree = QtGui.QStandardItem(g["duree"])
            descriptionfilm = QtGui.QStandardItem(g["descriptionfilm"])
            item2 = (nom2, duree, descriptionfilm)
            self.treeViewModel2.appendRow(item2)
            self.mainw.treeView_2.setCurrentIndex(self.treeViewModel2.index(0, 0))
            for dict in g["categories"]:
                vide8 = QtGui.QStandardItem("*****")
                vide9 = QtGui.QStandardItem("*****")
                vide10 = QtGui.QStandardItem("*****")
                nomcat = QtGui.QStandardItem(dict["nom"])
                descriptioncat = QtGui.QStandardItem(dict["description"])
                childitem2 = (vide8, vide9, vide10, nomcat, descriptioncat)
                nom2.appendRow(childitem2)

            for dictact in g["acteurs"]:
                text1 = QtGui.QStandardItem("*****")
                text2 = QtGui.QStandardItem("*****")
                text3 = QtGui.QStandardItem("*****")
                text4 = QtGui.QStandardItem("*****")
                text5 = QtGui.QStandardItem("*****")
                nomacteur = QtGui.QStandardItem(dictact["nom"])
                prenomacteur = QtGui.QStandardItem(dictact["prenom"])
                sexeacteur = QtGui.QStandardItem(dictact["sexe"])
                personnage = QtGui.QStandardItem(dictact["nompersonnage"])
                debutemploi = QtGui.QStandardItem(dictact["debutemploi"])
                finemploi = QtGui.QStandardItem(dictact["finemploi"])
                cachet = QtGui.QStandardItem(dictact["cachet"])
                childfilm = (text1, text2, text3, text4, text5, nomacteur, prenomacteur, sexeacteur,
                             personnage, debutemploi, finemploi, cachet)
                vide8.appendRow(childfilm)


    def modifwindow(self):
        self.mainwindow()                              #Affiche la fenêtre principale
        self.mainw.actionGestion.setVisible(False)     #Cache le bouton Gestion Usager du menu principal

    def viewwindow(self):
        self.mainwindow()                              # Fait la même chose que la fonction précédente
        self.mainw.actionGestion.setVisible(False)
        self.mainw.pushButton.hide()                   #Cache les 6 boutons ajouter/modifier/supprimer de la
        self.mainw.pushButton_2.hide()                 #fenêtre principale pour permettre un accès en lecture
        self.mainw.pushButton_3.hide()                 #seulement des listes de clients et de films.
        self.mainw.pushButton_4.hide()
        self.mainw.pushButton_5.hide()
        self.mainw.pushButton_6.hide()

    def showgestuser(self):
        self.showgest = GestUser()  #Importe la fenêtre de gestion des usagers
        self.showgest.setWindowModality(QtCore.Qt.ApplicationModal)
        self.showgest.show()
        self.showgest.setWindowTitle("Gestion des utilisateurs")
        self.showgest.pushButton.clicked.connect(self.showpopuser) #Ouvre le formulaire d'usager si on appuie
        self.showgest.pushButton_2.clicked.connect(self.modifpopup) #Ouvre le formulaire pour modifier l'usager
        self.showgest.pushButton_3.clicked.connect(self.deleteuser) #Envoie vers la fonction supprimer usager
        self.model3()

    def model3(self):
        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Nom', 'Prenom', 'Sexe', 'Date Embauche', 'Code Usager',
                                              'Mot de passe', 'Type Acces'])
        self.showgest.treeView.setModel(self.model)  # Active le modèle
        try:  # Défini un try avant de démarrer la boucle
            for c in (self.dictuser):  # Pour chaque dictionnaire dans la liste, on créé une ligne avec les informations ci bas
                self.model.appendRow([QtGui.QStandardItem(c['nom']),   #Ajoute chaque information dans les colonnes.
                                       QtGui.QStandardItem(c['prenom']),
                                       QtGui.QStandardItem(c['sexe']),
                                       QtGui.QStandardItem(c['dateembauche']),
                                       QtGui.QStandardItem(c['codeutilisateur']),
                                       QtGui.QStandardItem(c['password']),
                                       QtGui.QStandardItem(c['acces'])])
        except Exception:  #Si la boucle n'a pas fonctionné, annule la boucle
            pass

    def logout(self):

        self.mainw.close()      #Ferme toutes les fenêtres et l'application
        self.connex.show()          #Démarre l'affichage de la fenêtre de connexion

    def closeall(self):
        app.closeAllWindows()       #Ferme toutes les fenêtres et l'application

    def showpopuser(self): #Ouvre le formulaire pour créer un nouvel employé ou le modifier
        self.showpopusager = FormUsager()  #Importe la fenêtre de formulaire de l'usager
        self.showpopusager.setWindowModality(QtCore.Qt.ApplicationModal)
        self.showpopusager.show()        #L'affiche
        self.showpopusager.setWindowTitle("Ajout d'un nouvel utilisateur")
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
            msg = QtWidgets.QMessageBox() #Cherche si le code est déjà dans le dictuser
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Code utilisateur déjà utilisé")
            msg.setInformativeText('')
            msg.setWindowTitle("Erreur")
            msg.exec_()
        elif len(self.showpopusager.lineEdit_5.text()) < 8:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Le mot de passe doit avoir 8 caractère minimum")
            msg.setInformativeText('')
            msg.setWindowTitle("Erreur")
            msg.exec_()
        else:
            self.model.appendRow(
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
        self.donnees = [d.data() for d in self.showgest.treeView.selectedIndexes()] #Créé une liste des données sélectionées
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
            self.showpopusager = FormUsager()
            self.showpopusager.setWindowModality(QtCore.Qt.ApplicationModal)
            self.showpopusager.show()
            self.showpopusager.setWindowTitle("Modification d'un utilisateur")
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
        if len(self.showpopusager.lineEdit_5.text()) < 8:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Le mot de passe doit avoir 8 caractère minimum")
            msg.setInformativeText('')
            msg.setWindowTitle("Erreur")
            msg.exec_()
        else:
            changeusager = next( #va chercher le même usager et le change par les informations ci bas
                item for item in self.dictuser if item['codeutilisateur'] == self.showpopusager.lineEdit_3.text())
            changeusager['nom'] = self.showpopusager.lineEdit.text()
            changeusager['prenom'] = self.showpopusager.lineEdit_2.text()
            changeusager['sexe'] = self.showpopusager.comboBox.currentText()
            changeusager['dateembauche'] = self.showpopusager.dateEdit.text()
            changeusager['password'] = self.showpopusager.lineEdit_5.text()
            changeusager['acces'] = self.showpopusager.comboBox_2.currentText()
            self.model3()
            self.showpopusager.close()
            self.saveuser()


    def deleteuser(self):
        donnees = [e.data() for e in self.showgest.treeView.selectedIndexes()]  # Créé une liste des données sélectionées
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
        donnees = [f.data() for f in self.showgest.treeView.selectedIndexes()]
        if indexes:
            index = indexes[0]  # L'index correspond à la liste des items de la rangée
            self.model.removeRow(index.row())  # Enlève l'item
            self.dictuser = [element for element in self.dictuser if element.get('codeutilisateur', '') != donnees[4]]
            self.saveuser()

    def popupclient(self):
        self.popupcustomer = FormClient()
        self.popupcustomer.setWindowModality(QtCore.Qt.ApplicationModal)
        self.popupcustomer.show()
        self.popupcustomer.setWindowTitle("Ajout d'un nouveau client")
        self.popupcustomer.pushButton.clicked.connect(self.savecustomer)
        self.popupcustomer.pushButton_2.clicked.connect(self.popupcustomer.close)
        self.popupcustomer.pushButton_3.clicked.connect(self.ajoutercarte)
        self.popupcustomer.pushButton_4.clicked.connect(self.suppcarte)
        self.model3 = QtGui.QStandardItemModel()
        self.popupcustomer.treeView.setModel(self.model3)  # Active le modèle
        self.model3.setHorizontalHeaderLabels(['Numéro de carte', 'Date Expiration', 'Code Carte'])
        identifiant = 1
        for l in self.dictclient:  # Je fais une boucle pour aller chercher le prochain chiffre disponible pour l'ID
            while identifiant == l["identifiant"]:
                identifiant = identifiant + 1
        self.client = Client(identifiant, self.popupcustomer.lineEdit.text(), self.popupcustomer.lineEdit_2.text(),
                        self.popupcustomer.comboBox.currentText(), self.popupcustomer.dateEdit.text(),
                        self.popupcustomer.lineEdit_3.text(), self.popupcustomer.lineEdit_5.text(), [])
        self.dataclient = vars(self.client)
        self.popupcustomer.setWindowTitle(str(identifiant))

    def savecustomer(self):
        identifiant = 1
        for l in self.dictclient:  # Je fais une boucle pour aller chercher le prochain chiffre disponible pour l'ID
            while identifiant == l["identifiant"]:
                identifiant = identifiant + 1
        updatedclient = Client(identifiant, self.popupcustomer.lineEdit.text(), self.popupcustomer.lineEdit_2.text(),
                        self.popupcustomer.comboBox.currentText(), self.popupcustomer.dateEdit.text(),
                        self.popupcustomer.lineEdit_3.text(), self.popupcustomer.lineEdit_5.text(), [])
        self.updateddataclient = vars(updatedclient)
        self.updateddataclient["cartes"] = self.dataclient["cartes"]
        if self.popupcustomer.lineEdit.text() == "" or self.popupcustomer.lineEdit_2.text() == "" or \
                self.popupcustomer.lineEdit_3.text() == "" or self.popupcustomer.lineEdit_5.text() == "":
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Veuillez compléter les informations manquantes")
            msg.setInformativeText('')
            msg.setWindowTitle("Erreur")
            msg.exec_()
        elif any(d["courriel"] == self.popupcustomer.lineEdit_3.text() for d in self.dictclient):
            msg = QtWidgets.QMessageBox()  # Cherche si le code est déjà dans le dictuser
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Ce courriel est déjà utilisé")
            msg.setInformativeText('')
            msg.setWindowTitle("Erreur")
            msg.exec_()
        elif len(self.popupcustomer.lineEdit_5.text()) < 8:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Le mot de passe doit avoir 8 caractère minimum")
            msg.setInformativeText('')
            msg.setWindowTitle("Erreur")
            msg.exec_()
        else:
            identifiant = QtGui.QStandardItem(str(self.updateddataclient["identifiant"]))
            nom = QtGui.QStandardItem(self.updateddataclient["nom"])
            prenom = QtGui.QStandardItem(self.updateddataclient["prenom"])
            sexe = QtGui.QStandardItem(self.updateddataclient["sexe"])
            date = QtGui.QStandardItem(self.updateddataclient["dateinscription"])
            courriel = QtGui.QStandardItem(self.updateddataclient["courriel"])
            password = QtGui.QStandardItem(self.updateddataclient["motdepasse"])
            item = (identifiant, nom, prenom, sexe, date, courriel, password)
            self.treeViewModel.appendRow(item)
            for dict in self.updateddataclient["cartes"]:
                vide1 = QtGui.QStandardItem("*****")
                vide2 = QtGui.QStandardItem("*****")
                vide3 = QtGui.QStandardItem("*****")
                vide4 = QtGui.QStandardItem("*****")
                vide5 = QtGui.QStandardItem("*****")
                vide6 = QtGui.QStandardItem("*****")
                vide7 = QtGui.QStandardItem("*****")
                numero = QtGui.QStandardItem(dict["noCarte"])
                expiration = QtGui.QStandardItem(dict["expiration"])
                codecarte = QtGui.QStandardItem(dict["codecarte"])
                childitem = (vide1, vide2, vide3, vide4, vide5, vide6, vide7, numero, expiration, codecarte)
                identifiant.appendRow(childitem)
            self.mainw.treeView.setCurrentIndex(self.treeViewModel.index(0, 0))
            self.dictclient.append(self.updateddataclient)
            self.saveclient()
            self.popupcustomer.close()

    def modifcustomer(self):
        self.donneesclient = self.mainw.treeView.selectedIndexes()[0]
        if self.donneesclient.data() == "*****":
            self.donneesclient = self.donneesclient.parent()

        for dict in self.dictclient :
            if str(dict["identifiant"]) == self.donneesclient.data():
                self.dataclient = dict

        self.popupcustomer = FormClient()
        self.popupcustomer.setWindowModality(QtCore.Qt.ApplicationModal)
        self.popupcustomer.show()
        self.popupcustomer.setWindowTitle("Modification d'un client")
        self.popupcustomer.pushButton.clicked.connect(self.savemodifcustomer)
        self.popupcustomer.pushButton_2.clicked.connect(self.popupcustomer.close)
        self.popupcustomer.pushButton_3.clicked.connect(self.ajoutercarte)
        self.popupcustomer.pushButton_4.clicked.connect(self.suppcarte)
        self.model3 = QtGui.QStandardItemModel()
        self.popupcustomer.treeView.setModel(self.model3)  # Active le modèle
        self.model3.setHorizontalHeaderLabels(['Numéro de carte', 'Date Expiration', 'Code Carte'])
        for h in self.dataclient["cartes"]:
            numero = QtGui.QStandardItem(h["noCarte"])
            expiration = QtGui.QStandardItem(h["expiration"])
            codecarte = QtGui.QStandardItem(h["codecarte"])
            item = (numero, expiration, codecarte)
            self.model3.appendRow(item)
        index = self.popupcustomer.comboBox.findText(self.dataclient["sexe"], QtCore.Qt.MatchFlag.MatchFixedString)
        date = QtCore.QDate.fromString(self.dataclient["dateinscription"], "dd-MM-yyyy")

        self.popupcustomer.setWindowTitle(str(self.dataclient["identifiant"]))
        self.popupcustomer.lineEdit.setText(self.dataclient["nom"])
        self.popupcustomer.lineEdit_2.setText(self.dataclient["prenom"])
        self.popupcustomer.comboBox.setCurrentIndex(index)
        self.popupcustomer.dateEdit.setDate(date)
        self.popupcustomer.lineEdit_3.setText(self.dataclient["courriel"])
        self.popupcustomer.lineEdit_5.setText(self.dataclient["motdepasse"])

    def ajoutercarte(self):
        self.showpopcarte = Popcarte()
        self.showpopcarte.setWindowModality(QtCore.Qt.ApplicationModal)
        self.showpopcarte.show()
        self.showpopcarte.setWindowTitle("Ajout d'une carte de crédit")
        self.showpopcarte.lineEdit.setFocus()
        self.showpopcarte.pushButton.clicked.connect(self.savecarte)
        self.showpopcarte.pushButton_2.clicked.connect(self.showpopcarte.close)

    def savecarte(self):
        if self.showpopcarte.lineEdit.text() == "" or self.showpopcarte.lineEdit_2.text() == "":
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Veuillez compléter les informations manquantes")
            msg.setInformativeText('')
            msg.setWindowTitle("Erreur")
            msg.exec_()
        else:
            carte = CarteCredit(self.showpopcarte.lineEdit.text(),
                                self.showpopcarte.dateEdit.text(), self.showpopcarte.lineEdit_2.text())
            self.dictcarte = vars(carte)
            numero = QtGui.QStandardItem(self.dictcarte["noCarte"])
            expiration = QtGui.QStandardItem(self.dictcarte["expiration"])
            codesecret = QtGui.QStandardItem(self.dictcarte["codecarte"])
            item = (numero, expiration, codesecret)
            self.model3.appendRow(item)
            self.dataclient["cartes"].append(self.dictcarte)
            self.showpopcarte.close()


    def suppcarte(self):
        self.datacarte = [f.data() for f in self.popupcustomer.treeView.selectedIndexes()]
        if self.datacarte == [] :
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Veuillez sélectionner une carte à supprimer")
            msg.setInformativeText('')
            msg.setWindowTitle("Erreur")
            msg.exec_()
        else:
            box = QtWidgets.QMessageBox()
            box.setIcon(QtWidgets.QMessageBox.Question)
            box.setWindowTitle('Confirmation')
            box.setText('Êtes vous sûr de vouloir supprimer cette carte de crédit?')
            box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            buttonY = box.button(QtWidgets.QMessageBox.Yes)
            buttonY.setText('Oui')
            buttonN = box.button(QtWidgets.QMessageBox.No)
            buttonN.setText('Non')
            box.exec_()

            if box.clickedButton() == buttonY:
                self.deletecarte()
            elif box.clickedButton() == buttonN:
                pass

    def deletecarte(self):
        indexes = self.popupcustomer.treeView.selectedIndexes()
        donnees = [f.data() for f in self.popupcustomer.treeView.selectedIndexes()]
        if indexes:
            index = indexes[0]  # L'index correspond à la liste des items de la rangée
            self.model3.removeRow(index.row())  # Enlève l'item
            self.dataclient["cartes"] = [element for element in self.dataclient["cartes"] if
                                 element.get('noCarte', '') != donnees[0]]



    def savemodifcustomer(self):
        if self.popupcustomer.lineEdit_3.text() != self.dataclient["courriel"] and \
                any(j["courriel"] == self.popupcustomer.lineEdit_3.text() for j in self.dictclient):
            msg = QtWidgets.QMessageBox() #Cherche si le courriel qui a changé est déjà dans le dictuser
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Ce courriel est déjà utilisé")
            msg.setInformativeText('')
            msg.setWindowTitle("Erreur")
            msg.exec_()
        elif len(self.popupcustomer.lineEdit_5.text()) < 8:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Le mot de passe doit avoir 8 caractère minimum")
            msg.setInformativeText('')
            msg.setWindowTitle("Erreur")
            msg.exec_()
        else:
            changeusager = next(  # va chercher le même client et le change par les informations ci bas
                item for item in self.dictclient if item["identifiant"] == self.dataclient["identifiant"])
            changeusager['nom'] = self.popupcustomer.lineEdit.text()
            changeusager['prenom'] = self.popupcustomer.lineEdit_2.text()
            changeusager['sexe'] = self.popupcustomer.comboBox.currentText()
            changeusager['dateinscription'] = self.popupcustomer.dateEdit.text()
            changeusager['courriel'] = self.popupcustomer.lineEdit_3.text()
            changeusager['motdepasse'] = self.popupcustomer.lineEdit_5.text()
            self.model1()
            self.popupcustomer.close()
            self.saveclient()

    def suppclient(self):
        self.deleteclient = self.mainw.treeView.selectedIndexes()[0]
        if self.deleteclient.data() == "*****":
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Veuillez sélectionner directement le client à supprimer")
            msg.setInformativeText('')
            msg.setWindowTitle("Erreur")
            msg.exec_()
        else:
            box = QtWidgets.QMessageBox()
            box.setIcon(QtWidgets.QMessageBox.Question)
            box.setWindowTitle('Confirmation')
            box.setText('Êtes vous sûr de vouloir supprimer ce client?')
            box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            buttonY = box.button(QtWidgets.QMessageBox.Yes)
            buttonY.setText('Oui')
            buttonN = box.button(QtWidgets.QMessageBox.No)
            buttonN.setText('Non')
            box.exec_()

            if box.clickedButton() == buttonY:
                self.yesdeletecustomer()
            elif box.clickedButton() == buttonN:
                pass

    def yesdeletecustomer(self):
        indexes = self.mainw.treeView.selectedIndexes()
        donnees = [f.data() for f in self.mainw.treeView.selectedIndexes()]
        if indexes:
            index = indexes[0]  # L'index correspond à la liste des items de la rangée
            self.treeViewModel.removeRow(index.row())  # Enlève l'item
            self.dictclient = [element for element in self.dictclient if
                             element.get('identifiant', '') != int(donnees[0])]
            self.saveclient()

    def popupfilm(self):
        self.popupfilm = Popfilm()
        self.popupfilm.setWindowModality(QtCore.Qt.ApplicationModal)
        self.popupfilm.show()
        self.popupfilm.setWindowTitle("Ajout d'un nouveau film")
        self.popupfilm.pushButton.clicked.connect(self.savemovie)
        self.popupfilm.pushButton_2.clicked.connect(self.popupfilm.close)
        self.popupfilm.pushButton_3.clicked.connect(self.popupcategorie)
        self.popupfilm.pushButton_4.clicked.connect(self.suppcategorie)
        self.popupfilm.pushButton_5.clicked.connect(self.popacteur)
        self.popupfilm.pushButton_6.clicked.connect(self.suppacteur)
        self.model4 = QtGui.QStandardItemModel()
        self.popupfilm.treeView.setModel(self.model4)
        self.model4.setHorizontalHeaderLabels(["Nom de catégorie", "Description de la catégorie"])
        self.model5 = QtGui.QStandardItemModel()
        self.popupfilm.treeView_2.setModel(self.model5)
        self.model5.setHorizontalHeaderLabels(["Nom", "Prénom", "Sexe", "Personnage", "Début de l'emploi",
                                               "Fin de l'emploi", "Cachet"])
        self.movie = Film(self.popupfilm.lineEdit.text(), self.popupfilm.timeEdit.text(),
                          self.popupfilm.lineEdit_2.text(), [], [])
        self.datafilm = vars(self.movie)


    def savemovie(self):
        updatedfilm = Film(self.popupfilm.lineEdit.text(), self.popupfilm.timeEdit.text(),
                               self.popupfilm.lineEdit_2.text(), [], [])
        self.updateddatafilm = vars(updatedfilm)
        self.updateddatafilm["categories"] = self.datafilm["categories"]
        self.updateddatafilm["acteurs"] = self.datafilm["acteurs"]
        print(self.updateddatafilm)
        if self.popupfilm.lineEdit.text() == "" or self.popupfilm.lineEdit_2.text() == "" :
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Veuillez compléter les informations manquantes")
            msg.setInformativeText('')
            msg.setWindowTitle("Erreur")
            msg.exec_()
        elif any(d["nom"] == self.popupfilm.lineEdit.text() for d in self.dictmovie):
            msg = QtWidgets.QMessageBox()  # Cherche si le code est déjà dans le dictuser
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Ce nom de film est déjà utilisé")
            msg.setInformativeText('')
            msg.setWindowTitle("Erreur")
            msg.exec_()
        else:
            nom = QtGui.QStandardItem(self.updateddatafilm["nom"])
            duree = QtGui.QStandardItem(self.updateddatafilm["duree"])
            descriptionfilm = QtGui.QStandardItem(self.updateddatafilm["descriptionfilm"])
            item3 = (nom, duree, descriptionfilm)
            self.treeViewModel2.appendRow(item3)
            for dict in self.updateddatafilm["categories"]:
                vide1 = QtGui.QStandardItem("*****")
                vide2 = QtGui.QStandardItem("*****")
                vide3 = QtGui.QStandardItem("*****")
                nomfilm = QtGui.QStandardItem(dict["nom"])
                descricat = QtGui.QStandardItem(dict["description"])
                childitem3 = (vide1, vide2, vide3, nomfilm, descricat)
                nom.appendRow(childitem3)
            for dictact in self.updateddatafilm["acteurs"]:
                text1 = QtGui.QStandardItem("*****")
                text2 = QtGui.QStandardItem("*****")
                text3 = QtGui.QStandardItem("*****")
                text4 = QtGui.QStandardItem("*****")
                text5 = QtGui.QStandardItem("*****")
                nomacteur = QtGui.QStandardItem(dictact["nom"])
                prenomacteur = QtGui.QStandardItem(dictact["prenom"])
                sexeacteur = QtGui.QStandardItem(dictact["sexe"])
                personnage = QtGui.QStandardItem(dictact["nompersonnage"])
                debutemploi = QtGui.QStandardItem(dictact["debutemploi"])
                finemploi = QtGui.QStandardItem(dictact["finemploi"])
                cachet = QtGui.QStandardItem(dictact["cachet"])
                childfilm2 = (text1, text2, text3, text4, text5, nomacteur, prenomacteur, sexeacteur,
                             personnage, debutemploi, finemploi, cachet)
                vide1.appendRow(childfilm2)

            self.mainw.treeView_2.setCurrentIndex(self.treeViewModel2.index(0, 0))
            self.dictmovie.append(self.updateddatafilm)
            self.savefilm()
            self.popupfilm.close()

    def modiffilm(self):
        self.donneesfilm = self.mainw.treeView_2.selectedIndexes()[0]
        while self.donneesfilm.data() == "*****":
            self.donneesfilm = self.donneesfilm.parent()

        for dict in self.dictmovie :
            if dict["nom"] == self.donneesfilm.data():
                self.datafilm = dict

        self.popupfilm = Popfilm()
        self.popupfilm.setWindowModality(QtCore.Qt.ApplicationModal)
        self.popupfilm.show()
        self.popupfilm.setWindowTitle("Modification d'un film")
        self.popupfilm.pushButton.clicked.connect(self.savemodifmovie)
        self.popupfilm.pushButton_2.clicked.connect(self.popupfilm.close)
        self.popupfilm.pushButton_3.clicked.connect(self.popupcategorie)
        self.popupfilm.pushButton_4.clicked.connect(self.suppcategorie)
        self.popupfilm.pushButton_5.clicked.connect(self.popacteur)
        self.popupfilm.pushButton_6.clicked.connect(self.suppacteur)
        self.model4 = QtGui.QStandardItemModel()
        self.popupfilm.treeView.setModel(self.model4)
        self.model4.setHorizontalHeaderLabels(["Nom de catégorie", "Description de la catégorie"])
        for m in self.datafilm["categories"]:
            nom = QtGui.QStandardItem(m["nom"])
            descriptioncat = QtGui.QStandardItem(m["description"])
            item = (nom, descriptioncat)
            self.model4.appendRow(item)

        time = QtCore.QTime.fromString(self.datafilm["duree"])
        self.popupfilm.lineEdit.setText(self.datafilm["nom"])
        self.popupfilm.lineEdit.setEnabled(False)
        self.popupfilm.lineEdit_2.setText(self.datafilm["descriptionfilm"])
        self.popupfilm.timeEdit.setTime(time)

        self.model5 = QtGui.QStandardItemModel()
        self.popupfilm.treeView_2.setModel(self.model5)
        self.model5.setHorizontalHeaderLabels(["Nom", "Prénom", "Sexe", "Personnage", "Début de l'emploi",
                                               "Fin de l'emploi", "Cachet"])

        for n in self.datafilm["acteurs"] :
            nomacteur = QtGui.QStandardItem(n["nom"])
            prenomacteur = QtGui.QStandardItem(n["prenom"])
            sexe = QtGui.QStandardItem(n["sexe"])
            nomperso = QtGui.QStandardItem(n["nompersonnage"])
            debutemploi = QtGui.QStandardItem(n["debutemploi"])
            finemploi = QtGui.QStandardItem(n["finemploi"])
            cachet = QtGui.QStandardItem(n["cachet"])
            item2 = (nomacteur, prenomacteur, sexe, nomperso, debutemploi, finemploi, cachet)
            self.model5.appendRow(item2)

    def popupcategorie(self):
        self.showpopcat = Popcategorie()
        self.showpopcat.setWindowModality(QtCore.Qt.ApplicationModal)
        self.showpopcat.show()
        self.showpopcat.setWindowTitle("Ajout d'une nouvelle catégorie")
        self.showpopcat.lineEdit.setFocus()
        self.showpopcat.pushButton.clicked.connect(self.savecat)
        self.showpopcat.pushButton_2.clicked.connect(self.showpopcat.close)

    def savecat(self):
        if self.showpopcat.lineEdit.text() == "" or self.showpopcat.lineEdit_2.text() == "":
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Veuillez compléter les informations manquantes")
            msg.setInformativeText('')
            msg.setWindowTitle("Erreur")
            msg.exec_()
        else :
            cat = Categoriefilm(self.showpopcat.lineEdit.text(), self.showpopcat.lineEdit_2.text())
            self.dictcat = vars(cat)
            nomcat = QtGui.QStandardItem(self.dictcat["nom"])
            descriptioncat = QtGui.QStandardItem(self.dictcat["description"])
            item = (nomcat, descriptioncat)
            self.model4.appendRow(item)
            self.datafilm["categories"].append(self.dictcat)
            self.showpopcat.close()

    def suppcategorie(self):
        self.datacat = [f.data() for f in self.popupfilm.treeView.selectedIndexes()]
        if self.datacat == []:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Veuillez sélectionner une catégorie à supprimer")
            msg.setInformativeText('')
            msg.setWindowTitle("Erreur")
            msg.exec_()
        else:
            box = QtWidgets.QMessageBox()
            box.setIcon(QtWidgets.QMessageBox.Question)
            box.setWindowTitle('Confirmation')
            box.setText('Êtes vous sûr de vouloir supprimer cette catégorie?')
            box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            buttonY = box.button(QtWidgets.QMessageBox.Yes)
            buttonY.setText('Oui')
            buttonN = box.button(QtWidgets.QMessageBox.No)
            buttonN.setText('Non')
            box.exec_()

            if box.clickedButton() == buttonY:
                self.deletecat()
            elif box.clickedButton() == buttonN:
                pass

    def deletecat(self):
        indexes = self.popupfilm.treeView.selectedIndexes()
        donnees = [f.data() for f in self.popupfilm.treeView.selectedIndexes()]
        if indexes:
            index = indexes[0]  # L'index correspond à la liste des items de la rangée
            self.model4.removeRow(index.row())  # Enlève l'item
            self.datafilm["categories"] = [element for element in self.datafilm["categories"] if
                                            element.get('nom', '') != donnees[0]]

    def popacteur(self):
        self.showpopupacteur = Popacteur()
        self.showpopupacteur.setWindowModality(QtCore.Qt.ApplicationModal)
        self.showpopupacteur.show()
        self.showpopupacteur.setWindowTitle("Ajout d'un nouvel acteur")

        self.showpopupacteur.lineEdit.setFocus()
        self.showpopupacteur.pushButton.clicked.connect(self.saveacteur)
        self.showpopupacteur.pushButton_2.clicked.connect(self.showpopupacteur.close)

    def saveacteur(self):
        if self.showpopupacteur.lineEdit.text() == "" or self.showpopupacteur.lineEdit_2.text() == "" or \
                self.showpopupacteur.lineEdit_3.text() == "":
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Veuillez compléter les informations manquantes")
            msg.setInformativeText('')
            msg.setWindowTitle("Erreur")
            msg.exec_()
        else:
            acteur = Acteur(self.showpopupacteur.lineEdit.text(), self.showpopupacteur.lineEdit_2.text(),
                            self.showpopupacteur.comboBox.currentText(),self.showpopupacteur.lineEdit_4.text(),
                            self.showpopupacteur.dateEdit.text(), self.showpopupacteur.dateEdit_2.text(),
                            self.showpopupacteur.lineEdit_3.text())
            self.dictacteur = vars(acteur)
            nom = QtGui.QStandardItem(self.dictacteur["nom"])
            prenom = QtGui.QStandardItem(self.dictacteur["prenom"])
            sexe = QtGui.QStandardItem(self.dictacteur["sexe"])
            nomperso = QtGui.QStandardItem(self.dictacteur["nompersonnage"])
            debutemploi = QtGui.QStandardItem(self.dictacteur["debutemploi"])
            finemploi = QtGui.QStandardItem(self.dictacteur["finemploi"])
            cachet = QtGui.QStandardItem(self.dictacteur["cachet"])
            item = (nom, prenom, sexe, nomperso, debutemploi, finemploi, cachet)
            self.model5.appendRow(item)
            self.datafilm["acteurs"].append(self.dictacteur)
            self.showpopupacteur.close()

    def suppacteur(self):
        self.dataacteur = [f.data() for f in self.popupfilm.treeView_2.selectedIndexes()]
        if self.dataacteur == []:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Veuillez sélectionner un acteur à supprimer")
            msg.setInformativeText('')
            msg.setWindowTitle("Erreur")
            msg.exec_()
        else:
            box = QtWidgets.QMessageBox()
            box.setIcon(QtWidgets.QMessageBox.Question)
            box.setWindowTitle('Confirmation')
            box.setText('Êtes vous sûr de vouloir supprimer cet acteur?')
            box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            buttonY = box.button(QtWidgets.QMessageBox.Yes)
            buttonY.setText('Oui')
            buttonN = box.button(QtWidgets.QMessageBox.No)
            buttonN.setText('Non')
            box.exec_()

            if box.clickedButton() == buttonY:
                self.deleteacteur()
            elif box.clickedButton() == buttonN:
                pass

    def deleteacteur(self):
        indexes = self.popupfilm.treeView_2.selectedIndexes()
        donnees = [f.data() for f in self.popupfilm.treeView_2.selectedIndexes()]
        if indexes:
            index = indexes[0]  # L'index correspond à la liste des items de la rangée
            self.model5.removeRow(index.row())  # Enlève l'item
            self.datafilm["acteurs"] = [element for element in self.datafilm["acteurs"] if
                                           element.get('nompersonnage', '') != donnees[3]]

    def savemodifmovie(self):

        changefilm = next(
            item for item in self.dictmovie if item["nom"] == self.datafilm["nom"])
        changefilm["nom"] = self.popupfilm.lineEdit.text()
        changefilm["duree"] = self.popupfilm.timeEdit.text()
        changefilm["descriptionfilm"] = self.popupfilm.lineEdit_2.text()

        self.model2()
        self.popupfilm.close()
        self.savefilm()


    def suppfilm(self):
        self.deletefilm = self.mainw.treeView_2.selectedIndexes()[0]
        if self.deletefilm.data() == "*****":
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Veuillez sélectionner directement le film à supprimer")
            msg.setInformativeText('')
            msg.setWindowTitle("Erreur")
            msg.exec_()
        else:
            box = QtWidgets.QMessageBox()
            box.setIcon(QtWidgets.QMessageBox.Question)
            box.setWindowTitle('Confirmation')
            box.setText('Êtes vous sûr de vouloir supprimer ce film?')
            box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            buttonY = box.button(QtWidgets.QMessageBox.Yes)
            buttonY.setText('Oui')
            buttonN = box.button(QtWidgets.QMessageBox.No)
            buttonN.setText('Non')
            box.exec_()

            if box.clickedButton() == buttonY:
                self.yesdeletemovie()
            elif box.clickedButton() == buttonN:
                pass

    def yesdeletemovie(self):
        indexes = self.mainw.treeView_2.selectedIndexes()
        donnees = [f.data() for f in self.mainw.treeView_2.selectedIndexes()]

        if indexes:
            index = indexes[0]  # L'index correspond à la liste des items de la rangée
            self.treeViewModel2.removeRow(index.row())  # Enlève l'item
            self.dictmovie = [element for element in self.dictmovie if
                             element.get('nom', '') != donnees[0]]
            self.savefilm()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.showlogin()
    sys.exit(app.exec_())
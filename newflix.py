### Auteur: Claude Bélanger        ###
### Date : Mars et Avril 2021      ###
### Courriel: urzawrym@hotmail.com ###

# Importe le module pour gérer la fermeture de toutes les fenêtres du logiciel (pour la fenêtre déconnexion)
import os
# Importe le module pour encrypter et décrypter les données à l'aide d'une clé
from cryptography.fernet import Fernet
# Importe le module permettant de faire une copie indépendante d'une variable (utilisée pour les dict. temporaires)
import copy
# Importe le module permettant de convertir directement les bytes en dictionnaire après avoir décrypté les données
from ast import literal_eval
# Importe l'affichage de la fenêtre principale
from mainwindowform import *
# Importe l'affichage de la fenêtre gestion usager
from gestionusersform import *
# Importe le formulaire de création/modification d'usager
from popupuser import *
# Importe le formulaire de création/modification de client
from popupcustomerform import *
# Importe la fenêtre de connexion du démarrage du logiciel
from logindialog import *
# Importe les classes Personnes, Employés, Clients, Cartes crédits, Films,Categorie avec toute la gestion des héritages
# entre les classes, tel que demandé dans la mise en situation
from classes import *
# Importe le formulaire de création de carte de crédit
from popcard import *
# Importe le formulaire de création d'acteur
from popupacteur import *
# Importe le formulaire de création de catégorie de film
from popupcat import *
# Importe la fenêtre pour créer ou modifier un film
from popupmovieform import *

################## Aucune classe provenant de QT Designer n'est modifiée. Ici on créé les classes ##################
################## localement qui importent et initialisent les classes provenant de QT Designer. ##################

class FenPrinci(QtWidgets.QMainWindow, Ui_MainWindow): # Initialise mainwindow.py. Fenêtre principale du logiciel.
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

class GestUser(QtWidgets.QMainWindow, Ui_GestiUser): # Initialise gestionusersform.py. Fenêtre de gestion des employés
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

class FormUsager(QtWidgets.QDialog, Ui_FormUser): # Initialise popupuser.py. Formulaire pour créer/modifier un employé
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)

class Connexion(QtWidgets.QDialog, Ui_Connexion): # Initialise logindialog.py. Fenêtre de connexion au démarrage
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)

class FormClient(QtWidgets.QMainWindow, Ui_FormCustomer): # Init. popupcostumerform.py. Fen. pour créer/modif. un client
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

class Popcarte(QtWidgets.QDialog, Ui_Carte):  # Init. popupcarte.py. Fenêtre pour ajouter une carte de crédit
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)

class Formfilm(QtWidgets.QMainWindow, Ui_FormFilm): # Init. popupmovieform.py. Fenêtre pour créer/modifier un film
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

class Popcategorie(QtWidgets.QDialog, Ui_Cat): # Init. popupcat.py. Fenêtre pour ajouter une catégorie
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)

class Popacteur(QtWidgets.QDialog, Ui_Acteur): # Init. popupacteur.py. Fenêtre pour ajouter un acteur
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)

################## C'est dans cette classe que l'action se passe, toutes les modifications visuelles ##################
################## et les interactions avec l'utilisateur vont se faire à partir d'ici.              ##################

class Controller:

    # Charge la clé pour encrypter/décrypter dans la variable self.key.
    def load_key(self):
        try:
            file = open('key.key', 'rb')
            self.key = file.read()
            file.close()
            self.fernet = Fernet(self.key)
        except Exception:
            pass

    # Ouvre le fichier des usagers, décrypte les données et charge le dict. d'usager dans la variable self.dictuser
    def loaduser(self):
        try:
            with open("userscrypt.json", "rb") as file:
                file_user = file.read()
                usercrypt = self.fernet.decrypt(file_user)
                self.dictuser = literal_eval(usercrypt.decode('utf8'))

        except Exception:
            pass

    # Sauvegarde le dictionnaire des usagers dans le fichier .json des usagers après l'avoir encrypté
    def saveuser(self):
        try:
            with open("userscrypt.json", "wb") as file:
                newdictuser = str(self.dictuser)
                usercrypt = newdictuser.encode('utf8')
                encrypted_user = self.fernet.encrypt(usercrypt)
                file.write(encrypted_user)
        except Exception:
            pass

    # Ouvre le fichier des clients, décrypte les données et charge le dict. de clients dans la variable self.dictclient
    def loadclient(self):
        try:
            with open("clientscrypt.json","rb") as file:
                file_client = file.read()
                customercrypt = self.fernet.decrypt(file_client)
                self.dictclient = literal_eval(customercrypt.decode('utf8'))
        except Exception:
            pass

    # Sauvegarde le dictionnaire des clients dans le fichier .json des clients après l'avoir encrypté
    def saveclient(self):
        try:
            with open("clientscrypt.json", "wb") as file:
                newdictcustomer = str(self.dictclient)
                customercrypt = newdictcustomer.encode('utf8')
                encrypted_customer = self.fernet.encrypt(customercrypt)
                file.write(encrypted_customer)
        except Exception:
            pass

    # Ouvre le fichier des films, décrypte les données et charge le dict. de films dans la variable self.dictmovie
    def loadfilm(self):
        try:
            with open("filmscrypt.json", "rb") as file:
                file_film = file.read()
                moviescrypt = self.fernet.decrypt(file_film)
                self.dictmovie = literal_eval(moviescrypt.decode('utf8'))
        except Exception:
            pass

    # Sauvegarde le dictionnaire des films dans le fichier .json des films après l'avoir encrypté
    def savefilm(self):
        try:
            with open("filmscrypt.json", "wb") as file:
                newdictmovie = str(self.dictmovie)
                moviecrypt = newdictmovie.encode('utf8')
                encrypted_movies = self.fernet.encrypt(moviecrypt)
                file.write(encrypted_movies)
        except Exception:
            pass

    # Importe la classe Connexion, active le bouton de connexion et affiche la fenêtre de connexion avec son nom
    def showlogin(self):
        self.connex = Connexion()
        self.connex.pushButton.clicked.connect(self.testconnex)
        self.connex.show()
        self.connex.setWindowTitle("Connexion")

    # Charge les différents dictionnaires utilisés dans le logiciel ainsi que la clé d'encryption/décryption
    def testconnex(self):
        self.load_key()
        self.loaduser()
        self.loadfilm()
        self.loadclient()

        # Avant de démarrer la boucle, je met un try et je met un statut login faux
        self.logged_in = False
        try:
            while not self.logged_in:
                # Dans toute la liste d'usagers, vérifie chaque dict. pour retrouver les 3 mêmes paramètres
                for a in (self.dictuser):
                    if a['codeutilisateur'] == self.connex.lineEdit.text() and \
                            a['password'] == self.connex.lineEdit_2.text() and a["acces"] == "Admin":
                        # Si les 3 inputs de l'usager correspond à un dict. avec accès admin, active adminwindow
                        self.adminwindow()
                        self.logged_in = True   #Le "true" met fin à la boucle.
                    elif a['codeutilisateur'] == self.connex.lineEdit.text() and \
                            a['password'] == self.connex.lineEdit_2.text() and a["acces"] == "Modification":
                        # Si les 3 inputs de l'usager correspond à un dict. avec accès modif, active modifwindow
                        self.modifwindow()
                        self.logged_in = True
                    elif a['codeutilisateur'] == self.connex.lineEdit.text() and \
                            a['password'] == self.connex.lineEdit_2.text() and a["acces"] == "Lecture":
                        # Si les 3 inputs de l'usager correspond à un dict. avec accès lecture, active mainwindow
                        self.mainwindow()
                        self.logged_in = True
        # Si la boucle n'est toujours pas fermée après les 3 premiers tests, affiche la fenêtre identifiants erronés
                if self.logged_in is not True:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setText("Identifiants erronés")
                    msg.setInformativeText('')
                    msg.setWindowTitle("Erreur")
                    msg.exec_()
                    self.connex.lineEdit.setFocus() # Remet le focus du clavier sur la ligne de l'usager
                    break # Casse la boucle car aucun identifiant n'a fonctionné
        except Exception: # Si la boucle n'a pas fonctionné
            pass

    # Charge la fenêtre principale du logiciel, l'affiche mais avec les boutons gestion et modif. cachés par défaut
    def mainwindow(self):
        self.connex.lineEdit.clear()  # Vide la ligne usager de la fenêtre de connexion
        self.connex.lineEdit_2.clear()  # Vide la ligne mot de passe de la fenêtre de connexion
        self.connex.lineEdit.setFocus()  # Met le focus sur la ligne usager de la fenêtre de connexion
        self.connex.hide()  # Cache la fenêtre de connexion
        self.mainw = FenPrinci()
    # Par sécurité, le bouton gestion et les 6 boutons de modifications de clients et films sont cachés. C'est par
    # le test de connexion qu'ils seront affichés, selon le niveau d'accès de l'usager.
        self.mainw.actionGestion.setVisible(False)
        self.mainw.pushButton.hide()
        self.mainw.pushButton_2.hide()
        self.mainw.pushButton_3.hide()
        self.mainw.pushButton_4.hide()
        self.mainw.pushButton_5.hide()
        self.mainw.pushButton_6.hide()
        self.mainw.show()
        self.mainw.setWindowTitle("Newflix")
        # Permet d'afficher la fenêtre de gestion des usagers si ce bouton est utilisé
        self.mainw.actionGestion.triggered.connect(self.showgestuser)
        # Active la méthode pour se déconnecter du logiciel via le bouton dans le menu
        self.mainw.actionDeconnexion.triggered.connect(self.logout)
        # Active la méthode pour quitter complètement le logiciel via le bouton dans le menu
        self.mainw.actionQuitter.triggered.connect(self.closeall)
        # Permet d'utiliser les 6 boutons pour gérer les clients et les films s'ils sont visibles
        self.mainw.pushButton.clicked.connect(self.popupclient)
        self.mainw.pushButton_2.clicked.connect(self.modifcustomer)
        self.mainw.pushButton_3.clicked.connect(self.suppclient)
        self.mainw.pushButton_5.clicked.connect(self.popupfilm)
        self.mainw.pushButton_4.clicked.connect(self.modiffilm)
        self.mainw.pushButton_6.clicked.connect(self.suppfilm)
        # Démarre les 2 modèles d'arbre qui permettront de voir les clients et les films
        self.model1()
        self.model2()

    # Créer le modèle pour les clients et va chercher les clients dans le dictionnaire correspondant
    def model1(self):
        self.treeViewModel = QtGui.QStandardItemModel()
        self.mainw.treeView.setModel(self.treeViewModel)
        # Bloque la modification des informations directement dans l'arbre. Une fenêtre de modification sera utilisée
        self.mainw.treeView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # Ajuste automatiquement les fenêtres au contenu du dictionnaire des clients
        self.mainw.treeView.header().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        # Créer les entêtes de l'arbre
        self.header = ['ID', 'Nom', "Prénom", "Sexe", "Date Inscription", "Courriel Client", "Mot de passe",
                                     "Numero de Carte", "Expiration", "Code secret"]
        self.treeViewModel.setHorizontalHeaderLabels(self.header)
        # Permet d'afficher les clients selon l'ordre alphabétique de n'importe quelle colonne
        self.mainw.treeView.setSortingEnabled(True)
        # Alterne les couleurs des rangées
        self.mainw.treeView.setAlternatingRowColors(True)

        # Pour chaque client dans le dictionnaire des clients, sépare les informations pour les ajouter dans l'arbre
        # selon les colonnes correspondantes. Les mots de passes seront remplacées par des étoiles dans le modèle
        for b in self.dictclient:
            identifiant = QtGui.QStandardItem(str(b["identifiant"]))
            nom = QtGui.QStandardItem(b["nom"])
            prenom = QtGui.QStandardItem(b["prenom"])
            sexe = QtGui.QStandardItem(b["sexe"])
            date = QtGui.QStandardItem(b["dateinscription"])
            courriel = QtGui.QStandardItem(b["courriel"])
            password = QtGui.QStandardItem("********")
            item = (identifiant, nom, prenom, sexe, date, courriel, password)
            self.treeViewModel.appendRow(item)
            # Met le focus sur le premier client automatiquement
            self.mainw.treeView.setCurrentIndex(self.treeViewModel.index(0, 0))
            # Pour chaque client, ajoute les cartes de crédits dans une range "enfant" de ce client
            for dict in b["cartes"]:
                vide1 = QtGui.QStandardItem("-----")
                vide2 = QtGui.QStandardItem("-----")
                vide3 = QtGui.QStandardItem("-----")
                vide4 = QtGui.QStandardItem("-----")
                vide5 = QtGui.QStandardItem("-----")
                vide6 = QtGui.QStandardItem("-----")
                vide7 = QtGui.QStandardItem("-----")
                numero = QtGui.QStandardItem(dict["noCarte"])
                expiration = QtGui.QStandardItem(dict["expiration"])
                codecarte = QtGui.QStandardItem(dict["codecarte"])
                childitem = (vide1, vide2, vide3, vide4, vide5, vide6, vide7, numero, expiration, codecarte)
                identifiant.appendRow(childitem)
                # Ouvre par défaut tout l'arbre des données
                self.mainw.treeView.expandAll()

    # Créer le modèle pour les films et va chercher les films dans le dictionnaire correspondant
    def model2(self):
        self.treeViewModel2 = QtGui.QStandardItemModel()
        self.mainw.treeView_2.setModel(self.treeViewModel2)
        # Bloque la modification des informations directement dans l'arbre. Une fenêtre de modification sera utilisée
        self.mainw.treeView_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # Ajuste automatiquement les fenêtres au contenu du dictionnaire des clients
        self.mainw.treeView_2.header().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        # Créer les entêtes de l'arbre
        self.header2 = ["Nom", "Durée", "Description", "Catégories", "Description Catégorie", "Nom de l'acteur",
                        "Prénom de l'acteur", "Sexe", "Nom du personnage", "Début de l'emploi", "Fin de l'emploi",
                        "Cachet"]
        self.treeViewModel2.setHorizontalHeaderLabels(self.header2)
        # Permet d'afficher les clients selon l'ordre alphabétique de n'importe quelle colonne
        self.mainw.treeView_2.setSortingEnabled(True)
        # Alterne les couleurs des rangées
        self.mainw.treeView_2.setAlternatingRowColors(True)

        # Pour chaque cfilm dans le dictionnaire des films, sépare les informations pour les ajouter dans l'arbre
        # selon les colonnes correspondantes
        for g in self.dictmovie:
            nom2 = QtGui.QStandardItem(g["nom"])
            duree = QtGui.QStandardItem(g["duree"])
            descriptionfilm = QtGui.QStandardItem(g["descriptionfilm"])
            item2 = (nom2, duree, descriptionfilm)
            self.treeViewModel2.appendRow(item2)
            # Met le focus sur le premier film automatiquement
            self.mainw.treeView_2.setCurrentIndex(self.treeViewModel2.index(0, 0))

            # Pour chaque film, ajoute les catérogies dans une range "enfant" de ce film
            for dict in g["categories"]:
                vide8 = QtGui.QStandardItem("-----")
                vide9 = QtGui.QStandardItem("-----")
                vide10 = QtGui.QStandardItem("-----")
                nomcat = QtGui.QStandardItem(dict["nom"])
                descriptioncat = QtGui.QStandardItem(dict["description"])
                childitem2 = (vide8, vide9, vide10, nomcat, descriptioncat)
                nom2.appendRow(childitem2)

            # Pour chaque film, ajoute les acteurs dans une range "enfant" des catégories de ce film
            for dictact in g["acteurs"]:
                text1 = QtGui.QStandardItem("-----")
                text2 = QtGui.QStandardItem("-----")
                text3 = QtGui.QStandardItem("-----")
                text4 = QtGui.QStandardItem("-----")
                text5 = QtGui.QStandardItem("-----")
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
                # Ouvre par défaut tout l'arbre des données
                self.mainw.treeView_2.expandAll()

    # Est activé par un usager admin. Affiche la fenêtre, le bouton Gestion et les 6 boutons pour gérer les clients/films
    def adminwindow(self):
        self.mainwindow()
        self.mainw.actionGestion.setVisible(True)
        self.mainw.pushButton.show()
        self.mainw.pushButton_2.show()
        self.mainw.pushButton_3.show()
        self.mainw.pushButton_4.show()
        self.mainw.pushButton_5.show()
        self.mainw.pushButton_6.show()

    # Est activé par un usager avec accès modif. Affiche la fenêtre et les 6 boutons pour gérer les clients/films
    def modifwindow(self):
        self.mainwindow()
        self.mainw.pushButton.show()
        self.mainw.pushButton_2.show()
        self.mainw.pushButton_3.show()
        self.mainw.pushButton_4.show()
        self.mainw.pushButton_5.show()
        self.mainw.pushButton_6.show()

    # Active et affiche la fenêtre de gestion des usagers. Active les boutons de la fenêtre ainsi que le modèle d'arbre
    def showgestuser(self):
        self.showgest = GestUser()
        self.showgest.setWindowModality(QtCore.Qt.ApplicationModal) # Bloque l'accès aux fenêtres sous celle-ci
        self.showgest.show()
        self.showgest.setWindowTitle("Gestion des utilisateurs")
        self.showgest.pushButton.clicked.connect(self.showpopuser) # Ouvre le formulaire d'usager si on appuie
        self.showgest.pushButton_2.clicked.connect(self.modifpopup) # Ouvre le formulaire pour modifier l'usager
        self.showgest.pushButton_3.clicked.connect(self.deleteuser) # Envoie vers la fonction supprimer usager
        self.showgest.pushButton_4.clicked.connect(self.showgest.close) # Ferme la fenêtre
        self.modele6() # Affiche l'arbre des usagers


    def modele6(self):
        self.model6 = QtGui.QStandardItemModel()
        self.showgest.treeView.setModel(self.model6)  # Active le modèle
        self.showgest.treeView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers) # Bloque l'édition
        self.showgest.treeView.header().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.model6.setHorizontalHeaderLabels(['Nom', 'Prenom', 'Sexe', 'Date Embauche', 'Code Usager',
                                              'Mot de passe', 'Type Acces'])

        try:  # Défini un try avant de démarrer la boucle
            # Pour chaque dictionnaire dans la liste d'usagers, on créé une ligne avec les informations ci bas
            for c in self.dictuser:
                nom = QtGui.QStandardItem(c["nom"])
                prenom = QtGui.QStandardItem(c["prenom"])
                sexe = QtGui.QStandardItem(c["sexe"])
                dateembauche = QtGui.QStandardItem(c["dateembauche"])
                codeuser = QtGui.QStandardItem(c["codeutilisateur"])
                password = QtGui.QStandardItem("********")
                acces = QtGui.QStandardItem(c["acces"])
                item = (nom, prenom, sexe, dateembauche, codeuser, password, acces)
                self.model6.appendRow(item)
                self.showgest.treeView.setCurrentIndex(self.model6.index(0, 0))
        except Exception:  #Si la boucle n'a pas fonctionné
            pass

    def logout(self):
        os.execl(sys.executable, sys.executable, *sys.argv)     # Ferme toutes les fenêtres et l'application
        self.connex.show()          # Démarre l'affichage de la fenêtre de connexion

    def closeall(self):
        app.closeAllWindows()       # Ferme toutes les fenêtres et l'application

    # Ouvre la fenêtre pour créer un nouvel employé
    def showpopuser(self):
        self.showpopusager = FormUsager()
        self.showpopusager.setWindowModality(QtCore.Qt.ApplicationModal) # Bloque l'accès aux autres fenêtres
        self.showpopusager.show()
        self.showpopusager.setWindowTitle("Ajout d'un nouvel utilisateur")
        self.showpopusager.pushButton.clicked.connect(self.savinguser) # Active le test de sauvegarde si bouton utilisé
        self.showpopusager.pushButton_2.clicked.connect(self.showpopusager.close) # Ferme la fenêtre sans sauvegarder

    # Ici j'utilise la classe Employe héritée de la classe Personne pour inscrire les données du formulaire dans
    # une liste de dictionnaire. Chaque dict = 1 usager. La liste est ensuite enregistrée dans un fichier json crypté
    def savinguser(self):
        employee=Employe(self.showpopusager.lineEdit.text(), self.showpopusager.lineEdit_2.text(),
                         self.showpopusager.comboBox.currentText(), self.showpopusager.dateEdit.text(),
                         self.showpopusager.lineEdit_3.text(), self.showpopusager.lineEdit_5.text(),
                         self.showpopusager.comboBox_2.currentText())
        self.dictemployee=vars(employee)

        # S'il manque des informations, si l'usager existe déjà ou si le mot de passe n'a pas 8 caractères, affiche
        # des fenêtres d'erreur indiquant ce qui doit être corrigé
        if self.showpopusager.lineEdit.text() == "" or self.showpopusager.lineEdit_2.text() == "" or \
                    self.showpopusager.lineEdit_3.text() == "" or self.showpopusager.lineEdit_5.text() == "":
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Veuillez compléter les informations manquantes")
            msg.setInformativeText('')
            msg.setWindowTitle("Erreur")
            msg.exec_()
        elif any(d["codeutilisateur"] == self.showpopusager.lineEdit_3.text() for d in self.dictuser):
            msg = QtWidgets.QMessageBox() # Cherche si le code est déjà dans le dictuser
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
        # Si tout est ok, ajoute une rangée dans le modèle avec les informations, ajoute l'usager dans le dictionnaire
        # des usagers, sauvegarde le fichier crypté et ferme la fenêtre de création d'usager
        else:
            self.model6.appendRow(
                    [QtGui.QStandardItem(self.dictemployee["nom"]),
                     QtGui.QStandardItem(self.dictemployee["prenom"]),
                     QtGui.QStandardItem(self.dictemployee["sexe"]),
                     QtGui.QStandardItem(self.dictemployee["dateembauche"]),
                     QtGui.QStandardItem(self.dictemployee["codeutilisateur"]),
                     QtGui.QStandardItem("********"),
                     QtGui.QStandardItem(self.dictemployee["acces"])])
            self.dictuser.append(self.dictemployee)
            self.saveuser()
            self.showpopusager.close()

    # Si l'usager est l'admin, affiche une fenêtre expliquant qu'il ne peut être modifé,sinon ouvre la fenêtre des
    # nouveaux usagers mais avec les informations pré-remplies de l'usager sélectionné
    def modifpopup(self):
        self.donnees = self.showgest.treeView.selectedIndexes()[4] # Va chercher le nom de l'usager sélectionné

        # Créer un dictionnaire temporaire (self.showuser) de l'usager sélectionné afin d'effectuer les modifications
        for dict in self.dictuser:
            if dict["codeutilisateur"] == self.donnees.data():
                self.showuser = dict

        if self.showuser["codeutilisateur"] == "admin":
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("L'administrateur système ne peut être modifié")
            msg.setInformativeText('')
            msg.setWindowTitle("Erreur")
            msg.exec_()
        # On ouvre la fenêtre de nouveau usager et on pré-charge les lineedit etc avec les informations de l'usager
        # sélectionné. Un peu de conversion en int doit être fait pour les combobox et les dateedit.
        else:
            self.showpopusager = FormUsager()
            self.showpopusager.setWindowModality(QtCore.Qt.ApplicationModal)
            self.showpopusager.show()
            self.showpopusager.setWindowTitle("Modification d'un utilisateur")
            self.showpopusager.pushButton.clicked.connect(self.modifuser)
            self.showpopusager.pushButton_2.clicked.connect(self.showpopusager.close)
            index = self.showpopusager.comboBox.findText(self.showuser["sexe"],QtCore.Qt.MatchFlag.MatchFixedString)
            date = QtCore.QDate.fromString(self.showuser["dateembauche"], "dd-MM-yyyy")
            index2 = self.showpopusager.comboBox_2.findText(self.showuser["acces"],QtCore.Qt.MatchFlag.MatchFixedString)
            # Comme l'identifiant est unique, on bloque la ligneedit pour qu'il ne puisse être modifié
            self.showpopusager.lineEdit_3.setEnabled(False)
            self.showpopusager.lineEdit.setText(self.showuser["nom"])
            self.showpopusager.lineEdit_2.setText(self.showuser["prenom"])
            self.showpopusager.comboBox.setCurrentIndex(index)
            self.showpopusager.dateEdit.setDate(date)
            self.showpopusager.lineEdit_3.setText(self.showuser["codeutilisateur"])
            self.showpopusager.lineEdit_5.setText(self.showuser["password"])
            self.showpopusager.comboBox_2.setCurrentIndex(index2)

    # Si le mot de passe n'a pas 8 caractères, ouvre la fenêtre d'erreur
    def modifuser(self):
        if len(self.showpopusager.lineEdit_5.text()) < 8:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Le mot de passe doit avoir 8 caractère minimum")
            msg.setInformativeText('')
            msg.setWindowTitle("Erreur")
            msg.exec_()
        # Avec la commande next, va chercher l'usager ayant le même codeutilisateur et le rempalce par les informations
        # des différents lineedit etc de la fenêtre d'usager. Rafraîchit le modèle et sauvegarde le fichier json
        else:
            changeusager = next(  # va chercher le même usager et le change par les informations ci bas
                item for item in self.dictuser if item["codeutilisateur"] == self.showuser["codeutilisateur"])
            changeusager["nom"] = self.showpopusager.lineEdit.text()
            changeusager["prenom"] = self.showpopusager.lineEdit_2.text()
            changeusager["sexe"] = self.showpopusager.comboBox.currentText()
            changeusager["dateembauche"] = self.showpopusager.dateEdit.text()
            changeusager["password"] = self.showpopusager.lineEdit_5.text()
            changeusager["acces"] = self.showpopusager.comboBox_2.currentText()
            self.showpopusager.close()
            self.modele6()
            self.saveuser()

    # Si l'usager à supprimer et l'admin, ouvre la fenêtre d'erreur
    def deleteuser(self):
        donnees = [e.data() for e in self.showgest.treeView.selectedIndexes()] # Créé une liste des données sélectionées
        if donnees[4] == "admin":
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("L'administrateur système ne peut être supprimé")
            msg.setInformativeText('')
            msg.setWindowTitle("Erreur")
            msg.exec_()
        else: self.testdelete()

    # Ouvre une fenêtre de confirmation pour demander si l'usager sélectionné doit vraiment être supprimé
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

    # Avec l'usager sélectionné, on remonte à l'index0 et on supprime l'usager du modèle et du dictionnaire des usagers.
    # On sauvegarde le fichier json crypté des usagers
    def yesdelete(self):
        indexes = self.showgest.treeView.selectedIndexes()
        donnees = [f.data() for f in self.showgest.treeView.selectedIndexes()]
        if indexes:
            index = indexes[0]
            self.model6.removeRow(index.row())
            self.dictuser = [element for element in self.dictuser if element.get('codeutilisateur', '') != donnees[4]]
            self.saveuser()

    # Charge et affiche la fenêtre du nouveau client et prépare les boutons pour les méthodes correspondantes.
    # Un dictionnaire temporaire de client sera créé afin d'y ajouter des cartes de crédits mais que celles-ci ne
    # soient pas enregistrées si le bouton Annuler est utilisé par l'utilisateur du logiciel
    def popupclient(self):
        self.popupcustomer = FormClient()
        self.popupcustomer.setWindowModality(QtCore.Qt.ApplicationModal)
        self.popupcustomer.show()
        self.popupcustomer.pushButton.clicked.connect(self.savecustomer)
        self.popupcustomer.pushButton_2.clicked.connect(self.popupcustomer.close)
        self.popupcustomer.pushButton_3.clicked.connect(self.ajoutercarte)
        self.popupcustomer.pushButton_4.clicked.connect(self.suppcarte)
        # Créer le modèle pour la liste des cartes de crédit du nouveau client
        self.model3 = QtGui.QStandardItemModel()
        self.popupcustomer.treeView.setModel(self.model3)  # Active le modèle
        self.popupcustomer.treeView.header().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.popupcustomer.treeView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.model3.setHorizontalHeaderLabels(['Numéro de carte', 'Date Expiration', 'Code Carte'])

        # Contrairement aux usagers qui ont un nom d'utilisateur unique, les clients ont le droit de modifier leurs
        # courriels. Je vais donc ajouter un identifiant unique à la classe Client et l'utiliser pour faire la
        # distinction entre chaque client.

        # Je fais une boucle pour aller chercher le prochain chiffre disponible pour l'identifiant unique du prochain
        # client que je vais créer et je l'inclus dans une variable identifiant
        identifiant = 1
        try:
            for l in self.dictclient:
                while identifiant == l["identifiant"]:
                    identifiant = identifiant + 1
        except Exception:
            pass

        # Je créé un dictionnaire temporaire en utilisant la classe Client héritée de la classe Personne
        self.client = Client(identifiant, self.popupcustomer.lineEdit.text(), self.popupcustomer.lineEdit_2.text(),
                        self.popupcustomer.comboBox.currentText(), self.popupcustomer.dateEdit.text(),
                        self.popupcustomer.lineEdit_3.text(), self.popupcustomer.lineEdit_5.text(), [])
        self.dataclient = vars(self.client)
        self.popupcustomer.setWindowTitle(str(identifiant))
        self.popupcustomer.lineEdit.setFocus()

    # Ici je recréé un dictionnaire du client de la classe Client, il servira pour mettre à jour la liste des clients.
    # Il va aller chercher la liste des cartes de crédits temporairement enregistrées dans le dict. self.dataclient
    def savecustomer(self):
        identifiant = 1
        try:
            for l in self.dictclient:
                while identifiant == l["identifiant"]:
                    identifiant = identifiant + 1
        except Exception:
            pass
        updatedclient = Client(identifiant, self.popupcustomer.lineEdit.text(), self.popupcustomer.lineEdit_2.text(),
                        self.popupcustomer.comboBox.currentText(), self.popupcustomer.dateEdit.text(),
                        self.popupcustomer.lineEdit_3.text(), self.popupcustomer.lineEdit_5.text(), [])
        self.updateddataclient = vars(updatedclient)
        # C'est ici que le client mis à jour va prendre les cartes temporairement stockées dans self.dataclient
        self.updateddataclient["cartes"] = self.dataclient["cartes"]
        # Vérifie s'il manque des informations, si le courriel a déjà été utilisé et si le mot de passe a min. 8 carac.
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
            # Ajoute le nouveau client dans le modèle des clients
            identifiant = QtGui.QStandardItem(str(self.updateddataclient["identifiant"]))
            nom = QtGui.QStandardItem(self.updateddataclient["nom"])
            prenom = QtGui.QStandardItem(self.updateddataclient["prenom"])
            sexe = QtGui.QStandardItem(self.updateddataclient["sexe"])
            date = QtGui.QStandardItem(self.updateddataclient["dateinscription"])
            courriel = QtGui.QStandardItem(self.updateddataclient["courriel"])
            password = QtGui.QStandardItem("********")
            item = (identifiant, nom, prenom, sexe, date, courriel, password)
            self.treeViewModel.appendRow(item)
            # Ajoute les nouvelles cartes dans la rangée enfant du client nouvellement créé
            for dict in self.updateddataclient["cartes"]:
                vide1 = QtGui.QStandardItem("-----")
                vide2 = QtGui.QStandardItem("-----")
                vide3 = QtGui.QStandardItem("-----")
                vide4 = QtGui.QStandardItem("-----")
                vide5 = QtGui.QStandardItem("-----")
                vide6 = QtGui.QStandardItem("-----")
                vide7 = QtGui.QStandardItem("-----")
                numero = QtGui.QStandardItem(dict["noCarte"])
                expiration = QtGui.QStandardItem(dict["expiration"])
                codecarte = QtGui.QStandardItem(dict["codecarte"])
                childitem = (vide1, vide2, vide3, vide4, vide5, vide6, vide7, numero, expiration, codecarte)
                identifiant.appendRow(childitem)
            # Remet le focus sur le premier client
            self.mainw.treeView.setCurrentIndex(self.treeViewModel.index(0, 0))
            # Ajoute le novueau client au dictionnaire des clients
            self.dictclient.append(self.updateddataclient)
            # Sauvegarde le dictionnaire dans le json crypté
            self.saveclient()
            # Ferme le formulaire de nouveau client
            self.popupcustomer.close()

    # Prépare la modification du client sélectionné
    def modifcustomer(self):
        # Si la rangée sélectionnée est une rangée enfant du client, remonte jusqu'à la rangée du client pour prendre
        # les informations du client sélectionné
        self.donneesclient = self.mainw.treeView.selectedIndexes()[0]
        if self.donneesclient.data() == "-----":
            self.donneesclient = self.donneesclient.parent()

        # Prépare 2 dictionnaires, donc une copie qui sera utilisée comme dictionnaire temporaire si le bouton Annuler
        # est utilisé
        for dict in self.dictclient :
            if str(dict["identifiant"]) == self.donneesclient.data():
                self.showclient = dict
                self.dataclient = copy.deepcopy(self.showclient)

        # Ouvre la fenêtre du nouveau client, prépare les boutons correspondants
        self.popupcustomer = FormClient()
        self.popupcustomer.setWindowModality(QtCore.Qt.ApplicationModal)
        self.popupcustomer.show()
        self.popupcustomer.setWindowTitle("Modification d'un client")
        self.popupcustomer.pushButton.clicked.connect(self.savemodifcustomer)
        self.popupcustomer.pushButton_2.clicked.connect(self.popupcustomer.close)
        self.popupcustomer.pushButton_3.clicked.connect(self.ajoutercarte)
        self.popupcustomer.pushButton_4.clicked.connect(self.suppcarte)
        self.popupcustomer.lineEdit.setFocus()
        # Créer un modèle pour afficher la liste des cartes de crédits du client
        self.model3 = QtGui.QStandardItemModel()
        self.popupcustomer.treeView.setModel(self.model3)  # Active le modèle
        self.model3.setHorizontalHeaderLabels(['Numéro de carte', 'Date Expiration', 'Code Carte'])
        self.popupcustomer.treeView.header().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.popupcustomer.treeView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # Inclus dans le modèle les cartes de crédit provenant du client sélectionné
        for h in self.showclient["cartes"]:
            numero = QtGui.QStandardItem(h["noCarte"])
            expiration = QtGui.QStandardItem(h["expiration"])
            codecarte = QtGui.QStandardItem(h["codecarte"])
            item = (numero, expiration, codecarte)
            self.model3.appendRow(item)
        # Prépare et pré-inscrit les informations dans les lineedit etc. du formulaire de nouveau client
        index = self.popupcustomer.comboBox.findText(self.dataclient["sexe"], QtCore.Qt.MatchFlag.MatchFixedString)
        date = QtCore.QDate.fromString(self.dataclient["dateinscription"], "dd-MM-yyyy")
        self.popupcustomer.setWindowTitle(str(self.dataclient["identifiant"]))
        self.popupcustomer.lineEdit.setText(self.dataclient["nom"])
        self.popupcustomer.lineEdit_2.setText(self.dataclient["prenom"])
        self.popupcustomer.comboBox.setCurrentIndex(index)
        self.popupcustomer.dateEdit.setDate(date)
        self.popupcustomer.lineEdit_3.setText(self.dataclient["courriel"])
        self.popupcustomer.lineEdit_5.setText(self.dataclient["motdepasse"])


    # Charge et affiche le petit formulaire pour ajouter une nouvelle carte de crédit avec les boutons correspondants
    def ajoutercarte(self):
        self.showpopcarte = Popcarte()
        self.showpopcarte.setWindowModality(QtCore.Qt.ApplicationModal)
        self.showpopcarte.show()
        self.showpopcarte.setWindowTitle("Ajout d'une carte de crédit")
        self.showpopcarte.lineEdit.setFocus()
        self.showpopcarte.pushButton.clicked.connect(self.savecarte)
        self.showpopcarte.pushButton_2.clicked.connect(self.showpopcarte.close)

    # Valide s'il manque des informations
    def savecarte(self):
        if self.showpopcarte.lineEdit.text() == "" or self.showpopcarte.lineEdit_2.text() == "":
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Veuillez compléter les informations manquantes")
            msg.setInformativeText('')
            msg.setWindowTitle("Erreur")
            msg.exec_()
        # AJoute la carte dans le modèle de la fenêtre des clients et charge la nouvelle carte dans le dictionnaire
        # temporaire du client (au cas où l'usager appuierait sur Annuler les modifications du client)
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

    # Valide si une carte est sélectionnée, si oui, affiche la fenêtre de confirmation de suppression de la carte
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
    # Si la confirmation est effectuée, remonte à l'index0 de la carte sélectionnée et la retire du moèle, la retire
    # aussi du dictionnaire temporaire du client à modifier/créer
    def deletecarte(self):
        indexes = self.popupcustomer.treeView.selectedIndexes()
        donnees = [f.data() for f in self.popupcustomer.treeView.selectedIndexes()]
        if indexes:
            index = indexes[0]  # L'index correspond à la liste des items de la rangée
            self.model3.removeRow(index.row())  # Enlève l'item
            self.dataclient["cartes"] = [element for element in self.dataclient["cartes"] if
                                 element.get('noCarte', '') != donnees[0]]


    # Valide si le courriel a été modifié, si oui, valide si le nouveau existe dans la liste des clients. Si oui,
    # fait apparaître la fenêtre de courriel déjà utilisé. Valide si le mot de passe a 8 caractères minimum.
    def savemodifcustomer(self):
        # Cherche si le courriel qui a changé est déjà dans le dictuser
        if self.popupcustomer.lineEdit_3.text() != self.dataclient["courriel"] and \
                any(j["courriel"] == self.popupcustomer.lineEdit_3.text() for j in self.dictclient):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Ce courriel est déjà utilisé")
            msg.setInformativeText('')
            msg.setWindowTitle("Erreur")
            msg.exec_()
        # Vérifie si le mot de passe fait au moins 8 caractères, sinon une alerte pop
        elif len(self.popupcustomer.lineEdit_5.text()) < 8:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Le mot de passe doit avoir 8 caractère minimum")
            msg.setInformativeText('')
            msg.setWindowTitle("Erreur")
            msg.exec_()
        else:
            # Va chercher le même client qui correspond à l'identifiant et le change par les informations ci bas
            changeclient = next(
                item for item in self.dictclient if item["identifiant"] == self.dataclient["identifiant"])
            changeclient["nom"] = self.popupcustomer.lineEdit.text()
            changeclient["prenom"] = self.popupcustomer.lineEdit_2.text()
            changeclient["sexe"] = self.popupcustomer.comboBox.currentText()
            changeclient["dateinscription"] = self.popupcustomer.dateEdit.text()
            changeclient["courriel"] = self.popupcustomer.lineEdit_3.text()
            changeclient["motdepasse"] = self.popupcustomer.lineEdit_5.text()
            changeclient["cartes"] = self.dataclient["cartes"]
            # Rafraîchit le modèle
            self.model1()
            self.popupcustomer.close()
            # Sauvegarde le dictionnaire dans le json crypté
            self.saveclient()

    # Pour éviter les erreurs, on valide que le client à supprimer est réellement sélectionné (et non une rangée enfant)
    def suppclient(self):
        self.deleteclient = self.mainw.treeView.selectedIndexes()[0]
        if self.deleteclient.data() == "-----":
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Veuillez sélectionner directement le client à supprimer")
            msg.setInformativeText('')
            msg.setWindowTitle("Erreur")
            msg.exec_()
        # Affiche la fenêtre pour confirmer la suppression du client
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

    # Remonte à l'index0 du client sélectionné et le retire du modèle. Le retire aussi du dicitonnaire des clients et
    # sauvegarde le fichier json crypté
    def yesdeletecustomer(self):
        indexes = self.mainw.treeView.selectedIndexes()
        donnees = [f.data() for f in self.mainw.treeView.selectedIndexes()]
        if indexes:
            index = indexes[0]  # L'index correspond à la liste des items de la rangée
            self.treeViewModel.removeRow(index.row())  # Enlève l'item
            self.dictclient = [element for element in self.dictclient if
                             element.get('identifiant', '') != int(donnees[0])]
            self.saveclient()

    # Charge la fenêtre de nouveau film et l'affiche avec ses boutons correspondants
    def popupfilm(self):
        self.popupfilm = Formfilm()
        self.popupfilm.setWindowModality(QtCore.Qt.ApplicationModal)
        self.popupfilm.show()
        self.popupfilm.setWindowTitle("Ajout d'un nouveau film")
        self.popupfilm.pushButton.clicked.connect(self.savemovie)
        self.popupfilm.pushButton_2.clicked.connect(self.popupfilm.close)
        self.popupfilm.pushButton_3.clicked.connect(self.popupcategorie)
        self.popupfilm.pushButton_4.clicked.connect(self.suppcategorie)
        self.popupfilm.pushButton_5.clicked.connect(self.popacteur)
        self.popupfilm.pushButton_6.clicked.connect(self.suppacteur)
        # Créé le modèle pour afficher les futures catégories
        self.model4 = QtGui.QStandardItemModel()
        self.popupfilm.treeView.setModel(self.model4)
        self.model4.setHorizontalHeaderLabels(["Nom de catégorie", "Description de la catégorie"])
        self.popupfilm.treeView.header().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.popupfilm.treeView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # Créé le modèle pour afficher les futurs acteurs
        self.model5 = QtGui.QStandardItemModel()
        self.popupfilm.treeView_2.setModel(self.model5)
        self.model5.setHorizontalHeaderLabels(["Nom", "Prénom", "Sexe", "Personnage", "Début de l'emploi",
                                               "Fin de l'emploi", "Cachet"])
        self.popupfilm.treeView_2.header().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.popupfilm.treeView_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # Créé un dictionnaire temporaire du nouveau film en se basant sur la Classe FIlm
        self.movie = Film(self.popupfilm.lineEdit.text(), self.popupfilm.timeEdit.text(),
                          self.popupfilm.lineEdit_2.text(), [], [])
        self.datafilm = vars(self.movie)
        self.popupfilm.lineEdit.setFocus()

    # Créer un dictionnaire qui servira à mettre à jour le dictionnaire des films, ce dictionnaire va aller prendre
    # les dictionnaires temporaires de catérogies et d'acteurs de la variable self.datafilm
    def savemovie(self):
        updatedfilm = Film(self.popupfilm.lineEdit.text(), self.popupfilm.timeEdit.text(),
                               self.popupfilm.lineEdit_2.text(), [], [])
        self.updateddatafilm = vars(updatedfilm)
        self.updateddatafilm["categories"] = self.datafilm["categories"]
        self.updateddatafilm["acteurs"] = self.datafilm["acteurs"]
        # Valide s'il manque des informations ou si le nom du film a déjà été utilisé
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
        # Ajoute le nouveau film dans le modèle2 de la page principale
        else:
            nom = QtGui.QStandardItem(self.updateddatafilm["nom"])
            duree = QtGui.QStandardItem(self.updateddatafilm["duree"])
            descriptionfilm = QtGui.QStandardItem(self.updateddatafilm["descriptionfilm"])
            item3 = (nom, duree, descriptionfilm)
            self.treeViewModel2.appendRow(item3)
            # Ajoute les catérogies dans la rangée enfant des films
            for dict in self.updateddatafilm["categories"]:
                vide1 = QtGui.QStandardItem("-----")
                vide2 = QtGui.QStandardItem("-----")
                vide3 = QtGui.QStandardItem("-----")
                nomfilm = QtGui.QStandardItem(dict["nom"])
                descricat = QtGui.QStandardItem(dict["description"])
                childitem3 = (vide1, vide2, vide3, nomfilm, descricat)
                nom.appendRow(childitem3)
            # Ajoute les acteurs dans la rangée enfant des catégories
            for dictact in self.updateddatafilm["acteurs"]:
                text1 = QtGui.QStandardItem("-----")
                text2 = QtGui.QStandardItem("-----")
                text3 = QtGui.QStandardItem("-----")
                text4 = QtGui.QStandardItem("-----")
                text5 = QtGui.QStandardItem("-----")
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

            # Remet le focus sur le premier film, ajoute le film dans le dictionnaire des films, sauvegarde le fichier
            # json crypté et ferme le formulaire de nouveau film
            self.mainw.treeView_2.setCurrentIndex(self.treeViewModel2.index(0, 0))
            self.dictmovie.append(self.updateddatafilm)
            self.savefilm()
            self.popupfilm.close()

    # Tant que c'est une rangée enfant qui est sélectionnée, remonte au parent jusqu'à avoir le nom du film
    def modiffilm(self):
        self.donneesfilm = self.mainw.treeView_2.selectedIndexes()[0]
        try:
            while self.donneesfilm.data() == "-----":
                self.donneesfilm = self.donneesfilm.parent()
        except Exception:
            pass

        # Prépare 2 dictionnaires, donc une copie qui sera utilisée comme dictionnaire temporaire si le bouton Annuler
        # est utilisé
        for dict in self.dictmovie :
            if dict["nom"] == self.donneesfilm.data():
                self.showfilm = dict
                self.datafilm = copy.deepcopy(self.showfilm)

        # Affiche le formulaire de nouveau film avec les boutons, et pré-remplies les informations selon le film
        # sélectionné ainsi que les 2 modèles pour les catérogies et les acteurs
        self.popupfilm = Formfilm()
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
        self.popupfilm.treeView.header().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.popupfilm.treeView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        for m in self.showfilm["categories"]:
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
        self.popupfilm.treeView_2.header().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.popupfilm.treeView_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.popupfilm.lineEdit_2.setFocus()

        for n in self.showfilm["acteurs"] :
            nomacteur = QtGui.QStandardItem(n["nom"])
            prenomacteur = QtGui.QStandardItem(n["prenom"])
            sexe = QtGui.QStandardItem(n["sexe"])
            nomperso = QtGui.QStandardItem(n["nompersonnage"])
            debutemploi = QtGui.QStandardItem(n["debutemploi"])
            finemploi = QtGui.QStandardItem(n["finemploi"])
            cachet = QtGui.QStandardItem(n["cachet"])
            item2 = (nomacteur, prenomacteur, sexe, nomperso, debutemploi, finemploi, cachet)
            self.model5.appendRow(item2)

    # Charge et ouvre le formulaire de nouvelle catégorie ainsi que les boutons correspondants
    def popupcategorie(self):
        self.showpopcat = Popcategorie()
        self.showpopcat.setWindowModality(QtCore.Qt.ApplicationModal)
        self.showpopcat.show()
        self.showpopcat.setWindowTitle("Ajout d'une nouvelle catégorie")
        self.showpopcat.lineEdit.setFocus()
        self.showpopcat.pushButton.clicked.connect(self.savecat)
        self.showpopcat.pushButton_2.clicked.connect(self.showpopcat.close)

    # Valide s'il manque des informations et charge la catérogie dans le modèle ainsi que dans la variable temporaire
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

    # Valide si une catégorie est sélectionnée et affiche la fenêtre de confirmation de suppression
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
    # Pour la catégorie sélectionnée, la supprime du modèle ainsi que du dictionnaire temporaire
    def deletecat(self):
        indexes = self.popupfilm.treeView.selectedIndexes()
        donnees = [f.data() for f in self.popupfilm.treeView.selectedIndexes()]
        if indexes:
            index = indexes[0]  # L'index correspond à la liste des items de la rangée
            self.model4.removeRow(index.row())  # Enlève l'item
            self.datafilm["categories"] = [element for element in self.datafilm["categories"] if
                                            element.get('nom', '') != donnees[0]]

    # Charge et ouvre le formulaire de nouvel acteur ainsi que les boutons correspondants
    def popacteur(self):
        self.showpopupacteur = Popacteur()
        self.showpopupacteur.setWindowModality(QtCore.Qt.ApplicationModal)
        self.showpopupacteur.show()
        self.showpopupacteur.setWindowTitle("Ajout d'un nouvel acteur")

        self.showpopupacteur.lineEdit.setFocus()
        self.showpopupacteur.pushButton.clicked.connect(self.saveacteur)
        self.showpopupacteur.pushButton_2.clicked.connect(self.showpopupacteur.close)

    # Valide s'il manque des informations et charge l'acteur dans le modèle ainsi que dans la variable temporaire
    # en utilisant la classe Acteur héritée de Personne
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

    # Valide si un acteur est sélectionné, si oui, affiche la fenêtre de confirmation de suppression de l'acteur
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

    # Pour l'acteur sélectionné, le supprime du modèle ainsi que du dictionnaire temporaire
    def deleteacteur(self):
        indexes = self.popupfilm.treeView_2.selectedIndexes()
        donnees = [f.data() for f in self.popupfilm.treeView_2.selectedIndexes()]
        if indexes:
            index = indexes[0]  # L'index correspond à la liste des items de la rangée
            self.model5.removeRow(index.row())  # Enlève l'item
            self.datafilm["acteurs"] = [element for element in self.datafilm["acteurs"] if
                                           element.get('nompersonnage', '') != donnees[3]]

    # Va chercher le même film qui correspond dans le dictionnaire des films et le change par les informations ci bas
    # et charge aussi les dictionnaires temporaires des catégories et des films. Sauvegarde le json crypté
    def savemodifmovie(self):
        changefilm = next(
            item for item in self.dictmovie if item["nom"] == self.datafilm["nom"])
        changefilm["nom"] = self.popupfilm.lineEdit.text()
        changefilm["duree"] = self.popupfilm.timeEdit.text()
        changefilm["descriptionfilm"] = self.popupfilm.lineEdit_2.text()
        changefilm["categories"] = self.datafilm["categories"]
        changefilm["acteurs"] = self.datafilm["acteurs"]

        self.model2()
        self.popupfilm.close()
        self.savefilm()

    # Pour éviter les erreurs, on valide que le client à supprimer est réellement sélectionné (et non une rangée enfant)
    def suppfilm(self):
        self.deletefilm = self.mainw.treeView_2.selectedIndexes()[0]
        if self.deletefilm.data() == "-----":
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Veuillez sélectionner directement le film à supprimer")
            msg.setInformativeText('')
            msg.setWindowTitle("Erreur")
            msg.exec_()
    # Ouvre la fenêtre de confirmation de suppresion
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

    # Remonte à l'index0 du film sélectionné et le retire du modèle. Le retire aussi du dicitonnaire des films et
    # sauvegarde le fichier json crypté
    def yesdeletemovie(self):
        indexes = self.mainw.treeView_2.selectedIndexes()
        donnees = [f.data() for f in self.mainw.treeView_2.selectedIndexes()]

        if indexes:
            index = indexes[0]  # L'index correspond à la liste des items de la rangée
            self.treeViewModel2.removeRow(index.row())  # Enlève l'item
            self.dictmovie = [element for element in self.dictmovie if
                             element.get('nom', '') != donnees[0]]
            self.savefilm()

#Active le module système et démarre le logiciel en activant la méthode showlogin
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.showlogin()
    sys.exit(app.exec_())
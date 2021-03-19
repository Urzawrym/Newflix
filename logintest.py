from PyQt5 import QtCore, QtGui, QtWidgets
from cryptography.fernet import Fernet

"""key = Fernet.generate_key()
file = open('key.key','wb')
file.write(key)
file.close()

file = open('key.key','rb')
key = file.read()
file.close()"""


class Personne:
    def __init__(self, prenom, nom, sexe):
        self.nom = nom
        self.prenom = prenom
        self.sexe = sexe

    def getPrenom(self):
        return self.prenom

    def setPrenom(self, prenom):
        if type(prenom) == str:
            self.prenom = prenom

    def getNom(self):
        return self.nom

    def setNom(self, nom):
        if type(nom) == str:
            self.nom = nom

    def setSexe(self, sexe):
        if type(sexe) == str:
            self.sexe = sexe

class Employe(Personne):
    def __init__(self, prenom, nom, sexe, dateembauche, codeutilisateur, password, acces):
        super().__init__(prenom, nom, sexe)
        self.dateembauche = dateembauche
        self.codeutilisateur = codeutilisateur
        self.password = password
        self.acces = acces

class Client(Personne):
    def __init__(self, prenom, nom, sexe, dateinscription, courriel, motdepasse, cartes):
        super().__init__(prenom,nom,sexe)
        self.dateinscription = dateinscription
        self.courriel = courriel
        self.motdepasse = motdepasse
        self.cartes = []

    def setCredit(self,credit):
        self.cartes.append(credit)
    def getListeCredit(self):
        return self.cartes
    def getNbCredit(self):
        return len(self.cartes)

class CarteCredit:
    "Carte de crédit"
    def __init__(self, noCarte, Expiration, codecarte):
            self.noCarte = noCarte
            self.expiration = Expiration
            self.codecarte = codecarte

class Acteur(Personne):
    def __init__(self, prenom, nom, sexe, film, nompersonnage, debutemploi, finemploi, cachet):
        super().__init__(prenom, nom, sexe)
        self.film = film
        self.nompersonnage = nompersonnage
        self.debutemploi = debutemploi
        self.finemploi = finemploi
        self.cachet = cachet

class Film:
    def __init__(self, nom, duree, descriptionfilm, categorie):
        self.nom = nom
        self.duree = duree
        self.description = descriptionfilm
        self.categorie = []

class Categoriefilm:
    def __init__(self, nom, descriptioncat):
        self.nom = nom
        self.description = descriptioncat


AdminUser = {"admin":"admin123"}
ModifList = {"claude":"1234","mathieu":"royer"}
Viewlist = {"meo":"5678"}


class Ui_MainWindow(object):
    def setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(713, 554)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(580, 40, 75, 23))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 70, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(580, 100, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.ListeClient = QtWidgets.QListWidget(self.centralwidget)
        self.ListeClient.setGeometry(QtCore.QRect(20, 40, 551, 192))
        self.ListeClient.setObjectName("ListeClient")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(580, 310, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(580, 340, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.ListeClient_2 = QtWidgets.QListWidget(self.centralwidget)
        self.ListeClient_2.setGeometry(QtCore.QRect(20, 280, 551, 192))
        self.ListeClient_2.setObjectName("ListeClient_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(580, 280, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 131, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 260, 181, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 713, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.actionGestion = QtWidgets.QAction(MainWindow)
        self.actionGestion.setObjectName("actionGestion")
        self.actionGestion.triggered.connect(self.GestUi)
        self.actionD_connexion = QtWidgets.QAction(MainWindow)
        self.actionD_connexion.setObjectName("actionD_connexion")
        self.actionD_connexion.triggered.connect(self.LogoutUi)
        self.actionQuitter = QtWidgets.QAction(MainWindow)
        self.actionQuitter.setObjectName("actionQuitter")
        self.actionQuitter.triggered.connect(self.CloseUi)
        self.menuMenu.addSeparator()
        self.menuMenu.addSeparator()
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionGestion)
        self.menuMenu.addAction(self.actionD_connexion)
        self.menuMenu.addAction(self.actionQuitter)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.retranslateUi2(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi2(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Newflix"))
        self.pushButton_1.setText(_translate("MainWindow", "Ajouter"))
        self.pushButton_2.setText(_translate("MainWindow", "Modifier"))
        self.pushButton_3.setText(_translate("MainWindow", "Supprimer"))
        self.pushButton_4.setText(_translate("MainWindow", "Modifier"))
        self.pushButton_5.setText(_translate("MainWindow", "Supprimer"))
        self.pushButton_6.setText(_translate("MainWindow", "Ajouter"))
        self.label.setText(_translate("MainWindow", "Liste des clients"))
        self.label_2.setText(_translate("MainWindow", "Liste des films"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionGestion.setText(_translate("MainWindow", "Gestion Employés"))
        self.actionD_connexion.setText(_translate("MainWindow", "Déconnexion"))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter"))

    def GestionUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(685, 156)
        self.listWidget_1 = QtWidgets.QListWidget(Form)
        self.listWidget_1.setGeometry(QtCore.QRect(10, 30, 571, 111))
        self.listWidget_1.setObjectName("listWidget")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(590, 30, 75, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.userUi)
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(590, 70, 75, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(590, 110, 75, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 281, 16))
        self.label_3.setObjectName("label_3")
        self.retranslateUi3(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi3(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Liste employés"))
        self.pushButton_7.setText(_translate("Form", "Ajouter"))
        self.pushButton_8.setText(_translate("Form", "Modifier"))
        self.pushButton_9.setText(_translate("Form", "Supprimer"))
        self.label_3.setText(_translate("Form", "Liste des employés"))

    def GestUi(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.GestionUi(self.window)
        self.window.show()
        MainWindow.hide()

    def popuserUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(408, 207)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 113, 20))
        self.lineEdit.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 60, 47, 13))
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 80, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 110, 47, 13))
        self.label_6.setObjectName("label_6")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(10, 130, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 150, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Form)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 170, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(140, 10, 91, 16))
        self.label_7.setObjectName("label_7")
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(140, 30, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(270, 10, 111, 16))
        self.label_8.setObjectName("label_8")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(270, 30, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(270, 60, 111, 16))
        self.label_9.setObjectName("label_9")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(270, 80, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.radioButton_4 = QtWidgets.QRadioButton(Form)
        self.radioButton_4.setGeometry(QtCore.QRect(140, 80, 82, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(Form)
        self.radioButton_5.setGeometry(QtCore.QRect(140, 100, 82, 17))
        self.radioButton_5.setObjectName("radioButton_5")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(140, 60, 71, 16))
        self.label_10.setObjectName("label_10")
        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(110, 140, 131, 41))
        self.pushButton_10.setObjectName("pushButton")
        self.pushButton_11 = QtWidgets.QPushButton(Form)
        self.pushButton_11.setGeometry(QtCore.QRect(260, 140, 131, 41))
        self.pushButton_11.setObjectName("pushButton_2")
        self.retranslateUi4(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi4(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Formulaire employé"))
        self.label_4.setText(_translate("Form", "Nom :"))
        self.label_5.setText(_translate("Form", "Prénom :"))
        self.label_6.setText(_translate("Form", "Sexe :"))
        self.radioButton.setText(_translate("Form", "Masculin"))
        self.radioButton_2.setText(_translate("Form", "Féminin"))
        self.radioButton_3.setText(_translate("Form", "Non défini"))
        self.label_7.setText(_translate("Form", "Date embauche :"))
        self.label_8.setText(_translate("Form", "Code utilisateur :"))
        self.label_9.setText(_translate("Form", "Mot de passe :"))
        self.radioButton_4.setText(_translate("Form", "Total"))
        self.radioButton_5.setText(_translate("Form", "Lecture"))
        self.label_10.setText(_translate("Form", "Type accès :"))
        self.pushButton_10.setText(_translate("Form", "Sauvegarder"))
        self.pushButton_11.setText(_translate("Form", "Annuler"))

    def userUi(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.popuserUi(self.window)
        self.window.show()


    def LoginUi(self, Connexion):
        MainWindow.setObjectName("Connexion")
        MainWindow.resize(229, 177)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.login = QtWidgets.QLineEdit(self.centralwidget)
        self.login.setObjectName("login")
        self.login.returnPressed.connect(self.testconnex)
        self.gridLayout.addWidget(self.login, 0, 1, 1, 1)
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.password.returnPressed.connect(self.testconnex)
        self.gridLayout.addWidget(self.password, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.testconnex)
        self.pushButton.setAutoDefault(True)
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Connexion", "Connexion"))
        self.login.setPlaceholderText(_translate("MainWindow", "Usager"))
        self.password.setPlaceholderText(_translate("MainWindow", "Mot de passe"))
        self.pushButton.setText(_translate("MainWindow", "Connexion"))

    def CloseUi(self):
        app.closeAllWindows()

    def LogoutUi(self):
        app.closeAllWindows()
        MainWindow.show()

    def AdminUi(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setup(self.window)
        self.window.show()
        MainWindow.hide()

    def MainUi(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setup(self.window)
        self.window.show()
        self.ui.actionGestion.setVisible(False)
        MainWindow.hide()

    def ViewUi(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setup(self.window)
        self.window.show()
        self.ui.pushButton_1.hide()
        self.ui.pushButton_2.hide()
        self.ui.pushButton_3.hide()
        self.ui.pushButton_4.hide()
        self.ui.pushButton_5.hide()
        self.ui.pushButton_6.hide()
        self.ui.actionGestion.setVisible(False)
        MainWindow.hide()


    def testconnex(self):
        if AdminUser.get(self.login.text()) == self.password.text():
            self.AdminUi()
            self.login.clear()
            self.password.clear()
            self.login.setFocus()
        elif ModifList.get(self.login.text()) == self.password.text():
            self.MainUi()
            self.login.clear()
            self.password.clear()
            self.login.setFocus()
        elif Viewlist.get(self.login.text()) == self.password.text():
            self.ViewUi()
            self.login.clear()
            self.password.clear()
            self.login.setFocus()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Identifiants erronés")
            msg.setInformativeText('')
            msg.setWindowTitle("Erreur")
            msg.exec_()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.LoginUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
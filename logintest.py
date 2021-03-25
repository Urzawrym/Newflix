from PyQt5 import QtCore, QtGui, QtWidgets
import json
import sys


#from cryptography.fernet import Fernet

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

    def getSexe(self):
        return self.sexe

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

    """def __str__(self):
        return "Nom {}, Prénom {}, Sexe {}, Date d'embauche {}, " \
               "Code d'employé {}, Mot de passe {}, Accès {}".format(self.nom, self.prenom, self.sexe, self.dateembauche,
                                                                  self.codeutilisateur, self.password, self.acces)"""

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
        self.descriptioncat = descriptioncat



class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.gestuser = Ui_GestUser()

        self.setObjectName("MainWindow")
        self.resize(713, 554)
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(580, 40, 80, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 80, 80, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(580, 120, 80, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.ListeClient = QtWidgets.QListWidget(self.centralwidget)
        self.ListeClient.setGeometry(QtCore.QRect(20, 40, 551, 192))
        self.ListeClient.setObjectName("ListeClient")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(580, 320, 80, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(580, 360, 80, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.ListeClient_2 = QtWidgets.QListWidget(self.centralwidget)
        self.ListeClient_2.setGeometry(QtCore.QRect(20, 280, 551, 192))
        self.ListeClient_2.setObjectName("ListeClient_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(580, 280, 80, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 131, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 260, 181, 16))
        self.label_2.setObjectName("label_2")
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 713, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.setMenuBar(self.menubar)
        self.actionGestion = QtWidgets.QAction()
        self.actionGestion.setObjectName("actionGestion")
        self.actionDeconnexion = QtWidgets.QAction()
        self.actionDeconnexion.setObjectName("actionDeconnexion")
        self.actionQuitter = QtWidgets.QAction()
        self.actionQuitter.setObjectName("actionQuitter")
        self.menuMenu.addSeparator()
        self.menuMenu.addSeparator()
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionGestion)
        self.menuMenu.addAction(self.actionDeconnexion)
        self.menuMenu.addAction(self.actionQuitter)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.actionGestion.triggered.connect(self.GestUi)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Ajouter"))
        self.pushButton_2.setText(_translate("MainWindow", "Modifier"))
        self.pushButton_3.setText(_translate("MainWindow", "Supprimer"))
        self.pushButton_4.setText(_translate("MainWindow", "Modifier"))
        self.pushButton_5.setText(_translate("MainWindow", "Supprimer"))
        self.pushButton_6.setText(_translate("MainWindow", "Ajouter"))
        self.label.setText(_translate("MainWindow", "Liste des clients"))
        self.label_2.setText(_translate("MainWindow", "Liste des films"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionGestion.setText(_translate("MainWindow", "Gestion Employés"))
        self.actionDeconnexion.setText(_translate("MainWindow", "Déconnexion"))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter"))

    def GestUi(self):
        if self.gestuser.isVisible():
            self.gestuser.hide()
        else:
            self.gestuser.show()

class Ui_GestUser(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.userui = Ui_FormUser()

        self.setObjectName("Form")
        self.resize(685, 156)
        self.listWidget = QtWidgets.QListWidget(self)
        self.listWidget.setGeometry(QtCore.QRect(10, 30, 571, 111))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(590, 30, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 70, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(590, 110, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 10, 281, 16))
        self.label.setObjectName("label")
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.pushButton.clicked.connect(self.userui)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Ajouter"))
        self.pushButton_2.setText(_translate("Form", "Modifier"))
        self.pushButton_3.setText(_translate("Form", "Supprimer"))
        self.label.setText(_translate("Form", "Liste des employés"))

    def userui(self):
        if self.userui.isVisible():
            self.userui.hide()
        else:
            self.userui.show()

class Ui_FormUser(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setObjectName("Form")
        self.resize(408, 207)
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 113, 20))
        self.lineEdit.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(10, 60, 47, 13))
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 80, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(10, 110, 47, 13))
        self.label_6.setObjectName("label_6")
        self.radioButton = QtWidgets.QRadioButton(self)
        self.radioButton.setGeometry(QtCore.QRect(10, 130, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 150, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 170, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(140, 10, 91, 16))
        self.label_7.setObjectName("label_7")
        self.dateEdit = QtWidgets.QDateEdit(self)
        self.dateEdit.setGeometry(QtCore.QRect(140, 30, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(270, 10, 111, 16))
        self.label_8.setObjectName("label_8")
        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_3.setGeometry(QtCore.QRect(270, 30, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_9 = QtWidgets.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(270, 60, 111, 16))
        self.label_9.setObjectName("label_9")
        self.lineEdit_5 = QtWidgets.QLineEdit(self)
        self.lineEdit_5.setGeometry(QtCore.QRect(270, 80, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.radioButton_4 = QtWidgets.QRadioButton(self)
        self.radioButton_4.setGeometry(QtCore.QRect(140, 80, 82, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self)
        self.radioButton_5.setGeometry(QtCore.QRect(140, 100, 82, 17))
        self.radioButton_5.setObjectName("radioButton_5")
        self.label_10 = QtWidgets.QLabel(self)
        self.label_10.setGeometry(QtCore.QRect(140, 60, 71, 16))
        self.label_10.setObjectName("label_10")
        self.pushButton_10 = QtWidgets.QPushButton(self)
        self.pushButton_10.setGeometry(QtCore.QRect(110, 140, 131, 41))
        self.pushButton_10.setObjectName("pushButton")
        self.pushButton_11 = QtWidgets.QPushButton(self)
        self.pushButton_11.setGeometry(QtCore.QRect(260, 140, 131, 41))
        self.pushButton_11.setObjectName("pushButton_2")
        self.retranslateUi4()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi4(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
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

class Ui_Connexion(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setObjectName("Connexion")
        self.resize(270, 122)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(100, 80, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.login = QtWidgets.QLineEdit(self)
        self.login.setGeometry(QtCore.QRect(100, 20, 161, 20))
        self.login.setObjectName("lineEdit_3")
        self.password = QtWidgets.QLineEdit(self)
        self.password.setGeometry(QtCore.QRect(100, 50, 161, 20))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("lineEdit_4")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 20, 91, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 111, 20))
        self.label_2.setObjectName("label_2")
        self.retranslateUi()
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Connexion", "Connexion"))
        self.label.setText(_translate("Connexion", "Code employé :"))
        self.label_2.setText(_translate("Connexion", " Mot de passe :"))

    def testconnex(self):
        dlg = Ui_Connexion()
        result = dlg.exec_()
        if result:
            with open("testuser.json", "r") as f:
                dicto = json.load(f)
                logged_in = False
            while not logged_in:
                for a in (dicto):
                    if self.login.text() == "admin" and self.password.text() == "admin123":
                        self.AdminUi()
                        self.login.clear()
                        self.password.clear()
                        self.login.setFocus()
                        logged_in = True
                    elif a['codeutilisateur'] == self.login.text() and a['password'] == self.password.text() \
                            and a["acces"] == "Modification":
                        self.MainUi()
                        self.login.clear()
                        self.password.clear()
                        self.login.setFocus()
                        logged_in = True
                    elif a['codeutilisateur'] == self.login.text() and a['password'] == self.password.text() \
                            and a["acces"] == "Lecture":
                        self.ViewUi()
                        self.login.clear()
                        self.password.clear()
                        self.login.setFocus()
                        logged_in = True
                if logged_in is not True:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setText("Identifiants erronés")
                    msg.setInformativeText('')
                    msg.setWindowTitle("Erreur")
                    msg.exec_()
                    break

    def Saveuser(self):
        employee=Employe(self.lineEdit.text(),self.lineEdit_2.text(),self.comboBox.currentText(),
                         self.dateEdit.text(),self.lineEdit_3.text(),self.lineEdit_5.text(),
                         self.comboBox_2.currentText())
        dictemployee=vars(employee)
        with open("testuser.json", "r") as f:
            dic = json.load(f)
            if self.lineEdit.text() == "" or self.lineEdit_2.text() == "" or self.lineEdit_3.text() == ""\
                    or self.lineEdit_5.text() == "":
               msg = QtWidgets.QMessageBox()
               msg.setIcon(QtWidgets.QMessageBox.Warning)
               msg.setText("Veuillez compléter les informations manquantes")
               msg.setInformativeText('')
               msg.setWindowTitle("Erreur")
               msg.exec_()
            elif any(d["codeutilisateur"] == self.lineEdit_3.text() for d in dic):
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












    def CloseUi(self):
        app.closeAllWindows()

    def LogoutUi(self):
        app.closeAllWindows()








    def AdminUi(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.PrinciUi(self.window)
        self.window.show()



    def MainUi(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.PrinciUi(self.window)
        self.window.show()
        self.ui.actionGestion.setVisible(False)


    def ViewUi(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.PrinciUi(self.window)
        self.window.show()
        self.ui.pushButton_1.hide()
        self.ui.pushButton_2.hide()
        self.ui.pushButton_3.hide()
        self.ui.pushButton_4.hide()
        self.ui.pushButton_5.hide()
        self.ui.pushButton_6.hide()
        self.ui.actionGestion.setVisible(False)


    def testconnex(self):
        with open("testuser.json", "r") as f:
            dicto = json.load(f)
            logged_in = False
        while not logged_in:
            for a in (dicto):
                if self.login.text() == "admin" and self.password.text() == "admin123":
                    self.AdminUi()
                    self.login.clear()
                    self.password.clear()
                    self.login.setFocus()
                    logged_in = True
                elif a['codeutilisateur'] == self.login.text() and a['password'] == self.password.text() \
                        and a["acces"] == "Modification":
                    self.MainUi()
                    self.login.clear()
                    self.password.clear()
                    self.login.setFocus()
                    logged_in = True
                elif a['codeutilisateur'] == self.login.text() and a['password'] == self.password.text() \
                        and a["acces"] == "Lecture":
                    self.ViewUi()
                    self.login.clear()
                    self.password.clear()
                    self.login.setFocus()
                    logged_in = True
            if logged_in is not True:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Identifiants erronés")
                msg.setInformativeText('')
                msg.setWindowTitle("Erreur")
                msg.exec_()
                break




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Ui_Connexion()
    w.show()
    app.exec_()
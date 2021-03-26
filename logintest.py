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


class Ui_MainWindow(QtWidgets.QMainWindow): #Il s'agit d'aller chercher la fenêtre principale du logiciel
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



        self.actionGestion.triggered.connect(self.GestUi)



    def GestUi(self):
        if self.gestuser.isVisible():
            self.gestuser.hide()
        else:
            self.gestuser.show()

class GestUser(QtWidgets.QDialog): #Ici on va aller chercher la fenêtre de gestion des employés
    def __init__(self):
        super().__init__()
        self.ui = Ui_GestiUser()
        self.ui.setupUi(self)


        self.pushButton.clicked.connect(self.userui)


    def userui(self):
        if self.ui.isVisible():
            self.ui.hide()
        else:
            self.ui.show()

class FormUser(QtWidgets.QDialog): #Il s'agit du formulaire pour créer ou modifier un employé
    def __init__(self):
        super().__init__()
        self.ui = Ui_FormUser()
        self.ui.setupUi(self)

class Connexion(QtWidgets.QDialog): #Il s'agit de la petite fenêtre de démarrage
    def __init__(self):
        super().__init__()
        self.ui = Ui_Connexion()
        self.ui.setupUi(self)


    def testconnex(self):
        dlg = Connexion()
        result = dlg.exec_()
        if result:
            return "accepté"
        """if dlg.exec_():
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
                    break"""

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


    """def testconnex(self):
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
                break"""




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Connexion()
    w.show()
    app.exec_()
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


class AdminWindow(QtWidgets.QMainWindow): #Ouvre la fenêtre principale du logiciel
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def ShowUi(self):
        self.modifui = AdminWindow(self.ui)
        self.ui.actionGestion.setVisible(False)








    """def GestUi(self):
        if self.gestuser.isVisible():
            self.gestuser.hide()
        else:
            self.gestuser.show()"""

class ModifWindow(QtWidgets.QMainWindow): #Ouvre la fenêtre principale du logiciel mais sans le menu Gestion usager
    def __init__(self):
        super().__init__()
        self.ui = AdminWindow()
        self.ui.setupUi(self)
        self.ui.actionGestion.setVisible(False)

class ViewWindow(QtWidgets.QMainWindow): #Ouvre la fenêtre principale du logiciel mais sans le menu Gestion usager
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionGestion.setVisible(False)

class GestUser(QtWidgets.QDialog): #Ouvre la fenêtre de gestion des employés
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

class FormUser(QtWidgets.QDialog): #Ouvre le formulaire pour créer ou modifier un employé
    def __init__(self):
        super().__init__()
        self.ui = Ui_FormUser()
        self.ui.setupUi(self)

class Connexion(QtWidgets.QDialog): #Ouvre la petite fenêtre de démarrage
    def __init__(self):
        super().__init__()
        self.adminwindow = AdminWindow()
        self.adminwindow.ShowUi()
        self.modifwindow = AdminWindow()

        self.ui = Ui_Connexion()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.testconnex) #Trigger le test login avec le bouton OK


    def testconnex(self):
        with open("testuser.json", "r") as f:
            dicto = json.load(f)
            logged_in = False

        while not logged_in:
            for a in (dicto):
                if self.ui.lineEdit.text() == "admin" and self.ui.lineEdit_2.text() == "admin123":
                    self.adminwindow.show()
                    self.ui.lineEdit.clear()
                    self.ui.lineEdit_2.clear()
                    self.ui.lineEdit.setFocus()
                    self.hide()
                    logged_in = True


                elif a['codeutilisateur'] == self.ui.lineEdit.text() and a['password'] == self.ui.lineEdit_2.text() \
                        and a["acces"] == "Modification":
                    self.modifwindow.show()
                    self.ui.lineEdit.clear()
                    self.ui.lineEdit_2.clear()
                    self.ui.lineEdit.setFocus()
                    self.hide()
                    logged_in = True

                elif a['codeutilisateur'] == self.ui.lineEdit.text() and a['password'] == self.ui.lineEdit_2.text() \
                        and a["acces"] == "Lecture":
                    self.ViewUi()
                    self.ui.lineEdit.clear()
                    self.ui.lineEdit_2.clear()
                    self.ui.lineEdit.setFocus()
                    self.hide()
                    logged_in = True

            if logged_in is not True :
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Identifiants erronés")
                msg.setInformativeText('')
                msg.setWindowTitle("Erreur")
                msg.exec_()
                break

    def AdminUi(self):
        self.adminwindow.show()

    def ModifUi(self):
        self.modifwindow.show()




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








    """def AdminUi(self):
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
        self.ui.actionGestion.setVisible(False)"""


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
    w = Connexion() #Démarre le logiciel avec la petite fenêtre de connexion
    w.show()
    app.exec_()
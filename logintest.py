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


class AdminWindow(QtWidgets.QMainWindow, Ui_MainWindow): #Ouvre la fenêtre principale du logiciel
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

class GestUser(QtWidgets.QDialog, Ui_GestiUser): #Ouvre la fenêtre de gestion des employés
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)

class FormUser(QtWidgets.QDialog, Ui_FormUser): #Ouvre le formulaire pour créer ou modifier un employé
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)

class Connexion(QtWidgets.QDialog, Ui_Connexion): #Ouvre la petite fenêtre de démarrage
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)

class Controller:

    def __init__(self):
        pass

    def showlogin(self):
        self.connex = Connexion()
        self.connex.pushButton.clicked.connect(self.testconnex)
        self.connex.show()

    def adminwindow(self):
        self.admin = AdminWindow()
        self.admin.show()

    def modifwindow(self):
        self.modif = AdminWindow()
        self.modif.actionGestion.setVisible(False)
        self.modif.show()

    def viewwindow(self):
        self.view = AdminWindow()
        self.view.actionGestion.setVisible(False)
        self.view.pushButton.hide()
        self.view.pushButton_2.hide()
        self.view.pushButton_3.hide()
        self.view.pushButton_4.hide()
        self.view.pushButton_5.hide()
        self.view.pushButton_6.hide()
        self.view.show()

    def testconnex(self):
        with open("testuser.json", "r") as f:
            dicto = json.load(f)
            logged_in = False
        while not logged_in:
            for a in (dicto):
                if self.connex.lineEdit.text() == "admin" and self.connex.lineEdit_2.text() == "admin123":
                    self.adminwindow()
                    self.connex.lineEdit.clear()
                    self.connex.lineEdit_2.clear()
                    self.connex.lineEdit.setFocus()
                    self.connex.hide()
                    logged_in = True
                elif a['codeutilisateur'] == self.connex.lineEdit.text() and a['password'] == self.connex.lineEdit_2.text() \
                        and a["acces"] == "Modification":
                    self.modifwindow()
                    self.connex.lineEdit.clear()
                    self.connex.lineEdit_2.clear()
                    self.connex.lineEdit.setFocus()
                    self.connex.hide()
                    logged_in = True
                elif a['codeutilisateur'] == self.connex.lineEdit.text() and a['password'] == self.connex.lineEdit_2.text() \
                        and a["acces"] == "Lecture":
                    self.viewwindow()
                    self.connex.lineEdit.clear()
                    self.connex.lineEdit_2.clear()
                    self.connex.lineEdit.setFocus()
                    self.connex.hide()
                    logged_in = True
            if logged_in is not True:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Identifiants erronés")
                msg.setInformativeText('')
                msg.setWindowTitle("Erreur")
                msg.exec_()
                self.connex.lineEdit.setFocus()
                break

    """def AdminUi(self):
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
                break"""




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.showlogin()
    sys.exit(app.exec_())
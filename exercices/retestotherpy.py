# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from mainwindow import *
from logindialog import *

class AdminWindow(QtWidgets.QMainWindow): #Ouvre la fenêtre principale du logiciel
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.testhide()
    def testhide(self):
        self.ui.actionGestion.setVisible(False)
        #self.show()

class Connexion(QtWidgets.QDialog): #Ouvre la petite fenêtre de démarrage
    def __init__(self):
        super().__init__()
        self.ui = Ui_Connexion()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.testconnex) #Trigger le test login avec le bouton OK
        self.secondwindow = AdminWindow()
    """def addWidget(self):
        temp = AdminWindow()
        self.kod.append(temp)
        self.scrollLayout.addRow(temp)

    def remove_widget(self):
        self.kod.pop().deleteLater()"""

    def testconnex(self):
        testwindow = self.secondwindow.testhide()
        testwindow.show()

        """with open("testuser.json", "r") as f:
            dicto = json.load(f)
            logged_in = False

        while not logged_in:
            for a in (dicto):
                if self.ui.lineEdit.text() == "admin" and self.ui.lineEdit_2.text() == "admin123":
                    self.mainwindow.show()
                    #self.mainwindow.actionGestion.setVisible(True)
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
                break"""








if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w= Connexion()
    w.show()
    sys.exit(app.exec_())
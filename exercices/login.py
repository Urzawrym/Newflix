# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_Connexion(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("Connexion")
        self.resize(229, 177)
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.login = QtWidgets.QLineEdit(self.centralwidget)
        self.login.setObjectName("login")
        #self.login.returnPressed.connect(self.testconnex)
        self.gridLayout.addWidget(self.login, 0, 1, 1, 1)
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        #self.password.returnPressed.connect(self.testconnex)
        self.gridLayout.addWidget(self.password, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        #self.pushButton.clicked.connect(self.testconnex)
        self.pushButton.setAutoDefault(True)
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 2)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Connexion", "Connexion"))
        self.login.setPlaceholderText(_translate("MainWindow", "Usager"))
        self.password.setPlaceholderText(_translate("MainWindow", "Mot de passe"))
        self.pushButton.setText(_translate("MainWindow", "Connexion"))

    def open_login_dialog(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Connexion
        ui.setupUi(Dialog)
        Dialog.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Ui_Connexion()
    w.show()
    app.exec_()
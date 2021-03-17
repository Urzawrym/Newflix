from PyQt5 import QtCore, QtGui, QtWidgets

#class Personne




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
        self.actionD_connexion = QtWidgets.QAction(MainWindow)
        self.actionD_connexion.setObjectName("actionD_connexion")
        self.actionQuitter = QtWidgets.QAction(MainWindow)
        self.actionQuitter.setObjectName("actionQuitter")
        self.menuMenu.addSeparator()
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionD_connexion)
        self.menuMenu.addAction(self.actionQuitter)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.retranslateUi2(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi2(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_1.setText(_translate("MainWindow", "Ajouter"))
        self.pushButton_2.setText(_translate("MainWindow", "Modifier"))
        self.pushButton_3.setText(_translate("MainWindow", "Supprimer"))
        self.pushButton_4.setText(_translate("MainWindow", "Modifier"))
        self.pushButton_5.setText(_translate("MainWindow", "Supprimer"))
        self.pushButton_6.setText(_translate("MainWindow", "Ajouter"))
        self.label.setText(_translate("MainWindow", "Liste des clients"))
        self.label_2.setText(_translate("MainWindow", "Liste des films"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionD_connexion.setText(_translate("MainWindow", "Déconnexion"))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter"))

    def LoginUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(229, 177)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        #self.label = QtWidgets.QLabel(self.centralwidget)
        #self.label.setObjectName("label")
        #self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.login = QtWidgets.QLineEdit(self.centralwidget)
        self.login.setObjectName("login")
        self.gridLayout.addWidget(self.login, 0, 1, 1, 1)
        #self.label_2 = QtWidgets.QLabel(self.centralwidget)
        #self.label_2.setObjectName("label_2")
        #self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        #self.label.setText(_translate("MainWindow", "Usager :"))
        self.login.setPlaceholderText(_translate("MainWindow", "Usager"))
        #self.label_2.setText(_translate("MainWindow", "Mot de passe :"))
        self.password.setPlaceholderText(_translate("MainWindow", "Mot de passe"))
        self.pushButton.setText(_translate("MainWindow", "Connexion"))

    def MainUi(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setup(self.window)
        self.window.show()
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
        MainWindow.hide()


    def testconnex(self):
        if (self.login.text() == "claude" and self.password.text() == "1234") :
            self.MainUi()
        elif (self.login.text() == "mathieu" and self.password.text() == "royer"):
            self.ViewUi()


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

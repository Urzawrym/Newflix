# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(713, 554)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(580, 40, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 70, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(580, 100, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(20, 40, 551, 192))
        self.treeView.setObjectName("treeView")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(580, 280, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(580, 310, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.treeView_2 = QtWidgets.QTreeView(self.centralwidget)
        self.treeView_2.setGeometry(QtCore.QRect(20, 280, 551, 192))
        self.treeView_2.setAlternatingRowColors(True)
        self.treeView_2.setObjectName("ListeClient")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(580, 340, 75, 23))
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
        self.actionDeconnexion = QtWidgets.QAction(MainWindow)
        self.actionDeconnexion.setObjectName("actionDeconnexion")
        self.actionQuitter = QtWidgets.QAction(MainWindow)
        self.actionQuitter.setObjectName("actionQuitter")
        self.menuMenu.addSeparator()
        self.menuMenu.addSeparator()
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionGestion)
        self.menuMenu.addAction(self.actionDeconnexion)
        self.menuMenu.addAction(self.actionQuitter)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Ajouter"))
        self.pushButton_2.setText(_translate("MainWindow", "Modifier"))
        self.pushButton_3.setText(_translate("MainWindow", "Supprimer"))
        self.pushButton_4.setText(_translate("MainWindow", "Ajouter"))
        self.pushButton_5.setText(_translate("MainWindow", "Modifier"))
        self.pushButton_6.setText(_translate("MainWindow", "Supprimer"))
        self.label.setText(_translate("MainWindow", "Liste des clients"))
        self.label_2.setText(_translate("MainWindow", "Liste des films"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionGestion.setText(_translate("MainWindow", "Gestion Employés"))
        self.actionDeconnexion.setText(_translate("MainWindow", "Déconnexion"))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
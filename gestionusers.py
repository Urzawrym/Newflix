# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gestionusers.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_GestUser(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
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

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Ajouter"))
        self.pushButton_2.setText(_translate("Form", "Modifier"))
        self.pushButton_3.setText(_translate("Form", "Supprimer"))
        self.label.setText(_translate("Form", "Liste des employés"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Ui_GestUser()
    w.show()
    app.exec_()
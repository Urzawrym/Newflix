# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'popupuser.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

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

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Ui_FormUser()
    w.show()
    app.exec_()
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'popupuser.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormUser(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(408, 207)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 113, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 113, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 80, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 47, 13))
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(10, 130, 113, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(140, 10, 113, 20))
        self.label_5.setObjectName("label_5")
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(140, 30, 113, 20))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit.setMaximumDate(QtCore.QDate(7999, 12, 28))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDisplayFormat("dd-MM-yyyy")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(270, 10, 113, 20))
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(270, 30, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(270, 60, 111, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(270, 80, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(140, 80, 113, 20))
        self.comboBox_2.setObjectName("comboBox")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(140, 60, 113, 20))
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(140, 165, 113, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 165, 113, 30))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Nom :"))
        self.label_3.setText(_translate("Form", "Prénom :"))
        self.label_4.setText(_translate("Form", "Sexe :"))
        self.comboBox.setItemText(0, _translate("Form", "Masculin"))
        self.comboBox.setItemText(1, _translate("Form", "Feminin"))
        self.comboBox.setItemText(2, _translate("Form", "Non défini"))
        self.label_5.setText(_translate("Form", "Date embauche :"))
        self.label_6.setText(_translate("Form", "Code utilisateur :"))
        self.label_7.setText(_translate("Form", "Mot de passe :"))
        self.comboBox_2.setItemText(0, _translate("Form", "Lecture"))
        self.comboBox_2.setItemText(1, _translate("Form", "Modification"))
        self.comboBox_2.setItemText(2, _translate("Form", "Admin"))
        self.label_8.setText(_translate("Form", "Type accès :"))
        self.pushButton.setText(_translate("Form", "Sauvegarder"))
        self.pushButton_2.setText(_translate("Form", "Annuler"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_FormUser()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
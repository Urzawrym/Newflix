from PyQt5.QtWidgets import (QMainWindow, QDialog, QApplication,
        QLineEdit, QPushButton, QFormLayout, QMessageBox, QWidget)
#from PyQt5.QtWidgets import (QMainWindow, QDialog, QApplication,
#        QLineEdit, QPushButton, QFormLayout, QMessageBox, QWidget)

from PyQt5.QtCore import pyqtSignal

import sys

class LoginDialog(QDialog):

    loginSignal = pyqtSignal(str, str) #Create a custom signal, which you can use
                                       #to send two string arguments to a connected function.

    def __init__(self, mainWindow):
        super(LoginDialog, self).__init__()

        self.setGeometry(200,200,500,300)
        self.setWindowTitle('Login')

        self.usernameInput = QLineEdit()
        self.passwordInput = QLineEdit()
        self.loginButton = QPushButton('Login')
        self.resetButton = QPushButton('Reset')

        #*****> CONNECT BUTTON TO A FUNCTION THAT EMITS CUSTOM SIGNAL <*****
        self.loginButton.clicked.connect(self.emitLoginSignal)
        self.resetButton.clicked.connect(self.onclickReset)

        loginLayout = QFormLayout()
        loginLayout.addRow("Username", self.usernameInput)
        loginLayout.addRow("Password", self.passwordInput)
        loginLayout.addRow(self.loginButton, self.resetButton)
        self.setLayout(loginLayout)

    def emitLoginSignal(self):
        #***> EMIT CUSTOM SIGNAL <****
        self.loginSignal.emit(
            self.usernameInput.text(),
            self.passwordInput.text()
        )


    def onclickReset(self):
        pass


class MyAdminWindow(QWidget):

    def __init__(self):
        super(MyAdminWindow, self).__init__()

        self.setGeometry(200,200,500,300)
        self.setWindowTitle("MainWindow")

        self.searchbar = QLineEdit()
        self.searchbtn = QPushButton('Search')
        self.logoutbtn = QPushButton('Logout')

        self.searchbtn.clicked.connect(self.onsearch)
        self.logoutbtn.clicked.connect(self.onlogout)

        formLayout = QFormLayout()
        formLayout.addRow(self.searchbar, self.searchbtn)
        formLayout.addRow(self.logoutbtn)
        self.setLayout(formLayout)

        self.loginDialog = LoginDialog(self)
        #*****> CONNECT TO CUSTOM SIGNAL HERE: <*******
        self.loginDialog.loginSignal.connect(self.validateUser)
        self.loginDialog.exec_()

    def onsearch(self):
        pass
    def onlogout(self):
        pass


    def validateUser(self, username, password):
        if  username == 'admin' and password == 'someone':
            self.loginDialog.close()
            self.show()  #Now show the window.
        else:
            QMessageBox.warning(self, 'Error', 'incorrect cred')


app = QApplication([])
window = MyAdminWindow()
#Don't show() the window
sys.exit(app.exec_())
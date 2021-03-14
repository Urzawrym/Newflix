from PyQt5 import QtWidgets
from mainwindow import Ui_MainWindow
from viewwindow import Ui_ViewWindow

class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.textName = QtWidgets.QLineEdit(self)
        self.textName.setPlaceholderText('Usager')
        self.textName.setFocus()
        self.textPass = QtWidgets.QLineEdit(self)
        self.textPass.setPlaceholderText('Mot de passe')
        self.buttonLogin = QtWidgets.QPushButton('Connexion', self)
        self.buttonLogin.clicked.connect(self.Login)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.textName)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)

    def Login(self):
        if (self.textName.text() == 'foo' and
            self.textPass.text() == 'bar'):
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(
                self, 'Erreur', 'Usager ou mot de passe erroné')

class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = Login()

    if login.exec_() == QtWidgets.QDialog.Accepted:
        window = Window()
        window.show()
        sys.exit(app.exec_())
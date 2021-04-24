import unittest
from newflix import *
from cryptography.fernet import Fernet
from ast import literal_eval


class TestNewflix(unittest.TestCase):

    def testClasse(self):
        personneTest = Employe("Belanger", "Claude", "Masculin", "23-04-2021", "claude", "12345678", "Lecture")

        dictpersonneTest = vars(personneTest)

        dictresult = {"nom" : "Belanger", "prenom" : "Claude", "sexe" : "Masculin", "dateembauche" : "23-04-2021",
                      "codeutilisateur" : "claude", "password" : "12345678", "acces" : "Lecture"}

        self.assertEqual(dictpersonneTest, dictresult)

    def load_key(self):
        try:
            file = open('key.key', 'rb')
            self.key = file.read()
            file.close()
            self.fernet = Fernet(self.key)
        except Exception:
            pass

    # Ouvre le fichier des usagers, décrypte les données et charge le dict. d'usager dans la variable self.dictuser
    def loaduser(self):
        try:
            with open("userscrypt.json", "rb") as file:
                file_user = file.read()
                usercrypt = self.fernet.decrypt(file_user)
                self.dictuser = literal_eval(usercrypt.decode('utf8'))

        except Exception:
            pass


    # Vu que les données sont cryptées, je peux utiliser le test unitaire pour m'assurer que le mot de passe de
    # l'administrateur est bien admin123, en cas d'erreur je peux même voir quel est le mot de passe actuel
    def testuser(self):
        self.load_key()
        self.loaduser()
        motdepasseadmin = "admin124"

        for dict in self.dictuser:
            if dict["codeutilisateur"] == "admin":
                self.admin = dict

        self.assertEqual(motdepasseadmin, self.admin["password"])

    def test(self):
        login = controller.testconnex()


if __name__ == "__main__":
    unittest.main()
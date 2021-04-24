import unittest
from newflix import *

class Testtestconnex(unittest.TestCase):

    def test_testconnex(self):
        usertest = {"nom": "Administrateur", "prenom": "Admin", "sexe": "Masculin", "dateembauche": "01-01-0000",
                "codeutilisateur": "admin", "password": "admin123", "acces": "Admin"}
        control = Controller()
        control.testconnex()
        testlogin = False
        self.assertEqual(control.logged_in, testlogin)

        #control.connex.lineEdit = usertest["codeutilisateur"]
        #control.connex.lineEdit_2 = usertest["password"]


if __name__ == "__main__":
    unittest.main()
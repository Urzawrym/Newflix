import unittest
from newflix import *

class TestNewflix(unittest.TestCase):

    # Permet de s'assurer que le statut login est toujours faux avant de démarrer le logiciel
    def test_testconnex(self):
        control = Controller()
        control.testconnex()
        testlogin = False
        self.assertEqual(control.logged_in, testlogin)

    # Après avoir décripté les usagers, permet de vérifier le mot de passe de l'administrateur
    def test_loaduser(self):
        control = Controller()
        control.load_key()
        control.loaduser()

        motdepasseadmin = "admin123"
        for dict in control.dictuser:
            if dict["codeutilisateur"] == "admin":
                self.admin = dict

        self.assertEqual(motdepasseadmin, self.admin["password"])

    # Permet de s'assurer que la classe Employé héritée de la classe Personne est bien représentée
    def testClasse(self):
        personneTest = Employe("Belanger", "Claude", "Masculin", "23-04-2021", "claude", "12345678", "Lecture")
        dictpersonneTest = vars(personneTest)
        dictresult = {"nom" : "Belanger", "prenom" : "Claude", "sexe" : "Masculin", "dateembauche" : "23-04-2021",
                      "codeutilisateur" : "claude", "password" : "12345678", "acces" : "Lecture"}

        self.assertEqual(dictpersonneTest, dictresult)

if __name__ == "__main__":
    unittest.main()
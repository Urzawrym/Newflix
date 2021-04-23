import unittest
import newflix


class TestNewflix(unittest.TestCase):

    def testClasse(self):
        personneTest = newflix.Employe("Belanger", "Claude", "Masculin", "23-04-2021", "claude", "12345678", "Lecture")

        dictpersonneTest = vars(personneTest)

        dictresult = {"nom" : "Belanger", "prenom" : "Claude", "sexe" : "Masculin", "dateembauche" : "23-04-2021",
                      "codeutilisateur" : "claude", "password" : "12345678", "acces" : "Lecture"}

        self.assertEqual(dictpersonneTest, dictresult)








if __name__ == "__main__":
    unittest.main()
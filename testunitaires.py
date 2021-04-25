### Auteur: Claude Bélanger        ###
### Date : Mars et Avril 2021      ###
### Courriel: urzawrym@hotmail.com ###

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

    # Après avoir décripté les films, permet de vérifier si un film précis est bien visible
    def test_loadfilm(self):
        control = Controller()
        control.load_key()
        control.loadfilm()

        nomfilm = "Origin"
        for dict in control.dictmovie:
            if dict["nom"] == "Origin":
                self.film = dict

        self.assertEqual(self.film["nom"], nomfilm)

    # Après avoir décripté les clients, permet de vérifier si le courriel d'un client est bien visible
    def test_loadclient(self):
        control = Controller()
        control.load_key()
        control.loadclient()

        courrieclient = "cbelanger@trucmuche.ca"
        for dict in control.dictclient:
            if dict["courriel"] == "cbelanger@trucmuche.ca":
                self.client = dict

        self.assertEqual(self.client["courriel"], courrieclient)

    # Permet de s'assurer que la classe Employé héritée de la classe Personne est bien représentée
    def testEmploye(self):
        personneTest = Employe("Belanger", "Claude", "Masculin", "23-04-2021", "claude", "12345678", "Lecture")
        dictpersonneTest = vars(personneTest)
        dictresult = {"nom" : "Belanger", "prenom" : "Claude", "sexe" : "Masculin", "dateembauche" : "23-04-2021",
                      "codeutilisateur" : "claude", "password" : "12345678", "acces" : "Lecture"}

        self.assertEqual(dictpersonneTest, dictresult)

    # Permet de s'assurer que la classe Client héritée de la classe Personne est bien représentée
    def testClient(self):
        personneTest = Client(1, "Belanger", "Claude", "Masculin", "23-04-2021", "claude@trucmuche.ca", "12345678", [])
        dictpersonneTest = vars(personneTest)
        dictresult = {"identifiant" : 1, "nom" : "Belanger", "prenom" : "Claude", "sexe" : "Masculin",
                      "dateinscription" : "23-04-2021", "courriel" : "claude@trucmuche.ca", "motdepasse" : "12345678",
                      "cartes" : []}

        self.assertEqual(dictpersonneTest, dictresult)

    # Permet de s'assurer que la classe Cartecredit est bien représentée
    def testCartecredit(self):
        carteTest = CarteCredit("123456789012", "23-04-2023", "004")
        dictcarteTest = vars(carteTest)
        dictresult = {"noCarte": "123456789012", "expiration": "23-04-2023", "codecarte": "004"}

        self.assertEqual(dictcarteTest, dictresult)

    # Permet de s'assurer que la classe Acteur héritée de la classe Personne est bien représentée
    def testActeur(self):
        personneTest = Acteur("Belanger", "Claude", "Masculin", "Brian", "23-04-2021", "23-05-2021", "450000")
        dictpersonneTest = vars(personneTest)
        dictresult = {"nom" : "Belanger", "prenom" : "Claude", "sexe" : "Masculin",
                      "nompersonnage" : "Brian", "debutemploi" : "23-04-2021", "finemploi" : "23-05-2021",
                      "cachet" : "450000"}

        self.assertEqual(dictpersonneTest, dictresult)

    # Permet de s'assurer que la classe Film est bien représentée
    def testFilm(self):
        filmTest = Film("Avatar", "02:15", "Elle ava tord", [], [])
        dictfilmTest = vars(filmTest)
        dictresult = {"nom" : "Avatar", "duree" : "02:15", "descriptionfilm" : "Elle ava tord",
                      "categories" : [], "acteurs" : []}

        self.assertEqual(dictfilmTest, dictresult)

    # Permet de s'assurer que la classe Categoriefilm est bien représentée
    def testCategoriefilm(self):
        catTest = Categoriefilm("Action", "Ca bouge")
        dictcatTest = vars(catTest)
        dictresult = {"nom": "Action", "description": "Ca bouge"}

        self.assertEqual(dictcatTest, dictresult)


if __name__ == "__main__":
    unittest.main()
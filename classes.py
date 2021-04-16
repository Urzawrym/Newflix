

class Personne:
    def __init__(self, nom, prenom, sexe):
        self.nom = nom
        self.prenom = prenom
        self.sexe = sexe

    """def getPrenom(self):
        return self.prenom

    def setPrenom(self, prenom):
        if type(prenom) == str:
            self.prenom = prenom

    def getNom(self):
        return self.nom

    def setNom(self, nom):
        if type(nom) == str:
            self.nom = nom

    def getSexe(self):
        return self.sexe

    def setSexe(self, sexe):
        if type(sexe) == str:
            self.sexe = sexe"""

class Employe(Personne):
    def __init__(self, nom, prenom, sexe, dateembauche, codeutilisateur, password, acces):
        super().__init__(nom, prenom, sexe)
        self.dateembauche = dateembauche
        self.codeutilisateur = codeutilisateur
        self.password = password
        self.acces = acces

    """def __str__(self):
        return "Nom {}, Prénom {}, Sexe {}, Date d'embauche {}, " \
               "Code d'employé {}, Mot de passe {}, Accès {}".format(self.nom, self.prenom, self.sexe, self.dateembauche,
                                                                  self.codeutilisateur, self.password, self.acces)"""

class Client(Personne):
    def __init__(self, identifiant, nom, prenom, sexe, dateinscription, courriel, motdepasse, cartes):
        super().__init__(nom,prenom,sexe)
        self.identifiant = identifiant
        self.dateinscription = dateinscription
        self.courriel = courriel
        self.motdepasse = motdepasse
        self.cartes = []


class CarteCredit:
    "Carte de crédit"
    def __init__(self, noCarte, expiration, codecarte):
            self.noCarte = noCarte
            self.expiration = expiration
            self.codecarte = codecarte

class Acteur(Personne):
    def __init__(self, nom, prenom, sexe, film, nompersonnage, debutemploi, finemploi, cachet):
        super().__init__(nom, prenom, sexe)
        self.film = film
        self.nompersonnage = nompersonnage
        self.debutemploi = debutemploi
        self.finemploi = finemploi
        self.cachet = cachet

class Film:
    def __init__(self, nom, duree, descriptionfilm, categorie, acteurs):
        self.nom = nom
        self.duree = duree
        self.description = descriptionfilm
        self.categorie = []
        self.acteurs = []

class Categoriefilm:
    def __init__(self, nom, description):
        self.nom = nom
        self.description = description
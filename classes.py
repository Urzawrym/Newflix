### Auteur: Claude Bélanger        ###
### Date : Mars et Avril 2021      ###
### Courriel: urzawrym@hotmail.com ###


################## J'ai créé toutes les classes et héritages demandés dans la mise en situation      ##################
################## dans un fichier python distinct afin de les retrouver plus facilement             ##################

class Personne:
    def __init__(self, nom, prenom, sexe):
        self.nom = nom
        self.prenom = prenom
        self.sexe = sexe

class Employe(Personne):
    def __init__(self, nom, prenom, sexe, dateembauche, codeutilisateur, password, acces):
        super().__init__(nom, prenom, sexe)
        self.dateembauche = dateembauche
        self.codeutilisateur = codeutilisateur
        self.password = password
        self.acces = acces

class Client(Personne):
    def __init__(self, identifiant, nom, prenom, sexe, dateinscription, courriel, motdepasse, cartes):
        super().__init__(nom,prenom,sexe)
        self.identifiant = identifiant
        self.dateinscription = dateinscription
        self.courriel = courriel
        self.motdepasse = motdepasse
        self.cartes = []

class CarteCredit:
    def __init__(self, noCarte, expiration, codecarte):
            self.noCarte = noCarte
            self.expiration = expiration
            self.codecarte = codecarte

class Acteur(Personne):
    def __init__(self, nom, prenom, sexe, nompersonnage, debutemploi, finemploi, cachet):
        super().__init__(nom, prenom, sexe)
        self.nompersonnage = nompersonnage
        self.debutemploi = debutemploi
        self.finemploi = finemploi
        self.cachet = cachet

class Film:
    def __init__(self, nom, duree, descriptionfilm, categorie, acteurs):
        self.nom = nom
        self.duree = duree
        self.descriptionfilm = descriptionfilm
        self.categories = []
        self.acteurs = []

class Categoriefilm:
    def __init__(self, nom, description):
        self.nom = nom
        self.description = description
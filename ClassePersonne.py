class Personne:
    'Ceci fait une personne'
    def __init__(self, prenom, nom):
        self.nom = nom
        self.prenom = prenom
        self.carte = []
    def getPrenom(self):
        return self.prenom
    def setPrenom(self, prenom):
        if type(prenom) == str:
            self.prenom = prenom
    def getNom(self):
        return self._nom
    def setNom(self,nom):
        if type(nom) == str:
            self._nom = nom
    def setCredit(self,credit):
        self.carte.append(credit)
    def getListeCredit(self):
        return self.carte
    def getNbCredit(self):
        return len(self.carte)
    #def __str__(self):
        #return "Le nom est {}, le prenom est {}".format(self._nom, self._prenom)

class CarteCredit:
    "Carte de crédit"
    def __init__(self, noCarte, Expiration):
            self.noCarte = noCarte
            self.expiration = Expiration
    def __str__(self):
        return "Le numéro est {} et l'expiration est {}".format(self.noCarte,self.expiration)

class Client(Personne):
    def __init__(self, prenom, nom, dateinscription, courriel):
        #Personne.__init__(self,prenom,nom)
        super().__init__(prenom,nom)
        self.dateinscription = dateinscription
        self.courriel = courriel

    def __str__(self):
        return "Prenom {}, nom {}, di {}, courriel {}".format(self.prenom, self.nom, self.dateinscription, self.courriel)



if __name__ == "__main__":
    c1 = CarteCredit('12456', "12/6")
    p1 = Personne('Martin', 'Couture')
    client1 = Client("Martin", "Coutu", "12/6", "aa@aa.ca")
    print(client1)
    print(vars(client1))


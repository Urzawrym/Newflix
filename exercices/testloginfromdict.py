import json
#dicto= [{"nom": "Administrateur", "prenom": "Admin", "sexe": "Masculin", "dateembauche": "01/01/00", "codeutilisateur": "admin", "password": "admin123", "acces": "Admin"}, {"nom": "", "prenom": "", "sexe": "Masculin", "dateembauche": "01/01/00", "codeutilisateur": "user1", "password": "password1", "acces": "Lecture"}, {"nom": "Claude", "prenom": "Belanger", "sexe": "Masculin", "dateembauche": "18/05/83", "codeutilisateur": "claude", "password": "1234", "acces": "Lecture"}, {"nom": "Mathieu", "prenom": "Royer", "sexe": "Masculin", "dateembauche": "17/12/84", "codeutilisateur": "mathieu", "password": "royer", "acces": "Modification"}, {"nom": "Meo", "prenom": "Ouellet", "sexe": "F\u00e9minin", "dateembauche": "17/12/84", "codeutilisateur": "meo", "password": "0987", "acces": "Modification"}, {"nom": "Meo", "prenom": "Ouellet", "sexe": "Feminin", "dateembauche": "1984-05-13", "codeutilisateur": "franky", "password": "0987", "acces": "Lecture"}, {"nom": "", "prenom": "", "sexe": "Masculin", "dateembauche": "2000-01-01", "codeutilisateur": "test", "password": "1234", "acces": "Lecture"}, {"nom": "", "prenom": "", "sexe": "Masculin", "dateembauche": "2000-01-01", "codeutilisateur": "meo2", "password": "1234", "acces": "Lecture"},{"nom": "d", "prenom": "d", "sexe": "Masculin", "dateembauche": "2000-01-01", "codeutilisateur": "d", "password": "1234", "acces": "Admin"}]



login = "patate"
password = "admin123"

logged_in = False
found_username = False
with open("testuser.json", "r") as f:
    dicto = json.load(f)

while not logged_in:
    for a in (dicto):
            if a['codeutilisateur'] == login and a['password'] == password and a["acces"] == "Admin":
                print("yes admin")
                logged_in = True
            elif a['codeutilisateur'] == login and a['password'] == password and a["acces"] == "Modification":
                print("yes modif")
                logged_in = True
            elif a['codeutilisateur'] == login and a['password'] == password and a["acces"] == "Lecture":
                print("yes view")
                logged_in = True
    if logged_in is not True:
        print("Utilisateur ou mot de passe érronés")
        break






    #elif a['codeutilisateur'] == "user1" and a['password'] == "password1" and a["acces"] == "Lecture":
        #print("no")


class Personne:
    def __init__(self, nom, adresse):
        self.nom = nom
        self.adresse = adresse

    def afficher(self):
        print(f"le nom : {self.nom}, Adresse : {self.adresse}")

class Employe (Personne):
    def __init__(self, nom, adresse, cnss):
        self.cnss = cnss
        Personne.__init__(self, nom, adresse)

    def afficher(self):
        Personne.afficher(self)
        print(f"CNSS : {self.cnss}")

class Enseignant (Personne):
    def __init__(self, nom, adresse, cnops) :
        self.cnops = cnops
        Personne.__init__(self, nom, adresse)
    
    def afficher(self):
        Personne.afficher(self)
        print(f"CNOPS : {self.cnops}")

class Etudiant (Personne):
    def __init__(self, nom, adresse, cne) :
        self.cne = cne
        Personne.__init__(self, nom, adresse)

    def afficher(self):
        Personne.afficher(self)
        print(f"CNE : {self.cne}")

e1 = Employe("malak", "casa", 4585)

e1.afficher()
Personne.afficher(e1)   # à tester le polymorphisme
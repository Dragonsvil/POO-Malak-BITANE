class Etudiant :
    def __init__(self, matricule, nom, prenom, note) :
        self.matricule = matricule
        self.nom = nom
        self.prenom = prenom
        self.note = note

    def afficher(self):
        print(f"le matricule : {self.matricule}, le nom : {self.nom}, le prenom : {self.prenom}, la note : {self.note}")


e1 = Etudiant("R1344", "bitane", "malak", 20)
e2 = Etudiant("R1345", "EL HAMdi", "khawla", 20)    

somme = e1.note + e2.note
print(f"la somme est : {somme}")
print(f"la moyenne est: {somme/2}")


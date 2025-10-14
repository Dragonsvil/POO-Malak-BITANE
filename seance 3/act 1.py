class Voiture : 
    def __init__(self, code, marque, kilometrage):
        self.code = code
        self.marque = marque
        self.kilometrage = kilometrage

    def mod_kilo(self, n):
        self.kilometrage = self.kilometrage + n
        return self.kilometrage

    def afficher(self):
        print(f"le code est : {self.code}")
        print(f"la marque est : {self.marque}")
        print(f"le nouveau kilometrage est : {self.kilometrage}")

v1 = Voiture("MA001", "BMW", 15000)
v2 = Voiture("MA002", "maserati", 70000)
v3 = Voiture("MA003", "mustang", 120000)

n = int(input("entrez le nouveau kilometrage : "))

v1.mod_kilo(n)
v1.afficher()
v2.afficher()
v3.afficher()

#1
"""
a = int(input("entrez le premier nombre: "))
b = int(input("entrez le deuxieme nombre: "))
somme = a + b
produit = a * b

print("la somme est:", somme, " et le produit est:", produit)


#2
m = int(input("entrez un nombre: "))
n = int(input("entrez un deuxieme nombre: "))

m,n = n,m
print("m et n permutés sont:", m, " et", n)

#3
a = int(input("entrez a: "))
b = int(input("entrez b: "))
c = int(input("entrez c: "))

liste = [a, b, c]
grand = a
for element in liste:
    if element > grand:
        grand = element

print("le plus grand element est:", grand)

"""

#4
distance = float(input(("entrez la distance: ")))

choix = input("entrez l'unité (km ou mille) : ")
choix = choix.lower()

match choix :
    case "km" : 
        distance = distance * 0.621371
        print("la distance en mille est:", distance,"mille")

    case "mille" : 
        distance = distance / 0.621371
        print("la distance en km est:", distance,"km")
    case _ :
        print("option invalide: écrire soit 'km' soit 'mille'")



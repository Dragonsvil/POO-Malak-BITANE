#F1
""""
def bonjour (n):
    for i in range(n):
        print("bonjour")


n = int(input("entrez le nombre : "))
print(bonjour(n))           

#F2
def divisible10 (n):
    if n%10 == 0: 
        print(f"{n} est divisble par 10")
    else:
        print(f"{n} n'est pas divisible par 10")

n = int(input("entre le nombre: "))
print(divisible10(n))


#F3
def factorielle (n):
    fact = 1
    for i in range (1, n+1):
        fact *= i
    return fact

n = int(input("entrez le nombre: "))
print( factorielle(n))


#F4
def nombre_voy (mot):
    mot = chaine.lower()
    voyelle = ["a", "e", "i", "o", "u", "y"]
    i = 0
    for letter in chaine :
        if letter in voyelle:
            i = i+1
        else: continue 
    return i

chaine = input("entrez le mot: ")
print(nombre_voy(mot))

#F5
def multiplication(n):
    for i in range(1, 11):
        produit = n * i
        print(f" {n} * {i} = {produit}")
    return None

n = int(input("entrez le nombre: "))
print(multiplication(n)) 

#F6
def nombre_cara (mot):
    mot = mot.lower()
    longueur = len(mot)
    return longueur

mot = input("entrez le mot: ")
print(nombre_cara(mot))
"""


#F7 version non recursive
def fibonacci (n):
    un = 0
    bn = 1
    for i in range(n):
        temp = un
        un = bn
        bn = un + temp
        
    return un  

n = int(input("entrez le nombre : "))

print(f"la suite de fibonacci donne: {fibonacci(n)}")


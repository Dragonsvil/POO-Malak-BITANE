try:
    a = input("entrez a: ")
    nombre = int(a)
    inv = 1/nombre
    print(inv)
except ZeroDivisionError :
    print("erreur")
except  ValueError :
    print("erreur")

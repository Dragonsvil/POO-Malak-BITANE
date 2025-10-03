L3 = []
for i in range(5):
    element = int(input(f"entrez l'element {i+1}: "))
    L3.append(element)

for element in L3:
    print(element)

somme = 0
for i in L3:
    somme = somme + i
print("la somme des elements de la liste est: ", somme) 

produit = 1
for i in range (2, 5):
    produit = L3[i] * produit
print("le produit est: ", produit)

max = L3[0]
for element in L3:
    if element > max:
        max = element
print("le max est :", max)

min = L3[0]
for element in L3:
    if element < min:
        min = element
print("le min est :", min)

i = 0
for element in L3:
    if element%3 == 0:
        i = i+1
print("le nombre de multiples de 3 est :", i)

L3.reverse()
print(L3)


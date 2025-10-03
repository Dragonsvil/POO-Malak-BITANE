machine = {
    "m1" : "192.168.0.1",
    "m2" : "192.168.0.2",
    "m3" : "192.168.0.3",
    "m4" : "192.168.0.4",
    "m5" : "192.168.0.5"
}


machine2 = machine["m2"]
print("l'adresse IP de la machine 2 est: ", machine2)

longueur = len(machine)
print(f"il existe {longueur} machines répertoriées ")

machine["m6"] = "192.168.0.6"
print(machine)

del machine["m4"]
print(machine)

est_dans_dictionnaire = "m5" in machine
print("la machine est dans dictionnaire ? ",est_dans_dictionnaire)


print("\nprogramme: ")

nom = input("entrez le nom d'une machine : ")
nom = nom.lower()

est_dans_dictionnaire = nom in machine
print(f"la machine {nom} est dans dictionnaire? {est_dans_dictionnaire}")

if est_dans_dictionnaire :
    print("l'adresse IP est: ", machine[nom] )
else:
    print("la machine n'est pas repertoriée")

adresse_ip = ["192.168.0.1", "10.0.0.1", "172.16.0.1", "200.100.50.1", "169.254.0.1"]

classes = {
"192.168.0.1" : "classe C" ,
"10.0.0.1" : "classe A",
"172.16.0.1" : "classe B" ,
"200.100.50.1" :  "adresse IP publique",
"169.254.0.1" : "APIPA"
}

#qst 1
print("quelle est la 1ere adresse dans la liste: ")
print(adresse_ip[0], "\n")

#qst 2
print("quelle est la derniere adresse dans la liste: ")
print(adresse_ip[len(adresse_ip)-1], "\n")

#qst 3
print("quelle est la troisieme adresse dans la liste: ")
print(adresse_ip[2], "\n")

#qst 4
adresse_ip.append("172.31.0.1")
print(adresse_ip)

#qst 5
adresse_ip.remove("200.100.50.1")
print(adresse_ip, "\n")

#qst 6
print(f"il reste {len(adresse_ip)} adresse restante \n")

#qst 7
est_dans_liste = "192.168.0.1" in adresse_ip
print(f"Est ce que '192.168.0.1' est dans liste? {est_dans_liste}")

#qst 8
classe1 = classes["10.0.0.1"]
print("\nla classe d'adresse '10.0.0.1' est: ", classe1, "\n")

#qst 9
adresse_ip.sort()
print("liste par ordre croissant: ",adresse_ip)

#qst 10
for cle, valeur in classes.items():
    c = 0
    if valeur == "classe C":
        c += 1

if c == len(classes):
    est_dans_classesC = True
else:
    est_dans_classesC = False
    print("\ntoutes les adresses IP apparartiennet à la classe C ?", est_dans_classesC)

#qst 11
for cle, valeur in classes.items():
    c = 0
    if valeur == "adresse IP publique":
        c += 1

print("\nil existe ", c, "adresses IP publiques")

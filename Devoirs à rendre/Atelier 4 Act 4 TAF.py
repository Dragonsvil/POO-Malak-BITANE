with open ("Table_de_multiplication.txt", "w+") as file :
    for i in range (1, 10):
        file.write(f"la table de multiplication de {i} est :\n")
        for j in range(1, 11) :
            file.write(f"{i:02d} * {j:02d} = {i*j}\n")
        file.write("\n")
    file.close()
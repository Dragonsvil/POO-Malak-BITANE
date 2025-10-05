def fibonacci_recusive (n):
    if n<=0 :
        return 0
    elif n == 1:
        return 1
    
    return fibonacci_recusive(n-1) + fibonacci_recusive(n-2)
    
nombre = int(input("entrez le nombre: "))

for i in range(nombre+1):
    print(f"la suite de fibonacci donne: F({i}) = {fibonacci_recusive(i)}")

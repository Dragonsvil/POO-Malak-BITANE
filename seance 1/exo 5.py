#1
"""
max = int(input("le nombre max: "))
for i in range (max):
    for j in range (i+1):
        print(i+1, end =" ")
    print("")

#2 act 6
n = 1
for i in range (5):
    for j in range(i):
        print(n, end=" ")
        n = n+1  
    print("")

#2 autre methode
for i in range(1, 5):
    for j in range(1, i+1):
        print(int(i*(i-1)/2)+j, end=" ")
    print("")

#3 act 15
for i in range(5):
    for j in range(i):
        print(j+1, end=" ")
    print("")


#4 act 16
for i in range(5):
    for j in range(i):
        print(i, end="")
    print("")

#5 act 17
for i in range(6):
    for j in range(i):
        print(i-j, end=" ")
    print("")

#act 17 pyramide inverse
for i in range (5,0,-1):
    for j in range(i):
        print(i-j, end=" ")
    print("")

#8 act 18
for i in range(6):
    for j in range(i):
        print("*", end=" ")
    print("")
for i in range (6, 0, -1):
    for j in range(i):
        print ("*", end=" ")
    print("")

#8 act 18 deuxieme methode
n = 10;
for i in range(1, n+1):
    if (i<= n//2) :
        print("*" *i)
    elif n!=i:
        print("* "* (n-i))

"""

#9 act 19
#8 act 18 mais avec les nombres pas les *

for i in range(5,0,-1):
    for j in range(5-i):
        print(" ",end="")
    for k in range (i):
        print("*",end=" ")
    print("")
for i in range(6):
    for j in range(5-i):
        print(" ",end="")
    for k in range (i):
        print("*",end=" ")
    print("")





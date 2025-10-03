class Point:
    def __init__(self, x, y):   # methode de construction
        self.x = x
        self.y = y
    
    def afficher(self):   # methode d'affichage
        print("la valeur de x = ", self.x, "la valeur de y = ", self.y)

    def deplacer(self, dx, dy):    # methode de deplacement
        self.x = self.x + dx
        self.y = self.y + dy

a = Point(4,5)
b = Point(3,2)

a.afficher()
a.deplacer(2 , 5)
a.afficher()

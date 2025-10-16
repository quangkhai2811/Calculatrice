from tkiteasy import *



class Calculatrice():
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre1
        self.graphiqueInit()

    def add(self):
        addition = self.nombre1 + self.nombre2

        return (addition)

    def substract(self):
       soustraction = self.nombre1 - self.nombre2

        return (soustraction)

    def multiply(self):
       multplication = 1
       for _ in range (self.nombre2):
           multiplication = self.nombre1 + multiplication

        return (multiplication)

    def divide(self):
        return False test r

    def newDivided(self):
        return True if self.divide() else False





    def power(self ):
        for _ in range (self.nombre2):
            puissance = self.nombre1

        return 0

    def fibonacci(self):
        return 0

    def prime(self):
        return 0

    def exponential(self):
        return 0

    def graphiqueInit(self):
        g = ouvrirFenetre(800, 600)
        g.dessinerRectangle()


from tkiteasy import *



class Calculatrice():
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre1
        self.graphiqueInit()

    def add(self):
        return (self.nombre1 + self.nombre2) * 0.5

    def substract(self):
        return (self.nombre1 - self.nombre2)

    def multiply(self):
        return 0

    def divide(self):
        return 0

    def power(self ):
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


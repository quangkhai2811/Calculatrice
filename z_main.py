from tkiteasy import *



class Calculatrice():
    def __init__(self, nombre1, nombre2,nbr):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        self.nbr = nbr



    def add(self,a,b):
        addition = a + b
        return (addition)

    def substract(self,a,b):
       soustraction = a - b
       return (soustraction)


    def multiply(self,a,b):
        if a==0 or b==0:
            return 0
        else:
            multiplication = a
            for _ in range(1,b):
                multiplication = multiplication + a
            return (multiplication)

    def divide(self,a,b):
        if b == 0:
            raise ZeroDivisionError("erreur")

        elif a >= b:
            compteur1 = 0 # compteur1 représente le rest
            division = a
            while division >= b:
                division = division - b
                compteur1 +=1
            return compteur1, division

        elif b > a:
            compteur2 = 0
            division = self.multiply(a, 100)
            while division > 0:
                division = division - b
                compteur2 += 1
            reponse= resultat = float(f"0.{str(compteur2).rjust(2,'0')}") #comprendre le rjust
            return reponse, division   # ici division représente le reste

    def power(self,a,b):
        if b == 0:
            return 1

        else:
            puissance = a
        for _ in range(1, b):
            multiplication = 0
            for _ in range(puissance):
                multiplication += a
            puissance = multiplication
        return puissance


    def fibonacci(self):
        if self.nbr < 0:
            raise ValueError("n doit être un entier positif ou nul")
        elif self.nbr == 0:
            return 0
        elif self.nbr == 1:
            return 1

        a, b = 0, 1
        for _ in range(2, self.nbr + 1):
            a, b = b, a + b
        return b

#ATTENTION ne pas utiliser %
    def prime(self):
        if self.nbr < 2:
            return False
        for i in range(2, self.nbr):
            _, reste = self.divide(self.nbr, i)
            if reste == 0:
                return False
        return True

    def exponential(self):
        #ici on approxime e par 2,718
        n = self.nbr
        base = 2718  # 2,718 * 1000 pour gérer les millièmes
        result = 1000  # correspond à 1.000

        for _ in range(n):
            # Multiplier result par base
            result = self.multiply(result, base)
            # Ajuster l'échelle : diviser par 1000 avec divide
            quotient, _ = self.divide(result, 1000)
            result = quotient

        # Utiliser divide pour récupérer quotient et reste pour l'affichage
        quotient, reste = self.divide(result, 1000)
        reste_str = str(reste).rjust(3, '0') #ici ont affiche un décimal qui est un str
        return f"{quotient}.{reste_str}"

n=Calculatrice(1,1,2)
print(n.add(1,5))
print(n.substract(5,2))
print(n.multiply(1,2))
print(n.divide(9,4))
print(n.power(2,3))
print(n.fibonacci())
print(n.exponential())
print(n.prime())



machine = Calculatrice(1,2)
print(machine.multiply())






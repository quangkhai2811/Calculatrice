from tkinter import *

def add(a, b):
    addition = a + b
    return addition

def substract(a, b):
    soustraction = a - b
    return soustraction

def multiply(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        multiplication = a
        for _ in range(1, int(b)):
            multiplication = multiplication + a
        return multiplication

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("erreur")

    elif a >= b:
        compteur1 = 0  # quotient
        division = a
        while division >= b:
            division = division - b
            compteur1 += 1
        return compteur1, division

    elif b > a:
        compteur2 = 0
        division = multiply(a, 100)
        while division > 0:
            division = division - b
            compteur2 += 1
        reponse = float(f"0.{str(compteur2).rjust(2,'0')}")
        return reponse, division


def power(a, b):
    if b == 0:
        return 1
    else:
        puissance = a
    for _ in range(1, int(b)):
        multiplication = 0
        for _ in range(int(puissance)):
            multiplication += a
        puissance = multiplication
    return puissance


def fibonacci(n):
    if n < 0:
        raise ValueError("n doit être un entier positif ou nul")
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, int(n) + 1):
        a, b = b, a + b
    return b


def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n)):
        _, reste = divide(n, i)
        if reste == 0:
            return False
    return True


def exponential(n):
    base = 2718  # 2.718 * 1000
    result = 1000  # correspond à 1.000

    for _ in range(int(n)):
        result = multiply(result, base)
        quotient, _ = divide(result, 1000)
        result = quotient

    quotient, reste = divide(result, 1000)
    reste_str = str(reste).rjust(3, '0')
    return f"{quotient}.{reste_str}"


# Gestion des boutons Tkinter

def button_press(num):
    global equation_text
    equation_text += str(num)
    equation_label.set(equation_text)


def set_operator(op):
    global first_num, operator, equation_text
    try:
        first_num = float(equation_text)
        operator = op
        equation_text += op
        equation_label.set(equation_text)
    except ValueError:
        equation_label.set("Erreur")
        equation_text = ""


def equals():
    global equation_text, first_num, operator
    try:
        if operator not in equation_text:
            return

        second_part = equation_text.split(operator)[1]
        second_num = float(second_part)

        if operator == '+':
            result = add(first_num, second_num)
        elif operator == '-':
            result = substract(first_num, second_num)
        elif operator == '*':
            result = multiply(first_num, second_num)
        elif operator == '/':
            quotient, _ = divide(first_num, second_num)
            result = quotient
        elif operator == '^':
            result = power(first_num, second_num)
        else:
            result = "Erreur"

        equation_label.set(str(result))
        equation_text = str(result)

    except ZeroDivisionError:
        equation_label.set("Division par 0")
        equation_text = ""
    except (IndexError, ValueError):
        equation_label.set("Erreur")
        equation_text = ""


def calc_fibo():
    global equation_text
    try:
        n = int(equation_text)
        result = fibonacci(n)
        equation_label.set(str(result))
        equation_text = str(result)
    except ValueError:
        equation_label.set("Erreur")
        equation_text = ""


def calc_prime():
    global equation_text
    try:
        n = int(equation_text)
        result = prime(n)
        equation_label.set("Premier" if result else "Pas premier")
        equation_text = ""
    except ValueError:
        equation_label.set("Erreur")
        equation_text = ""


def calc_exp():
    global equation_text
    try:
        n = int(equation_text)
        result = exponential(n)
        equation_label.set(str(result))
        equation_text = str(result)
    except ValueError:
        equation_label.set("Erreur")
        equation_text = ""


def clear():
    global equation_text, first_num, operator
    equation_text = ""
    first_num = 0
    operator = ""
    equation_label.set("")


# Interface Tkinter
window = Tk()
window.title("Calculatrice sans eval() - complète")
window.geometry("430x650")
window.resizable(False, False)

equation_text = ""
first_num = 0
operator = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('Arial', 20),
              bg="white", width=22, height=2, anchor="e", relief="sunken")
label.pack(pady=10)

frame = Frame(window)
frame.pack()

# Boutons chiffres
buttons = [
    (1,0,0), (2,0,1), (3,0,2),
    (4,1,0), (5,1,1), (6,1,2),
    (7,2,0), (8,2,1), (9,2,2),
    (0,3,0)
]

for (num, r, c) in buttons:
    Button(frame, text=str(num), height=3, width=7, font=20,
           command=lambda n=num: button_press(n)).grid(row=r, column=c)

# Opérateurs
Button(frame, text="+", height=3, width=7, font=20,
       command=lambda: set_operator('+')).grid(row=0, column=3)
Button(frame, text="-", height=3, width=7, font=20,
       command=lambda: set_operator('-')).grid(row=1, column=3)
Button(frame, text="*", height=3, width=7, font=20,
       command=lambda: set_operator('*')).grid(row=2, column=3)
Button(frame, text="/", height=3, width=7, font=20,
       command=lambda: set_operator('/')).grid(row=3, column=3)
Button(frame, text="^", height=3, width=7, font=20,
       command=lambda: set_operator('^')).grid(row=3, column=2)
Button(frame, text=".", height=3, width=7, font=20,
       command=lambda: button_press('.')).grid(row=3, column=1)

# Ton bouton ÉGAL est ici
Button(frame, text="=", height=3, width=7, font=20,
       command=equals).grid(row=4, column=3, pady=5)

# Ligne supplémentaire pour Fibo / Prime / Exp
extra_frame = Frame(window)
extra_frame.pack(pady=10)

Button(extra_frame, text="Fibo", height=2, width=10, font=20,
       command=calc_fibo).grid(row=0, column=0, padx=5)
Button(extra_frame, text="Prime", height=2, width=10, font=20,
       command=calc_prime).grid(row=0, column=1, padx=5)
Button(extra_frame, text="Exp", height=2, width=10, font=20,
       command=calc_exp).grid(row=0, column=2, padx=5)

Button(window, text="Effacer", height=2, width=10, font=20,
       command=clear).pack(pady=10)

window.mainloop()

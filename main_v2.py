from tkinter import *

# --- Fonctions de calcul ---
def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b


# --- Gestion des boutons ---
def button_press(num):
    """Ajoute un chiffre ou un point à l'équation"""
    global equation_text
    equation_text += str(num)
    equation_label.set(equation_text)


def set_operator(op):
    """Stocke l'opérateur et l'affiche sans effacer le texte"""
    global first_num, operator, equation_text
    try:
        # On récupère le premier nombre et on ajoute le symbole
        first_num = float(equation_text)
        operator = op
        equation_text += op
        equation_label.set(equation_text)
    except ValueError:
        equation_label.set("Erreur")
        equation_text = ""


def equals():
    """Effectue le calcul selon l'opérateur"""
    global equation_text, first_num, operator

    try:
        # Sépare la partie après l’opérateur
        if operator not in equation_text:
            return

        second_part = equation_text.split(operator)[1]
        second_num = float(second_part)

        # Choix de l’opération
        if operator == '+':
            result = addition(first_num, second_num)
        elif operator == '-':
            result = soustraction(first_num, second_num)
        elif operator == '*':
            result = multiplication(first_num, second_num)
        elif operator == '/':
            result = division(first_num, second_num)
        else:
            result = "Erreur"

        # Affichage du résultat
        equation_label.set(str(result))
        equation_text = str(result)

    except ZeroDivisionError:
        equation_label.set("Division par 0")
        equation_text = ""
    except (IndexError, ValueError):
        equation_label.set("Erreur")
        equation_text = ""


def clear():
    """Réinitialise l'écran et les variables"""
    global equation_text, first_num, operator
    equation_text = ""
    first_num = 0
    operator = ""
    equation_label.set("")


# --- Interface Tkinter ---
window = Tk()
window.title("Calculatrice sans eval()")
window.geometry("400x500")
window.resizable(False, False)

equation_text = ""
first_num = 0
operator = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('Arial', 20),
              bg="white", width=20, height=2, anchor="e", relief="sunken")
label.pack(pady=10)

frame = Frame(window)
frame.pack()

# --- Boutons chiffres ---
buttons = [
    (1,0,0), (2,0,1), (3,0,2),
    (4,1,0), (5,1,1), (6,1,2),
    (7,2,0), (8,2,1), (9,2,2),
    (0,3,0)
]

for (num, r, c) in buttons:
    Button(frame, text=str(num), height=3, width=7, font=20,
           command=lambda n=num: button_press(n)).grid(row=r, column=c)

# --- Opérateurs ---
Button(frame, text="+", height=3, width=7, font=20,
       command=lambda: set_operator('+')).grid(row=0, column=3)

Button(frame, text="-", height=3, width=7, font=20,
       command=lambda: set_operator('-')).grid(row=1, column=3)

Button(frame, text="*", height=3, width=7, font=20,
       command=lambda: set_operator('*')).grid(row=2, column=3)

Button(frame, text="/", height=3, width=7, font=20,
       command=lambda: set_operator('/')).grid(row=3, column=3)

# --- Autres boutons ---
Button(frame, text="=", height=3, width=7, font=20,
       command=equals).grid(row=3, column=2)

Button(frame, text=".", height=3, width=7, font=20,
       command=lambda: button_press('.')).grid(row=3, column=1)

Button(window, text="Effacer", height=2, width=10, font=20,
       command=clear).pack(pady=10)

window.mainloop()

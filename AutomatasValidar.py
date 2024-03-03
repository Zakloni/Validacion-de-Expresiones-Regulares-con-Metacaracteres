import re
import tkinter as tk
from tkinter import ttk, messagebox

def Validar(ExpresionRegular, Cadena):
    patron = re.compile(ExpresionRegular)
    return bool(patron.match(Cadena))

def RevisarFrase():
    Frase = OpcionV.get()
    Cadena = Entrada.get()

    Expresiones = {
        1: r'\b[a-zA-Z]{3}\b',
        2: r'\b[1-9]\d{0,2}\b',
        3: r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Z|a-z]{2,}\b',
        4: r'\+52\d{10}\b',
        5: r'\b[a-z]{3}\b',
        6: r'\b^[aeiouAEIOU][a-zA-Z]*[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]\b',
        7: r'^[\+\-]?\d+(\.\d{1,2})?$',
        8: r'\b(http://|https://)\b',
        9: r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$',
        10: r'[a-zA-Z0-9]+$',
        11: r'[A-Z][a-z]+$',
        12: r'\b[a-zA-Z0-9]{5}\b',
        13: r'\b[a-zA-Z]{4}ing\b',
        14: r'^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$'
    }

    if Frase in Expresiones:
        if Validar(Expresiones[Frase], Cadena):
            messagebox.showinfo("Resultado de Validación", "Pertenece al lenguaje!")
        else:
            messagebox.showerror("Resultado de Validación", "No pertenece al lenguaje.)")
    else:
        messagebox.showerror("Error", "Opción invalida seleccionada.")


root = tk.Tk()
root.title("Validador de Expresiones Regulares")

OpcionV = tk.IntVar()
OpcionV.set(1)  

ExpresionesString = {
    1: "\b[a-zA-Z]{3}\b",
    2: "\b[1-9]\\d{0,2}\b",
    3: "\b[a-zA-Z0-9./%+]+@[a-zA-Z].[a-zA-Z]{3}(.[a-zA-Z]{2,3})?\b",
    4: "\b\\+52[0-9]{10}\b",
    5: "\b[a-z]{3}\b",
    6: "\b^[aeiouAEIOU].*[^aeiouAEIOU]\b",
    7: "\b-?\\d+(\\.\\d{1,2})?\b",
    8: "\b(http://|https://).+\b",
    9: "\b[0[1-9]|(1|2)(0-9)|3(0|1)][0(1-9)|1(0|1|2)][(19|20)\\d\\d]\b",
    10: "\b[a-zA-Z0-9]+\b",
    11: "\b[A-Z][a-z]+\b",
    12: "\b[a-zA-Z0-9]{5}\b",
    13: "\b[a-zA-Z]{4}ing\b",
    14: "\b([0-9A-Fa-f]{2}:){6}([0-9A-Fa-f]{2})\b"
}
Menu = ttk.Combobox(root, textvariable = OpcionV, values = list(range(1, 15)), state = "readonly", width = 50)
Menu.pack()
Menu.set("[a-zA-Z]{3}")  

tk.Label(root, text="Ingrese la cadena a validar:").pack()
Entrada = tk.Entry(root, width = 50) 
Entrada.pack()

validate_button = tk.Button(root, text="Revisar validación", command = RevisarFrase)
validate_button.pack()
validate_button.bind('<Return>', RevisarFrase)


root.mainloop()


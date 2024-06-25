# Aula 4: Implementando as funções de cálculo
import tkinter as tk

def inserir_numero(numero):
    atual = display.get()
    display.delete(0, tk.END)
    display.insert(0, atual + numero)

def calcular():
    try:
        resultado = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(resultado))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Erro")

def limpar_display():
    display.delete(0, tk.END)

def criar_janela_principal():
    root = tk.Tk()
    root.title("Calculadora")
    root.configure(bg="black")

    # Display
    global display
    display = tk.Entry(root, font=("Arial", 24), borderwidth=5, relief="sunken", justify='right', bg="gray", fg="white")
    display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

    # Botões (layout inicial sem funcionalidade)
    botoes = [
        ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
        ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
        ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
        ('0', 5, 0), ('.', 5, 2), ('=', 5, 3), ('+', 4, 3)
    ]

    for (text, row, col) in botoes:
        tk.Button(root, text=text, font=("Arial", 18), width=5, height=2).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    return root

root = criar_janela_principal()
root.mainloop()

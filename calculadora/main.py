import tkinter as tk
import math

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

def calcular_raiz():
    try:
        resultado = math.sqrt(float(display.get()))
        display.delete(0, tk.END)
        display.insert(0, str(resultado))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Erro")

def criar_janela_principal():
    root = tk.Tk()
    root.title("Calculadora")
    root.configure(bg="black")

    # Display
    global display
    display = tk.Entry(root, font=("Arial", 24), borderwidth=5, relief="sunken", justify='right', bg="gray", fg="white")
    display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

    # Botões
    botoes = [
        ('C', 1, 0, limpar_display), ('√', 1, 1, calcular_raiz), ('%', 1, 2, lambda: inserir_numero('%')), ('/', 1, 3, lambda: inserir_numero('/')),
        ('7', 2, 0, lambda: inserir_numero('7')), ('8', 2, 1, lambda: inserir_numero('8')), ('9', 2, 2, lambda: inserir_numero('9')), ('*', 2, 3, lambda: inserir_numero('*')),
        ('4', 3, 0, lambda: inserir_numero('4')), ('5', 3, 1, lambda: inserir_numero('5')), ('6', 3, 2, lambda: inserir_numero('6')), ('-', 3, 3, lambda: inserir_numero('-')),
        ('1', 4, 0, lambda: inserir_numero('1')), ('2', 4, 1, lambda: inserir_numero('2')), ('3', 4, 2, lambda: inserir_numero('3')), ('+', 4, 3, lambda: inserir_numero('+')),
        ('0', 5, 0, lambda: inserir_numero('0')), ('.', 5, 2, lambda: inserir_numero('.')), ('=', 5, 3, calcular)
    ]

    for (text, row, col, command) in botoes:
        bg_color = 'darkgray' if text.isdigit() or text == '.' else 'darkorange'
        if text == '0':
            tk.Button(root, text=text, font=("Arial", 18), width=12, height=2, bg=bg_color, fg='white', command=command).grid(row=row, column=col, columnspan=2, padx=5, pady=5, sticky="nsew")
        else:
            tk.Button(root, text=text, font=("Arial", 18), width=5, height=2, bg=bg_color, fg='white', command=command).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    # Ajuste da grade
    for i in range(6):
        root.grid_rowconfigure(i, weight=1)
    for i in range(4):
        root.grid_columnconfigure(i, weight=1)

    return root

root = criar_janela_principal()
root.mainloop()

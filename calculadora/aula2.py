# Aula 2: Criando a interface principal
import tkinter as tk

def criar_janela_principal():
    root = tk.Tk()
    root.title("Calculadora")
    root.configure(bg="black")

    # Display
    global display
    display = tk.Entry(root, font=("Arial", 24), borderwidth=5, relief="sunken", justify='right', bg="gray", fg="white")
    display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

    return root

root = criar_janela_principal()
root.mainloop()

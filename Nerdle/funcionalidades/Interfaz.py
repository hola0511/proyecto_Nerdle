import tkinter as tk
#from funcionalidades import comparar_problemas  , command=comparar_problemas
ventana = tk.Tk()
ventana.title("Nerdle")
ventana.geometry("600x400")

bienvenida = tk.Label(ventana, text = "Bienbenido a Nerdle")
bienvenida.pack()
reglas = tk.Label(ventana, text = "tienes 6 intetos para adivinar la secuencia de numeros la cual esta formada por 8 elementos")
reglas1 = tk.Label(ventana, text = "entre los cuales pueden estas incluidos numeros del '0' al '9' y operadores")
reglas2 = tk.Label(ventana, text = "tales como '+', '-', '*', '/','='")
reglas.pack()
reglas1.pack()
reglas2.pack()

intento = tk.Entry()
intento.pack()

guess = tk.Button(text="guardar intento")
guess.pack()


ventana.mainloop()

import tkinter as tk

ventana = tk.Tk()
ventana.title("Nerdle")
ventana.geometry("500x400")

bienvenida = tk.Label(ventana, text = "Bienbenido a Nerdle")
bienvenida.pack()
reglas = tk.Label(ventana, text = "tienes 6 intetos para adivinar la secuencia de numeros la cual esta formada por 8 elementos")
reglas1 = tk.Label(ventana, text = "entre los cuales pueden estas incluidos numeros del '0' al '9' y operadores")
reglas2 = tk.Label(ventana, text = "tales como '+', '-', '*', '/','='")
reglas.pack()
reglas1.pack()
reglas2.pack()



ventana.mainloop()

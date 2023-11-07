import tkinter as tk
import funcionalidades

ventana = tk.Tk()
ventana.title("Nerdle")
ventana.geometry("600x400")

bienvenida = tk.Label(ventana, text="Bienbenido a Nerdle")
bienvenida.pack()

reglas = tk.Label(ventana, text="tienes 6 intetos para adivinar la secuencia de numeros la cual esta formada por "
                                "8 elementos")
reglas1 = tk.Label(ventana, text="entre los cuales pueden estas incluidos numeros del '0' al '9' y operadores")
reglas2 = tk.Label(ventana, text="tales como '+', '-', '*', '/','='")
reglas.pack()
reglas1.pack()
reglas2.pack()

intento_pantalla = tk.Entry()
intento_pantalla.pack()

retroalimentacion = tk.Label(ventana, text="Retroalimentacion")
retroalimentacion1 = tk.Label(ventana, text=funcionalidades.Juego.comparar_problemas())
retroalimentacion.pack()
retroalimentacion1.pack()

guardar_intento = tk.Button(text="guardar intento", command=funcionalidades.Juego.comparar_problemas)
guardar_intento.pack()

intentos = tk.Label(ventana, text=funcionalidades.Juego.cantidad_intentos())
intentos.pack()

if funcionalidades.Juego.cantidad_intentos() < 0:
    mostrar_problema = tk.Label(ventana, text=funcionalidades.Problema.mostrar_problema())
    mostrar_problema.pack()

ventana.mainloop()

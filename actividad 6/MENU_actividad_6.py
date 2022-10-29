import time
import tkinter
import tkinter as tk
from tkinter import *
import subprocess


#{} []
print ("---------------------")
print (" Carlos Ortiz Serrano")
print (" Carnet 200917231")
print (" Lic. en Informatica")
print ("ACTIVIDAD No.6  ")
print ("I N C I S O -1-\n ")

#crear ventana
def accion_1():
    texto.configure(text="Ha elgido Calculo de Hipotenusa")
    subprocess.call("hipotenusa.py", shell=True)
    texto.place(x=100, y=100)
    
def accion_2():
    texto.configure(text="Ha elgido Calculo del Area")
    texto.place(x=100, y=100)
    subprocess.call("area.py", shell=True)

# creamos la ventana principal
ventana = tk.Tk()
ventana.title('Ventana principal')
ventana.geometry('400x300')

# creamos una barra de menús y la añadimos a la ventana principal
# cada ventana solo puede tener una barra de menús
barra_menus = tk.Menu(ventana)
ventana.config(menu=barra_menus)

# creamos un menú cuyo contenedor será la barra de menús
menu = tk.Menu(barra_menus, tearoff=False)

# añadimos opciones al menú indicando su nombre y acción asociado
menu.add_command(label='Calculo de Hipotenusa', command=accion_1)
menu.add_command(label='Calculo del Area', command=accion_2)

# añadimos una línea separadora y la opción de salir
menu.add_separator()
menu.add_command(label='Salir', command=ventana.destroy)

# finalmente añadimos el menú a la barra de menús
barra_menus.add_cascade(label="Menú", menu=menu)

# añadimos una etiqueta para ver el efecto de los botones del menú
texto = tk.Label(ventana, text='MENU Principal')
texto.place(x=100, y=100)

ventana.mainloop()  # ejecutamos la ventana principal

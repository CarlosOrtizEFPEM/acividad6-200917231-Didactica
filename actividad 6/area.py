import time
import tkinter
import tkinter as tk
from math import sqrt
from tkinter import *

#{} []
print ("---------------------")
print (" Carlos Ortiz Serrano")
print (" Carnet 200917231")
print (" Lic. en Informatica")
print ("ACTIVIDAD No.6  ")
print ("I N C I S O -1-\n ")

#crear ventana
ventana=tkinter.Tk()
ventana.geometry("400x500")
ventana.title("Actividad No.5")


#codigop de programa
def Area():
    base=0
    altura=0
    
    resul_area=(float(txt_base.get())*(float(txt_altura.get())/2))
    lbl_resul_area["text"]=resul_area

 
fuenteElementos = ("Arial", 18)

#" ----INICIO DE Area de RECTANGULO-------"
lbl_titulo=tkinter.Label(ventana,text="Triangulo Rectangulo -AREA-",font=("Arial",12))
lbl_titulo.grid(row=0, column=0, columnspan=4, sticky=(tkinter.W,tkinter.E))

lbl_base = tkinter.Label(ventana, text="Ingrese Base", font= fuenteElementos,fg="red")
txt_base = tkinter.Entry(ventana, font= fuenteElementos)

lbl_altura = tkinter.Label(ventana, text="Ingrese Altura", font= fuenteElementos, fg="red")
txt_altura= tkinter.Entry(ventana, font= fuenteElementos)

lbl_base.grid(row=1, column=0)
txt_base.grid(row=1, column=1, columnspan=3)

lbl_altura.grid(row=2, column=0)
txt_altura.grid(row=2, column=1, columnspan=3)

btn_Area=tkinter.Button(ventana,text="Area",font=fuenteElementos,command=Area, bg="Khaki")
btn_Area.grid(row=4, column=0, sticky=(tkinter.W, tkinter.E, ))

lbl_resul_area = tkinter.Label(ventana, text="---", font= fuenteElementos)
lbl_resul_area.grid(row=5, column=0, columnspan=4, sticky=(tkinter.W, tkinter.E))

lbl_rotulo = tkinter.Label(ventana, text="RESULTADO :", font= fuenteElementos)
lbl_rotulo.grid(row=5, column=0, columnspan=1, sticky=(tkinter.W, tkinter.E))

#insertar imagen y colocarla en x,y

img=PhotoImage(file="area.png")
fondo=Label(ventana,image=img).place(x=40,y=180)


#" ----FIN DE TRIANGULO RECTANGULO-------"

#mandara llamar a funciones
    
ventana.mainloop()


#generar pausa en ejecucion
#duracion = 2
#time.sleep(duracion)
#exit()

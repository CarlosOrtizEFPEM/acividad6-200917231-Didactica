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
def Hipotenusa():
    resul_hipotenusa=(float(txt_cateto_a.get())* float(txt_cateto_a.get()))+(float(txt_cateto_b.get())* float(txt_cateto_b.get()))
    lbl_resul_hipotenusa["text"]=resul_hipotenusa
    
  
 
fuenteElementos = ("Arial", 18)

#" ----INICIO DE TRIANGULO RECTANGULO-------"
lbl_titulo=tkinter.Label(ventana,text="Triangulo Rectangulo -HIPOTENUSA-",font=("Arial",12))
lbl_titulo.grid(row=0, column=0, columnspan=4, sticky=(tkinter.W,tkinter.E))

lbl_cateto_a = tkinter.Label(ventana, text="Cateto A", font= fuenteElementos,fg="purple")
txt_cateto_a = tkinter.Entry(ventana, font= fuenteElementos)

lbl_cateto_b = tkinter.Label(ventana, text="Cateto B", font= fuenteElementos, fg="purple")
txt_cateto_b= tkinter.Entry(ventana, font= fuenteElementos)

lbl_cateto_a.grid(row=1, column=0)
txt_cateto_a.grid(row=1, column=1, columnspan=3)

lbl_cateto_b.grid(row=2, column=0)
txt_cateto_b.grid(row=2, column=1, columnspan=3)


btn_Hipotenusa=tkinter.Button(ventana,text="Hipotenusa",font=fuenteElementos,command=Hipotenusa, bg="CadetBlue")
btn_Hipotenusa.grid(row=4, column=0, sticky=(tkinter.W, tkinter.E, ))

lbl_resul_hipotenusa = tkinter.Label(ventana, text="---", font= fuenteElementos)
lbl_resul_hipotenusa.grid(row=5, column=0, columnspan=4, sticky=(tkinter.W, tkinter.E))

lbl_rotulo = tkinter.Label(ventana, text="RESULTADO :", font= fuenteElementos)
lbl_rotulo.grid(row=5, column=0, columnspan=1, sticky=(tkinter.W, tkinter.E))

img=PhotoImage(file="triangulo.png")
fondo=Label(ventana,image=img).place(x=40,y=180)


#" ----FIN DE TRIANGULO RECTANGULO-------"




def Area():
    print ("Area de un Triangulo")
    base=0
    altura=0

    base=(float(input("Ingrese la Base: ")))
    altura=(float(input("ingrese la Altura : ")))

    area=(base*(altura/2))
    print ("El area es :",area)
    

#mandara llamar a funciones
    
ventana.mainloop()

##Hipotenusa()
##Area()




#generar pausa en ejecucion
#duracion = 2
#time.sleep(duracion)
exit()

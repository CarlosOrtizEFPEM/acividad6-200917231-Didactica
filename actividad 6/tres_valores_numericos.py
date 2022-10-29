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
ventana.geometry("450x500")
ventana.title("Actividad No.6")

#codigos de programa
"""
def Numero_mayor():
    #Indicar cual de los valores es el mayor.
    numero_1 = str(input("ingrese valor"))
    numero_2 = str(input("ingrese valor"))
    numero_3 = str(input("ingrese valor"))
            
    # Recorrer y comparar
    if numero_1 > numero_2 and numero_1 > numero_3:
        print("Mayor:", numero_1)
    if numero_2 > numero_1 and numero_2 > numero_3:
        print("Mayor:", numero_2)
    if numero_3 > numero_1 and numero_3 > numero_2:
        print("Mayor:", numero_3)
"""
   

def Numero_mayor():
    numero_1=0
    numero_2=0
    numero_3=0

#numero 1 mayor
    if (str(txt_numero_1.get())>(str(txt_numero_2.get()))):
        lbl_comparar_numero["text"]=txt_numero_1.get()
    if (str(txt_numero_1.get())>(str(txt_numero_3.get()))):
        lbl_comparar_numero["text"]=txt_numero_1.get()

#numero 2 mayor
    if (str(txt_numero_2.get())>(str(txt_numero_3.get()))):
        lbl_comparar_numero["text"]=txt_numero_2.get()
    if (str(txt_numero_2.get())>(str(txt_numero_1.get()))):
        lbl_comparar_numero["text"]=txt_numero_2.get()

#numero 3 mayor
    if (str(txt_numero_3.get())>(str(txt_numero_2.get()))):
        lbl_comparar_numero["text"]=txt_numero_3.get()
    if (str(txt_numero_3.get())>(str(txt_numero_1.get()))):
        lbl_comparar_numero["text"]=txt_numero_3.get()

def Numero_menor():
#numero 1  menor
    if (str(txt_numero_1.get())<(str(txt_numero_2.get()))):
        lbl_comparar_numero["text"]=txt_numero_1.get()
    if (str(txt_numero_1.get())<(str(txt_numero_3.get()))):
        lbl_comparar_numero["text"]=txt_numero_1.get()

#numero 2 menor
    if (str(txt_numero_2.get())<(str(txt_numero_3.get()))):
        lbl_comparar_numero["text"]=txt_numero_2.get()
    if (str(txt_numero_2.get())<(str(txt_numero_1.get()))):
        lbl_comparar_numero["text"]=txt_numero_2.get()

#numero 3 menor
    if (str(txt_numero_3.get())<(str(txt_numero_2.get()))):
        lbl_comparar_numero["text"]=txt_numero_3.get()
    if (str(txt_numero_3.get())<(str(txt_numero_1.get()))):
        lbl_comparar_numero["text"]=txt_numero_3.get()

#Promedio de los numeros
def Promedio():
    resul_promedio=(float(txt_numero_1.get())+(float(txt_numero_2.get())+(float(txt_numero_3.get()))))/2
    lbl_comparar_numero["text"]=resul_promedio

#comparar numeros par o impar
def par_impar():
    resul_promedio=((float(txt_numero_1.get())+(float(txt_numero_2.get())+(float(txt_numero_3.get()))))/2)
    if resul_promedio %2==0:
        lbl_comparar_numero["text"]=resul_par_impar
    else:
        lbl_comparar_numero["text"]=resul_par_impar
                                                 
 
fuenteElementos = ("Arial", 18)

#" ----INICIO DE asignacion -------"
lbl_titulo=tkinter.Label(ventana,text="Comparar VALORES-",font=("Arial",12))
lbl_titulo.grid(row=0, column=0, columnspan=4, sticky=(tkinter.W,tkinter.E))

lbl_numero_1 = tkinter.Label(ventana, text="Ingrese Valor 1", font= fuenteElementos,fg="red")
txt_numero_1 = tkinter.Entry(ventana, font= fuenteElementos)

lbl_numero_2 = tkinter.Label(ventana, text="Ingrese Valor 2", font= fuenteElementos, fg="red")
txt_numero_2 = tkinter.Entry(ventana, font= fuenteElementos)

lbl_numero_3 = tkinter.Label(ventana, text="Ingrese Valor 3", font= fuenteElementos, fg="red")
txt_numero_3 = tkinter.Entry(ventana, font= fuenteElementos)

#posiciones de label y text
lbl_numero_1.grid(row=1, column=0)
txt_numero_1.grid(row=1, column=1, columnspan=3)

lbl_numero_2.grid(row=2, column=0)
txt_numero_2.grid(row=2, column=1, columnspan=3)

lbl_numero_3.grid(row=3, column=0)
txt_numero_3.grid(row=3, column=1, columnspan=3)

#botones de accion
btn_Numero_mayor=tkinter.Button(ventana,text="Numero Mayor",font=fuenteElementos, command=Numero_mayor, bg="Khaki")
btn_Numero_mayor.grid(row=4, column=0, sticky=(tkinter.W, tkinter.E, ))

btn_Numero_menor=tkinter.Button(ventana,text="Numero Menor",font=fuenteElementos, command=Numero_menor, bg="Khaki")
btn_Numero_menor.grid(row=5, column=0, sticky=(tkinter.W, tkinter.E, ))

btn_promedio=tkinter.Button(ventana,text="Promedio",font=fuenteElementos, command=Promedio, bg="Khaki")
btn_promedio.grid(row=4, column=1, sticky=(tkinter.W, tkinter.E, ))

btn_par_impar=tkinter.Button(ventana,text="Par-Impar",font=fuenteElementos, command=par_impar, bg="Khaki")
btn_par_impar.grid(row=5, column=1, sticky=(tkinter.W, tkinter.E, ))
                    

lbl_comparar_numero = tkinter.Label(ventana, text=0, font= fuenteElementos)
lbl_comparar_numero.grid(row=8, column=0, columnspan=4, sticky=(tkinter.W, tkinter.E))

lbl_rotulo_general = tkinter.Label(ventana, text="Resultado es:", font= fuenteElementos)
lbl_rotulo_general.grid(row=8, column=0, columnspan=1, sticky=(tkinter.W, tkinter.E))

#insertar imagen y colocarla en x,y

#img=PhotoImage(file="area.png")
#fondo=Label(ventana,image=img).place(x=40,y=180)


#" ----FIN DE TRIANGULO RECTANGULO-------"

#mandara llamar a funciones
    
Numero_mayor()
Numero_menor()
Promedio()
par_impar()
                     
ventana.mainloop()



#generar pausa en ejecucion
#duracion = 2
#time.sleep(duracion)
#exit()

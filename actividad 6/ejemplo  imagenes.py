import tkinter
from tkinter import *
import tkinter as tk
from tkinter.ttk import *

ventana=tkinter.Tk()
img=PhotoImage(file="triangulo.png")
fondo=Label(ventana,image=img).place(x=10,y=10)





"""
ventana=tkinter.Tk()
logo = PhotoImage(file="triangulo.png")

lblMensaje= tk.Label(ventana, image=logo).pack()

#lblMensaje2= tk.Label(ventana, image=logo).pack(side="left")


##mensaje="""
##ahora colocamos texto
##juntop a una imagen
##y experimentamos como
##va a lucir juntos
"""


##lblMensaje2= tk.Label(ventana, image=logo).pack(side="right")
##lblMensaje3= tk.Label(ventana, text=mensaje).pack(side="left")

lblMensaje4=tk.Label(ventana,text=mensaje,image=logo, compound=tk.CENTER).pack()
"""

  
"""
ventana = tkinter.Tk()

Label(ventana, text = 'dale clic', font =('Verdana', 15)).pack(side = TOP, pady = 10)

photo = PhotoImage(file = "triangulo.png") 
photoimage = photo.subsample(3, 3) 
Button(ventana, text = 'Click Me !', image = photoimage,compound = LEFT).pack(side = TOP)
"""


ventana.mainloop()

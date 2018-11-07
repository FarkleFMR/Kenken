import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
import random
cont=0
seg=0
minu=0
hor=0
ganar=True
contniv=1
stop=False
f=None
cargar=False
p=None
listaf3=[]
listaf4=[]
listaf5=[]
listaf6=[]
listaf7=[]
listaf8=[]
listaf9=[]
listai3=[]
listai4=[]
listai5=[]
listai6=[]
listai7=[]
listai8=[]
listai9=[]
listad3=[]
listad4=[]
listad5=[]
listad6=[]
listad7=[]
listad8=[]
listad9=[]
canvas_width = 200
canvas_height = 200

def paint( event ):
   python_green = "#476042"
   x1, y1 = ( event.x - 1 ), ( event.y - 1 )
   x2, y2 = ( event.x + 1 ), ( event.y + 1 )
   w.create_oval( x1, y1, x2, y2, fill = python_green )

def Manual():
   os.startfile("Manual_de_usuario_kenken.pdf")
def Top_ten():
   os.startfile("Top 10.txt")
  
   

def nombre():
    root.withdraw()
    nom=tk.Tk()
    name=Label(nom,text="Name")
    name.grid(row=1,column=1,)
    e82=Entry(nom)
    e82.grid(row=1,column=4)
    def play():
        global tres
        global cuatro
        global cinco
        global seis
        global siete
        global ocho
        global nueve
        global multi
        global cont
        global seg
        global minu
        global hor
        global p
        global cargar
        global f
        global facil
        global normal
        global dificil
        global sir
        global nor
        global timer
        global sis
        global nos
        global listaf3
        global listaf4
        global listaf5
        global listaf6
        global listaf7
        global listaf8
        global listaf9
        global listai3
        global listai4
        global listai5
        global listai6
        global listai7
        global listai8
        global listai9
        global listad3
        global listad4
        global listad5
        global listad6
        global listad7
        global listad8
        global listad9
        pl=tk.Tk()
        nom.withdraw()
        if tres==True:
           e1=tk.Entry(pl,width=4)
           e2=tk.Entry(pl,width=4)
           e3=tk.Entry(pl,width=4)
           e4=tk.Entry(pl,width=4)
           e5=tk.Entry(pl,width=4)
           e6=tk.Entry(pl,width=4)
           e7=tk.Entry(pl,width=4)
           e8=tk.Entry(pl,width=4)
           e9=tk.Entry(pl,width=4)
           def cambia_color(event):
              casilla=tk.Entry(pl)
              lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9]
              for i in lista:
                 casilla.config(bg="white")
                 if casilla.focus_get():
                    if i==casilla.focus_get():
                       casilla=i
                       casilla.config(bg="lightblue")
                       break
                        
           def cambia_blanco(event):
              casilla=tk.Entry(pl)
              lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9]
              for i in lista:
                 if casilla.focus_get():
                    if i==casilla.focus_get():
                       casilla=i
                       casilla.config(bg="white")
                       break
           e1.grid(row=1,column=1)
           e1.bind("<Enter>",cambia_color)
           e2.grid(row=1,column=2)
           e2.bind("<Enter>",cambia_color)
           e3.grid(row=1,column=3)
           e3.bind("<Enter>",cambia_color)
           e4.grid(row=2,column=1)
           e4.bind("<Enter>",cambia_color)

           e5.grid(row=2,column=2)
           e6.grid(row=2,column=3)
           e7.grid(row=3,column=1)
           e8.grid(row=3,column=2)
           e9.grid(row=3,column=3)
           e5.bind("<Enter>",cambia_color)
           e6.bind("<Enter>",cambia_color)
           e7.bind("<Enter>",cambia_color)
           e8.bind("<Enter>",cambia_color)
           e9.bind("<Enter>",cambia_color)
           e1.bind("<Button-1>",cambia_blanco)
           e2.bind("<Button-1>",cambia_blanco)
           e3.bind("<Button-1>",cambia_blanco)
           e4.bind("<Button-1>",cambia_blanco)

           e5.bind("<Button-1>",cambia_blanco)
           e6.bind("<Button-1>",cambia_blanco)
           e7.bind("<Button-1>",cambia_blanco)
           e8.bind("<Button-1>",cambia_blanco)
           e9.bind("<Button-1>",cambia_blanco)
           matriz=[[e1,e2,e3],
               [e4,e5,e6],
               [e7,e8,e9]]
        elif cuatro==True:
           e1=tk.Entry(pl,width=4)
           e2=tk.Entry(pl,width=4)
           e3=tk.Entry(pl,width=4)
           e4=tk.Entry(pl,width=4)
           e5=tk.Entry(pl,width=4)
           e6=tk.Entry(pl,width=4)
           e7=tk.Entry(pl,width=4)
           e8=tk.Entry(pl,width=4)
           e9=tk.Entry(pl,width=4)
           e10=tk.Entry(pl,width=4)
           e11=tk.Entry(pl,width=4)
           e12=tk.Entry(pl,width=4)
           e13=tk.Entry(pl,width=4)
           e14=tk.Entry(pl,width=4)
           e15=tk.Entry(pl,width=4)
           e16=tk.Entry(pl,width=4)
           def cambia_color(event):
              casilla=tk.Entry(pl)
              lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16]
              for i in lista:
                 casilla.config(bg="white")
                 if casilla.focus_get():
                    if i==casilla.focus_get():
                       casilla=i
                       casilla.config(bg="lightblue")
                       break
                        
           def cambia_blanco(event):
              casilla=tk.Entry(pl)
              lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16]
              for i in lista:
                 if casilla.focus_get():
                    if i==casilla.focus_get():
                       casilla=i
                       casilla.config(bg="white")
                       break
           e1.grid(row=1,column=1)
           e1.bind("<Enter>",cambia_color)
           e2.grid(row=1,column=2)
           e2.bind("<Enter>",cambia_color)
           e3.grid(row=1,column=3)
           e3.bind("<Enter>",cambia_color)
           e4.grid(row=1,column=4)
           e4.bind("<Enter>",cambia_color)

           e5.grid(row=2,column=1)
           e6.grid(row=2,column=2)
           e7.grid(row=2,column=3)
           e8.grid(row=2,column=4)
           e9.grid(row=3,column=1)
           e10.grid(row=3,column=2)
           e11.grid(row=3,column=3)
           e12.grid(row=3,column=4)
           e13.grid(row=4,column=1)
           e14.grid(row=4,column=2)
           e15.grid(row=4,column=3)
           e16.grid(row=4,column=4)
           e5.bind("<Enter>",cambia_color)
           e6.bind("<Enter>",cambia_color)
           e7.bind("<Enter>",cambia_color)
           e8.bind("<Enter>",cambia_color)
           e9.bind("<Enter>",cambia_color)
           e10.bind("<Enter>",cambia_color)
           e11.bind("<Enter>",cambia_color)
           e12.bind("<Enter>",cambia_color)
           e13.bind("<Enter>",cambia_color)
           e14.bind("<Enter>",cambia_color)
           e15.bind("<Enter>",cambia_color)
           e16.bind("<Enter>",cambia_color)
           e1.bind("<Button-1>",cambia_blanco)
           e2.bind("<Button-1>",cambia_blanco)
           e3.bind("<Button-1>",cambia_blanco)
           e4.bind("<Button-1>",cambia_blanco)

           e5.bind("<Button-1>",cambia_blanco)
           e6.bind("<Button-1>",cambia_blanco)
           e7.bind("<Button-1>",cambia_blanco)
           e8.bind("<Button-1>",cambia_blanco)
           e9.bind("<Button-1>",cambia_blanco)
           e10.bind("<Button-1>",cambia_blanco)
           e11.bind("<Button-1>",cambia_blanco)
           e12.bind("<Button-1>",cambia_blanco)
           e13.bind("<Button-1>",cambia_blanco)
           e14.bind("<Button-1>",cambia_blanco)
           e15.bind("<Button-1>",cambia_blanco)
           e16.bind("<Button-1>",cambia_blanco)
           matriz=[[e1,e2,e3,e4],
               [e5,e6,e7,e8],
               [e9,e10,e11,e12],
               [e13,e14,e15,e16]]
        elif cinco==True:
           e1=tk.Entry(pl,width=4)
           e2=tk.Entry(pl,width=4)
           e3=tk.Entry(pl,width=4)
           e4=tk.Entry(pl,width=4)
           e5=tk.Entry(pl,width=4)
           e6=tk.Entry(pl,width=4)
           e7=tk.Entry(pl,width=4)
           e8=tk.Entry(pl,width=4)
           e9=tk.Entry(pl,width=4)
           e10=tk.Entry(pl,width=4)
           e11=tk.Entry(pl,width=4)
           e12=tk.Entry(pl,width=4)
           e13=tk.Entry(pl,width=4)
           e14=tk.Entry(pl,width=4)
           e15=tk.Entry(pl,width=4)
           e16=tk.Entry(pl,width=4)
           e17=tk.Entry(pl,width=4)
           e18=tk.Entry(pl,width=4)
           e19=tk.Entry(pl,width=4)
           e20=tk.Entry(pl,width=4)
           e21=tk.Entry(pl,width=4)
           e22=tk.Entry(pl,width=4)
           e23=tk.Entry(pl,width=4)
           e24=tk.Entry(pl,width=4)
           e25=tk.Entry(pl,width=4)
           def cambia_color(event):
              casilla=tk.Entry(pl)
              lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25]
              for i in lista:
                 casilla.config(bg="white")
                 if casilla.focus_get():
                    if i==casilla.focus_get():
                       casilla=i
                       casilla.config(bg="lightblue")
                       break
                        
           def cambia_blanco(event):
              casilla=tk.Entry(pl)
              lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25]
              for i in lista:
                 if casilla.focus_get():
                    if i==casilla.focus_get():
                       casilla=i
                       casilla.config(bg="white")
                       break
           e1.grid(row=1,column=1)
           e1.bind("<Enter>",cambia_color)
           e2.grid(row=1,column=2)
           e2.bind("<Enter>",cambia_color)
           e3.grid(row=1,column=3)
           e3.bind("<Enter>",cambia_color)
           e4.grid(row=1,column=4)
           e4.bind("<Enter>",cambia_color)

           e5.grid(row=1,column=5)
           e6.grid(row=2,column=1)
           e7.grid(row=2,column=2)
           e8.grid(row=2,column=3)
           e9.grid(row=2,column=4)
           e10.grid(row=2,column=5)
           e11.grid(row=3,column=1)
           e12.grid(row=3,column=2)
           e13.grid(row=3,column=3)
           e14.grid(row=3,column=4)
           e15.grid(row=3,column=5)
           e16.grid(row=4,column=1)
           e17.grid(row=4,column=2)
           e18.grid(row=4,column=3)
           e19.grid(row=4,column=4)
           e20.grid(row=4,column=5)
           e21.grid(row=5,column=1)
           e22.grid(row=5,column=2)
           e23.grid(row=5,column=3)
           e24.grid(row=5,column=4)
           e25.grid(row=5,column=5)
           e5.bind("<Enter>",cambia_color)
           e6.bind("<Enter>",cambia_color)
           e7.bind("<Enter>",cambia_color)
           e8.bind("<Enter>",cambia_color)
           e9.bind("<Enter>",cambia_color)
           e10.bind("<Enter>",cambia_color)
           e11.bind("<Enter>",cambia_color)
           e12.bind("<Enter>",cambia_color)
           e13.bind("<Enter>",cambia_color)
           e14.bind("<Enter>",cambia_color)
           e15.bind("<Enter>",cambia_color)
           e16.bind("<Enter>",cambia_color)
           e17.bind("<Enter>",cambia_color)
           e18.bind("<Enter>",cambia_color)
           e19.bind("<Enter>",cambia_color)
           e20.bind("<Enter>",cambia_color)
           e21.bind("<Enter>",cambia_color)
           e22.bind("<Enter>",cambia_color)
           e23.bind("<Enter>",cambia_color)
           e24.bind("<Enter>",cambia_color)
           e25.bind("<Enter>",cambia_color)
           e1.bind("<Button-1>",cambia_blanco)
           e2.bind("<Button-1>",cambia_blanco)
           e3.bind("<Button-1>",cambia_blanco)
           e4.bind("<Button-1>",cambia_blanco)

           e5.bind("<Button-1>",cambia_blanco)
           e6.bind("<Button-1>",cambia_blanco)
           e7.bind("<Button-1>",cambia_blanco)
           e8.bind("<Button-1>",cambia_blanco)
           e9.bind("<Button-1>",cambia_blanco)
           e10.bind("<Button-1>",cambia_blanco)
           e11.bind("<Button-1>",cambia_blanco)
           e12.bind("<Button-1>",cambia_blanco)
           e13.bind("<Button-1>",cambia_blanco)
           e14.bind("<Button-1>",cambia_blanco)
           e15.bind("<Button-1>",cambia_blanco)
           e16.bind("<Button-1>",cambia_blanco)
           e17.bind("<Button-1>",cambia_blanco)
           e18.bind("<Button-1>",cambia_blanco)
           e19.bind("<Button-1>",cambia_blanco)
           e20.bind("<Button-1>",cambia_blanco)
           e21.bind("<Button-1>",cambia_blanco)
           e22.bind("<Button-1>",cambia_blanco)
           e23.bind("<Button-1>",cambia_blanco)
           e24.bind("<Button-1>",cambia_blanco)
           e25.bind("<Button-1>",cambia_blanco)
           matriz=[[e1,e2,e3,e4,e5],
               [e6,e7,e8,e9,e10],
               [e11,e12,e13,e14,e15],
               [e16,e17,e18,e19,e20],
               [e21,e22,e23,e24,e25]]
        elif seis==True:
        
           e1=tk.Entry(pl,width=4)
           e2=tk.Entry(pl,width=4)
           e3=tk.Entry(pl,width=4)
           e4=tk.Entry(pl,width=4)
           e5=tk.Entry(pl,width=4)
           e6=tk.Entry(pl,width=4)
           e7=tk.Entry(pl,width=4)
           e8=tk.Entry(pl,width=4)
           e9=tk.Entry(pl,width=4)
           e10=tk.Entry(pl,width=4)
           e11=tk.Entry(pl,width=4)
           e12=tk.Entry(pl,width=4)
           e13=tk.Entry(pl,width=4)
           e14=tk.Entry(pl,width=4)
           e15=tk.Entry(pl,width=4)
           e16=tk.Entry(pl,width=4)
           e17=tk.Entry(pl,width=4)
           e18=tk.Entry(pl,width=4)
           e19=tk.Entry(pl,width=4)
           e20=tk.Entry(pl,width=4)
           e21=tk.Entry(pl,width=4)
           e22=tk.Entry(pl,width=4)
           e23=tk.Entry(pl,width=4)
           e24=tk.Entry(pl,width=4)
           e25=tk.Entry(pl,width=4)
           e26=tk.Entry(pl,width=4)
           e27=tk.Entry(pl,width=4)
           e28=tk.Entry(pl,width=4)
           e29=tk.Entry(pl,width=4)
           e30=tk.Entry(pl,width=4)
           e31=tk.Entry(pl,width=4)
           e32=tk.Entry(pl,width=4)
           e33=tk.Entry(pl,width=4)
           e34=tk.Entry(pl,width=4)
           e35=tk.Entry(pl,width=4)
           e36=tk.Entry(pl,width=4)
           def cambia_color(event):
              casilla=tk.Entry(pl)
              lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36]
              for i in lista:
                 casilla.config(bg="white")
                 if casilla.focus_get():
                    if i==casilla.focus_get():
                       casilla=i
                       casilla.config(bg="lightblue")
                       break
                        
           def cambia_blanco(event):
              casilla=tk.Entry(pl)
              lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36]
              for i in lista:
                 if casilla.focus_get():
                    if i==casilla.focus_get():
                       casilla=i
                       casilla.config(bg="white")
                       break
           e1.grid(row=1,column=1)
           e1.bind("<Enter>",cambia_color)
           e2.grid(row=1,column=2)
           e2.bind("<Enter>",cambia_color)
           e3.grid(row=1,column=3)
           e3.bind("<Enter>",cambia_color)
           e4.grid(row=1,column=4)
           e4.bind("<Enter>",cambia_color)

           e5.grid(row=1,column=5)
           e6.grid(row=1,column=6)
           e7.grid(row=2,column=1)
           e8.grid(row=2,column=2)
           e9.grid(row=2,column=3)
           e10.grid(row=2,column=4)
           e11.grid(row=2,column=5)
           e12.grid(row=2,column=6)
           e13.grid(row=3,column=1)
           e14.grid(row=3,column=2)
           e15.grid(row=3,column=3)
           e16.grid(row=3,column=4)
           e17.grid(row=3,column=5)
           e18.grid(row=3,column=6)
           e19.grid(row=4,column=1)
           e20.grid(row=4,column=2)
           e21.grid(row=4,column=3)
           e22.grid(row=4,column=4)
           e23.grid(row=4,column=5)
           e24.grid(row=4,column=6)
           e25.grid(row=5,column=1)
           e26.grid(row=5,column=2)
           e27.grid(row=5,column=3)
           e28.grid(row=5,column=4)
           e29.grid(row=5,column=5)
           e30.grid(row=5,column=6)
           e31.grid(row=6,column=1)
           e32.grid(row=6,column=2)
           e33.grid(row=6,column=3)
           e34.grid(row=6,column=4)
           e35.grid(row=6,column=5)
           e36.grid(row=6,column=6)
           e5.bind("<Enter>",cambia_color)
           e6.bind("<Enter>",cambia_color)
           e7.bind("<Enter>",cambia_color)
           e8.bind("<Enter>",cambia_color)
           e9.bind("<Enter>",cambia_color)
           e10.bind("<Enter>",cambia_color)
           e11.bind("<Enter>",cambia_color)
           e12.bind("<Enter>",cambia_color)
           e13.bind("<Enter>",cambia_color)
           e14.bind("<Enter>",cambia_color)
           e15.bind("<Enter>",cambia_color)
           e16.bind("<Enter>",cambia_color)
           e17.bind("<Enter>",cambia_color)
           e18.bind("<Enter>",cambia_color)
           e19.bind("<Enter>",cambia_color)
           e20.bind("<Enter>",cambia_color)
           e21.bind("<Enter>",cambia_color)
           e22.bind("<Enter>",cambia_color)
           e23.bind("<Enter>",cambia_color)
           e24.bind("<Enter>",cambia_color)
           e25.bind("<Enter>",cambia_color)
           e26.bind("<Enter>",cambia_color)
           e27.bind("<Enter>",cambia_color)
           e28.bind("<Enter>",cambia_color)
           e29.bind("<Enter>",cambia_color)
           e30.bind("<Enter>",cambia_color)
           e31.bind("<Enter>",cambia_color)
           e32.bind("<Enter>",cambia_color)
           e33.bind("<Enter>",cambia_color)
           e34.bind("<Enter>",cambia_color)
           e35.bind("<Enter>",cambia_color)
           e36.bind("<Enter>",cambia_color)
           e1.bind("<Button-1>",cambia_blanco)
           e2.bind("<Button-1>",cambia_blanco)
           e3.bind("<Button-1>",cambia_blanco)
           e4.bind("<Button-1>",cambia_blanco)

           e5.bind("<Button-1>",cambia_blanco)
           e6.bind("<Button-1>",cambia_blanco)
           e7.bind("<Button-1>",cambia_blanco)
           e8.bind("<Button-1>",cambia_blanco)
           e9.bind("<Button-1>",cambia_blanco)
           e10.bind("<Button-1>",cambia_blanco)
           e11.bind("<Button-1>",cambia_blanco)
           e12.bind("<Button-1>",cambia_blanco)
           e13.bind("<Button-1>",cambia_blanco)
           e14.bind("<Button-1>",cambia_blanco)
           e15.bind("<Button-1>",cambia_blanco)
           e16.bind("<Button-1>",cambia_blanco)
           e17.bind("<Button-1>",cambia_blanco)
           e18.bind("<Button-1>",cambia_blanco)
           e19.bind("<Button-1>",cambia_blanco)
           e20.bind("<Button-1>",cambia_blanco)
           e21.bind("<Button-1>",cambia_blanco)
           e22.bind("<Button-1>",cambia_blanco)
           e23.bind("<Button-1>",cambia_blanco)
           e24.bind("<Button-1>",cambia_blanco)
           e25.bind("<Button-1>",cambia_blanco)
           e26.bind("<Button-1>",cambia_blanco)
           e27.bind("<Button-1>",cambia_blanco)
           e28.bind("<Button-1>",cambia_blanco)
           e29.bind("<Button-1>",cambia_blanco)
           e30.bind("<Button-1>",cambia_blanco)
           e31.bind("<Button-1>",cambia_blanco)
           e32.bind("<Button-1>",cambia_blanco)
           e33.bind("<Button-1>",cambia_blanco)
           e34.bind("<Button-1>",cambia_blanco)
           e35.bind("<Button-1>",cambia_blanco)
           e36.bind("<Button-1>",cambia_blanco)
           matriz=[[e1,e2,e3,e4,e5,e6],
               [e7,e8,e9,e10,e11,e12],
               [e13,e14,e15,e16,e17,e18],
               [e19,e20,e21,e22,e23,e24],
               [e25,e26,e27,e28,e29,e30],
               [e31,e32,e33,e34,e35,e36]]
        elif siete==True:
           e1=tk.Entry(pl,width=4)
           e2=tk.Entry(pl,width=4)
           e3=tk.Entry(pl,width=4)
           e4=tk.Entry(pl,width=4)
           e5=tk.Entry(pl,width=4)
           e6=tk.Entry(pl,width=4)
           e7=tk.Entry(pl,width=4)
           e8=tk.Entry(pl,width=4)
           e9=tk.Entry(pl,width=4)
           e10=tk.Entry(pl,width=4)
           e11=tk.Entry(pl,width=4)
           e12=tk.Entry(pl,width=4)
           e13=tk.Entry(pl,width=4)
           e14=tk.Entry(pl,width=4)
           e15=tk.Entry(pl,width=4)
           e16=tk.Entry(pl,width=4)
           e17=tk.Entry(pl,width=4)
           e18=tk.Entry(pl,width=4)
           e19=tk.Entry(pl,width=4)
           e20=tk.Entry(pl,width=4)
           e21=tk.Entry(pl,width=4)
           e22=tk.Entry(pl,width=4)
           e23=tk.Entry(pl,width=4)
           e24=tk.Entry(pl,width=4)
           e25=tk.Entry(pl,width=4)
           e26=tk.Entry(pl,width=4)
           e27=tk.Entry(pl,width=4)
           e28=tk.Entry(pl,width=4)
           e29=tk.Entry(pl,width=4)
           e30=tk.Entry(pl,width=4)
           e31=tk.Entry(pl,width=4)
           e32=tk.Entry(pl,width=4)
           e33=tk.Entry(pl,width=4)
           e34=tk.Entry(pl,width=4)
           e35=tk.Entry(pl,width=4)
           e36=tk.Entry(pl,width=4)
           e37=tk.Entry(pl,width=4)
           e38=tk.Entry(pl,width=4)
           e39=tk.Entry(pl,width=4)
           e40=tk.Entry(pl,width=4)
           e41=tk.Entry(pl,width=4)
           e42=tk.Entry(pl,width=4)
           e43=tk.Entry(pl,width=4)
           e44=tk.Entry(pl,width=4)
           e45=tk.Entry(pl,width=4)
           e46=tk.Entry(pl,width=4)
           e47=tk.Entry(pl,width=4)
           e48=tk.Entry(pl,width=4)
           e49=tk.Entry(pl,width=4)
           def cambia_color(event):
              casilla=tk.Entry(pl)
              lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49]
              for i in lista:
                 casilla.config(bg="white")
                 if casilla.focus_get():
                    if i==casilla.focus_get():
                       casilla=i
                       casilla.config(bg="lightblue")
                       break
                        
           def cambia_blanco(event):
              casilla=tk.Entry(pl)
              lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49]
              for i in lista:
                 if casilla.focus_get():
                    if i==casilla.focus_get():
                       casilla=i
                       casilla.config(bg="white")
                       break
           e1.grid(row=1,column=1)
           e1.bind("<Enter>",cambia_color)
           e2.grid(row=1,column=2)
           e2.bind("<Enter>",cambia_color)
           e3.grid(row=1,column=3)
           e3.bind("<Enter>",cambia_color)
           e4.grid(row=1,column=4)
           e4.bind("<Enter>",cambia_color)

           e5.grid(row=1,column=5)
           e6.grid(row=1,column=6)
           e7.grid(row=1,column=7)
           e8.grid(row=2,column=1)
           e9.grid(row=2,column=2)
           e10.grid(row=2,column=3)
           e11.grid(row=2,column=4)
           e12.grid(row=2,column=5)
           e13.grid(row=2,column=6)
           e14.grid(row=2,column=7)
           e15.grid(row=3,column=1)
           e16.grid(row=3,column=2)
           e17.grid(row=3,column=3)
           e18.grid(row=3,column=4)
           e19.grid(row=3,column=5)
           e20.grid(row=3,column=6)
           e21.grid(row=3,column=7)
           e22.grid(row=4,column=1)
           e23.grid(row=4,column=2)
           e24.grid(row=4,column=3)
           e25.grid(row=4,column=4)
           e26.grid(row=4,column=5)
           e27.grid(row=4,column=6)
           e28.grid(row=4,column=7)
           e29.grid(row=5,column=1)
           e30.grid(row=5,column=2)
           e31.grid(row=5,column=3)
           e32.grid(row=5,column=4)
           e33.grid(row=5,column=5)
           e34.grid(row=5,column=6)
           e35.grid(row=5,column=7)
           e36.grid(row=6,column=1)
           e37.grid(row=6,column=2)
           e38.grid(row=6,column=3)
           e39.grid(row=6,column=4)
           e40.grid(row=6,column=5)
           e41.grid(row=6,column=6)
           e42.grid(row=6,column=7)
           e43.grid(row=7,column=1)
           e44.grid(row=7,column=2)
           e45.grid(row=7,column=3)
           e46.grid(row=7,column=4)
           e47.grid(row=7,column=5)
           e48.grid(row=7,column=6)
           e49.grid(row=7,column=7)
           e5.bind("<Enter>",cambia_color)
           e6.bind("<Enter>",cambia_color)
           e7.bind("<Enter>",cambia_color)
           e8.bind("<Enter>",cambia_color)
           e9.bind("<Enter>",cambia_color)
           e10.bind("<Enter>",cambia_color)
           e11.bind("<Enter>",cambia_color)
           e12.bind("<Enter>",cambia_color)
           e13.bind("<Enter>",cambia_color)
           e14.bind("<Enter>",cambia_color)
           e15.bind("<Enter>",cambia_color)
           e16.bind("<Enter>",cambia_color)
           e17.bind("<Enter>",cambia_color)
           e18.bind("<Enter>",cambia_color)
           e19.bind("<Enter>",cambia_color)
           e20.bind("<Enter>",cambia_color)
           e21.bind("<Enter>",cambia_color)
           e22.bind("<Enter>",cambia_color)
           e23.bind("<Enter>",cambia_color)
           e24.bind("<Enter>",cambia_color)
           e25.bind("<Enter>",cambia_color)
           e26.bind("<Enter>",cambia_color)
           e27.bind("<Enter>",cambia_color)
           e28.bind("<Enter>",cambia_color)
           e29.bind("<Enter>",cambia_color)
           e30.bind("<Enter>",cambia_color)
           e31.bind("<Enter>",cambia_color)
           e32.bind("<Enter>",cambia_color)
           e33.bind("<Enter>",cambia_color)
           e34.bind("<Enter>",cambia_color)
           e35.bind("<Enter>",cambia_color)
           e36.bind("<Enter>",cambia_color)
           e37.bind("<Enter>",cambia_color)
           e38.bind("<Enter>",cambia_color)
           e39.bind("<Enter>",cambia_color)
           e40.bind("<Enter>",cambia_color)
           e41.bind("<Enter>",cambia_color)
           e42.bind("<Enter>",cambia_color)
           e43.bind("<Enter>",cambia_color)
           e44.bind("<Enter>",cambia_color)
           e45.bind("<Enter>",cambia_color)
           e46.bind("<Enter>",cambia_color)
           e47.bind("<Enter>",cambia_color)
           e48.bind("<Enter>",cambia_color)
           e49.bind("<Enter>",cambia_color)
           e1.bind("<Button-1>",cambia_blanco)
           e2.bind("<Button-1>",cambia_blanco)
           e3.bind("<Button-1>",cambia_blanco)
           e4.bind("<Button-1>",cambia_blanco)
           e5.bind("<Button-1>",cambia_blanco)
           e6.bind("<Button-1>",cambia_blanco)
           e7.bind("<Button-1>",cambia_blanco)
           e8.bind("<Button-1>",cambia_blanco)
           e9.bind("<Button-1>",cambia_blanco)
           e10.bind("<Button-1>",cambia_blanco)
           e11.bind("<Button-1>",cambia_blanco)
           e12.bind("<Button-1>",cambia_blanco)
           e13.bind("<Button-1>",cambia_blanco)
           e14.bind("<Button-1>",cambia_blanco)
           e15.bind("<Button-1>",cambia_blanco)
           e16.bind("<Button-1>",cambia_blanco)
           e17.bind("<Button-1>",cambia_blanco)
           e18.bind("<Button-1>",cambia_blanco)
           e19.bind("<Button-1>",cambia_blanco)
           e20.bind("<Button-1>",cambia_blanco)
           e21.bind("<Button-1>",cambia_blanco)
           e22.bind("<Button-1>",cambia_blanco)
           e23.bind("<Button-1>",cambia_blanco)
           e24.bind("<Button-1>",cambia_blanco)
           e25.bind("<Button-1>",cambia_blanco)
           e26.bind("<Button-1>",cambia_blanco)
           e27.bind("<Button-1>",cambia_blanco)
           e28.bind("<Button-1>",cambia_blanco)
           e29.bind("<Button-1>",cambia_blanco)
           e30.bind("<Button-1>",cambia_blanco)
           e31.bind("<Button-1>",cambia_blanco)
           e32.bind("<Button-1>",cambia_blanco)
           e33.bind("<Button-1>",cambia_blanco)
           e34.bind("<Button-1>",cambia_blanco)
           e35.bind("<Button-1>",cambia_blanco)
           e36.bind("<Button-1>",cambia_blanco)
           e37.bind("<Button-1>",cambia_blanco)
           e38.bind("<Button-1>",cambia_blanco)
           e39.bind("<Button-1>",cambia_blanco)
           e40.bind("<Button-1>",cambia_blanco)
           e41.bind("<Button-1>",cambia_blanco)
           e42.bind("<Button-1>",cambia_blanco)
           e43.bind("<Button-1>",cambia_blanco)
           e44.bind("<Button-1>",cambia_blanco)
           e45.bind("<Button-1>",cambia_blanco)
           e46.bind("<Button-1>",cambia_blanco)
           e47.bind("<Button-1>",cambia_blanco)
           e48.bind("<Button-1>",cambia_blanco)
           e49.bind("<Button-1>",cambia_blanco)
           matriz=[[e1,e2,e3,e4,e5,e6,e7],
               [e8,e9,e10,e11,e12,e13,e14],
               [e15,e16,e17,e18,e19,e20,e21],
               [e22,e23,e24,e25,e26,e26,e28],
               [e29,e30,e31,e32,e33,e34,e35],
               [e36,e37,e38,e39,e40,e41,e42],
               [e43,e44,e45,e46,e47,e48,e49]]
        elif ocho==True:
           e1=tk.Entry(pl,width=4)
           e2=tk.Entry(pl,width=4)
           e3=tk.Entry(pl,width=4)
           e4=tk.Entry(pl,width=4)
           e5=tk.Entry(pl,width=4)
           e6=tk.Entry(pl,width=4)
           e7=tk.Entry(pl,width=4)
           e8=tk.Entry(pl,width=4)
           e9=tk.Entry(pl,width=4)
           e10=tk.Entry(pl,width=4)
           e11=tk.Entry(pl,width=4)
           e12=tk.Entry(pl,width=4)
           e13=tk.Entry(pl,width=4)
           e14=tk.Entry(pl,width=4)
           e15=tk.Entry(pl,width=4)
           e16=tk.Entry(pl,width=4)
           e17=tk.Entry(pl,width=4)
           e18=tk.Entry(pl,width=4)
           e19=tk.Entry(pl,width=4)
           e20=tk.Entry(pl,width=4)
           e21=tk.Entry(pl,width=4)
           e22=tk.Entry(pl,width=4)
           e23=tk.Entry(pl,width=4)
           e24=tk.Entry(pl,width=4)
           e25=tk.Entry(pl,width=4)
           e26=tk.Entry(pl,width=4)
           e27=tk.Entry(pl,width=4)
           e28=tk.Entry(pl,width=4)
           e29=tk.Entry(pl,width=4)
           e30=tk.Entry(pl,width=4)
           e31=tk.Entry(pl,width=4)
           e32=tk.Entry(pl,width=4)
           e33=tk.Entry(pl,width=4)
           e34=tk.Entry(pl,width=4)
           e35=tk.Entry(pl,width=4)
           e36=tk.Entry(pl,width=4)
           e37=tk.Entry(pl,width=4)
           e38=tk.Entry(pl,width=4)
           e39=tk.Entry(pl,width=4)
           e40=tk.Entry(pl,width=4)
           e41=tk.Entry(pl,width=4)
           e42=tk.Entry(pl,width=4)
           e43=tk.Entry(pl,width=4)
           e44=tk.Entry(pl,width=4)
           e45=tk.Entry(pl,width=4)
           e46=tk.Entry(pl,width=4)
           e47=tk.Entry(pl,width=4)
           e48=tk.Entry(pl,width=4)
           e49=tk.Entry(pl,width=4)
           e50=tk.Entry(pl,width=4)
           e51=tk.Entry(pl,width=4)
           e52=tk.Entry(pl,width=4)
           e53=tk.Entry(pl,width=4)
           e54=tk.Entry(pl,width=4)
           e55=tk.Entry(pl,width=4)
           e56=tk.Entry(pl,width=4)
           e57=tk.Entry(pl,width=4)
           e58=tk.Entry(pl,width=4)
           e59=tk.Entry(pl,width=4)
           e60=tk.Entry(pl,width=4)
           e61=tk.Entry(pl,width=4)
           e62=tk.Entry(pl,width=4)
           e63=tk.Entry(pl,width=4)
           e64=tk.Entry(pl,width=4)
           def cambia_color(event):
              casilla=tk.Entry(pl)
              lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49,e50,e51,e52,e53,e54,e55,e56,e57,e58,e59,e60,e61,e62,e63,e64]
              for i in lista:
                 casilla.config(bg="white")
                 if casilla.focus_get():
                    if i==casilla.focus_get():
                       casilla=i
                       casilla.config(bg="lightblue")
                       break
                        
           def cambia_blanco(event):
              casilla=tk.Entry(pl)
              lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49,e50,e51,e52,e53,e54,e55,e56,e57,e58,e59,e60,e61,e62,e63,e64]
              for i in lista:
                 if casilla.focus_get():
                    if i==casilla.focus_get():
                       casilla=i
                       casilla.config(bg="white")
                       break
           e1.grid(row=1,column=1)
           e1.bind("<Enter>",cambia_color)
           e2.grid(row=1,column=2)
           e2.bind("<Enter>",cambia_color)
           e3.grid(row=1,column=3)
           e3.bind("<Enter>",cambia_color)
           e4.grid(row=1,column=4)
           e4.bind("<Enter>",cambia_color)

           e5.grid(row=1,column=5)
           e6.grid(row=1,column=6)
           e7.grid(row=1,column=7)
           e8.grid(row=1,column=8)
           e9.grid(row=2,column=1)
           e10.grid(row=2,column=2)
           e11.grid(row=2,column=3)
           e12.grid(row=2,column=4)
           e13.grid(row=2,column=5)
           e14.grid(row=2,column=6)
           e15.grid(row=2,column=7)
           e16.grid(row=2,column=8)
           e17.grid(row=3,column=1)
           e18.grid(row=3,column=2)
           e19.grid(row=3,column=3)
           e20.grid(row=3,column=4)
           e21.grid(row=3,column=5)
           e22.grid(row=3,column=6)
           e23.grid(row=3,column=7)
           e24.grid(row=3,column=8)
           e25.grid(row=4,column=1)
           e26.grid(row=4,column=2)
           e27.grid(row=4,column=3)
           e28.grid(row=4,column=4)
           e29.grid(row=4,column=5)
           e30.grid(row=4,column=6)
           e31.grid(row=4,column=7)
           e32.grid(row=4,column=8)
           e33.grid(row=5,column=1)
           e34.grid(row=5,column=2)
           e35.grid(row=5,column=3)
           e36.grid(row=5,column=4)
           e37.grid(row=5,column=5)
           e38.grid(row=5,column=6)
           e39.grid(row=5,column=7)
           e40.grid(row=5,column=8)
           e41.grid(row=6,column=1)
           e42.grid(row=6,column=2)
           e43.grid(row=6,column=3)
           e44.grid(row=6,column=4)
           e45.grid(row=6,column=5)
           e46.grid(row=6,column=6)
           e47.grid(row=6,column=7)
           e48.grid(row=6,column=8)
           e49.grid(row=7,column=1)
           e50.grid(row=7,column=2)
           e51.grid(row=7,column=3)
           e52.grid(row=7,column=4)
           e53.grid(row=7,column=5)
           e54.grid(row=7,column=6)
           e55.grid(row=7,column=7)
           e56.grid(row=7,column=8)
           e57.grid(row=8,column=1)
           e58.grid(row=8,column=2)
           e59.grid(row=8,column=3)
           e60.grid(row=8,column=4)
           e61.grid(row=8,column=5)
           e62.grid(row=8,column=6)
           e63.grid(row=8,column=7)
           e64.grid(row=8,column=8)
           e5.bind("<Enter>",cambia_color)
           e6.bind("<Enter>",cambia_color)
           e7.bind("<Enter>",cambia_color)
           e8.bind("<Enter>",cambia_color)
           e9.bind("<Enter>",cambia_color)
           e10.bind("<Enter>",cambia_color)
           e11.bind("<Enter>",cambia_color)
           e12.bind("<Enter>",cambia_color)
           e13.bind("<Enter>",cambia_color)
           e14.bind("<Enter>",cambia_color)
           e15.bind("<Enter>",cambia_color)
           e16.bind("<Enter>",cambia_color)
           e17.bind("<Enter>",cambia_color)
           e18.bind("<Enter>",cambia_color)
           e19.bind("<Enter>",cambia_color)
           e20.bind("<Enter>",cambia_color)
           e21.bind("<Enter>",cambia_color)
           e22.bind("<Enter>",cambia_color)
           e23.bind("<Enter>",cambia_color)
           e24.bind("<Enter>",cambia_color)
           e25.bind("<Enter>",cambia_color)
           e26.bind("<Enter>",cambia_color)
           e27.bind("<Enter>",cambia_color)
           e28.bind("<Enter>",cambia_color)
           e29.bind("<Enter>",cambia_color)
           e30.bind("<Enter>",cambia_color)
           e31.bind("<Enter>",cambia_color)
           e32.bind("<Enter>",cambia_color)
           e33.bind("<Enter>",cambia_color)
           e34.bind("<Enter>",cambia_color)
           e35.bind("<Enter>",cambia_color)
           e36.bind("<Enter>",cambia_color)
           e37.bind("<Enter>",cambia_color)
           e38.bind("<Enter>",cambia_color)
           e39.bind("<Enter>",cambia_color)
           e40.bind("<Enter>",cambia_color)
           e41.bind("<Enter>",cambia_color)
           e42.bind("<Enter>",cambia_color)
           e43.bind("<Enter>",cambia_color)
           e44.bind("<Enter>",cambia_color)
           e45.bind("<Enter>",cambia_color)
           e46.bind("<Enter>",cambia_color)
           e47.bind("<Enter>",cambia_color)
           e48.bind("<Enter>",cambia_color)
           e49.bind("<Enter>",cambia_color)
           e50.bind("<Enter>",cambia_color)
           e51.bind("<Enter>",cambia_color)
           e52.bind("<Enter>",cambia_color)
           e53.bind("<Enter>",cambia_color)
           e54.bind("<Enter>",cambia_color)
           e55.bind("<Enter>",cambia_color)
           e56.bind("<Enter>",cambia_color)
           e57.bind("<Enter>",cambia_color)
           e58.bind("<Enter>",cambia_color)
           e59.bind("<Enter>",cambia_color)
           e60.bind("<Enter>",cambia_color)
           e61.bind("<Enter>",cambia_color)
           e62.bind("<Enter>",cambia_color)
           e63.bind("<Enter>",cambia_color)
           e64.bind("<Enter>",cambia_color)
           e1.bind("<Button-1>",cambia_blanco)
           e2.bind("<Button-1>",cambia_blanco)
           e3.bind("<Button-1>",cambia_blanco)
           e4.bind("<Button-1>",cambia_blanco)
           e5.bind("<Button-1>",cambia_blanco)
           e6.bind("<Button-1>",cambia_blanco)
           e7.bind("<Button-1>",cambia_blanco)
           e8.bind("<Button-1>",cambia_blanco)
           e9.bind("<Button-1>",cambia_blanco)
           e10.bind("<Button-1>",cambia_blanco)
           e11.bind("<Button-1>",cambia_blanco)
           e12.bind("<Button-1>",cambia_blanco)
           e13.bind("<Button-1>",cambia_blanco)
           e14.bind("<Button-1>",cambia_blanco)
           e15.bind("<Button-1>",cambia_blanco)
           e16.bind("<Button-1>",cambia_blanco)
           e17.bind("<Button-1>",cambia_blanco)
           e18.bind("<Button-1>",cambia_blanco)
           e19.bind("<Button-1>",cambia_blanco)
           e20.bind("<Button-1>",cambia_blanco)
           e21.bind("<Button-1>",cambia_blanco)
           e22.bind("<Button-1>",cambia_blanco)
           e23.bind("<Button-1>",cambia_blanco)
           e24.bind("<Button-1>",cambia_blanco)
           e25.bind("<Button-1>",cambia_blanco)
           e26.bind("<Button-1>",cambia_blanco)
           e27.bind("<Button-1>",cambia_blanco)
           e28.bind("<Button-1>",cambia_blanco)
           e29.bind("<Button-1>",cambia_blanco)
           e30.bind("<Button-1>",cambia_blanco)
           e31.bind("<Button-1>",cambia_blanco)
           e32.bind("<Button-1>",cambia_blanco)
           e33.bind("<Button-1>",cambia_blanco)
           e34.bind("<Button-1>",cambia_blanco)
           e35.bind("<Button-1>",cambia_blanco)
           e36.bind("<Button-1>",cambia_blanco)
           e37.bind("<Button-1>",cambia_blanco)
           e38.bind("<Button-1>",cambia_blanco)
           e39.bind("<Button-1>",cambia_blanco)
           e40.bind("<Button-1>",cambia_blanco)
           e41.bind("<Button-1>",cambia_blanco)
           e42.bind("<Button-1>",cambia_blanco)
           e43.bind("<Button-1>",cambia_blanco)
           e44.bind("<Button-1>",cambia_blanco)
           e45.bind("<Button-1>",cambia_blanco)
           e46.bind("<Button-1>",cambia_blanco)
           e47.bind("<Button-1>",cambia_blanco)
           e48.bind("<Button-1>",cambia_blanco)
           e49.bind("<Button-1>",cambia_blanco)
           e50.bind("<Button-1>",cambia_blanco)
           e51.bind("<Button-1>",cambia_blanco)
           e52.bind("<Button-1>",cambia_blanco)
           e53.bind("<Button-1>",cambia_blanco)
           e54.bind("<Button-1>",cambia_blanco)
           e55.bind("<Button-1>",cambia_blanco)
           e56.bind("<Button-1>",cambia_blanco)
           e57.bind("<Button-1>",cambia_blanco)
           e58.bind("<Button-1>",cambia_blanco)
           e59.bind("<Button-1>",cambia_blanco)
           e60.bind("<Button-1>",cambia_blanco)
           e61.bind("<Button-1>",cambia_blanco)
           e62.bind("<Button-1>",cambia_blanco)
           e63.bind("<Button-1>",cambia_blanco)
           e64.bind("<Button-1>",cambia_blanco)
           matriz=[[e1,e2,e3,e4,e5,e6,e7,e8],
               [e9,e10,e11,e12,e13,e14,e15,e16],
               [e17,e18,e19,e20,e21,e22,e23,24],
               [e25,e26,e27,e28,e29,e30,e31,e32],
               [e33,e34,e35,e36,e37,e38,e39,e40],
               [e41,e42,e43,e44,e45,e46,e47,e48],
               [e49,e50,e51,e52,e53,e54,e55,e56],
               [e57,e58,e59,e60,e61,e62,e63,e64]]
        elif nueve==True:
           e1=tk.Entry(pl,width=4)
           e2=tk.Entry(pl,width=4)
           e3=tk.Entry(pl,width=4)
           e4=tk.Entry(pl,width=4)
           e5=tk.Entry(pl,width=4)
           e6=tk.Entry(pl,width=4)
           e7=tk.Entry(pl,width=4)
           e8=tk.Entry(pl,width=4)
           e9=tk.Entry(pl,width=4)
           e10=tk.Entry(pl,width=4)
           e11=tk.Entry(pl,width=4)
           e12=tk.Entry(pl,width=4)
           e13=tk.Entry(pl,width=4)
           e14=tk.Entry(pl,width=4)
           e15=tk.Entry(pl,width=4)
           e16=tk.Entry(pl,width=4)
           e17=tk.Entry(pl,width=4)
           e18=tk.Entry(pl,width=4)
           e19=tk.Entry(pl,width=4)
           e20=tk.Entry(pl,width=4)
           e21=tk.Entry(pl,width=4)
           e22=tk.Entry(pl,width=4)
           e23=tk.Entry(pl,width=4)
           e24=tk.Entry(pl,width=4)
           e25=tk.Entry(pl,width=4)
           e26=tk.Entry(pl,width=4)
           e27=tk.Entry(pl,width=4)
           e28=tk.Entry(pl,width=4)
           e29=tk.Entry(pl,width=4)
           e30=tk.Entry(pl,width=4)
           e31=tk.Entry(pl,width=4)
           e32=tk.Entry(pl,width=4)
           e33=tk.Entry(pl,width=4)
           e34=tk.Entry(pl,width=4)
           e35=tk.Entry(pl,width=4)
           e36=tk.Entry(pl,width=4)
           e37=tk.Entry(pl,width=4)
           e38=tk.Entry(pl,width=4)
           e39=tk.Entry(pl,width=4)
           e40=tk.Entry(pl,width=4)
           e41=tk.Entry(pl,width=4)
           e42=tk.Entry(pl,width=4)
           e43=tk.Entry(pl,width=4)
           e44=tk.Entry(pl,width=4)
           e45=tk.Entry(pl,width=4)
           e46=tk.Entry(pl,width=4)
           e47=tk.Entry(pl,width=4)
           e48=tk.Entry(pl,width=4)
           e49=tk.Entry(pl,width=4)
           e50=tk.Entry(pl,width=4)
           e51=tk.Entry(pl,width=4)
           e52=tk.Entry(pl,width=4)
           e53=tk.Entry(pl,width=4)
           e54=tk.Entry(pl,width=4)
           e55=tk.Entry(pl,width=4)
           e56=tk.Entry(pl,width=4)
           e57=tk.Entry(pl,width=4)
           e58=tk.Entry(pl,width=4)
           e59=tk.Entry(pl,width=4)
           e60=tk.Entry(pl,width=4)
           e61=tk.Entry(pl,width=4)
           e62=tk.Entry(pl,width=4)
           e63=tk.Entry(pl,width=4)
           e64=tk.Entry(pl,width=4)
           e65=tk.Entry(pl,width=4)
           e66=tk.Entry(pl,width=4)
           e67=tk.Entry(pl,width=4)
           e68=tk.Entry(pl,width=4)
           e69=tk.Entry(pl,width=4)
           e70=tk.Entry(pl,width=4)
           e71=tk.Entry(pl,width=4)
           e72=tk.Entry(pl,width=4)
           e73=tk.Entry(pl,width=4)
           e74=tk.Entry(pl,width=4)
           e75=tk.Entry(pl,width=4)
           e76=tk.Entry(pl,width=4)
           e77=tk.Entry(pl,width=4)
           e78=tk.Entry(pl,width=4)
           e79=tk.Entry(pl,width=4)
           e80=tk.Entry(pl,width=4)
           e81=tk.Entry(pl,width=4)
           def cambia_color(event):
              casilla=tk.Entry(pl)
              lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49,e50,e51,e52,e53,e54,e55,e56,e57,e58,e59,e60,e61,e62,e63,e64,e65,e66,e67,e68,e69,e70,e71,e72,e73,e74,e75,e76,e77,e78,e79,e80,e81]
              for i in lista:
                 casilla.config(bg="white")
                 if casilla.focus_get():
                    if i==casilla.focus_get():
                       casilla=i
                       casilla.config(bg="lightblue")
                       break
                        
           def cambia_blanco(event):
              casilla=tk.Entry(pl)
              lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49,e50,e51,e52,e53,e54,e55,e56,e57,e58,e59,e60,e61,e62,e63,e64,e65,e66,e67,e68,e69,e70,e71,e72,e73,e74,e75,e76,e77,e78,e79,e80,e81]
              for i in lista:
                 if casilla.focus_get():
                    if i==casilla.focus_get():
                       casilla=i
                       casilla.config(bg="white")
                       break
           e1.grid(row=1,column=1)
           e1.bind("<Enter>",cambia_color)
           e2.grid(row=1,column=2)
           e2.bind("<Enter>",cambia_color)
           e3.grid(row=1,column=3)
           e3.bind("<Enter>",cambia_color)
           e4.grid(row=1,column=4)
           e4.bind("<Enter>",cambia_color)

           e5.grid(row=1,column=5)
           e6.grid(row=1,column=6)
           e7.grid(row=1,column=7)
           e8.grid(row=1,column=8)
           e9.grid(row=1,column=9)
           e10.grid(row=2,column=1)
           e11.grid(row=2,column=2)
           e12.grid(row=2,column=3)
           e13.grid(row=2,column=4)
           e14.grid(row=2,column=5)
           e15.grid(row=2,column=6)
           e16.grid(row=2,column=7)
           e17.grid(row=2,column=8)
           e18.grid(row=2,column=9)
           e19.grid(row=3,column=1)
           e20.grid(row=3,column=2)
           e21.grid(row=3,column=3)
           e22.grid(row=3,column=4)
           e23.grid(row=3,column=5)
           e24.grid(row=3,column=6)
           e25.grid(row=3,column=7)
           e26.grid(row=3,column=8)
           e27.grid(row=3,column=9)
           e28.grid(row=4,column=1)
           e29.grid(row=4,column=2)
           e30.grid(row=4,column=3)
           e31.grid(row=4,column=4)
           e32.grid(row=4,column=5)
           e33.grid(row=4,column=6)
           e34.grid(row=4,column=7)
           e35.grid(row=4,column=8)
           e36.grid(row=4,column=9)
           e37.grid(row=5,column=1)
           e38.grid(row=5,column=2)
           e39.grid(row=5,column=3)
           e40.grid(row=5,column=4)
           e41.grid(row=5,column=5)
           e42.grid(row=5,column=6)
           e43.grid(row=5,column=7)
           e44.grid(row=5,column=8)
           e45.grid(row=5,column=9)
           e46.grid(row=6,column=1)
           e47.grid(row=6,column=2)
           e48.grid(row=6,column=3)
           e49.grid(row=6,column=4)
           e50.grid(row=6,column=5)
           e51.grid(row=6,column=6)
           e52.grid(row=6,column=7)
           e53.grid(row=6,column=8)
           e54.grid(row=6,column=9)
           e55.grid(row=7,column=1)
           e56.grid(row=7,column=2)
           e57.grid(row=7,column=3)
           e58.grid(row=7,column=4)
           e59.grid(row=7,column=5)
           e60.grid(row=7,column=6)
           e61.grid(row=7,column=7)
           e62.grid(row=7,column=8)
           e63.grid(row=7,column=9)
           e64.grid(row=8,column=1)
           e65.grid(row=8,column=2)
           e66.grid(row=8,column=3)
           e67.grid(row=8,column=4)
           e68.grid(row=8,column=5)
           e69.grid(row=8,column=6)
           e70.grid(row=8,column=7)
           e71.grid(row=8,column=8)
           e72.grid(row=8,column=9)
           e73.grid(row=9,column=1)
           e74.grid(row=9,column=2)
           e75.grid(row=9,column=3)
           e76.grid(row=9,column=4)
           e77.grid(row=9,column=5)
           e78.grid(row=9,column=6)
           e79.grid(row=9,column=7)
           e80.grid(row=9,column=8)
           e81.grid(row=9,column=9)
           e5.bind("<Enter>",cambia_color)
           e6.bind("<Enter>",cambia_color)
           e7.bind("<Enter>",cambia_color)
           e8.bind("<Enter>",cambia_color)
           e9.bind("<Enter>",cambia_color)
           e10.bind("<Enter>",cambia_color)
           e11.bind("<Enter>",cambia_color)
           e12.bind("<Enter>",cambia_color)
           e13.bind("<Enter>",cambia_color)
           e14.bind("<Enter>",cambia_color)
           e15.bind("<Enter>",cambia_color)
           e16.bind("<Enter>",cambia_color)
           e17.bind("<Enter>",cambia_color)
           e18.bind("<Enter>",cambia_color)
           e19.bind("<Enter>",cambia_color)
           e20.bind("<Enter>",cambia_color)
           e21.bind("<Enter>",cambia_color)
           e22.bind("<Enter>",cambia_color)
           e23.bind("<Enter>",cambia_color)
           e24.bind("<Enter>",cambia_color)
           e25.bind("<Enter>",cambia_color)
           e26.bind("<Enter>",cambia_color)
           e27.bind("<Enter>",cambia_color)
           e28.bind("<Enter>",cambia_color)
           e29.bind("<Enter>",cambia_color)
           e30.bind("<Enter>",cambia_color)
           e31.bind("<Enter>",cambia_color)
           e32.bind("<Enter>",cambia_color)
           e33.bind("<Enter>",cambia_color)
           e34.bind("<Enter>",cambia_color)
           e35.bind("<Enter>",cambia_color)
           e36.bind("<Enter>",cambia_color)
           e37.bind("<Enter>",cambia_color)
           e38.bind("<Enter>",cambia_color)
           e39.bind("<Enter>",cambia_color)
           e40.bind("<Enter>",cambia_color)
           e41.bind("<Enter>",cambia_color)
           e42.bind("<Enter>",cambia_color)
           e43.bind("<Enter>",cambia_color)
           e44.bind("<Enter>",cambia_color)
           e45.bind("<Enter>",cambia_color)
           e46.bind("<Enter>",cambia_color)
           e47.bind("<Enter>",cambia_color)
           e48.bind("<Enter>",cambia_color)
           e49.bind("<Enter>",cambia_color)
           e50.bind("<Enter>",cambia_color)
           e51.bind("<Enter>",cambia_color)
           e52.bind("<Enter>",cambia_color)
           e53.bind("<Enter>",cambia_color)
           e54.bind("<Enter>",cambia_color)
           e55.bind("<Enter>",cambia_color)
           e56.bind("<Enter>",cambia_color)
           e57.bind("<Enter>",cambia_color)
           e58.bind("<Enter>",cambia_color)
           e59.bind("<Enter>",cambia_color)
           e60.bind("<Enter>",cambia_color)
           e61.bind("<Enter>",cambia_color)
           e62.bind("<Enter>",cambia_color)
           e63.bind("<Enter>",cambia_color)
           e64.bind("<Enter>",cambia_color)
           e65.bind("<Enter>",cambia_color)
           e66.bind("<Enter>",cambia_color)
           e67.bind("<Enter>",cambia_color)
           e68.bind("<Enter>",cambia_color)
           e69.bind("<Enter>",cambia_color)
           e70.bind("<Enter>",cambia_color)
           e71.bind("<Enter>",cambia_color)
           e72.bind("<Enter>",cambia_color)
           e73.bind("<Enter>",cambia_color)
           e74.bind("<Enter>",cambia_color)
           e75.bind("<Enter>",cambia_color)
           e76.bind("<Enter>",cambia_color)
           e77.bind("<Enter>",cambia_color)
           e78.bind("<Enter>",cambia_color)
           e79.bind("<Enter>",cambia_color)
           e80.bind("<Enter>",cambia_color)
           e81.bind("<Enter>",cambia_color)
           e1.bind("<Button-1>",cambia_blanco)
           e2.bind("<Button-1>",cambia_blanco)
           e3.bind("<Button-1>",cambia_blanco)
           e4.bind("<Button-1>",cambia_blanco)
           e5.bind("<Button-1>",cambia_blanco)
           e6.bind("<Button-1>",cambia_blanco)
           e7.bind("<Button-1>",cambia_blanco)
           e8.bind("<Button-1>",cambia_blanco)
           e9.bind("<Button-1>",cambia_blanco)
           e10.bind("<Button-1>",cambia_blanco)
           e11.bind("<Button-1>",cambia_blanco)
           e12.bind("<Button-1>",cambia_blanco)
           e13.bind("<Button-1>",cambia_blanco)
           e14.bind("<Button-1>",cambia_blanco)
           e15.bind("<Button-1>",cambia_blanco)
           e16.bind("<Button-1>",cambia_blanco)
           e17.bind("<Button-1>",cambia_blanco)
           e18.bind("<Button-1>",cambia_blanco)
           e19.bind("<Button-1>",cambia_blanco)
           e20.bind("<Button-1>",cambia_blanco)
           e21.bind("<Button-1>",cambia_blanco)
           e22.bind("<Button-1>",cambia_blanco)
           e23.bind("<Button-1>",cambia_blanco)
           e24.bind("<Button-1>",cambia_blanco)
           e25.bind("<Button-1>",cambia_blanco)
           e26.bind("<Button-1>",cambia_blanco)
           e27.bind("<Button-1>",cambia_blanco)
           e28.bind("<Button-1>",cambia_blanco)
           e29.bind("<Button-1>",cambia_blanco)
           e30.bind("<Button-1>",cambia_blanco)
           e31.bind("<Button-1>",cambia_blanco)
           e32.bind("<Button-1>",cambia_blanco)
           e33.bind("<Button-1>",cambia_blanco)
           e34.bind("<Button-1>",cambia_blanco)
           e35.bind("<Button-1>",cambia_blanco)
           e36.bind("<Button-1>",cambia_blanco)
           e37.bind("<Button-1>",cambia_blanco)
           e38.bind("<Button-1>",cambia_blanco)
           e39.bind("<Button-1>",cambia_blanco)
           e40.bind("<Button-1>",cambia_blanco)
           e41.bind("<Button-1>",cambia_blanco)
           e42.bind("<Button-1>",cambia_blanco)
           e43.bind("<Button-1>",cambia_blanco)
           e44.bind("<Button-1>",cambia_blanco)
           e45.bind("<Button-1>",cambia_blanco)
           e46.bind("<Button-1>",cambia_blanco)
           e47.bind("<Button-1>",cambia_blanco)
           e48.bind("<Button-1>",cambia_blanco)
           e49.bind("<Button-1>",cambia_blanco)
           e50.bind("<Button-1>",cambia_blanco)
           e51.bind("<Button-1>",cambia_blanco)
           e52.bind("<Button-1>",cambia_blanco)
           e53.bind("<Button-1>",cambia_blanco)
           e54.bind("<Button-1>",cambia_blanco)
           e55.bind("<Button-1>",cambia_blanco)
           e56.bind("<Button-1>",cambia_blanco)
           e57.bind("<Button-1>",cambia_blanco)
           e58.bind("<Button-1>",cambia_blanco)
           e59.bind("<Button-1>",cambia_blanco)
           e60.bind("<Button-1>",cambia_blanco)
           e61.bind("<Button-1>",cambia_blanco)
           e62.bind("<Button-1>",cambia_blanco)
           e63.bind("<Button-1>",cambia_blanco)
           e64.bind("<Button-1>",cambia_blanco)
           e65.bind("<Button-1>",cambia_blanco)
           e66.bind("<Button-1>",cambia_blanco)
           e67.bind("<Button-1>",cambia_blanco)
           e68.bind("<Button-1>",cambia_blanco)
           e69.bind("<Button-1>",cambia_blanco)
           e70.bind("<Button-1>",cambia_blanco)
           e71.bind("<Button-1>",cambia_blanco)
           e72.bind("<Button-1>",cambia_blanco)
           e73.bind("<Button-1>",cambia_blanco)
           e74.bind("<Button-1>",cambia_blanco)
           e75.bind("<Button-1>",cambia_blanco)
           e76.bind("<Button-1>",cambia_blanco)
           e77.bind("<Button-1>",cambia_blanco)
           e78.bind("<Button-1>",cambia_blanco)
           e79.bind("<Button-1>",cambia_blanco)
           e80.bind("<Button-1>",cambia_blanco)
           e81.bind("<Button-1>",cambia_blanco)
           matriz=[[e1,e2,e3,e4,e5,e6,e7,e8,e9],
               [e10,e11,e12,e13,e14,e15,e16,e17,e18],
               [e19,e20,e21,e22,e23,e24,e25,26,e27],
               [e28,e29,e30,e31,e32,e33,e34,e35,e36],
               [e37,e38,e39,e40,e41,e42,e43,e44,e45],
               [e46,e47,e48,e49,e50,e51,e52,e53,e54],
               [e55,e56,e57,e58,e59,e60,e61,e62,e63],
               [e64,e65,e66,e67,e68,e69,e70,e71,e72],
               [e73,e74,e75,e76,e77,e78,e79,e80,e81]]
        def savear():
           global cont
           global seg
           global minu
           global hor
           esta=open("juegos.dat","w")
           result=[]
           print(matriz)
           for i in range(len( matriz)):
              for j in range(len(matriz[0])):
                 
                 
                 
                  print(i)
                  a=matriz[i][j]
                  print(a)
                  result+=[a.get()]
           result=[result,[hor,minu,seg,cont]]
           esta.write(str(result))
           esta.close()
        def cargarsh():
           global cargar
           global cont
           global seg
           global minu
           global hor
           cargar=True
           esta=open("juegos.dat","r")
           esta2=esta.read()
           esta2=eval(esta2)
           hor=esta2[1][0]
           minu=esta2[1][1]
           seg=esta2[1][2]
           cont=esta2[1][3]
           esta.close()
           
           pl.destroy()
           play()
        def Nuevo_juego():
            global tres
            global cuatro
            global cinco
            global seis
            global siete
            global ocho
            global nueve
            global multi
            global listaf3
            global listaf4
            global listaf5
            global listaf6
            global listaf7
            global listaf8
            global listaf9
            global listai3
            global listai4
            global listai5
            global listai6
            global listai7
            global listai8
            global listai9
            global listad3
            global listad4
            global listad5
            global listad6
            global listad7
            global listad8
            global listad9
            global contniv
            if facil:
                if tres==True:
                   listaf3.remove(p)
                elif cuatro==True:
                   listaf4.remove(p)
                elif cinco==True:
                   listaf5.remove(p)
                elif seis==True:
                   listaf6.remove(p)
                elif siete==True:
                   listaf7.remove(p)
                elif ocho==True:
                   listaf8.remove(p)
                elif nueve==True:
                   listaf9.remove(p)
                pl.destroy()
            elif normal:
                if tres==True:
                   listai3.remove(p)
                elif cuatro==True:
                   listai4.remove(p)
                elif cinco==True:
                   listai5.remove(p)
                elif seis==True:
                   listai6.remove(p)
                elif siete==True:
                   listai7.remove(p)
                elif ocho==True:
                   listai8.remove(p)
                elif nueve==True:
                   listai9.remove(p)
                pl.destroy()
            else:
                if tres==True:
                   listad3.remove(p)
                elif cuatro==True:
                   listad4.remove(p)
                elif cinco==True:
                   listad5.remove(p)
                elif seis==True:
                   listad6.remove(p)
                elif siete==True:
                   listad7.remove(p)
                elif ocho==True:
                   listad8.remove(p)
                elif nueve==True:
                   listad9.remove(p)
                pl.destroy()
            if multi==True:
               if contniv==1:
                  tres=False
                  cuatro=True
                  contniv+=1
               elif contniv==2:
                  cuatro=False
                  cinco=True
                  contniv+=1
               elif contniv==3:
                  cinco=False
                  seis=True
                  contniv+=1
               elif contniv==4:
                  seis=False
                  siete=True
                  contniv+=1
               elif contniv==5:
                  siete=False
                  ocho=True
                  contniv+=1
               elif contniv==6:
                  ocho=False
                  nueve=True
            play()
               
        def comprobar():
            global ganar
            comprolinea=[]
            comprocol=[]
            result=0
            resultmilt=1
            
            l1=[]
            vaarios=""
            
            for i in range(len(p)):
                varia=p[i+1][0]
                if "x" in varia:
                    vaarios="X"
                elif "X" in varia:
                    vaarios="X"
                elif "+" in varia:
                    vaarios="+"
                elif "-" in varia:
                    vaarios="-"
                elif "/" in varia:
                    vaarios="/"
                varia=varia.replace("+","")
                varia=varia.replace("-","")
                varia=varia.replace("x","")
                varia=varia.replace("X","")
                varia=varia.replace("/","")
                for j in range(len(p[i+1])-1):
                    varla=p[i+1][j+1]
                    varla2=matriz[varla[0]-1][varla[1]-1]
                    varla3=varla2.get()
                    comprolinea+=[int(varla3)]
                    
                    vardiv=max(comprolinea)
                    
                if vaarios=="":
                    if int(varia)!=comprolinea[0]:
                        messagebox.showerror("Error", "Solucion incorrecta en las casillas")
                        comprolinea=[]
                        ganar=False
                if vaarios=="X":
                    for l in comprolinea:
                        resultmilt*=l
                    
                    
                    if resultmilt!=int(varia):
                        messagebox.showerror("Error", "Solucion incorrecta en las casillas")
                        ganar=False
                    comprolinea=[]
                    resultmilt=1
                        
                        
                        
                    
                elif vaarios=="+":
                    for l in comprolinea:
                        
                        result+=l
                    if result!=int(varia):
                        messagebox.showerror("Error", "Solucion incorrecta en las casillas")
                        ganar=False

                    comprolinea=[]
                    result=0
                            
                            
                elif vaarios=="-":
                    for l in comprolinea:
                        
                        result=abs(result-l)
                    print(result)
                    if result!=int(varia):
                        messagebox.showerror("Error", "Solucion incorrecta en las casillas")
                        ganar=False
                    comprolinea=[]
                    result=0
                elif vaarios=="/":
                    for l in range(len(comprolinea)-1):
                        comprolinea.remove(vardiv)
                        vardiv=vardiv//min(comprolinea)
                        comprolinea.remove(min(comprolinea))
                    
                    if vardiv!=int(varia):
                        messagebox.showerror("Error", "Solucion incorrecta en las casillas")
                        ganar=False
                        
                    
                    comprolinea=[]    
                else:
                    if int(varia)!=comprolinea[0]:
                        messagebox.showerror("Error", "Solucion incorrecta en las casillas")
                        ganar=False
                        comprolinea=[]
                        
                    
                
                
                #if result!=int(varia):
                 #   messagebox.showerror("Error", "Solucion incorrecta1")
                  #  break
               # result=0
                    
            for i in range(len(matriz)):
                for j in matriz[i]:
                    bar=int(j.get())
                    if bar in l1:
                        messagebox.showerror("Error", "Solucion incorrecta en las filas")
                        ganar=False
                        break
                    else:
                        l1+=[bar]
                    
                l1=[]
            l1=[]
            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    matri=matriz[j][i]
                    bar=int(matri.get())
                    print(bar,l1)
                    if bar in l1:
                        messagebox.showerror("Error", "Solucion incorrecta en las columnas")
                        ganar=False
                        break
                    else:
                        l1+=[bar]
                l1=[]
            if ganar:
               messagebox.showinfo("Enhorabuena", "Solucion lograda")
               #nombres=e82.get()
               #r=open("Top 10.txt","r")
            
               #nuv=r.read()
               #r.close()
            
               #r=open("Top 10.txt","w")
               #r.write(nuv+" "+nombres)
               #r.close()
               if multi:
                  Nuevo_juego()
            ganar=True
        
        if cargar:
           try:
              
              esta=open("juegos.dat","r")
              esta2=esta.read()
              esta2=eval(esta2)
              cont=0
              for i in range(len(matriz)):
                 for j in range(len(matriz[0])):
                    a=matriz[i][j]
                    a.insert (0,esta2[0][cont])
                    cont+=1
              esta.close()
           except:
              pl.withdraw()
              messagebox.showerror("Error", "No existen juegos guardados")
              for i in range(len(matriz)):
                 for j in range(len(matriz[0])):
                    a=matriz[i][j]
                    a.delete (0,END)
              pl.deiconify()

             
              
        if f is None:
            
            f = open("kenken_juegos.dat")
            f2=f.readlines()
            print(len(f2))
            for i in range(len(f2)):
                if f2[i][0]=="F":
                   if f2[i][1]=="3":
                      listaf3+=[eval(f2[i][2:])]
                   if f2[i][1]=="4":
                      listaf4+=[eval(f2[i][2:])]
                   if f2[i][1]=="5":
                      listaf5+=[eval(f2[i][2:])]
                   if f2[i][1]=="6":
                      listaf6+=[eval(f2[i][2:])]
                      print(listaf6)
                   if f2[i][1]=="7":
                      listaf7+=[eval(f2[i][2:])]
                   if f2[i][1]=="8":
                      listaf8+=[eval(f2[i][2:])]
                   if f2[i][1]=="9":
                      listaf9+=[eval(f2[i][2:])]
                elif f2[i][0]=="I":
                    if f2[i][1]=="3":
                       listai3+=[eval(f2[i][2:])]
                    if f2[i][1]=="4":
                       listai4+=[eval(f2[i][2:])]
                    if f2[i][1]=="5":
                       listai5+=[eval(f2[i][2:])]
                    if f2[i][1]=="6":
                       listai6+=[eval(f2[i][2:])]
                    if f2[i][1]=="7":
                       listai7+=[eval(f2[i][2:])]
                    if f2[i][1]=="8":
                       listai8+=[eval(f2[i][2:])]
                    if f2[i][1]=="9":
                       listai9+=[eval(f2[i][2:])]
                else:
                    if f2[i][1]=="3":
                      listad3+=[eval(f2[i][2:])]
                    if f2[i][1]=="4":
                       listad4+=[eval(f2[i][2:])]
                    if f2[i][1]=="5":
                       listad5+=[eval(f2[i][2:])]
                    if f2[i][1]=="6":
                       listad6+=[eval(f2[i][2:])]
                    if f2[i][1]=="7":
                       listad7+=[eval(f2[i][2:])]
                    if f2[i][1]=="8":
                       listad8+=[eval(f2[i][2:])]
                    if f2[i][1]=="9":
                       listad9+=[eval(f2[i][2:])]
        
        if facil is True:
            if tres==True:
               if listaf3 == []:
                  p=[]
                  messagebox.showerror("Error", "No existen niveles en la dificultad facil")
                  pl.withdraw()
                  root.deiconify()
               else:
                  print(cargar)
                  if cargar:
                     p=p
                  else:
                     p=listaf3[random.randint(0,len(listaf3)-1)]
            elif cuatro==True:
               if listaf4 == []:
                  p=[]
                  messagebox.showerror("Error", "No existen niveles en la dificultad facil")
                  pl.withdraw()
                  root.deiconify()
               else:
                  print(cargar)
                  if cargar:
                     p=p
                  else:
                     p=listaf4[random.randint(0,len(listaf4)-1)]
            elif cinco==True:
               if listaf5 == []:
                  p=[]
                  messagebox.showerror("Error", "No existen niveles en la dificultad facil")
                  pl.withdraw()
                  root.deiconify()
               else:
                  print(cargar)
                  if cargar:
                     p=p
                  else:
                     p=listaf5[random.randint(0,len(listaf5)-1)]
            elif seis==True:
               if listaf6 == []:
                  p=[]
                  messagebox.showerror("Error", "No existen niveles en la dificultad facil")
                  pl.withdraw()
                  root.deiconify()
               else:
                  print(cargar)
                  if cargar:
                     p=p
                  else:
                     p=listaf6[random.randint(0,len(listaf6)-1)]
            elif siete==True:
               if listaf7 == []:
                  p=[]
                  messagebox.showerror("Error", "No existen niveles en la dificultad facil")
                  pl.withdraw()
                  root.deiconify()
               else:
                  print(cargar)
                  if cargar:
                     p=p
                  else:
                     p=listaf7[random.randint(0,len(listaf7)-1)]
            elif ocho==True:
               if listaf8 == []:
                  p=[]
                  messagebox.showerror("Error", "No existen niveles en la dificultad facil")
                  pl.withdraw()
                  root.deiconify()
               else:
                  print(cargar)
                  if cargar:
                     p=p
                  else:
                     p=listaf8[random.randint(0,len(listaf8)-1)]
            elif nueve==True:
               if listaf9 == []:
                  p=[]
                  messagebox.showerror("Error", "No existen niveles en la dificultad facil")
                  pl.withdraw()
                  root.deiconify()
               else:
                  print(cargar)
                  if cargar:
                     p=p
                  else:
                     p=listaf9[random.randint(0,len(listaf9)-1)]
                #print(listaf)
               print(p)
        elif normal is True:
            if tres==True:
               if listai3 == []:
                  p=[]
                  messagebox.showerror("Error", "No existen niveles en la dificultad facil")
                  pl.withdraw()
                  root.deiconify()
               else:
                  print(cargar)
                  if cargar:
                     p=p
                  else:
                     p=listai3[random.randint(0,len(listai3)-1)]
            elif cuatro==True:
               if listai4 == []:
                  p=[]
                  messagebox.showerror("Error", "No existen niveles en la dificultad facil")
                  pl.withdraw()
                  root.deiconify()
               else:
                  print(cargar)
                  if cargar:
                     p=p
                  else:
                     p=listai4[random.randint(0,len(listai4)-1)]
            elif cinco==True:
               if listai5 == []:
                  p=[]
                  messagebox.showerror("Error", "No existen niveles en la dificultad facil")
                  pl.withdraw()
                  root.deiconify()
               else:
                  print(cargar)
                  if cargar:
                     p=p
                  else:
                     p=listai5[random.randint(0,len(listai5)-1)]
            elif seis==True:
               if listai6 == []:
                  p=[]
                  messagebox.showerror("Error", "No existen niveles en la dificultad facil")
                  pl.withdraw()
                  root.deiconify()
               else:
                  print(cargar)
                  if cargar:
                     p=p
                  else:
                     p=listai6[random.randint(0,len(listai6)-1)]
            elif siete==True:
               if listai7 == []:
                  p=[]
                  messagebox.showerror("Error", "No existen niveles en la dificultad facil")
                  pl.withdraw()
                  root.deiconify()
               else:
                  print(cargar)
                  if cargar:
                     p=p
                  else:
                     p=listai7[random.randint(0,len(listai7)-1)]
            elif ocho==True:
               if listai8 == []:
                  p=[]
                  messagebox.showerror("Error", "No existen niveles en la dificultad facil")
                  pl.withdraw()
                  root.deiconify()
               else:
                  print(cargar)
                  if cargar:
                     p=p
                  else:
                     p=listai8[random.randint(0,len(listai8)-1)]
            elif nueve==True:
               if listai9 == []:
                  p=[]
                  messagebox.showerror("Error", "No existen niveles en la dificultad facil")
                  pl.withdraw()
                  root.deiconify()
               else:
                  print(cargar)
                  if cargar:
                     p=p
                  else:
                     p=listai9[random.randint(0,len(listai9)-1)]
        else:
            if tres==True:
               if listad3 == []:
                  p=[]
                  messagebox.showerror("Error", "No existen niveles en la dificultad facil")
                  pl.withdraw()
                  root.deiconify()
               else:
                  print(cargar)
                  if cargar:
                     p=p
                  else:
                     p=listad3[random.randint(0,len(listad3)-1)]
            elif cuatro==True:
               if listad4 == []:
                  p=[]
                  messagebox.showerror("Error", "No existen niveles en la dificultad facil")
                  pl.withdraw()
                  root.deiconify()
               else:
                  print(cargar)
                  if cargar:
                     p=p
                  else:
                     p=listad4[random.randint(0,len(listad4)-1)]
            elif cinco==True:
               if listad5 == []:
                  p=[]
                  messagebox.showerror("Error", "No existen niveles en la dificultad facil")
                  pl.withdraw()
                  root.deiconify()
               else:
                  print(cargar)
                  if cargar:
                     p=p
                  else:
                     p=listad5[random.randint(0,len(listad5)-1)]
            elif seis==True:
               if listad6 == []:
                  p=[]
                  messagebox.showerror("Error", "No existen niveles en la dificultad facil")
                  pl.withdraw()
                  root.deiconify()
               else:
                  print(cargar)
                  if cargar:
                     p=p
                  else:
                     p=listad6[random.randint(0,len(listad6)-1)]
            elif siete==True:
               if listad7 == []:
                  p=[]
                  messagebox.showerror("Error", "No existen niveles en la dificultad facil")
                  pl.withdraw()
                  root.deiconify()
               else:
                  print(cargar)
                  if cargar:
                     p=p
                  else:
                     p=listad7[random.randint(0,len(listad7)-1)]
            elif ocho==True:
               if listad8 == []:
                  p=[]
                  messagebox.showerror("Error", "No existen niveles en la dificultad facil")
                  pl.withdraw()
                  root.deiconify()
               else:
                  print(cargar)
                  if cargar:
                     p=p
                  else:
                     p=listad8[random.randint(0,len(listad8)-1)]
            elif nueve==True:
               if listad9 == []:
                  p=[]
                  messagebox.showerror("Error", "No existen niveles en la dificultad facil")
                  pl.withdraw()
                  root.deiconify()
               else:
                  print(cargar)
                  if cargar:
                     p=p
                  else:
                     p=listad9[random.randint(0,len(listad9)-1)]
        row=1
        cargar=False
        
        for e in p:
            rules=tk.Label(pl,text=(e,"-",p[e]))
            rules.grid(row=row,column=7)
            row+=1
        def  insertar1():
            global tres
            global cuatro
            global cinco
            global seis
            global siete
            global ocho
            global nueve
            global multi
            casilla=tk.Entry(pl)
            if tres==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9]
            elif cuatro==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16]
            elif cinco==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25]
            elif seis==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36]
            elif siete==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49]
            elif ocho==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49,e50,e51,e52,e53,e54,e55,e56,e57,e58,e59,e60,e61,e62,e63,e64]
            elif nueve==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49,e50,e51,e52,e53,e54,e55,e56,e57,e58,e59,e60,e61,e62,e63,e64,e65,e66,e67,e68,e69,e70,e71,e72,e73,e74,e75,e76,e77,e78,e79,e80,e81]
            for i in lista:
                if casilla.focus_get():
                    if i==casilla.focus_get():
                        casilla=i
                        casilla.delete(0,END)
                        casilla.insert(1000000,"1")
                        break
            else:
                messagebox.showerror("Error", "Primero debe seleccionar una casilla")
           #Inserta numero 2 a la casilla en la que esta el cursor
        def  insertar2():
            global tres
            global cuatro
            global cinco
            global seis
            global siete
            global ocho
            global nueve
            global multi
            casilla=tk.Entry(pl)
            if tres==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9]
            elif cuatro==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16]
            elif cinco==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25]
            elif seis==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36]
            elif siete==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49]
            elif ocho==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49,e50,e51,e52,e53,e54,e55,e56,e57,e58,e59,e60,e61,e62,e63,e64]
            elif nueve==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49,e50,e51,e52,e53,e54,e55,e56,e57,e58,e59,e60,e61,e62,e63,e64,e65,e66,e67,e68,e69,e70,e71,e72,e73,e74,e75,e76,e77,e78,e79,e80,e81]
            for i in lista:
                if casilla.focus_get():
                    if i==casilla.focus_get():
                        casilla=i
                        casilla.delete(0,END)
                        casilla.insert(1000000,"2")
                        break

            else:
                messagebox.showerror("Error", "Primero debe seleccionar una casilla")
           #Inserta numero 3 a la casilla en la que esta el cursor
        def  insertar3():
            global tres
            global cuatro
            global cinco
            global seis
            global siete
            global ocho
            global nueve
            global multi
            casilla=tk.Entry(pl)
            if tres==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9]
            elif cuatro==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16]
            elif cinco==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25]
            elif seis==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36]
            elif siete==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49]
            elif ocho==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49,e50,e51,e52,e53,e54,e55,e56,e57,e58,e59,e60,e61,e62,e63,e64]
            elif nueve==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49,e50,e51,e52,e53,e54,e55,e56,e57,e58,e59,e60,e61,e62,e63,e64,e65,e66,e67,e68,e69,e70,e71,e72,e73,e74,e75,e76,e77,e78,e79,e80,e81]
            for i in lista:
                if casilla.focus_get():
                    if i==casilla.focus_get():
                        casilla=i
                        casilla.delete(0,END)
                        casilla.insert(1000000,"3")
                        break
            else:
                messagebox.showerror("Error", "Primero debe seleccionar una casilla")
                    
           #Inserta numero 4 a la casilla en la que esta el cursor
        def  insertar4():
            global tres
            global cuatro
            global cinco
            global seis
            global siete
            global ocho
            global nueve
            global multi
            casilla=tk.Entry(pl)
            if tres==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9]
            elif cuatro==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16]
            elif cinco==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25]
            elif seis==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36]
            elif siete==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49]
            elif ocho==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49,e50,e51,e52,e53,e54,e55,e56,e57,e58,e59,e60,e61,e62,e63,e64]
            elif nueve==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49,e50,e51,e52,e53,e54,e55,e56,e57,e58,e59,e60,e61,e62,e63,e64,e65,e66,e67,e68,e69,e70,e71,e72,e73,e74,e75,e76,e77,e78,e79,e80,e81]
            for i in lista:
                if casilla.focus_get():
                    if i==casilla.focus_get():
                        casilla=i
                        casilla.delete(0,END)
                        casilla.insert(1000000,"4")
                        break
            else:
                messagebox.showerror("Error", "Primero debe seleccionar una casilla")
           #Inserta numero 5 a la casilla en la que esta el cursor
        def  insertar5():
            global tres
            global cuatro
            global cinco
            global seis
            global siete
            global ocho
            global nueve
            global multi
            casilla=tk.Entry(pl)
            if tres==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9]
            elif cuatro==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16]
            elif cinco==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25]
            elif seis==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36]
            elif siete==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49]
            elif ocho==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49,e50,e51,e52,e53,e54,e55,e56,e57,e58,e59,e60,e61,e62,e63,e64]
            elif nueve==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49,e50,e51,e52,e53,e54,e55,e56,e57,e58,e59,e60,e61,e62,e63,e64,e65,e66,e67,e68,e69,e70,e71,e72,e73,e74,e75,e76,e77,e78,e79,e80,e81]
            for i in lista:
                if casilla.focus_get():
                    if i==casilla.focus_get():
                        casilla=i
                        casilla.delete(0,END)
                        casilla.insert(1000000,"5")
                        break
            else:
                messagebox.showerror("Error", "Primero debe seleccionar una casilla")
           #Inserta numero 6 a la casilla en la que esta el cursor
        def  insertar6():
            global tres
            global cuatro
            global cinco
            global seis
            global siete
            global ocho
            global nueve
            global multi
            casilla=tk.Entry(pl)
            if tres==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9]
            elif cuatro==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16]
            elif cinco==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25]
            elif seis==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36]
            elif siete==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49]
            elif ocho==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49,e50,e51,e52,e53,e54,e55,e56,e57,e58,e59,e60,e61,e62,e63,e64]
            elif nueve==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49,e50,e51,e52,e53,e54,e55,e56,e57,e58,e59,e60,e61,e62,e63,e64,e65,e66,e67,e68,e69,e70,e71,e72,e73,e74,e75,e76,e77,e78,e79,e80,e81]
            for i in lista:
                if casilla.focus_get():
                    if i==casilla.focus_get():
                        casilla=i
                        casilla.delete(0,END)
                        casilla.insert(1000000,"6")
                        break
            else:
                messagebox.showerror("Error", "Primero debe seleccionar una casilla")
           #Inserta numero 7 a la casilla en la que esta el cursor
        def  insertar7():
            global tres
            global cuatro
            global cinco
            global seis
            global siete
            global ocho
            global nueve
            global multi
            casilla=tk.Entry(pl)
            if tres==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9]
            elif cuatro==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16]
            elif cinco==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25]
            elif seis==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36]
            elif siete==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49]
            elif ocho==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49,e50,e51,e52,e53,e54,e55,e56,e57,e58,e59,e60,e61,e62,e63,e64]
            elif nueve==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49,e50,e51,e52,e53,e54,e55,e56,e57,e58,e59,e60,e61,e62,e63,e64,e65,e66,e67,e68,e69,e70,e71,e72,e73,e74,e75,e76,e77,e78,e79,e80,e81]
            for i in lista:
                if casilla.focus_get():
                    if i==casilla.focus_get():
                        casilla=i
                        casilla.delete(0,END)
                        casilla.insert(1000000,"7")
                        break
            else:
                messagebox.showerror("Error", "Primero debe seleccionar una casilla")
           #Inserta numero 8 a la casilla en la que esta el cursor
        def  insertar8():
            global tres
            global cuatro
            global cinco
            global seis
            global siete
            global ocho
            global nueve
            global multi
            casilla=tk.Entry(pl)
            if tres==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9]
            elif cuatro==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16]
            elif cinco==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25]
            elif seis==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36]
            elif siete==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49]
            elif ocho==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49,e50,e51,e52,e53,e54,e55,e56,e57,e58,e59,e60,e61,e62,e63,e64]
            elif nueve==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49,e50,e51,e52,e53,e54,e55,e56,e57,e58,e59,e60,e61,e62,e63,e64,e65,e66,e67,e68,e69,e70,e71,e72,e73,e74,e75,e76,e77,e78,e79,e80,e81]
            for i in lista:
                if casilla.focus_get():
                    if i==casilla.focus_get():
                        casilla=i
                        casilla.delete(0,END)
                        casilla.insert(1000000,"8")
                        break
            else:
                messagebox.showerror("Error", "Primero debe seleccionar una casilla")
           #Inserta numero 9 a la casilla en la que esta el cursor
        def  insertar9():
            global tres
            global cuatro
            global cinco
            global seis
            global siete
            global ocho
            global nueve
            global multi
            casilla=tk.Entry(pl)
            if tres==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9]
            elif cuatro==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16]
            elif cinco==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25]
            elif seis==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36]
            elif siete==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49]
            elif ocho==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49,e50,e51,e52,e53,e54,e55,e56,e57,e58,e59,e60,e61,e62,e63,e64]
            elif nueve==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49,e50,e51,e52,e53,e54,e55,e56,e57,e58,e59,e60,e61,e62,e63,e64,e65,e66,e67,e68,e69,e70,e71,e72,e73,e74,e75,e76,e77,e78,e79,e80,e81]
            for i in lista:
                if casilla.focus_get():
                    if i==casilla.focus_get():
                        casilla=i
                        casilla.delete(0,END)
                        casilla.insert(1000000,"9")
                        #casilla.config(bg="white")
                        break
            else:
                messagebox.showerror("Error", "Primero debe seleccionar una casilla")
                        
        def borrar():
            global tres
            global cuatro
            global cinco
            global seis
            global siete
            global ocho
            global nueve
            global multi
            casilla=tk.Entry(pl)
            if tres==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9]
            elif cuatro==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16]
            elif cinco==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25]
            elif seis==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36]
            elif siete==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49]
            elif ocho==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49,e50,e51,e52,e53,e54,e55,e56,e57,e58,e59,e60,e61,e62,e63,e64]
            elif nueve==True:
               lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49,e50,e51,e52,e53,e54,e55,e56,e57,e58,e59,e60,e61,e62,e63,e64,e65,e66,e67,e68,e69,e70,e71,e72,e73,e74,e75,e76,e77,e78,e79,e80,e81]
            for i in lista:
                     if casilla.focus_get():
                        if i==casilla.focus_get():
                           casilla=i
                           casilla.delete(0,END)
                           break
            else:
                messagebox.showerror("Error", "Primero debe seleccionar una casilla")
            

        if sir is True:
            labelcenti = Label(pl, fg="blue")
            labelcenti.grid(row=1, column=11, sticky=W, padx=10,pady=4)
            labelseg = Label(pl, fg="blue")
            labelseg.grid(row=1, column=10, sticky=W, padx=10,pady=4)
            labelmin = Label(pl, fg="blue")
            labelmin.grid(row=1, column=9, sticky=W, padx=10,pady=4)
            labelhor = Label(pl, fg="blue")
            labelhor.grid(row=1, column=8, sticky=W, padx=10,pady=4)
        #Inicia el plometro y cambia start por stop
        def start():
           global button13
           if sir is True:
               button1 = tk.Button(pl, text="1",width=2,height=1,command=insertar1)
               button2 = tk.Button(pl, text="2",width=2,height=1,command=insertar2)
               button3 = tk.Button(pl, text="3",width=2,height=1,command=insertar3)
               button4 = tk.Button(pl, text="4",width=2,height=1,command=insertar4)
               button5 = tk.Button(pl, text="5",width=2,height=1,command=insertar5)
               button6 = tk.Button(pl, text="6",width=2,height=1,command=insertar6)
               button7 = tk.Button(pl, text="7",width=2,height=1,command=insertar7)
               button8 = tk.Button(pl, text="8",width=2,height=1,command=insertar8)
               button9 = tk.Button(pl, text="9",width=2,height=1,command=insertar9)
               button10 = tk.Button(pl, text="borrador",width=6,height=1,command=borrar)
               


               button1.grid(row=10,column=1)
               button2.grid(row=10,column=2)
               button3.grid(row=10,column=3)
               button4.grid(row=11,column=1)
               button5.grid(row=11,column=2)
               button6.grid(row=11,column=3)
               button7.grid(row=12,column=1)
               button8.grid(row=12,column=2)
               button9.grid(row=12,column=3)
               button10.grid(row=11,column=4,columnspan=3)

               
               button12.config(text="Finish",bg="red",command=back)
               button13=Button(pl, text='Pause',bg="red",width=6,command=cronometro3)
               button13.grid(row=2, column=11,rowspan=2, sticky=W,  padx=10,pady=4)
               button14.config(text="Restart",width=6,command=restart)
               button17.config(text="guardar",command=savear)
               cronometro2()
           elif sir is False:
               button1 = tk.Button(pl, text="1",width=2,height=1,command=insertar1)
               button2 = tk.Button(pl, text="2",width=2,height=1,command=insertar2)
               button3 = tk.Button(pl, text="3",width=2,height=1,command=insertar3)
               button4 = tk.Button(pl, text="4",width=2,height=1,command=insertar4)
               button5 = tk.Button(pl, text="5",width=2,height=1,command=insertar5)
               button6 = tk.Button(pl, text="6",width=2,height=1,command=insertar6)
               button7 = tk.Button(pl, text="7",width=2,height=1,command=insertar7)
               button8 = tk.Button(pl, text="8",width=2,height=1,command=insertar8)
               button9 = tk.Button(pl, text="9",width=2,height=1,command=insertar9)
               button10 = tk.Button(pl, text="borrador",width=6,height=1,command=borrar)
               
               button1.grid(row=10,column=1)
               button2.grid(row=10,column=2)
               button3.grid(row=10,column=3)
               button4.grid(row=11,column=1)
               button5.grid(row=11,column=2)
               button6.grid(row=11,column=3)
               button7.grid(row=12,column=1)
               button8.grid(row=12,column=2)
               button9.grid(row=12,column=3)
               button10.grid(row=11,column=4,columnspan=3)
               button12.config(text="Finish",bg="red",command=back)
               button14.config(text="Restart",width=6,command=restart)
               button17.config(text="guardar",command=savear)
               
               
       #Reinicia el cronometro
        def restart():
           global cont
           global seg
           global minu
           global hor
           global stop
           stop=False
           cont=0
           seg=0
           minu=0
           hor=0
           if messagebox.askyesno('warning', 'seguro que quiere reiniciar?'):
               pl.destroy()
               play()
       #Devuelve al menú
        def back():
           global cont
           global seg
           global minu
           global hor
           global stop
           stop=False
           cont=0
           seg=0
           minu=0
           hor=0
           if messagebox.askyesno('warning', 'Seguro que quiere salir?'):
               pl.destroy()
               root.deiconify()
       #Funcion que cuenta las horas,minutos,segundos y centisegundos
        def cronometro2():
            global cont
            global seg
            global minu
            global hor
            if stop:
               cont=cont-1
            if cont==100:
               cont=0
               seg+=1
               labelseg.config(text=str(seg))
               if seg==59:
                  
                  seg=0
                  minu+=1
                  labelmin.config(text=str(minu))
                  
                  if minu==59:
                     minu=0
                     hor+=1
                     labelhor.config(text=str(hor))
            cont+=1
            labelcenti.config(text=str(cont))
            labelcenti.after(9, cronometro2)
        button12 =Button(pl, text='Start',bg="yellow",width=6,command=start)
        button12.grid(row=13, column=1,columnspan=3, sticky=W,  padx=10,pady=4)
        button14 =Button(pl, text='Change game',bg="lightblue",width=10,command=Nuevo_juego)
        button14.grid(row=13,column=4,columnspan=3, sticky=W,padx=10,pady=4)
        button15 = tk.Button(pl, text="comprobar",width=9,height=1,command=comprobar)
        button15.grid(row=9,column=4,columnspan=3)
        button16=Button(pl, text='Completed',bg="lightblue",width=10,command=Top_ten)
        button16.grid(row=14,column=4,columnspan=3)
        button17=Button(pl, text='cargar',bg="yellow",width=10,command=cargarsh)
        button17.grid(row=15,column=4,columnspan=3)
        

        
        if e82.get()=="":
            messagebox.showerror("Error", "Debe poner su nombre")
            pl.withdraw()
            nombre()
        nombr=Label(pl,text=("Name:",e82.get()))
        nombr.grid(row=16,column=1,columnspan=3)
        if facil==True:
            niv=Label(pl,text="Level:Easy")
            niv.grid(row=16,column=4,columnspan=3)
        elif normal==True:
            niv=Label(pl,text="Level:Normal")
            niv.grid(row=16,column=4,columnspan=3)
        elif dificil==True:
            niv=Label(pl,text="Level:Dificult")
            niv.grid(row=16,column=4,columnspan=3)
        pl.title("kenken")
    conf=Button(nom,text="Confirm",bg="lightgreen",width=6,command=play)
    conf.grid(row=2,column=1)
    
        
def cronometro3():
   global stop
   global button13
   if stop:
      stop=False
      button13.config(text="Stop",bg="red")
   else:
      stop=True
      button13.config(text="Continue",bg="yellow")
global tres
global cuatro
global cinco
global seis
global siete
global ocho
global nueve
global multi
global facil
global normal
global dificil
global sir
global nor
global timer
global sis
global nos
tres=False
cuatro=False
cinco=False
seis=True
siete=False
ocho=False
nueve=False
multi=False
facil=True
normal=False
dificil=False
sir=False
nor=True
timer=False
sis=False
nos=True
global v
global v1
global v2
global v3
global con
con=tk.Tk()
v = tk.IntVar()
v1 = tk.IntVar()
v2= tk.IntVar()
v3= tk.IntVar()
v.set(4)
v1.set(1)
v2.set(2)
v3.set(2)
con.withdraw()
def config():
    global v
    global v2
    global v3
    global con
    root.withdraw()
    con.deiconify()
    def eleccion1():
        global facil
        global normal
        global dificil
        if v1.get()==1:
            facil=True
            normal=False
            dificil=False
        elif v1.get()==2:
            facil=False
            normal=True
            dificil=False
        elif v1.get()==3:
            facil=False
            normal=False
            dificil=True
    def eleccion2():
        global sir
        global nor
        global timer
        if v2.get()==1:
            sir=True
            nor=False
            timer=False
        elif v2.get()==2:
            sir=False
            nor=True
            timer=False
        elif v2.get()==3:
            sir=False
            nor=False
            timer=True
    def eleccion3():
        global sis
        global nos
        if v3.get()==1:
            sis=True
            nos=False
        elif v3.get()==2:
            sis=False
            nos=True
    def eleccion4():
      global tres
      global cuatro
      global cinco
      global seis
      global siete
      global ocho
      global nueve
      global multi
      if v.get()==1:
         tres=True
         cuatro=False
         cinco=False
         seis=False
         siete=False
         ocho=False
         nueve=False
         multi=False
      elif v.get()==2:
         tres=False
         cuatro=True
         cinco=False
         seis=False
         siete=False
         ocho=False
         nueve=False
         multi=False
      elif v.get()==3:
         tres=False
         cuatro=False
         cinco=True
         seis=False
         siete=False
         ocho=False
         nueve=False
         multi=False
      elif v.get()==4:
         tres=False
         cuatro=False
         cinco=False
         seis=True
         siete=False
         ocho=False
         nueve=False
         multi=False
      elif v.get()==5:
         tres=False
         cuatro=False
         cinco=False
         seis=False
         siete=True
         ocho=False
         nueve=False
         multi=False
      elif v.get()==6:
         tres=False
         cuatro=False
         cinco=False
         seis=False
         siete=False
         ocho=True
         nueve=False
         multi=False
      elif v.get()==7:
         tres=False
         cuatro=False
         cinco=False
         seis=False
         siete=False
         ocho=False
         nueve=True
         multi=False
      elif v.get()==8:
         tres=True
         cuatro=False
         cinco=False
         seis=False
         siete=False
         ocho=False
         nueve=False
         multi=True
    tam=Label(con,text="Tamaño")
    tam.grid(row=0,column=1,sticky=W,padx=10,pady=4)
    radio9=Radiobutton(con,text="3x3",variable=v,command=eleccion4(),value=1)
    radio9.grid(row=0,column=2,sticky=W,padx=10,pady=4)
    radio10=Radiobutton(con,text="4x4",variable=v,command=eleccion4(),value=2)
    radio10.grid(row=1,column=2,sticky=W,padx=10,pady=4)
    radio11=Radiobutton(con,text="5x5",variable=v,command=eleccion4(),value=3)
    radio11.grid(row=2,column=2,sticky=W,padx=10,pady=4)
    radio12=Radiobutton(con,text="6x6",variable=v,command=eleccion4(),value=4)
    radio12.grid(row=3,column=2,sticky=W,padx=10,pady=4)
    radio13=Radiobutton(con,text="7x7",variable=v,command=eleccion4(),value=5)
    radio13.grid(row=4,column=2,sticky=W,padx=10,pady=4)
    radio14=Radiobutton(con,text="8x8",variable=v,command=eleccion4(),value=6)
    radio14.grid(row=5,column=2,sticky=W,padx=10,pady=4)
    radio15=Radiobutton(con,text="9x9",variable=v,command=eleccion4(),value=7)
    radio15.grid(row=6,column=2,sticky=W,padx=10,pady=4)
    radio16=Radiobutton(con,text="Multitamaño",variable=v,command=eleccion4(),value=8)
    radio16.grid(row=7,column=2,sticky=W,padx=10,pady=4)
    niv=Label(con,text="Level")
    niv.grid(row=8,column=1,sticky=W,padx=10,pady=4)
    radio1=Radiobutton(con,text="Easy",variable=v1,command=eleccion1(),value=1)
    radio1.grid(row=8,column=2,sticky=W,padx=10,pady=4)
    radio2=Radiobutton(con,text="Normal",variable=v1,command=eleccion1(),value=2)
    radio2.grid(row=9,column=2,sticky=W,padx=10,pady=4)
    radio3=Radiobutton(con,text="Dificult",variable=v1,command=eleccion1(),value=3)
    radio3.grid(row=10,column=2,sticky=W,padx=10,pady=4)
    rel=Label(con,text="Time")
    rel.grid(row=11,column=1,sticky=W,padx=10,pady=4)
    radio4=Radiobutton(con,text="Yes",variable=v2,command=eleccion2(),value=1)
    radio4.grid(row=11,column=2,sticky=W,padx=10,pady=4)
    radio5=Radiobutton(con,text="No",variable=v2,command=eleccion2(),value=2)
    radio5.grid(row=12,column=2,sticky=W,padx=10,pady=4)
    radio6=Radiobutton(con,text="Timer",variable=v2,command=eleccion2(),value=3)
    radio6.grid(row=13,column=2,sticky=W,padx=10,pady=4)
    sound=Label(con,text="Sound")
    sound.grid(row=14,column=1,sticky=W,padx=10,pady=4)
    radio7=Radiobutton(con,text="Yes",variable=v3,command=eleccion3(),value=1)
    radio7.grid(row=14,column=2,sticky=W,padx=10,pady=4)
    radio8=Radiobutton(con,text="No",variable=v3,command=eleccion3(),value=2)
    radio8.grid(row=15,column=2,sticky=W,padx=10,pady=4)
    def back():
        root.deiconify()
        con.withdraw()
    button=Button(con,text="Back",bg="red",width=6,command=back)
    button.grid(row=16,column=1)
    button=Button(con,text="Confirm",bg="lightgreen",width=6,command=config)
    button.grid(row=16,column=2)
def message():
   messagebox.showinfo("About...","Kenken \nVersion: 1.0 \nFecha:15/10/18 \nAutores: Adrian Rodriguez Castro \n               Jenaro Murillo Aldecoba")
root = tk.Tk()
w = Canvas(root, 
           width=canvas_width, 
           height=canvas_height)
w.pack(expand = YES, fill = BOTH)
w.bind( "<B1-Motion>", paint )
menubar = Menu(root)
ponderadomenu = Menu(menubar, tearoff=0)
ponderadomenu.add_command(label="Play",command=nombre)
ponderadomenu.add_separator()
ponderadomenu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="Play", menu=ponderadomenu)
cronomenu=Menu(menubar, tearoff=0)
cronomenu.add_command(label="Start",command=config)
cronomenu.add_separator()
cronomenu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="Config", menu=cronomenu)
aboutmenu = Menu(menubar, tearoff=0)
aboutmenu.add_command(label="About...",command=message)
menubar.add_cascade(label="About", menu=aboutmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index",command=Manual)
menubar.add_cascade(label="Help", menu=helpmenu)
root.title("Menu")
root.config(menu=menubar)
root.mainloop()

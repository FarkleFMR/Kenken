import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
import random
cont=0
seg=0
minu=0
hor=0
stop=False
f=None
cargar=False
p=None
listaf=[]
listai=[]
listad=[]
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
    e37=Entry(nom)
    e37.grid(row=1,column=4)
    def play():
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
        global listaf
        global listai
        global listad
        pl=tk.Tk()
        nom.withdraw()
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
        def savear():
           global cont
           global seg
           global minu
           global hor
           esta=open("juegos.dat","w")
           result=[]
           print(matriz)
           for i in range(len( matriz)-1):
              for j in range(len(matriz[0])-1):
                 
                 
                 
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
            global listaf
            global listai
            global listad
            if facil:
                listaf.remove(p)
                pl.destroy()
                play()
            elif normal:
                listai.remove(p)
                pl.destroy()
                play()
            else:
                listad.remove(p)
                pl.destroy()
                play()
        
        def comprobar():
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
                if vaarios=="X":
                    for l in comprolinea:
                        resultmilt*=l
                    
                    
                    if resultmilt!=int(varia):
                        messagebox.showerror("Error", "Solucion incorrecta en las casillas")
                    comprolinea=[]
                    resultmilt=1
                        
                        
                        
                    
                elif vaarios=="+":
                    for l in comprolinea:
                        
                        result+=l
                    if result!=int(varia):
                        messagebox.showerror("Error", "Solucion incorrecta en las casillas")

                    comprolinea=[]
                    result=0
                            
                            
                elif vaarios=="-":
                    for l in comprolinea:
                        
                        result=abs(result-l)
                    print(result)
                    if result!=int(varia):
                        messagebox.showerror("Error", "Solucion incorrecta en las casillas")
                    comprolinea=[]
                    result=0
                elif vaarios=="/":
                    for l in range(len(comprolinea)-1):
                        comprolinea.remove(vardiv)
                        vardiv=vardiv//min(comprolinea)
                        comprolinea.remove(min(comprolinea))
                    
                    if vardiv!=int(varia):
                        messagebox.showerror("Error", "Solucion incorrecta en las casillas")
                        
                    
                    comprolinea=[]    
                else:
                    if int(varia)!=comprolinea[0]:
                        messagebox.showerror("Error", "Solucion incorrecta en las casillas")
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
                        break
                    else:
                        l1+=[bar]
                l1=[]

            messagebox.showinfo("Enhorabuena", "Solucion lograda")
            nombres=e37.get()
            r=open("Top 10.txt","r")
            
            nuv=r.read()
            r.close()
            
            r=open("Top 10.txt","w")
            r.write(nuv+" "+nombres)
            r.close()
                        
                    
                        
                
                    
                    
                
            
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
        if cargar:
           try:
              
              esta=open("juegos.dat","r")
              esta2=esta.read()
              esta2=eval(esta2)
              cont=0
              for i in range(len(matriz)-1):
                 for j in range(len(matriz[0])-1):
                    a=matriz[i][j]
                    a.insert (0,esta2[0][cont])
                    cont+=1
              esta.close()
           except:
              pl.withdraw()
              messagebox.showerror("Error", "No existen juegos guardados")
              pl.deiconify()

             
              
        if f is None:
            
            f = open("kenken_juegos.dat")
            f2=f.readlines()
            print(len(f2))
            for i in range(len(f2)):
                if f2[i][0]=="F":
                    listaf+=[eval(f2[i][1:])]
                elif f2[i][0]=="I":
                    listai+=[eval(f2[i][1:])]
                else:
                    listad+=[eval(f2[i][1:])]
        
        if facil is True:
            if listaf == []:
                p=[]
                messagebox.showerror("Error", "No existen niveles en la dificultad facil")
                pl.withdraw()
                root.deiconify()
            else:
                print(cargar)
                if cargar:
                   p=p
                else:
                   p=listaf[random.randint(0,len(listaf)-1)]
                #print(listaf)
                print(p)
        elif normal is True:
            if listai == []:
                p=[]
                messagebox.showerror("Error", "No existen niveles en la dificultad intermedio")
                pl.withdraw()
                root.deiconify()
            else:
                 if cargar:
                   p=p
                 else:
                    p=listai[random.randint(0,len(listai)-1)]
        else:
            if listad == []:
                p=[]
                messagebox.showerror("Error", "No existen niveles en la dificultad dificil")
                pl.withdraw()
                root.deiconify()
            else:
                 if cargar:
                   p=p
                 else:
                    p=listad[random.randint(0,len(listad)-1)]
        row=1
        cargar=False
        
        for e in p:
            rules=tk.Label(pl,text=(e,"-",p[e]))
            rules.grid(row=row,column=7)
            row+=1
        def  insertar1():
            casilla=tk.Entry(pl)
            lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36]
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
            casilla=tk.Entry(pl)
            lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36]
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
            casilla=tk.Entry(pl)
            lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36]
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
            casilla=tk.Entry(pl)
            lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36]
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
            casilla=tk.Entry(pl)
            lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36]
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
            casilla=tk.Entry(pl)
            lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36]
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
            casilla=tk.Entry(pl)
            lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36]
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
            casilla=tk.Entry(pl)
            lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36]
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
            casilla=tk.Entry(pl)
            lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36]
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
            casilla=tk.Entry(pl)
            lista=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36]
            
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
               


               button1.grid(row=7,column=1)
               button2.grid(row=7,column=2)
               button3.grid(row=7,column=3)
               button4.grid(row=8,column=1)
               button5.grid(row=8,column=2)
               button6.grid(row=8,column=3)
               button7.grid(row=9,column=1)
               button8.grid(row=9,column=2)
               button9.grid(row=9,column=3)
               button10.grid(row=8,column=4,columnspan=3)

               
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
               
               button1.grid(row=7,column=1)
               button2.grid(row=7,column=2)
               button3.grid(row=7,column=3)
               button4.grid(row=8,column=1)
               button5.grid(row=8,column=2)
               button6.grid(row=8,column=3)
               button7.grid(row=9,column=1)
               button8.grid(row=9,column=2)
               button9.grid(row=9,column=3)
               button10.grid(row=8,column=4,columnspan=3)
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
        button12.grid(row=10, column=1,columnspan=3, sticky=W,  padx=10,pady=4)
        button14 =Button(pl, text='Change game',bg="lightblue",width=10,command=Nuevo_juego)
        button14.grid(row=10,column=4,columnspan=3, sticky=W,padx=10,pady=4)
        button15 = tk.Button(pl, text="comprobar",width=9,height=1,command=comprobar)
        button15.grid(row=9,column=4,columnspan=3)
        button16=Button(pl, text='Completed',bg="lightblue",width=10,command=Top_ten)
        button16.grid(row=11,column=4,columnspan=3)
        button17=Button(pl, text='cargar',bg="yellow",width=10,command=cargarsh)
        button17.grid(row=12,column=4,columnspan=3)
        

        
        if e37.get()=="":
            messagebox.showerror("Error", "Debe poner su nombre")
            pl.withdraw()
            nombre()
        nombr=Label(pl,text=("Name:",e37.get()))
        nombr.grid(row=13,column=1,columnspan=3)
        if facil==True:
            niv=Label(pl,text="Level:Easy")
            niv.grid(row=13,column=4,columnspan=3)
        elif normal==True:
            niv=Label(pl,text="Level:Normal")
            niv.grid(row=13,column=4,columnspan=3)
        elif dificil==True:
            niv=Label(pl,text="Level:Dificult")
            niv.grid(row=13,column=4,columnspan=3)
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
        if v.get()==1:
            facil=True
            normal=False
            dificil=False
        elif v.get()==2:
            facil=False
            normal=True
            dificil=False
        elif v.get()==3:
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
         tres=False
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

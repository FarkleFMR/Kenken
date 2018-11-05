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

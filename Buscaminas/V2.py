#Buscaminas

import random

play=1

print "BUSCAMINAS"
print "----------"
print "1-Principiante"
print "2-Intermedio"
print "3-Experto "
print "4-Leer de fichero "
print "5-Salir"

modo=int(input())
while (modo<1 or modo >5):
    modo=int(input("Introduzca un modo valido, por favor"))

print("En pruebas, solo funciona 1 y 2 ")

if (modo==1):
    size=9
elif (modo==2):
    size=16
else:
    size=0

matriz=[]
for i in range(size):
    matriz.append([])
    for j in range(size):
        matriz[i].append(u'\u2593')

oculta=[]
for i in range(size):
    oculta.append([])
    for j in range(size):
        mina=random.randint(1,10)
        if mina%5==0:
            mina=1
        else:
            mina=0
        oculta[i].append(mina)


for i in range(size):
    for j in range(size):
        if (i%2==0):
            salto=3
        else:
            salto=1

        if (j==0):
            print (salto*(" "))+matriz[i][j]+" ",
        else:
            print matriz[i][j]+" ",
    print "\n"
    
dic={}
for i in range(size):
    for j in range(size):
        pos=i*10+j
        dic.update({pos:oculta[i][j]})

accion=0
print "Elija una accion  \n"
print "1-Marcar"
print "2-Abrir \n"

accion=int(input())
while(accion<1 or accion>2):
    accion=int(input("Introduzca un valor correcto \n"))

if(accion==1):
    #MARCAR
    a=int(input("Posicion i: \n"))
    b=int(input("Posicion j: \n"))

    matriz[a][b]='X'
else:
    #ABRIR
    a=int(input("Posicion i: \n"))
    b=int(input("Posicion j: \n"))
    matriz[a][b]=dic[a*10+b]



for i in range(size):
    for j in range(size):
        if (i%2==0):
            salto=3
        else:
            salto=1

        if (j==0):
            if type(matriz[i][j]) == int:
                print (salto*(" "))+str(matriz[i][j])+" ",
            else:
                print (salto*(" "))+matriz[i][j]+" ",
        else:
            if type(matriz[i][j])==int:
                print str(matriz[i][j])+" ",
            else:
                print matriz[i][j]+" ",
    print "\n"


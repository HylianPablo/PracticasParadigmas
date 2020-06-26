#Buscaminas

import random
import sys

play=1

while (play==1):


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

    print("En pruebas, solo funciona 1 y 2 \n ")

    if (modo==1):
        size=9
        minas=10
    elif (modo==2):
        size=16
        minas=40
    else:
        sys.exit("Gracias por jugar")
        play-=1
        size=0
    


    #Tablero con las casillas tapadas
    matriz=[]
    for i in range(size):
        matriz.append([])
        for j in range(size):
            matriz[i].append(u'\u2593')


    #Tablero con las minas, alertas de minas...
    oculta=[]
    minas=minas*5
    for i in range(size):
        oculta.append([])
        for j in range(size):
            if minas>0:
                mina=random.randint(1,10)
                minas-=1
                if mina%5==0:
                    mina=1
                else:
                    mina=0
                oculta[i].append(mina)
            else:
                mina=0
                oculta[i].append(mina)

    #Esta funcion esta modificada y donde pone oculta deberia poner matriz

    def ImprimirTablero():
        for i in range(size):
            for j in range(size):
                if (i%2==0):
                    salto=3
                else:
                    salto=1
                if (j==0):
                    if type(oculta[i][j]) == int:
                        print (salto*(" "))+str(oculta[i][j])+" ",
                    else:
                        print (salto*(" "))+oculta[i][j]+" ",
                else:
                    if type(oculta[i][j])==int:
                        print str(oculta[i][j])+" ",
                    else:
                        print oculta[i][j]+" ",
            print "\n"
        return

    ImprimirTablero()

    
    dic={}
    for i in range(size):
        for j in range(size):
            pos=i*10+j
            dic.update({pos:oculta[i][j]})

    filas={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25,'@':26,'#':27,'$':28,'%':29,'&':30}

    def CambiaCaracteres(char,dic):
        print dic[char]
        return

    def Alrededor(i,j,oculta):
        cont=0
        cont+=oculta[i-1][j]
        cont+=oculta[i-1][j+1]
        cont+=oculta[i][j-1]
        cont+=oculta[i][j+1]
        cont+=oculta[i+1][j]
        cont+=oculta[i+1][j+1]
        return cont

    def Marcadas(i,j,oculta):
        cont=0
        if oculta[i-1][j]=='X':
            cont+=1
        if oculta[i-1][j]=='X':
            cont+=1
        if oculta[i-1][j+1]=='X':
            cont+=1
        if oculta[i][j-1]=='X':
            cont+=1
        if oculta[i][j+1]:
            cont+=1
        if oculta[i+1][j]:
            cont+=1
        if oculta[i+1][j+1]:
            cont+=1
        return cont

    columnas={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25,'=':26,'+':27,'-':28,':':29,'/':30}

    jugada=1

    while jugada==1:
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
            if matriz[a][b]==1:
                ImprimirTablero()
                sys.exit("Mina. Gracias por jugar \n")
            else:
                n=Alrededor(a,b,oculta)-Marcadas(a,b,matriz)
                if n==0:
                    matriz[a][b]=' '
                elif n<0:
                    matriz[a][b]='?'
                else:
                    matriz[a][b]=n
                



        ImprimirTablero()

        #Linea del while de los turnos a esta altura



    #*****Linea del while principal a esta altura*****
print "Gracias por jugar"

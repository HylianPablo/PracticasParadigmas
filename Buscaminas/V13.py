#Buscaminas

#IMPORTANTE Si al abrir sale 1, es que hay una ('1') mina cerca, no que haya mina y el programa funcione mal

import random
import time

play=1 #Variable que mantiene el juego abierto

while (play==1):


    print "BUSCAMINAS"
    print "----------"
    print "1-Principiante"
    print "2-Intermedio"
    print "3-Experto "
    print "4-Leer de fichero "
    print "5-Salir \n"
    
    
    modo=int(input())

    if modo!=5:
        while (modo<1 or modo >4):
            modo=int(input("Introduzca un modo valido, por favor"))

        if (modo==1):
            size1=9
            size2=9
            minas=10

        elif (modo==2):
            size1=16
            size2=16
            minas=40

        elif(modo==3):
            size1=16
            size2=30
            minas=99

        elif(modo==4):
            #request=raw_input("Introduzca el directorio del fichero \n")
            fich=open("mapa.txt")
            lins=fich.read().split('\n')
            size1=lins[0]
            size1=int(size1)
            size2=lins[1]
            size2=int(size2)
            
            #Pues se cuenta tambien el salto de linea FINAL como caracter

            oculta=[]       #Base para la matriz

            minas=0

            for i in range(size1+2):
                oculta.append([])
                for j in range(size2+2):
                        oculta[i].append(0)

            i=0
            j=0
            saltador=0
            minado=[]
            for linea in lins: #Tomamos cada linea en que hemos dividido el fichero leido 
                for digito in linea:
                    if saltador>1:
                        if digito=='*': #Si es '*', anexamos mina
                            minado.append(1)
                            minas+=1
                        else:
                            minado.append(0)
                saltador+=1
            
            cuentaminas=0
            for i in range(size1+2):
                for j in range(size2+2):
                    if i>1 and j>1:
                        oculta[i][j]=minado[cuentaminas]
                        cuentaminas+=1




            #print minado
            fich.close()

    

        minas2=minas            #Ayudara posteriormente a contar las minas


        tiempo=time.time()      #Tiempo al iniciar la partida

        #Funcion que nos permite cambiar caracteres a numeros
        def CambiaCaracteres(char,dic):
            cambio= dic[char]
            return cambio


        #Diccionario para cambiar letras a numeros en filas
        filas={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25,'@':26,'#':27,'$':28,'%':29,'&':30}

        #Diccionario para cambiar numeros a letras en filas
        filasINV={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z',26:'@',27:'#',28:'$',29:'%',30:'&'}

        #Diccionario para cambiar letras a numeros en columnas
        columnas={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25,'=':26,'+':27,'-':28,':':29,'/':30}

        #Diccionario para cambiar numeros a letras en filas
        columnasINV={0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z',26:'=',27:'+',28:'-',29:':',30:'/'}

        #Tablero con las casillas tapadas
        matriz=[]
        for i in range(size1+2):    #Rango +1 para el marco
            matriz.append([])
            for j in range(size2+2):
                matriz[i].append(u'\u2593')


        #Tablero con las minas, alertas de minas...
        if modo!=4:
            oculta=[]
            for i in range(size1+2):
                oculta.append([])
                for j in range(size2+2):
                    mina=random.randint(1,10)
                    #La variable equi sirve para controlar la probabilidad de minas
                    #equi=random.randint(1,5)
                    if i==0 or j==0 or i==size1+2 or j==size2+2:
                        oculta[i].append(0)
                    if (mina%7==0 and minas>0 and i!=0 and j!=0 ):   #Estas condiciones sirven para que la probabilidad no sea alta y las minas esten repartidas
                        oculta[i].append(1)
                        minas=minas-1
                    else:
                        oculta[i].append(0)
        if modo!=4:
            while minas>0:      #Si no se han generado minas suficientes se repite la accion, en bucle aparte, pues en el primero se genera la matriz
                for i in range(size1+2):
                    for j in range(size2+2):
                        if oculta[i][j]!=1 and i!=0 and j!=0:
                            mina=random.randint(1,10)
                            #equi=random.randint(1,5)
                            if(mina%7==0 and minas>0 ):
                                oculta[i][j]=1
                                minas=minas-1

    
         

        #Esta funcion define el tablero y como debe imprimirse

        def ImprimirTablero():      #Donde pone oculta deberai poner matriz
                                    #Se van a desplazar solamente las filas pares
                                    #El primer termino de cada fila se desplaza, los siguientes no, de esta forma queda mas ordenado
            print '\n',
            print ' '+u'\u250C' + (3*u'\u2500') + u'\u252C'+ ((size2-2)*((3*u'\u2500')+u'\u252C'))+ (3*u'\u2500')+u'\u2510',
            print '\n',
            

            for i in range(size1):
                if (i%2==1):
                    salto=3
                else:
                    salto=1
                for j in range(size2):
                    print (salto*(" "))+u'\u2502'+' '+ matriz[i][j]if(j==0) else(u'\u2502'+' '+matriz[i][j]),
                print u'\u2502',

                print '\n',
                if i==(size1-1):
                    print (' '+u'\u2514'+(size2-1)*(3*u'\u2500'+u'\u2534')+3*(u'\u2500')+u'\u2518')
                elif(i%2==0):
                    print ((' '+u'\u2514'+size2*(u'\u2500'+u'\u252C'+u'\u2500'+u'\u2534')+u'\u2500'+u'\u2510'))
                else:
                    print ((' '+u'\u250C'+size2*(u'\u2500'+u'\u2534'+u'\u2500'+u'\u252C')+u'\u2500'+u'\u2518'))


            return

        ImprimirTablero()

        def AbreTablero(matriz,oculta):  #Muestra todo el tablero SIN MARCO al perder o ganar una partida
            for i in range(1,size1+2):
                for j in range(1,size2+2):
                    if i%2==0:
                        salto=3
                    else:
                        salto=1
                    if matriz[i][j]=='X':
                        oculta[i][j]='#'
                    else:
                        if oculta[i][j]==1:
                            oculta[i][j]='*'
                        else:
                            oculta[i][j]=0

                    if j==1:
                        print (salto*(" "))+str(oculta[i][j])+" ",
                    else:
                        print str(oculta[i][j])+" ",
                print "\n"
            return
    
        
        #Diccionario para marcar o abrir una celda
        eleccion={'!':1,'*':2}

        #HAY QUE DEFINIR ESTAS DOS FUNCIONES EN LOS BORDES

        #Funcion que cuenta las minas alrededor de una casilla
        def Alrededor(i,j,oculta):
            cont=0
            if j%2!=0:
                cont+=oculta[i-1][j]
                cont+=oculta[i][j-1]
                cont+=oculta[i][j+1]
                cont+=oculta[i+1][j]
                cont+=oculta[i+1][j+1]
                cont+=oculta[i+1][j-1]
            else:
                cont+=oculta[i+1][j]
                cont+=oculta[i][j+1]
                cont+=oculta[i][j-1]
                cont+=oculta[i-1][j]
                cont+=oculta[i-1][j+1]
                cont+=oculta[i-1][j-1]
                
            return cont
        
        #Funcion que cuenta las casillas marcadas alrededor de una casilla
        def Marcadas(i,j,oculta):
            cont=0
            if j%2!=0:
                if matriz[i-1][j]=='X':
                    cont+=1
                if matriz[i][j-1]=='X':
                    cont+=1
                if matriz[i][j+1]=='X':
                    cont+=1
                if matriz[i+1][j]=='X':
                    cont+=1
                if matriz[i+1][j+1]=='X':
                    cont+=1
                if matriz[i+1][j-1]=='X':
                    cont+=1
            else:
                if matriz[i+1][j]=='X':
                    cont+=1
                if matriz[i][j+1]=='X':
                    cont+=1
                if matriz[i][j-1]=='X':
                    cont+=1
                if matriz[i-1][j]=='X':
                    cont+=1
                if matriz[i-1][j+1]=='X':
                    cont+=1
                if matriz[i-1][j-1]=='X':
                    cont+=1
            return cont

        def Numero(n):
            if n==0:
                return ' '
            elif n<0:
                return '?'
            else:
                return n

        def Actualizar(i,j,matriz,n):
            if j%2!=0:
                if matriz[i][j]!=u'\u2593':
                    matriz[i][j]=Numero(n)

                if matriz[i-1][j]!=u'\u2593':
                    matriz[i-1][j]=Numero(n)

                if matriz[i][j-1]!=u'\u2593':
                    matriz[i][j-1]=Numero(n)

                if matriz[i][j+1]!=u'\u2593':
                    matriz[i][j+1]=Numero(n)

                if matriz[i+1][j]!=u'\u2593':
                    matriz[i+1][j]=Numero(n)

                if matriz[i+1][j-1]!=u'\u2593':
                    matriz[i+1][j-1]=Numero(n)

                if matriz[i+1][j+1]!=u'\u2593':
                    matriz[i+1][j+1]=Numero(n)
            else:

                if matriz[i][j]!=u'\u2593':
                    matriz[i][j]=Numero(n)

                if matriz[i+1][j]!=u'\u2593':
                    matriz[i+1][j]=Numero(n)

                if matriz[i][j+1]!=u'\u2593':
                    matriz[i][j+1]=Numero(n)

                if matriz[i][j-1]!=u'\u2593':
                    matriz[i][j-1]=Numero(n)

                if matriz[i-1][j]!=u'\u2593':
                    matriz[i-1][j]=Numero(n)

                if matriz[i-1][j+1]!=u'\u2593':
                    matriz[i-1][j+1]=Numero(n)

                if matriz[i-1][j-1]!=u'\u2593':
                    matriz[i-1][j-1]=Numero(n)
            return

                    



        def Borra6(i,j,matriz,oculta): #Abre 6 y cuenta si hay minas
            cont=0
            matriz[i][j]=oculta[i][j]
            cont+=matriz[i][j]

            matriz[i-1][j]=oculta[i-1][j]
            cont+=matriz[i-1][j]

            matriz[i-1][j+1]=oculta[i-1][j+1]
            cont+=matriz[i-1][j+1]

            matriz[i][j-1]=oculta[i][j-1]
            cont+=matriz[i][j-1]

            matriz[i][j+1]=oculta[i][j+1]
            cont+=matriz[i][j+1]

            matriz[i+1][j]=oculta[i+1][j]
            cont+=matriz[i+1][j]

            matriz[i+1][j+1]=oculta[i+1][j+1]
            cont+=matriz[i+1][j+1]
            return cont


        #Bucle para introducir las jugadas
        jugada=1
        #tiempo1=0

        horas1=0
        minutos1=0
        segundos1=0

        marcadas=0
        while jugada==1:
            
            horas=0
            minutos=0
            segundos=0


            tiempoJugada=time.time()        #En cada turno se resta el tiempo actual cuando se inicio el programa y el actual de la jugada
            tiempoJugada=tiempoJugada-tiempo

            minutos=tiempoJugada/60         #Posteriormente se pasa a HH/MM/SS
            segundos=tiempoJugada%60
            horas=minutos/60
            minutos=minutos%60

            tiempoJugada=str("%02d:%02d:%02d"%(horas,minutos,segundos))

            print("Introduzca las ordenes como fila//columna//accion \n")
            print "MINAS RESTANTES : "+str(minas2)+ "\n"
            print "MARCADAS : "+str(marcadas)+"\n"
            print "TIEMPO TRANSCURRIDO : "+tiempoJugada+ "\n"

            ordenes=raw_input("Digame las ordenes \n")
            while (len(ordenes)<1) or (ordenes[2]!='*' and ordenes[2]!='!'):  #Validacion de entrada de datos
                print "ENTRADA ERRONEA \n"
                ordenes=raw_input("Digame las ordenes \n ")
            lon=len(ordenes)
            if ordenes[lon-1]!='!' and ordenes[lon-1]!='*':
                print "La ultima accion introducida es erronea y no se ha tomado en cuenta \n"

            count=0
            while count<lon:                        #Mientras no se alcance la longitud de la cadena de las ordenes
                for i in range(len(ordenes)):
                    count=count+1
                    if (ordenes[i]=='!') or (ordenes[i]=='*'):   #Si un punto de la cadena es ! o *, se toma una accion

                        miniorden1=ordenes[i-2] #Fila
                        miniorden2=ordenes[i-1] #Columna

                        miniorden33=ordenes[i] #Accion
                        miniorden3=CambiaCaracteres(miniorden33,eleccion) #Cambia ! con 1; y * con 2 // Luego se cambiaran las letras por numeros
                    
                        if(miniorden3==1):              
                            #MARCAR
                            A=CambiaCaracteres(miniorden1,filas)
                            #Sumamos 1 para que no toque el marco
                            A+=1
                            B=CambiaCaracteres(miniorden2,columnas)
                            B+=1
                            if matriz[A][B]!=0 and matriz[A][B]!='?':
                                if marcadas<minas2:
                                    if matriz[A][B]==u'\u2593':
                                        matriz[A][B]='X'
                                        marcadas+=1

                                        alrededor=Alrededor(A,B,oculta)
                                        marcadas=Marcadas(A,B,oculta)       #Vuelve a comprobar las minas, contando que al marcar una, resta 1 a las posibilidades de mina de alrededor
                                        n=alrededor-marcadas
                                        n=n-1
                                        n=Numero(n)
                                        Actualizar(A,B,matriz,n)

                                    else:
                                        matriz[A][B]=u'\u2593'
                                        marcadas-=1
                                else:
                                    print "NO SE PUEDEN MARCAR MAS CELDAS QUE MINAS \n"
                            else:
                                print "NO SE PUEDEN MARCAR CELDAS ABIERTAS \n"



                        else:
                            #ABRIR
                            A=CambiaCaracteres(miniorden1,filas)
                            A+=1
                            #Sumamos 1 para que no toque el marco
                            B=CambiaCaracteres(miniorden2,columnas)
                            B+=1
                            if matriz[A][B]!='X':  #Si la celda no esta marcada
                                if oculta[A][B]==1:
                                    jugada=0
                                    print "MINA --  FIN DEL JUEGO \n"
                                    print " \n"
                                    AbreTablero(matriz,oculta)
                                else:
                                    n=Alrededor(A,B,oculta)-Marcadas(A,B,matriz)
                                    if matriz[A][B]!= u'\u2593':  #Para abrir 6, abrir una abierta
                                        if n<=0:
                                            fin1=Borra6(A,B,matriz,oculta)
                                            if fin1>=1:  #Si fin1 es igual o mayor que 1, quiere decir que al abrir 6 hemos encontrado 1 o mas minas
                                                jugada=0
                                                print "MINA -- FIN DEL JUEGO \n"
                                                print "\n"
                                                AbreTablero(matriz,oculta)
                                        else:
                                            print "CELDA YA ABIERTA. NO SE PUEDEN ABRIR LAS CELDAS VECINAS POR NUMERO INSUFICIENTE DE MARCAS \n"
                                    else:
                                        matriz[A][B]=Numero(n)
                            else:
                                print "NO SE PUEDE ABRIR UNA CELDA MARCADA  \n"
                if jugada==1:
                    ImprimirTablero()
    
                



        #Linea del while de los turnos a esta altura


    else:
        play=0
    #*****Linea del while principal a esta altura*****
print "Gracias por jugar \n"

#Buscaminas

import random
import sys     #NO SE PUEDE USAR SYS, CAMBIAR

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

        print("En pruebas, solo funciona 1 y 2 \n ")

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
            request=raw_input("Introduzca el directorio del fichero \n")
            fich=open(request)
            lins=fich.read().split('\n')
            size1=(len(lins))-1 #Pues se cuenta tambien el salto de linea como caracter
            size2=0
            for i in lins:
                size2+=1
            size2-=1          #Pues se cuenta tambien el salto de linea FINAL como caracter

            oculta=[]
            minas=0
            i=-1
            j=0

            for linea in lins:  #Utilizamos la linea anterior para coger cada linea del fichero
                oculta.append([])
                i+=1
                j=0
                for digito in linea:
                    if digito!=' ' and digito!='\n': #Si no es un espacio en blanco, anexamos el digito a la matriz
                        oculta[i].append(int(digito))
                        if oculta[i][j]==1:
                            minas+=1
                        j+=1


            fich.close()

        else:
            sys.exit("Gracias por jugar")
            play-=1
            size=0
    


        minas2=minas

        #Tablero con las casillas tapadas
        matriz=[]
        for i in range(size1):
            matriz.append([])
            for j in range(size2):
                matriz[i].append(u'\u2593')


        #Tablero con las minas, alertas de minas...
        if modo!=4:
            oculta=[]
            for i in range(size1):
                oculta.append([])
                for j in range(size2):
                    mina=random.randint(1,10)
                    #La variable equi sirve para controlar la probabilidad de minas
                    equi=random.randint(1,5)
                    if (mina%5==0 and minas>0 and  equi!=3):   #Estas condiciones sirven para que la probabilidad no sea alta y las minas esten repartidas
                        oculta[i].append(1)
                        minas=minas-1
                    else:
                        oculta[i].append(0)
    
            

        #Esta funcion define el tablero y como debe imprimirse

        def ImprimirTablero():
            for i in range(size1):
                for j in range(size2):
                    if (i%2==0):                                #Se van a desplazar solamente las filas pares
                        salto=3
                    else:
                        salto=1
                    if (j==0):                                  #El primer termino de cada fila se desplaza, los siguientes no, de esta forma queda mas ordenado
                        if type(matriz[i][j]) == int:
                            print (salto*(" "))+str(matriz[i][j])+" ",      #Como el caracter puede ser numerico o simbolo, se transforme en string con srt() segun convenga
                        else:
                            print (salto*(" "))+matriz[i][j]+" ",
                    else:                                       #No se desplaza
                        if type(matriz[i][j])==int:
                            print str(matriz[i][j])+" ",
                        else:
                            print matriz[i][j]+" ",
                print "\n"
            return

        ImprimirTablero()

        def AbreTablero():
            for i in range(size1):
                for j in range(size2):
                    if (i%2==0):
                        salto=3
                    else:
                        salto=1
                    if(j==0):
                        print (salto*(" "))+str(oculta[i][j])+" ",
                    else:
                        print str(oculta[i][j])+" ",
                print "\n"
            return

    
        dic={}   #Este diccionario guarda las posiciones de la matriz oculta
        for i in range(size1):
            for j in range(size2):
                pos=i*10+j
                dic.update({pos:oculta[i][j]})


        #Diccionario para cambiar letras a numeros en filas
        filas={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25,'@':26,'#':27,'$':28,'%':29,'&':30}


        #Funcion que nos permite cambiar caracteres a numeros
        def CambiaCaracteres(char,dic):
            cambio= dic[char]
            return cambio
        
        #Diccionario para marcar o abrir una celda
        eleccion={'!':1,'*':2}

        #Funcion que cuenta las minas alrededor de una casilla
        def Alrededor(i,j,oculta):
            cont=0
            cont+=oculta[i-1][j]
            cont+=oculta[i-1][j+1]
            cont+=oculta[i][j-1]
            cont+=oculta[i][j+1]
            cont+=oculta[i+1][j]
            cont+=oculta[i+1][j+1]
            return cont
        
        #Funcion que cuenta las casillas marcadas alrededor de una casilla
        def Marcadas(i,j,oculta):
            cont=0
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

        def Borra6(i,j,matriz,oculta):
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


        #Diccionario para cambiar letras a numeros en columnas
        columnas={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25,'=':26,'+':27,'-':28,':':29,'/':30}

        #Bucle para introducir las jugadas
        jugada=1

        marcadas=0
        while jugada==1:
            
            print("Introduzca las ordenes como fila//columna//accion \n")
            print "MINAS RESTANTES : "+str(minas2)+ "\n"
            print "MARCADAS : "+str(marcadas)+"\n"
            #TIEMPO TRANSCURRIDO

            ordenes=raw_input("Digame las ordenes \n")
            while (len(ordenes)<1) or (ordenes[2]!='*' and ordenes[2]!='!'):  #Validacion de entrada de datos
                print "ENTRADA ERRONEA \n"
                ordenes=raw_input("Digame las ordenes \n ")

            count=0
            lon=len(ordenes)
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
                            B=CambiaCaracteres(miniorden2,columnas)
                            if matriz[A][B]!=0 and matriz[A][B]!='?':
                                if marcadas<minas2:
                                    if matriz[A][B]==u'\u2593':
                                        matriz[A][B]='X'
                                        marcadas+=1
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
                            B=CambiaCaracteres(miniorden2,columnas)
                            if matriz[A][B]!='X':
                                if matriz[A][B]==1:
                                    jugada=0
                                    print "MINA --  FIN DEL JUEGO \n"
                                    print " \n"
                                else:
                                    n=Alrededor(A,B,oculta)-Marcadas(A,B,matriz)
                                    if matriz[A][B]!= u'\u2593':
                                        if n<=0:
                                            fin1=Borra6(A,B,matriz,oculta)
                                            if fin1>=1:
                                                jugada=0
                                                print "MINA -- FIN DEL JUEGO \n"
                                                print "\n"
                                                AbreTablero()
                                        else:
                                            print "CELDA YA ABIERTA. NO SE PUEDEN ABRIR LAS CELDAS VECINAS POR NUMERO INSUFICIENTE DE MARCAS \n"
                                    else:
                                        if n==0:
                                            matriz[A][B]=' '
                                        elif n<0 and oculta[A][B]!=1:
                                            matriz[A][B]='?'
                                        else:
                                            matriz[A][B]=n
                            else:
                                print "NO SE PUEDE ABRIR UNA CELDA MARCADA  \n"
                if jugada==1:
                    ImprimirTablero()
                



        #Linea del while de los turnos a esta altura


    else:
        play=0
    #*****Linea del while principal a esta altura*****
print "Gracias por jugar \n"

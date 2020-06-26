#Moreno Calvo Angel
#Trigueros Vega Andres
import random
import time
cadena1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&'
cadena2 = 'abcdefghijklmnopqrstuvwxyz=+-:/'

COE  = u'\u2500' # ─
CNS  = u'\u2502' # │
CES  = u'\u250C' # ┌
CSO  = u'\u2510' # ┐
CNE  = u'\u2514' # └
CON  = u'\u2518' # ┘
COES = u'\u252C' # ┬
CNES = u'\u251C' # ├
CONS = u'\u2524' # ┤
CONE = u'\u2534' # ┴
CSOM = u'\u2593' # ▒

#'▓' si est cerrada y no marcada (celda sombreada)
#'X' si est cerrada y marcada
#' ' si est abierta y n = 0
#'?' si est abierta y n < 0 (se han marcado un número excesivo de celdas vecinas)
#El digito que indica n si esta abierta y n > 0


'''Al revelar el tablero (ya sea por explosión de mina o por finalizacion correcta) todas las celdas pasan
a estado abierto, y se pueden dar los siguientes estados adicionales:
'#' si esta abierta, marcada, y no contiene mina (marcado erroneo)
'*' si esta abierta, no marcada, y contiene mina (ausencia de marcado)
'''
class Celda:
    def __init__(self, bomba, ):
        self.delante = CSOM
        self.detras = bomba
        
        self.marcada = False
        self.cerrada = True


class Tablero:
    def __init__(self,mayusculas,minusculas,filas,columnas,bombas,):
        self.may = mayusculas
        self.min = minusculas
        self.tabla = [[ Celda(0) for i in range (columnas)]for j in range (filas)]
        self.cant_bombas = bombas
        self.bombas_restantes = bombas
        self.inicio = 0
        self.filas = filas
        self.columnas = columnas
        self.final = False


    def fuera_limites(self,fila,columna):
        return (fila<0 or fila > self.filas-1) or (columna < 0 or columna > self.columnas-1) 


    def bombas_alrededor(self, fila, columna):
        contador = 0
        if fila%2 == 0:
            rango = [(-1, -1),(-1, 0),(0, -1),(0, 1),(1, -1),(1, 0)]#par
        else:
            rango = [(-1, 1),(-1, 0),(0, -1),(0, 1),(1, 1),(1, 0)]#impar
        for a in range(len(rango)):#len(rango)
            if not self.fuera_limites(fila + rango[a][0], columna + rango[a][1]):
                if self.tabla[fila + rango[a][0]][columna + rango[a][1]].detras == '*':
                    contador+=1
                if self.tabla[fila + rango[a][0]][columna + rango[a][1]].marcada == True:
                    contador-=1
        if contador==0:
            return ' '
        elif contador<0:
            return '?'
        else:
            return str(contador)


    def comprobar_alrededor(self,fila,columna):
        if fila%2 == 0:
            rango = [(-1, -1),(-1, 0),(0, -1),(0, 1),(1, -1),(1, 0)]#par
        else:
            rango = [(-1, 1),(-1, 0),(0, -1),(0, 1),(1, 1),(1, 0)]#impar
        for a in range(len(rango)):#len(rango)
            if not self.fuera_limites(fila + rango[a][0],columna + rango[a][1]):
                if self.tabla[fila + rango[a][0]][columna + rango[a][1]].detras != '*':
                    self.tabla[fila + rango[a][0]][columna + rango[a][1]].detras = self.bombas_alrededor(fila + rango[a][0],columna + rango[a][1])
                if self.tabla[fila + rango[a][0]][columna + rango[a][1]].delante != CSOM and self.tabla[fila + rango[a][0]][columna + rango[a][1]].delante != 'x':
                    self.tabla[fila + rango[a][0]][columna + rango[a][1]].delante = self.tabla[fila + rango[a][0]][columna + rango[a][1]].detras

    
    def abrir_alrededor(self,fila,columna):
        self.tabla[fila][columna].delante = self.tabla[fila][columna].detras
        self.tabla[fila][columna].cerrada = False
        if self.tabla[fila][columna].delante == '*':
                            self.final = True
        if self.tabla[fila][columna].delante == ' ' or self.tabla[fila][columna].delante == '?':
            if fila%2 == 0:
                rango = [(-1, -1),(-1, 0),(0, -1),(0, 1),(1, -1),(1, 0)]#par
            else:
                rango = [(-1, 1),(-1, 0),(0, -1),(0, 1),(1, 1),(1, 0)]#impar
            for a in range(len(rango)):#len(rango)
                if not self.fuera_limites(fila + rango[a][0],columna + rango[a][1]):
                    if self.tabla[fila + rango[a][0]][columna + rango[a][1]].delante == CSOM :
                        
                        self.abrir_alrededor(fila + rango[a][0],columna + rango[a][1])

    
    def rellenar_bombas(self,filas,columnas,minas):
        minasA = 0
        while(minasA<minas):
            for i in range(filas):
                    for j in range(columnas):
                        if minasA<minas:
                            a = random.randint(0,filas*columnas-1)
                            if a == 0:
                                if self.tabla[i][j].detras == '*':
                                    minasA-=1
                                self.tabla[i][j].detras= '*'
                                minasA+=1
                            elif(self.tabla[i][j].detras != '*'):
                                self.tabla[i][j].detras= ' '


    def imprimir_bombas(self,filas,columnas):  
        print '   ',
        for a in range(columnas):
            print unichr(ord('a')+ a)+ '  ',
        print '\n',
        print '  ' + CES + (3 * COE) + COES + ((columnas-2)*((3 * COE) + COES)) + (3 * COE) + CSO,
        print '\n',
        for i in range(filas):
            for j in range(columnas):
                print (unichr(ord('A') + i) + ((3 if (i%2==1) else (1)) * (" "))+ CNS + ' ' + self.tabla[i][j].detras if (j== 0) else CNS + ' ' + self.tabla[i][j].detras),
            print CNS,
            print '\n',
            if i==filas-1:
                print ('  ' + CNE + (columnas-1)*(3*COE + CONE) + 3*(COE) + CON)
            elif (i%2==0):
                print (('  ' + CNE + (columnas)*(COE + COES + COE + CONE) + COE + CSO))
            else:
                print (('  ' + CES + (columnas)*(COE + CONE + COE + COES) + COE + CON))


    def imprimir_tablero(self,filas,columnas):
        print 'Bombas restantes: ' + str(self.bombas_restantes)
        print 'Tiempo jugando: ' + str(time.time () - self.inicio)
        print '   ',
        for a in range(columnas):
            print unichr(ord('a')+ a)+ '  ',
        print '\n',
        print '  ' + CES + (3 * COE) + COES + ((columnas-2)*((3 * COE) + COES)) + (3 * COE) + CSO,
        print '\n',
        for i in range(filas):
            for j in range(columnas):
                print (unichr(ord('A') + i) + ((3 if (i%2==1) else (1)) * (" "))+ CNS + ' ' + self.tabla[i][j].delante if (j== 0) else (CNS + ' ' + self.tabla[i][j].delante)),
            print CNS,
            print '\n',
            if i==filas-1:
                 print (3 if (i%2==1) else (1)) * (" ") +' '+ CNE + (columnas-1)*(3*COE + CONE) + 3*(COE) + CON
            elif (i%2==0):
                print (('  ' + CNE + (columnas)*(COE + COES + COE + CONE) + COE + CSO))
            else:
                print (('  ' + CES + (columnas)*(COE + CONE + COE + COES) + COE + CON))


    def movimiento(self,row,col,op): #evaluar situacion de alrededor(casos)
        if op == '!': #marcar
            if self.tabla[row][col].cerrada == False:
                print 'Movimiento no valido'
            elif self.tabla[row][col].marcada == True:
                
                self.tabla[row][col].delante = CSOM 
                self.bombas_restantes+=1
                self.tabla[row][col].marcada = False
                self.comprobar_alrededor(row,col)
            else:
                self.tabla[row][col].delante = 'x' 
                self.bombas_restantes-=1
                self.tabla[row][col].marcada = True
                self.comprobar_alrededor(row,col)
        if op == '*': #abrir
            if self.tabla[row][col].marcada == True:
                print 'Accion no valida'
            
            elif self.tabla[row][col].cerrada == False:
                self.abrir_alrededor(row,col)
            elif self.tabla[row][col].cerrada == True:
                self.tabla[row][col].delante = self.tabla[row][col].detras
                self.tabla[row][col].cerrada = False
                if self.tabla[row][col].delante == '*':
                    self.final = True

    def cerca_atras(self,filas,columnas):
        for i in range(filas):
            for j in range(columnas):
                if self.tabla[i][j].detras != '*':
                    self.tabla[i][j].detras = self.bombas_alrededor(i,j)


    def entrada(self): 
        jugada = ''
        jugada = raw_input("Indique celda y accion (! marcar, * abrir): ")
        jugada = jugada.replace(' ','')
        for a in range(len(jugada)/3):
            row = self.may.find(jugada[a*3])
            col = self.min.find(jugada[a*3+1])
            op = jugada[a*3+2]
            self.movimiento(row,col,op)

    def tablero_final(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                print self.tabla[i][j].marcada
                print(self.tabla[i][j].detras == '*')
                if (not self.tabla[i][j].marcada) and self.tabla[i][j].detras == '*':
                    self.tabla[i][j].delante = '*'
                elif self.tabla[i][j].marcada and self.tabla[i][j].detras != '*':
                    self.tabla[i][j].delante = '#'
                elif self.tabla[i][j].delante == 'x' and self.tabla[i][j].detras == '*':
                    self.tabla[i][j].delante = 'x'
                elif self.tabla[i][j].delante == '*':
                    self.tabla[i][j].delante = '*'
                else:
                    self.tabla[i][j].delante = ' '
    def todo_marcado(self):
        bandera = False
        contador = 0
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.tabla[i][j].marcada and self.tabla[i][j].detras == '*' :
                    contador+=1
                
                    

        
        if self.bombas_restantes ==0 and self.bombas_totales == contador:
            return True
        else:
            return False
#Buscaminas

def fichero(nfichero):
        columnas = filas = 0
        print nfichero
        f = open(nfichero)
        linea = list(f.readline())
        while linea[0]!= ' ':
            filas = int(str(filas)+str(linea[0]))
            linea.pop(0)
        linea.remove(' ')
        linea.remove('\n')
        for i in range(len(linea)):
            columnas = int(str(columnas)+linea[i])
        t.tabla = [[ Celda(0) for i in range (columnas)]for j in range (filas)]
        x = 0
        for i in range(filas):
            linea = f.readline()
            for j in range(columnas):
                if linea[j] == '*':
                    t.tabla[i][j].detras = '*'
                    x += 1
                else:
                    t.tabla[i][j].detras = ' '
        t.cantidad_bombas = x
        t.bombas_restantes = x
        f.close()
        return filas,columnas
def espacios(e):
    print e*('\n')
    return e

def jugar(filas,columnas):
    t.inicio = time.time()
    t.cerca_atras(filas,columnas)
    while (not t.final and not t.todo_marcado()) :
        espacios(70)
        t.imprimir_tablero(filas,columnas)
        t.entrada()
        
        
        #t.imprimir_tablero(filas,columnas)
    if t.final:
        print 'ha perdido la partida'
        t.tablero_final()
        t.imprimir_tablero(filas,columnas)
        
    else:
        print 'ha ganado!!!!'

partida =  True

modo=0

while(partida):
    bandera = True
    print "BUSCAMINAS"
    print "----------"
    print "1-Principiante (9x9, 10 minas)"
    print "2-Intermedio (16x16, 40 minas)"
    print "3-Experto (16x30, 99 minas)"
    print "4-Leer de fichero "
    print "5-Salir"
    while (bandera):
        try:
            modo=int(input("Introduzca el modo: "))
            bandera = False
        except:
            print 'no es un valor valido'
            bandera = True
    
        
    if (modo==1):
        filas=columnas=9
        minas = 10
        t = Tablero(cadena1,cadena2,filas,columnas,minas)
        t.rellenar_bombas(filas,columnas,minas)
        #t.imprimir_bombas(filas,columnas)
        jugar(filas,columnas)
    elif (modo==2):
        filas = columnas=16
        minas = 40
        t = Tablero(cadena1,cadena2,filas,columnas,minas)
        t.rellenar_bombas(filas,columnas,minas)
        
        jugar(filas,columnas)
    elif (modo == 3):
        filas, columnas, minas = 16,30,99
        t = Tablero(cadena1,cadena2,filas,columnas,minas)
        t.rellenar_bombas(filas,columnas,minas)
        t.imprimir_bombas(filas,columnas)
        jugar(filas,columnas)
    elif(modo == 4):
        print "Leer fichero"
        nfichero = raw_input('Escriba el nombre del fichero: ')
        t = Tablero(cadena1,cadena2,0,0,0)
        filas,columnas = fichero(nfichero)
        jugar(filas,columnas)
    elif(modo==5):
        partida = False
        exit

import random

class Celda:
    def __init__(self,mina):
        self.delante=u'\u2593'
        self.detras=mina

        self.marcada=False      #Inicialmente no esta marcada
        self.cerrada= True      #Inicialmente esta cerrada

class Tablero:
    def __init__(self,filas,columnas,minas):
        self.tabla=[[Celda(0) for i in range(columnas)]for j in range (filas)]
        self.minas=minas
        self.minas_restante=minas
        self.inicio=0
        self.filas=filas
        self.columnas=columnas
        self.final=False

    def fuera_limites(self,fila,columna):
        return (fila<0 or fila > self.filas-1) or (columna < 0 or columna >self.columnas-1)

    def rellenar_bombas(self,filas,columnas,minas):
        minasA=0
        while(minasA<minas):
            for i in range(filas):
                for j in range(columnas):
                    if minasA<minas:
                        a=random.randint(0,filas*columnas-1)
                        if a==0:
                            if self.tabla[i][j].detras=='*':
                                minasA-=1
                            self.tabla[i][j].detras='*'
                            minasA+=1
                        else:
                            if (self.tabla[i][j].detras != '*'):
                                self.tabla[i][j].detras=' '

    def imprimir(self,filas,columnas):
        for a in range(columnas):
            print ' ',
        print '\n',
        print '  '+ u'\u250C'+(3*u'\u2500')+u'\u252C'+((columnas-2)*((3*u'\u2500')+u'\u252C'))+(3*u'\u2500')+u'\u2510',
        print '\n',
        for i in range(filas):
            for j in range(columnas):
                print ' '+(3 if (i%2==1) else (1)) *(" ")+u'\u2502'+' '+self.tabla[i][j].delante if (j==0) else (u'\u2502'+' '+self.tabla[i][j].delante),
            print u'\u2502',
            print '\n',

            if i==filas-1:
                print (3 if(i%2==1) else (1))*(" ")+' '+u'\u2514'+(columnas-1)*(3*u'\u2500'+u'\u2534')+3*u'\u2500'+u'\u2518'
            elif(i%2==0):
                print (('  '+u'\u2514'+(columnas)*(u'\u2500'+ u'\u252C'+ u'\u2500'+u'\u2534')+u'\u2500'+u'\u2510'))
            else:
                print (('  '+u'\u250C'+(columnas)*(u'\u2500'+u'\u2534'+u'\u2500'+u'\u252C')+u'\u2500'+u'\u2518'))

def jugar(filas,columnas):
    t.imprimir(filas,columnas)


#Programa principal

filas=columnas=9
minas=10
t=Tablero(filas,columnas,minas)
t.rellenar_bombas(filas,columnas,minas)
jugar(filas,columnas)



                




import pygtk
pygtk.require('2.0')
import gtk
import random
import time

#Parte de objetos

class Celda:
    def __init__(self,mina,i,j,button):
        #self.principal=u'\u2593'  #En gtk seria la foto celda cerrada
        self.mina=mina
        self.boton=button

        self.i=i
        self.j=j

        self.cerrada=True   #Inicialmente esta cerrada
        self.marcada=False

class Tablero:
    def __init__(self):
        self.imagenes=[]
        self.imagenes.append(gtk.gdk.pixbuf_new_from_file("ycelda_cerrada.png"))
        self.imagenes.append(gtk.gdk.pixbuf_new_from_file("ycelda_mina.png"))
        self.imagenes.append(gtk.gdk.pixbuf_new_from_file("ycelda_0.png"))
        self.imagenes.append(gtk.gdk.pixbuf_new_from_file("ycelda_1.png"))
        self.imagenes.append(gtk.gdk.pixbuf_new_from_file("ycelda_2.png"))
        self.imagenes.append(gtk.gdk.pixbuf_new_from_file("ycelda_3.png"))  #Por ahora, 3 o mas equivalen a esta imagen
        self.imagenes.append(gtk.gdk.pixbuf_new_from_file("ycelda_marcada.png"))

        self.disponible=True

        self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Menu principal")
        self.window.set_border_width(20)
        self.window.set_size_request(200,100)
        self.window.connect("delete_event",self.delete_event)   #Cierra el programa si se pulsa la cruz del marco

        tabla=gtk.Table(3,3)
        dificultad=gtk.Label("Seleccione dificultad")
        tabla.attach(dificultad,0,3,0,1)

        self.button=gtk.Button("Principiante 9x9")
        self.button.connect("clicked",self.CrearTablero,9,9,10)
        tabla.attach(self.button,0,3,1,2)
        self.button.show()

        self.button=gtk.Button("Intermedio 11x11")
        self.button.connect("clicked",self.CrearTablero,11,11,30)
        tabla.attach(self.button,0,3,2,3)
        self.button.show()

        self.window.add(tabla)
        tabla.show()
        self.window.show()

    def delete_event(self,widget,event,data=None):
        gtk.main_quit()
        return False

    def Restart(self,widget,data=None):
        self.window.hide()
        Tablero()


    def FinMina(self,widget,event,lista,oculta,i,j,turno):
        celda=lista[i][j]
        a=i
        b=j
        mina=celda.mina
        button=celda.boton
        if self.disponible==True:
            if event.button==1:
                celda.cerrada=False
                total=MinasAlrededor(oculta,i,j)
                if total==0 and i>1 and j>1 and i<self.filas and j<self.columnas and turno==0:
                    self.FinMina(widget,event,lista,oculta,i-1,j,0)
                #Con los turnos se controla la recursividad    
                turno=1
                if i>1 and j>1 and i<self.filas and j<self.columnas and total==0 and turno==1:
                    self.FinMina(widget,event,lista,oculta,i+1,j,1)
                
                if mina==1:
                    button.get_image().set_from_pixbuf(self.imagenes[1])
                    print "FIN DEL JUEGO "
                    self.disponible=False
                else:
                    if total==0:
                        button.get_image().set_from_pixbuf(self.imagenes[2])
                    elif total==1:
                        button.get_image().set_from_pixbuf(self.imagenes[3])
                    elif total==2:
                        button.get_image().set_from_pixbuf(self.imagenes[4])
                    else:
                        button.get_image().set_from_pixbuf(self.imagenes[5])
            elif event.button==3:
                if celda.cerrada==True and celda.marcada==False:
                    button.get_image().set_from_pixbuf(self.imagenes[6])
                    celda.marcada=True
                elif celda.cerrada==True and celda.marcada==True:
                    button.get_image().set_from_pixbuf(self.imagenes[0])
                    celda.marcada=False

    def CrearTablero(self,widget,filas,columnas,minas):
        self.window.hide()

        self.filas=filas
        self.columnas=columnas

        self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Buscaminas")
        self.window.set_border_width(20)
        self.window.set_size_request(400,400)

        self.window.connect("delete_event",self.delete_event)


        oculta=[]
        for i in range(filas+2):
            oculta.append([])
            for j in range(columnas+2):
                if i>0 and j>0 and i<filas+1 and j<columnas+1:
                    mina=random.randint(1,7)
                    if mina==5 and minas>0:
                        oculta[i].append(0)
                        minas-=1
                    else:
                        oculta[i].append(0)
                else:
                    oculta[i].append(0)

        while minas>0:
            for i in range(filas+2):
                for j in range(columnas+2):
                    if i>0 and j>0 and i<filas+1 and j<columnas+1:
                        mina=random.randint(1,7)
                        if mina==5 and minas>0 and oculta[i][j]!=1:
                            oculta[i][j]=0
                            minas-=1
                        
                            
        table=gtk.Table(filas*2,columnas*2)
        self.window.add(table)

        lista=[]
        for i in range(filas+2):
            lista.append([])
            for j in range(columnas+2):
                if i>0 and j>0 and i<filas+1 and j<columnas+1: 
                    self.button=gtk.Button(None)
                    self.button.set_image(gtk.Image())
                    self.button.set_relief(gtk.RELIEF_NONE)
                    self.button.get_image().set_from_pixbuf(self.imagenes[0])
                    table.attach(self.button,i,i+1,j,j+1)
                    self.button.show()
                    if oculta[i][j]==1:
                        mina=1
                    else:
                        mina=0
                    C=Celda(mina,i+1,j+1,self.button)
                    lista[i].append(C)
                    self.button.connect("button-release-event",self.FinMina,lista,oculta,i,j-1,0)
                    #Teoria de por que sin j-1 coge una mas
                    #Se frena uno antes del rango maximo de j


        self.button=gtk.Button("Quit")
        self.button.connect("clicked",lambda w:gtk.main_quit())
        table.attach(self.button,0,filas+1,columnas+1,columnas+2)
        self.button.show()

        self.button=gtk.Button("Reset")
        self.button.connect("clicked",self.Restart)
        table.attach(self.button,0,filas+1,columnas+2,columnas+3)
        self.button.show()

        table.show()
        self.window.show()


#Programa principal
def main():
    gtk.main()
    return 0

def MinasAlrededor(oculta,i,j):
    total=0
    if oculta[i-1][j-1]==1:
        total+=1    
    if oculta[i-1][j]==1:
        total+=1
    if oculta[i-1][j+1]==1:
        total+=1
    if oculta[i][j-1]==1:
        total+=1
    if oculta[i][j+1]==1:
        total+=1
    if oculta[i+1][j-1]==1:
        total+=1
    if oculta[i+1][j]==1:
        total+=1
    if oculta[i+1][j+1]==1:
        total+=1

    return total
if __name__=="__main__":
    Tablero()
    main()

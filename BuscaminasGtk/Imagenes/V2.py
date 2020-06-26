import pygtk
pygtk.require('2.0')
import gtk
import random

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

    def FinMina(self,widget,event,celda,oculta):
        mina=celda.mina
        i=celda.i
        j=celda.j
        button=celda.boton
        if self.disponible==True:
            if event.button==1:
                celda.cerrada=False
                total=MinasAlrededor(oculta,i,j)
                if total==0:
                    aaaaa=1
                    #Borrar alrededor
                if mina==1:
                    button.get_image().set_from_pixbuf(self.imagenes[1])
                    print "FIN DEL JUEGO "
                    self.disponible=False
                else:
                    if total==0:
                        button.get_image().set_from_pixbuf(self.imagenes[2])
                        print "Ok"
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

        self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Buscaminas")
        self.window.set_border_width(20)
        self.window.set_size_request(400,400)

        self.window.connect("delete_event",self.delete_event)

        table=gtk.Table(filas+10,columnas+10)
        self.window.add(table)

        oculta=[]
        for i in range(filas+106):
            oculta.append([])
            for j in range(columnas+106):
                if i>100 and j>100 and i<filas+100 and j<columnas+100:
                    mina=random.randint(1,7)
                    if mina==5 and minas>0:
                        oculta[i].append(1)
                        minas-=1
                    else:
                        oculta[i].append(0)
                else:
                    oculta[i].append(0)

        while minas>0:
            for i in range(filas+106):
                for j in range(columnas+106):
                    if i>100 and j>100 and i<filas+100 and j<columnas+100:
                        mina=random.randint(1,7)
                        if mina==5 and minas>0 and oculta[i][j]!=1:
                            oculta[i][j]=1
                            minas-=1
                        
                            


        for ii in range(filas+106):
            for jj in range(columnas+106):
                if ii>100 and jj>100 and ii<filas+100 and jj<columnas+100:
                    if ii%2!=0:
                        espacio=2
                    else:
                        espacio=0
                    self.button=gtk.Button(None)
                    self.button.set_image(gtk.Image())
                    self.button.set_relief(gtk.RELIEF_NONE)
                    self.button.get_image().set_from_pixbuf(self.imagenes[0])
                    table.attach(self.button,ii+espacio,ii+1+espacio,jj,jj+1)
                    self.button.show()

                    if oculta[ii][jj]==1:
                        mina=1
                    else:
                        mina=0
                    C=Celda(mina,ii,jj,self.button)
                    self.button.connect("button-release-event",self.FinMina,C,oculta)
        


        self.button=gtk.Button("Quit")
        self.button.connect("clicked",lambda w:gtk.main_quit())
        table.attach(self.button,100,filas+100,columnas+105,columnas+106)
        self.button.show()

        self.button=gtk.Button("Reset")
        self.button.connect("clicked",self.Restart)
        table.attach(self.button,100,filas+100,columnas+106,columnas+107)
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

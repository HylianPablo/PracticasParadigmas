import pygtk
pygtk.require('2.0')
import gtk
import gobject
import random
import time

#Parte de objetos

class Celda:
    def __init__(self,mina,i,j,button):
        self.mina=mina
        self.boton=button

        self.i=i
        self.j=j

        self.cerrada=True   #Inicialmente esta cerradai
        self.marcada=False
        self.final=False

class Tablero:
    def __init__(self):
        self.imagenes=[]
        self.imagenes.append(gtk.gdk.pixbuf_new_from_file("xcelda_cerrada.png"))
        self.imagenes.append(gtk.gdk.pixbuf_new_from_file("xcelda_mina.png"))
        self.imagenes.append(gtk.gdk.pixbuf_new_from_file("xcelda_0.png"))
        self.imagenes.append(gtk.gdk.pixbuf_new_from_file("xcelda_1.png"))
        self.imagenes.append(gtk.gdk.pixbuf_new_from_file("xcelda_2.png"))
        self.imagenes.append(gtk.gdk.pixbuf_new_from_file("xcelda_3.png"))  
        self.imagenes.append(gtk.gdk.pixbuf_new_from_file("xcelda_4.png"))  
        self.imagenes.append(gtk.gdk.pixbuf_new_from_file("xcelda_5.png"))  
        self.imagenes.append(gtk.gdk.pixbuf_new_from_file("xcelda_6.png"))  
        self.imagenes.append(gtk.gdk.pixbuf_new_from_file("xcelda_boom.png"))  
        self.imagenes.append(gtk.gdk.pixbuf_new_from_file("xcelda_marcada_error.png"))  
        self.imagenes.append(gtk.gdk.pixbuf_new_from_file("xcelda_question.png"))  

        self.imagenes.append(gtk.gdk.pixbuf_new_from_file("xcelda_marcada.png"))

        self.disponible=True

        self.tpo0=time.time()
        self.timer=gobject.timeout_add(1000,self.clock)
        self.etq_tpo=gtk.Label(self.timer)

        self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Menu principal")
        self.window.set_border_width(20)
        self.window.set_size_request(250,200)
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.connect("delete_event",self.delete_event)   #Cierra el programa si se pulsa la cruz del marco

        tabla=gtk.Table(5,5)
        dificultad=gtk.Label("Seleccione dificultad")
        tabla.attach(dificultad,0,3,0,1)

        self.button=gtk.Button("Principiante 9x9")
        self.button.connect("clicked",self.CrearTablero,9,9,10)
        tabla.attach(self.button,0,3,1,2)
        self.button.show()

        self.button=gtk.Button("Intermedio 16x16")
        self.button.connect("clicked",self.CrearTablero,16,16,40)
        tabla.attach(self.button,0,3,2,3)
        self.button.show()

        self.button=gtk.Button("Experto 16x30")
        self.button.connect("clicked",self.CrearTablero,16,30,99)
        tabla.attach(self.button,0,3,3,4)
        self.button.show()

        self.button=gtk.Button("Leer de fichero")
        self.button.connect("clicked",self.LeerFichero)
        tabla.attach(self.button,0,3,4,5)
        self.button.show()

        self.window.add(tabla)
        tabla.show()
        self.window.show()

    def delete_event(self,widget,event,data=None):
        gtk.main_quit()
        return False
    
    def LeerFichero(self,widget):
        dlg=gtk.FileChooserDialog("Abrir fichero",None,gtk.FILE_CHOOSER_ACTION_OPEN,(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_OPEN,gtk.RESPONSE_OK))       
        if dlg.run()==gtk.RESPONSE_OK:
            res=dlg.get_filename()
        else:
            res=None
        dlg.destroy()

        res=str(res)

        fich=open(res)
        lins=fich.read().split('\n')
        primera=lins[0].split(" ")
        size1=primera[0]
        size1=int(size1)
        size2=primera[1]
        size2=int(size2)

        MinasFich=0

        for linea in lins:
            for digito in linea:
                if digito=='*':
                    MinasFich+=1
        self.SIZE1=size1
        self.SIZE2=size2
        self.MINASF=MinasFich
        self.CrearTablero(widget,size1,size2,MinasFich)
        fich.close()

    def Restart(self,widget,data=None):
        self.window.hide()
        Tablero()

    def clock(self):
        dt=int(time.time() - self.tpo0)
        self.etq_tpo.set_label("{0:02}:{1:02}".format(dt/60,dt%60))
        return True

    def MuestraTablero(self,lista):
        self.window.hide()
        
        self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("FIN DEL JUEGO")
        self.window.set_border_width(20)
        self.window.set_size_request(400,400)
        self.window.connect("delete_event",self.delete_event)   #Cierra el programa si se pulsa la cruz del marco
        self.window.set_position(gtk.WIN_POS_CENTER)

        FFixed=gtk.Fixed()
        alinear=gtk.Alignment(0.5,0.5,0,0)
        alinear.add(FFixed)
        self.window.add(alinear)

        for i in range(self.filas):
            for j in range(self.columnas):
                celda=lista[i][j]
                mina=celda.mina
                self.button=gtk.Button(None)
                self.button.set_image(gtk.Image())
                self.button.set_relief(gtk.RELIEF_NONE)
                if j%2==0:
                    espacio=1
                    FFixed.put(self.button,(i+espacio)*20-10,j*20)
                else:
                    FFixed.put(self.button,i*20,j*20)
                if mina==1:
                    if celda.marcada==True:
                        self.button.get_image().set_from_pixbuf(self.imagenes[12])
                        self.button.show()
                    else:
                        if celda.final==True:
                            self.button.get_image().set_from_pixbuf(self.imagenes[9])
                        else:
                            self.button.get_image().set_from_pixbuf(self.imagenes[1])
                        self.button.show()
                else:
                    if celda.marcada==True:
                        self.button.get_image().set_from_pixbuf(self.imagenes[10])
                    else:
                        self.button.get_image().set_from_pixbuf(self.imagenes[2])
                    self.button.show()

        self.button=gtk.Button("Quit")
        self.button.connect("clicked",lambda w:gtk.main_quit())
        FFixed.put(self.button,0,self.columnas*27)
        self.button.set_size_request(200,30)
        self.button.show()

        self.button=gtk.Button("Reset")
        self.button.connect("clicked",self.Restart)
        FFixed.put(self.button,0,self.columnas*30)
        self.button.set_size_request(200,30)
        self.button.show()


        FFixed.show()
        alinear.show()
        self.window.show()

    def MinadoAlrededor(self,lista,i,j):
        total=0
        if i>0 and j>0 and i<self.filas-1 and j<self.columnas-1:
            celda=lista[i][j-1]
            if celda.mina==1:
                total+=1
            if celda.marcada==True:
                total-=1

            celda=lista[i][j+1]
            if celda.mina==1:
                total+=1
            if celda.marcada==True:
                total-=1

            celda=lista[i-1][j]
            if celda.mina==1:
                total+=1
            if celda.marcada==True:
                total-=1

            celda=lista[i+1][j]
            if celda.mina==1:
                total+=1
            if celda.marcada==True:
                total-=1

            if j%2==0:
                celda=lista[i+1][j-1]
                if celda.mina==1:
                    total+=1
                if celda.marcada==True:
                    total-=1

                celda=lista[i-1][j-1]
                if celda.mina==1:
                    total+=1
                if celda.marcada==True:
                    total-=1

            else:
                celda=lista[i+1][j+1]
                if celda.mina==1:
                    total+=1
                if celda.marcada==True:
                    total-=1

                celda=lista[i-1][j+1]
                if celda.mina==1:
                    total+=1
                if celda.marcada==True:
                    total-=1

        return total


    def FinMina(self,widget,event,lista,i,j,turno):
        celda=lista[i][j]
        mina=celda.mina
        button=celda.boton
        if self.disponible==True:
            if event.button==1:
                celda.cerrada=False
                total=self.MinadoAlrededor(lista,i,j)
                #Con los turnos se controla la recursividad
                ###########################################
                if total==0 and i>0 and j>0 and i<self.filas-1 and j<self.columnas-1 and turno==0:
                    self.FinMina(widget,event,lista,i-1,j,0)
                    turno=1
                if i>0 and j>0 and i<self.filas-1 and j<self.columnas-1 and total==0 and turno==1:
                    self.FinMina(widget,event,lista,i+1,j,1)
                    turno=2
                if i>0 and j>0 and i<self.filas-1 and j<self.columnas-1 and total==0 and turno==2:
                    self.FinMina(widget,event,lista,i,j+1,2)
                    turno=3
                if i>0 and j>0 and i<self.filas-1 and j<self.columnas-1 and total==0 and turno==3:
                   self.FinMina(widget,event,lista,i,j-1,3)
                   turno=4
                if j%2==0:
                    if i>0 and j>0 and i<self.filas-1 and j<self.columnas-1 and total==0 and turno==4:
                        self.FinMina(widget,event,lista,i+1,j-1,4)
                        turno=5
                    if i>0 and j>0 and i<self.filas-1 and j<self.columnas-1 and total==0 and turno==5:
                        self.FinMina(widget,event,lista,i-1,j-1,5)
                else:
                    if i>0 and j>0 and i<self.filas-1 and j<self.columnas-1 and total==0 and turno==4:
                        self.FinMina(widget,event,lista,i+1,j+1,4)
                        turno=5
                    if i>0 and j>0 and i<self.filas-1 and j<self.columnas-1 and total==0 and turno==5:
                        self.FinMina(widget,event,lista,i-1,j+1,5)
                        
                #Zona de turnos
                ###################################################
                if mina==1:
                    button.get_image().set_from_pixbuf(self.imagenes[1])
                    print "FIN DEL JUEGO "
                    self.disponible=False
                    celda.final=True
                    self.MuestraTablero(lista)
                else:
                    self.CambiaImagenes(total,button,celda)
            #### MARCADAS ####
            elif event.button==3:
                if celda.cerrada==True and celda.marcada==False:
                    button.get_image().set_from_pixbuf(self.imagenes[12])
                    celda.marcada=True
                    self.NumeroMarcadas+=1
                    self.Etq_marcadas1.hide()
                    self.Etq_marcadas1=gtk.Label(self.NumeroMarcadas)
                    self.Fixed.put(self.Etq_marcadas1,240,225)
                    self.Etq_marcadas1.show()

                    self.Update(lista,i,j)

                elif celda.cerrada==True and celda.marcada==True:
                    button.get_image().set_from_pixbuf(self.imagenes[0])
                    celda.marcada=False
                    self.NumeroMarcadas-=1
                    self.Etq_marcadas1.hide()
                    self.Etq_marcadas1=gtk.Label(self.NumeroMarcadas)
                    self.Fixed.put(self.Etq_marcadas1,240,225)
                    self.Etq_marcadas1.show()
                    
                    self.Update(lista,i,j)
        
        self.Ganar(lista)

    def Update(self,lista,i,j):
        if i>0 and j>0 and i<self.filas-1 and j<self.columnas-1:
            celda=lista[i][j-1]
            total=self.MinadoAlrededor(lista,i,j)
            button=celda.boton
            self.CambiaImagenes(total,button,celda)

            celda=lista[i][j+1]
            total=self.MinadoAlrededor(lista,i,j)
            button=celda.boton
            self.CambiaImagenes(total,button,celda)
        
            celda=lista[i-1][j]
            total=self.MinadoAlrededor(lista,i,j)
            button=celda.boton
            self.CambiaImagenes(total,button,celda)

            celda=lista[i+1][j]
            total=self.MinadoAlrededor(lista,i,j)
            button=celda.boton
            self.CambiaImagenes(total,button,celda)

            if j%2==0:
                celda=lista[i+1][j-1]
                total=self.MinadoAlrededor(lista,i,j)
                button=celda.boton
                self.CambiaImagenes(total,button,celda)
        
                celda=lista[i-1][j-1]
                total=self.MinadoAlrededor(lista,i,j)
                button=celda.boton
                self.CambiaImagenes(total,button,celda)
            else:
                celda=lista[i+1][j+1]
                total=self.MinadoAlrededor(lista,i,j)
                button=celda.boton
                self.CambiaImagenes(total,button,celda)
        
                celda=lista[i-1][j+1]
                total=self.MinadoAlrededor(lista,i,j)
                button=celda.boton
                self.CambiaImagenes(total,button,celda)

    def CambiaImagenes(self,total,button,celda):
        if celda.cerrada==False:
            if total==0:
                button.get_image().set_from_pixbuf(self.imagenes[2])
            elif total<0:
                button.get_image().set_from_pixbuf(self.imagenes[11])
            elif total==1:
                button.get_image().set_from_pixbuf(self.imagenes[3])
            elif total==2:
                button.get_image().set_from_pixbuf(self.imagenes[4])
            elif total==3:
                button.get_image().set_from_pixbuf(self.imagenes[5])
            elif total==4:
                button.get_image().set_from_pixbuf(self.imagenes[6])
            elif total==5:
                button.get_image().set_from_pixbuf(self.imagenes[7])
            else:
                button.get_image().set_from_pixbuf(self.imagenes[8])

    def Ganar(self,lista):
        contador=0
        for i in range(self.filas):
            for j in range(self.columnas):
                celda=lista[i][j]
                if celda.cerrada==True or celda.marcada==True:
                    contador+=1
        if contador==self.NumeroMinas:
            self.disponible=False
            self.MuestraTablero(lista)

    def CrearTablero(self,widget,filas,columnas,minas):
        self.window.hide()

        self.filas=filas
        self.columnas=columnas
        self.NumeroMinas=minas
        self.NumeroMarcadas=0

        self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Buscaminas")
        self.window.set_border_width(20)
        self.window.set_size_request(self.filas*40,self.columnas*40)   #Encontrar un valor que ajuste la ventana, por ahora, este con 9x9 esta bien
        self.window.set_position(gtk.WIN_POS_CENTER)

        self.window.connect("delete_event",self.delete_event)



        oculta=[]
        for i in range(filas):
            oculta.append([])
            for j in range(columnas):
                mina=random.randint(1,7)
                if mina==5 and minas>0:
                    oculta[i].append(1)
                    minas-=1
                else:
                    oculta[i].append(0)
            else:
                oculta[i].append(0)

        while minas>0:
            for i in range(filas):
                for j in range(columnas):
                    mina=random.randint(1,7)
                    if mina==5 and minas>0 and oculta[i][j]!=1:
                        oculta[i][j]=1
                        minas-=1
                        
                            
        self.Fixed=gtk.Fixed()
        alinear=gtk.Alignment(0.5,0.5,0,0)
        alinear.add(self.Fixed)
        self.window.add(alinear)

        lista=[]
        for i in range(filas):
            lista.append([])
            for j in range(columnas):
                espacio=1
                self.button=gtk.Button(None)
                self.button.set_image(gtk.Image())
                self.button.set_relief(gtk.RELIEF_NONE)
                self.button.set_size_request(40,40)
                self.button.set_border_width(1)
                self.button.get_image().set_from_pixbuf(self.imagenes[0])
                if j%2==0:
                    self.Fixed.put(self.button,(i+espacio)*20-10,j*20)
                else:
                    self.Fixed.put(self.button,i*20,j*20)
                self.button.show()
                if oculta[i][j]==1:
                    mina=1
                else:
                    mina=0
                C=Celda(mina,i,j,self.button)
                lista[i].append(C)
                self.button.connect("button-release-event",self.FinMina,lista,i,j,0)

        self.button=gtk.Button("Quit")
        self.button.connect("clicked",lambda w:gtk.main_quit())
        self.Fixed.put(self.button,0,self.columnas*27)
        self.button.set_size_request(200,30)
        self.button.show()

        self.button=gtk.Button("Reset")
        self.button.connect("clicked",self.Restart)
        self.Fixed.put(self.button,0,self.columnas*30)
        self.button.set_size_request(200,30)
        self.button.show()

        Etq_minas=gtk.Label()
        Etq_minas.set_markup("<b>Numero de minas: </b>")
        self.Fixed.put(Etq_minas,self.filas*10,self.columnas*22)
        Etq_minas.show()

        Etq_minas1=gtk.Label(self.NumeroMinas)
        self.Fixed.put(Etq_minas1,self.filas*24,self.columnas*22)
        Etq_minas1.show()

        self.Etq_marcadas=gtk.Label()
        self.Etq_marcadas.set_markup("<b>Numero de marcadas: </b>")
        self.Fixed.put(self.Etq_marcadas,self.filas*10,self.columnas*24)
        self.Etq_marcadas.show()

        self.Etq_marcadas1=gtk.Label(self.NumeroMarcadas)
        self.Fixed.put(self.Etq_marcadas1,self.filas*27,self.columnas*24)
        self.Etq_marcadas1.show()

        self.Fixed.put(self.etq_tpo,self.filas,self.columnas*23)       #Etiqueta del tiempo
        self.etq_tpo.show()


        self.Fixed.show()
        alinear.show()
        self.window.show()


#Programa principal
def main():
    gtk.main()
    return 0

    return total
if __name__=="__main__":
    Tablero()
    main()

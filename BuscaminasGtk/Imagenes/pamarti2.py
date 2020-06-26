import pygtk
pygtk.require('2.0')
import gtk
import gobject
import random
import time
import pango

#BUSCAMINAS EN ENTORNO GRAFICO

#PABLO MARTINEZ LOPEZ && MANUEL MENDEZ CALVO

#Filas y columnas cambiadas de sitio en llamadas al tablero

#Parte de objetos

class Celda:
    def __init__(self,mina,i,j,button):
        self.mina=mina
        self.boton=button

        self.i=i
        self.j=j

        self.cerrada=True   #Inicialmente esta cerrada
        self.marcada=False
        self.final=False
        self.primera=True

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
        
        self.smiley=[]
        self.smiley.append(gtk.gdk.pixbuf_new_from_file("Restart.png"))
        
        self.disponible=True
        self.Fichero=False
        self.ganador=False

        self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Menu principal")
        self.window.set_border_width(20)
        self.window.set_size_request(250,250)
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.connect("delete_event",self.delete_event)   #Cierra el programa si se pulsa la cruz del marco

        tabla=gtk.Table(6,6)
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

        self.button=gtk.Button("Salir")
        self.button.connect("clicked",lambda w:gtk.main_quit())
        tabla.attach(self.button,0,3,5,6)
        self.button.show()

        self.window.add(tabla)
        tabla.show()
        self.window.show()

    def delete_event(self,widget,event,data=None):
        gtk.main_quit()
        return False
    
    def LeerFichero(self,widget):
        self.Fichero=True
        dlg=gtk.FileChooserDialog("Abrir fichero",None,gtk.FILE_CHOOSER_ACTION_OPEN,(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_OPEN,gtk.RESPONSE_OK))       
        if dlg.run()==gtk.RESPONSE_OK:
            res=dlg.get_filename()
        else:
            res=None
        dlg.destroy()

        res=str(res)
        
        self.OcultaFich=[]
        self.minado=[]

        fich=open(res)
        lins=fich.read().split('\n')
        primera=lins[0].split(" ")
        size1=primera[0]
        size1=int(size1)
        size2=primera[1]
        size2=int(size2)

        MinasFich=0


        for linea in lins:
            if linea!=lins[0]:
                for digito in linea:
                    if digito=='*':
                        MinasFich+=1
                        self.minado.append(1)
                    elif digito=='.':
                        self.minado.append(0)

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
        self.window.destroy()
        
        self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("FIN DEL JUEGO")
        self.window.set_border_width(20)
        self.window.set_size_request((self.columnas+10)*24,(self.filas+10)*24)
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
                if i%2==0:
                    espacio=1
                    FFixed.put(self.button,(j+1)*20-10,i*20)
                else:
                    FFixed.put(self.button,j*20,i*20)
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

        if self.ganador==True:
            self.EtqFinal=gtk.Label("ENHORABUENA. \n HA GANADO")
        else:
            self.EtqFinal=gtk.Label("FIN DEL JUEGO")
        if self.columnas<20:
            FFixed.put(self.EtqFinal,0,(self.columnas+2)*24)
        else:
              FFixed.put(self.EtqFinal,0,(self.columnas+2)*12)
        font=pango.FontDescription("arial black 20")
        self.EtqFinal.modify_font(font)
        self.EtqFinal.show()

        self.button=gtk.Button(None)
        self.button.set_image(gtk.Image())
        self.button.set_relief(gtk.RELIEF_NONE)
        self.button.get_image().set_from_pixbuf(self.smiley[0])
        self.button.connect("clicked",self.CrearTablero,self.filas,self.columnas,self.NumeroMinas)
        if self.columnas<20:
            FFixed.put(self.button,self.filas+100,(self.columnas)*24)
        else:
              FFixed.put(self.button,self.filas+300,(self.columnas)*12)
        self.button.set_size_request(45,45)
        self.button.show()

        self.button=gtk.Button("Volver al menu principal")
        self.button.connect("clicked",self.Restart)
        if self.columnas<20:
            FFixed.put(self.button,0,(self.columnas+6)*24)
        else:
            FFixed.put(self.button,300,(self.columnas+6)*12)
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

            if i%2==0:
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
                self.Avisos.hide()
                if celda.marcada==False:
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
                if i%2==0:
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
                    if self.PrimeraMina==True:
                        self.Avisos.hide()
                        celda.cerrada=True
                        self.PrimeraMina=False
                        self.ArreglaMina(lista,i,j,celda)
                        self.FinMina(widget,event,lista,i,j,0)
                    else:
                        if celda.marcada==True:
                            self.Avisos.hide()
                            self.Mensaje="No se pueden abrir \n celdas marcadas"
                            self.Avisos=gtk.Label(self.Mensaje)
                            self.Fixed.put(self.Avisos,self.filas*2,(self.columnas+4)*24)
                            self.Avisos.show()
                        else:
                            self.Avisos.hide()
                            button.get_image().set_from_pixbuf(self.imagenes[1])
                            print "FIN DEL JUEGO "
                            #self.disponible=False
                            celda.final=True
                            self.MuestraTablero(lista)
                elif mina!=1 and celda.marcada==False and celda.primera==True:
                    self.Avisos.hide()
                    self.PrimeraMina=False
                    self.CambiaImagenes(total,button,celda)
                    celda.primera=False
                elif celda.marcada==True:
                    self.Avisos.hide()
                    self.Mensaje="No se pueden abrir \n celdas marcadas"
                    self.Avisos=gtk.Label(self.Mensaje)
                    if self.columnas<20:
                        self.Fixed.put(self.Avisos,self.filas*2,(self.columnas+4)*24)
                    else:
                         self.Fixed.put(self.Avisos,self.filas*2,(self.columnas+4)*12)
                    self.Avisos.show()    
                elif mina!=1 and celda.marcada==False and celda.primera==False and total<=0:
                    self.Avisos.hide()
                    self.Update(lista,i,j)
                elif mina!=1 and celda.marcada==False and celda.primera==False and total>0:
                    self.Avisos.hide()
                    self.Mensaje="No se pueden abrir vecinas. \n por insuficientes marcas"
                    self.Avisos=gtk.Label(self.Mensaje)
                    if self.columnas<20:
                        self.Fixed.put(self.Avisos,self.filas*2,(self.columnas+4)*24)
                    else:
                          self.Fixed.put(self.Avisos,self.filas*2,(self.columnas+4)*12)
                    self.Avisos.show()
             
            #### MARCADAS ####
            elif event.button==3:
                if celda.cerrada==True and celda.marcada==False and self.NumeroMarcadas<self.NumeroMinas:
                    self.Avisos.hide()
                    button.get_image().set_from_pixbuf(self.imagenes[12])
                    celda.marcada=True
                    self.NumeroMarcadas+=1
                    self.Etq_marcadas1.hide()
                    self.Etq_marcadas1=gtk.Label(self.NumeroMarcadas)
                    if self.columnas<20:
                        self.Fixed.put(self.Etq_marcadas1,(self.filas+75)*2,(self.columnas+3)*24)
                    else:
                          self.Fixed.put(self.Etq_marcadas1,(self.filas+75)*2,(self.columnas+3)*12)
                    self.Etq_marcadas1.show()

                    self.Update(lista,i,j)

                elif celda.cerrada==True and celda.marcada==True:
                    self.Avisos.hide()
                    button.get_image().set_from_pixbuf(self.imagenes[0])
                    celda.marcada=False
                    self.NumeroMarcadas-=1
                    self.Etq_marcadas1.hide()
                    self.Etq_marcadas1=gtk.Label(self.NumeroMarcadas)
                    if self.columnas<20:
                        self.Fixed.put(self.Etq_marcadas1,(self.filas+75)*2,(self.columnas+3)*24)
                    else:
                           self.Fixed.put(self.Etq_marcadas1,(self.filas+75)*2,(self.columnas+3)*12)
                    self.Etq_marcadas1.show()
                    
                    self.Update(lista,i,j)
                elif celda.cerrada==True and celda.marcada==False and self.NumeroMarcadas>=self.NumeroMinas:
                    self.Avisos.hide()
                    self.Mensaje="No se pueden marcar mas \n celdas que minas"
                    self.Avisos=gtk.Label(self.Mensaje)
                    if self.columnas<20:
                        self.Fixed.put(self.Avisos,self.filas*2,(self.columnas+4)*24)
                    else:
                          self.Fixed.put(self.Avisos,self.filas*2,(self.columnas+4)*12)
                    self.Avisos.show()

                elif celda.cerrada==False:
                    self.Avisos.hide()
                    self.Mensaje="No se pueden marcar \n celdas abiertas"
                    self.Avisos=gtk.Label(self.Mensaje)
                    if self.columnas<20:
                        self.Fixed.put(self.Avisos,self.filas*2,(self.columnas+4)*24)
                    else:
                         self.Fixed.put(self.Avisos,self.filas*2,(self.columnas+4)*12)
                    self.Avisos.show()
        
        self.Ganar(lista)

    def ArreglaMina(self,lista,a,b,celdaOr):
        for i in range(self.filas):
            for j in range(self.columnas):
                celda=lista[i][j]
                if celda.mina!=1:
                    M=celda.mina
                    m=celdaOr.mina
                    celda.mina=m
                    celdaOr.mina=M
                    break

    def Update(self,lista,i,j):
        if i>0 and j>0 and i<self.filas-1 and j<self.columnas-1:
            celda=lista[i][j-1]
            total=self.MinadoAlrededor(lista,i,j-1)
            button=celda.boton
            self.CambiaImagenes(total,button,celda)

            celda=lista[i][j+1]
            total=self.MinadoAlrededor(lista,i,j+1)
            button=celda.boton
            self.CambiaImagenes(total,button,celda)
        
            celda=lista[i-1][j]
            total=self.MinadoAlrededor(lista,i-1,j)
            button=celda.boton
            self.CambiaImagenes(total,button,celda)

            celda=lista[i+1][j]
            total=self.MinadoAlrededor(lista,i+1,j)
            button=celda.boton
            self.CambiaImagenes(total,button,celda)

            if i%2==0:
                celda=lista[i+1][j-1]
                total=self.MinadoAlrededor(lista,i+1,j-1)
                button=celda.boton
                self.CambiaImagenes(total,button,celda)
        
                celda=lista[i-1][j-1]
                total=self.MinadoAlrededor(lista,i-1,j-1)
                button=celda.boton
                self.CambiaImagenes(total,button,celda)
            else:
                celda=lista[i+1][j+1]
                total=self.MinadoAlrededor(lista,i+1,j+1)
                button=celda.boton
                self.CambiaImagenes(total,button,celda)
        
                celda=lista[i-1][j+1]
                total=self.MinadoAlrededor(lista,i-1,j+1)
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
            self.ganador=True
            self.MuestraTablero(lista)

    def CrearTablero(self,widget,filas,columnas,minas):
        self.window.destroy()

        self.PrimeraMina=True
        self.disponible=True

        self.NumeroMinas=minas
        self.NumeroMarcadas=0

        self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Buscaminas")
        self.window.set_border_width(20)
        self.window.set_size_request((columnas+10)*24,(filas+10)*24)   #Encontrar un valor que ajuste la ventana, por ahora, este con 9x9 esta bien
        self.window.set_position(gtk.WIN_POS_CENTER)

        self.window.connect("delete_event",self.delete_event)


        self.tpo0=time.time()
        self.timer=gobject.timeout_add(1000,self.clock)
        self.etq_tpo=gtk.Label(self.timer)

                            
        self.Fixed=gtk.Fixed()
        alinear=gtk.Alignment(0.5,0.5,0,0)
        alinear.add(self.Fixed)
        self.window.add(alinear)


        lista=[]
        self.filas=filas
        self.columnas=columnas
        for i in range(filas):
            lista.append([])
            for j in range(columnas):
                self.button=gtk.Button(None)
                self.button.set_image(gtk.Image())
                self.button.set_relief(gtk.RELIEF_NONE)
                self.button.set_size_request(40,40)
                self.button.set_border_width(1)
                self.button.get_image().set_from_pixbuf(self.imagenes[0])
                if i%2!=0:
                    self.Fixed.put(self.button,(j+1)*20-10,i*20)
                else:
                    self.Fixed.put(self.button,j*20,i*20)
                self.button.show()
                x=random.randint(1,7)
                if x==5:
                    mina=0
                    minas-=0
                else:
                    mina=0
                C=Celda(mina,i,j,self.button)
                lista[i].append(C)
                #self.button.connect("button-release-event",self.FinMina,lista,i,j,0)

        if self.Fichero==False:
            self.LlenarMinas(lista,filas,columnas,minas)
        else:
            self.LlenarMinasFich(lista,filas,columnas)  

        self.button=gtk.Button("Acabar partida")
        self.button.connect("clicked",self.Restart)
        if self.columnas<20:
            self.Fixed.put(self.button,0,(self.columnas+6)*24)
        else:
            self.Fixed.put(self.button,230,(self.columnas+6)*12)
        self.button.set_size_request(200,30)
        self.button.show()

        self.button=gtk.Button(None)
        self.button.set_image(gtk.Image())
        self.button.set_relief(gtk.RELIEF_NONE)
        self.button.get_image().set_from_pixbuf(self.smiley[0])
        self.button.connect("clicked",self.CrearTablero,self.filas,self.columnas,self.NumeroMinas)
        if self.columnas<20:
            self.Fixed.put(self.button,self.filas+100,(self.columnas)*24)
        else:
            self.Fixed.put(self.button,self.filas+300,(self.columnas)*12)
        self.button.set_size_request(45,45)
        self.button.show()

        self.button=gtk.Button("#")
        self.button.connect("clicked",self.Defensa,lista,self.filas,self.columnas)
        if self.columnas<20:
            self.Fixed.put(self.button,self.filas+175,(self.columnas*24))
        else:
            self.Fixed.put(self.button,self.filas+375,(self.columnas*12))
        self.button.set_size_request(45,45)
        self.button.show()

        Etq_minas=gtk.Label()
        Etq_minas.set_markup("<b>Numero de minas: </b>")
        if self.columnas<20:
            self.Fixed.put(Etq_minas,self.filas*2,(self.columnas+2)*24)
        else:
             self.Fixed.put(Etq_minas,self.filas*2,(self.columnas+2)*12)
        Etq_minas.show()

        Etq_minas1=gtk.Label(self.NumeroMinas)
        if self.columnas<20:
            self.Fixed.put(Etq_minas1,(self.filas+65)*2,(self.columnas+2)*24)
        else:
            self.Fixed.put(Etq_minas1,(self.filas+65)*2,(self.columnas+2)*12)
        Etq_minas1.show()

        self.Etq_marcadas=gtk.Label()
        self.Etq_marcadas.set_markup("<b>Numero de marcadas: </b>")
        if self.columnas<20:
            self.Fixed.put(self.Etq_marcadas,self.filas*2,(self.columnas+3)*24)
        else:
            self.Fixed.put(self.Etq_marcadas,self.filas*2,(self.columnas+3)*12)
        self.Etq_marcadas.show()

        self.Etq_marcadas1=gtk.Label(self.NumeroMarcadas)
        if self.columnas<20:
            self.Fixed.put(self.Etq_marcadas1,(self.filas+75)*2,(self.columnas+3)*24)
        else:
            self.Fixed.put(self.Etq_marcadas1,(self.filas+75)*2,(self.columnas+3)*12)
        self.Etq_marcadas1.show()

        self.Mensaje="Prueba"
        self.Avisos=gtk.Label(self.Mensaje)
        if columnas<20:
            self.Fixed.put(self.Avisos,self.filas*2,(self.columnas+4)*24)
        else:
            self.Fixed.put(self.Avisos,self.filas*2,(self.columnas+4)*12)

        if self.columnas<20:
            self.Fixed.put(self.etq_tpo,self.filas*1,(self.columnas)*24)
        else:       #Etiqueta del tiempo
            self.Fixed.put(self.etq_tpo,self.filas*1,(self.columnas)*11)
        fuente=pango.FontDescription("ani 20")
        self.etq_tpo.modify_font(fuente)
        self.etq_tpo.show()

        self.Fixed.show()
        alinear.show()
        self.window.show()

    def Defensa(self,widget,lista,filas,columnas):
        self.disponible=False
        for i in range(filas):
            for j in range(columnas):
                celda=lista[i][j]
                button=celda.boton
                if celda.mina==1:
                    button.get_image().set_from_pixbuf(self.imagenes[1])
                else:
                    button.get_image().set_from_pixbuf(self.imagenes[2])

    def LlenarMinas(self,lista,filas,columnas,minas):
        while minas>0:
            for i in range(filas):
                for j in range(columnas):
                    mina=random.randint(1,filas*columnas)
                    celda=lista[i][j]
                    if mina==5 and minas>0 and celda.mina!=1:
                        celda.mina=1
                        minas-=1
        for i in range(filas):
            for j in range(columnas):
                celda=lista[i][j]
                button=celda.boton
                button.connect("button-release-event",self.FinMina,lista,i,j,0)

    def LlenarMinasFich(self,lista,filas,columnas):
        counter=0
        for i in range(filas):
            for j in range(columnas):
                celda=lista[i][j]
                celda.mina=self.minado[counter]
                counter+=1
        for i in range(filas):
            for j in range(columnas):
                celda=lista[i][j]
                button=celda.boton
                button.connect("button-release-event",self.FinMina,lista,i,j,0)
  
#Programa principal
def main():
    gtk.main()
    return 0

if __name__=="__main__":
    Tablero()
    main()

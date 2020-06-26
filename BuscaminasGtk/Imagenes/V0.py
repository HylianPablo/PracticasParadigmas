import pygtk
pygtk.require('2.0')
import gtk
import random

class Table:

    def callback(self,widget,casilla):
        print casilla
        if casilla == 1:
            #self.window.hide()
            
            self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
            self.window.set_title("Fin.")
            self.window.set_border_width(20)
            self.window.set_size_request(200,100)
            tabla_final=gtk.Table(3,3)
            self.window.add(tabla_final)
            self.etiqueta=gtk.Label("Fin del juego ")
            tabla_final.attach(self.etiqueta,0,2,2,3)
            button =gtk.Button("Quit")
            button.connect("clicked",lambda w:gtk.main_quit())
            tabla_final.attach(button,0,2,0,1)
            self.etiqueta.show()
            button.show()
            tabla_final.show()
            self.window.show()
            

    def delete_event(self,widget,event,data=None):
        gtk.main_quit()
        return False

    def start(self,widget,tamanyo):
        self.window.hide()

        self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Buscaminas")
        self.window.set_border_width(20)
        self.window.set_size_request(400,400)

        self.window.connect("delete_event",self.delete_event)

        table=gtk.Table(tamanyo+2,tamanyo+2)
        self.window.add(table)

        oculta=[]
        minas=10

        for i in range(tamanyo):
            oculta.append([])
            for j in range(tamanyo):
                button=gtk.Button(None)
                table.attach(button,i,(i+1),j,(j+1))

                mina=random.randint(1,3)
                if mina == 2 and minas>0:
                    minas-=1
                    oculta[i].append(1)
                    casilla=1
                else:
                    oculta[i].append(0)
                    casilla=0
                button.set_image(gtk.Image())
                button.set_relief(gtk.RELIEF_NONE)
                button.get_image().set_from_pixbuf(self.imagenes[0])
                button.connect("clicked",self.callback,casilla)
                button.show()



        button =gtk.Button("Quit")
        button.connect("clicked",lambda w:gtk.main_quit())
        table.attach(button,0,tamanyo,tamanyo,tamanyo+1)
        button.show()

        table.show()
        self.window.show()

    def __init__(self):

        self.imagenes=[]
        self.imagenes.append(gtk.gdk.pixbuf_new_from_file("ycelda_cerrada.png"))
        self.imagenes.append(gtk.gdk.pixbuf_new_from_file("ycelda_mina.png"))

        self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Dificultad")
        self.window.set_border_width(20)
        self.window.set_size_request(200,100)
        

        datos=gtk.Label("Introduzca un numero")
        tabla=gtk.Table(3,3)
        tabla.attach(datos,0,2,0,1)

        self.button=gtk.Button("Comenzar facil")
        self.button.connect("clicked",self.start,9)
        tabla.attach(self.button,0,2,1,2)
        self.button.show()

        self.button=gtk.Button("Comenzar dificil")
        self.button.connect("clicked",self.start,11)
        tabla.attach(self.button,0,2,2,3)
        self.button.show()
        self.window.add(tabla)
        tabla.show()
        self.window.show()




def main():
    gtk.main()
    return 0
if __name__ == "__main__":
    Table()
    main()

import pygtk
pygtk.require('2.0')
import gtk
import time
import gobject

class Tiempo:

    def delete_event(self,widget,event,data=None):
        gtk.main_quit()
        return False

    def click(self):
        dt=int(time.time() - self.tpo0)
        self.etq_tpo.set_label("{0:02}:{1:02}".format(dt/60,dt%60))
        return True

    def __init__(self):
        self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Tiempo")
        self.window.connect("delete_event",self.delete_event)
        self.window.set_border_width(20)
        self.window.set_size_request(300,300)
        self.window.set_position(gtk.WIN_POS_CENTER)


        table=gtk.Table(2,2)
        self.window.add(table)
        self.etq_tpo=gtk.Label()
        table.attach(self.etq_tpo,0,1,0,1)
        for i in range(9999):
            self.tpo0=time.time()
            self.timer=gobject.timeout_add(1000,self.click)
            self.etq_tpo.show()
        table.show()
        self.window.show()

def main():
    gtk.main()
    return 0

if __name__=="__main__":
    Tiempo()
    main()

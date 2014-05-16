from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title = "SimpleWindow")
        self.button = Gtk.Button(label = "Click Me")
        self.button.connect("clicked" , Gtk.main_quit)
        self.add(self.button)
        
    def on_clicked_button(self,widget):
        print "Hey You clicked a button"
    
win = MyWindow()
trash = win.connect("delete-event" , Gtk.main_quit)

win.show_all()
Gtk.main()
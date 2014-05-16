from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title = "Using Boxes")
        
        self.box = Gtk.Box(spacing = 100)
        
        self.add(self.box)
        
        self.button1 = Gtk.Button(label = "Hey Man !!")
        self.button1.connect("clicked" , self.on_clicked_button1)
        self.button1.set_focus_on_click(True)
        #self.button1.set_alignment(0.0,1.0)
        self.box.pack_start(self.button1 , True ,False ,5)
        
      
      
      
        self.button2 = Gtk.Button(label = "Good Bye !!")
        self.button2.connect("clicked", self.on_clicked_button2)
        self.box.pack_start(self.button2 ,True,False ,10)
        
        
        
        
    def on_clicked_button1(self , widget):
        print "You have clicked \"Hey Man Button\""
    def on_clicked_button2(self ,widget):
        print "You have clicked \"Good Bye Button\""
            
            
win = MyWindow()
win.connect("delete-event" , Gtk.main_quit)
win.set_size_request(600,100)
win.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
win.set_default_icon_from_file("/home/yash/Desktop/GTK/logo.png")
win.show_all()
Gtk.main()
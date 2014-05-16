from gi.repository import Gtk,Gdk
import webbrowser


class GridWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title = "Grid Example")
        
        self.set_border_width(15)
        
        self.vbox = Gtk.VBox(False,0)
       
        self.hbox = Gtk.HBox(False,2)
        label = Gtk.Label()
        label.set_markup("<span font_desc=\"25.0\" font_family = \"monospace\" weight = \"heavy\" color = \"#FFFFFF\">SDSLabs !!</span>")
        label.set_line_wrap(True)
        self.hbox.pack_start(label,True,True,0)
        
        
        self.grid = Gtk.Table(2,3,True)
        self.grid.set_row_spacings(20)
        self.grid.set_col_spacings(20)
        #self.add(self.grid)
        
# ....................................Defining Each Cell of the table !!..................................
        self.Muzi = Gtk.Button(label = None)
        self.Muzi.connect("clicked" , self.on_clicked_Muzi)
        self.Muzi.set_focus_on_click(True)
        self.Muzi_image = Gtk.Image()
        self.Muzi_image.set_from_file("/home/yash/Desktop/GTK/muzi.jpg")
        self.Muzi_image.show()
        self.Muzi.add(self.Muzi_image)
        
        
        self.CV = Gtk.Button(label = None)
        self.CV.connect("clicked" , self.on_clicked_CV)
        self.CV.set_focus_on_click(True)
        self.CV_image = Gtk.Image()
        self.CV_image.set_from_file("/home/yash/Desktop/GTK/cv.jpg")
        self.CV_image.show()
        self.CV.add(self.CV_image)
        
        
        self.SP = Gtk.Button(label = None)
        self.SP.connect("clicked" , self.on_clicked_SP)
        self.SP.set_focus_on_click(True)
        self.SP_image = Gtk.Image()
        self.SP_image.set_from_file("/home/yash/Desktop/GTK/sp.jpg")
        self.SP_image.show()
        self.SP.add(self.SP_image)
    
    
        self.erodos = Gtk.Button(label = None)
        self.erodos.connect("clicked" , self.on_clicked_erodos)
        self.erodos.set_focus_on_click(True)
        self.erodos_image = Gtk.Image()
        self.erodos_image.set_from_file("/home/yash/Desktop/GTK/erdos.jpg")
        self.erodos_image.show()
        self.erodos.add(self.erodos_image)
        
        
        self.echo = Gtk.Button(label = None)
        self.echo.connect("clicked" , self.on_clicked_echo)
        self.echo.set_focus_on_click(True)
        self.echo_image = Gtk.Image()
        self.echo_image.set_from_file("/home/yash/Desktop/GTK/echo.jpg")
        self.echo_image.show()
        self.echo.add(self.echo_image)
        
        
        self.filepanda = Gtk.Button(label = None)
        self.filepanda.connect("clicked" , self.on_clicked_filepanda)
        self.filepanda.set_focus_on_click(True)
        self.filepanda_image = Gtk.Image()
        self.filepanda_image.set_from_file("/home/yash/Desktop/GTK/filepanda.jpg")
        self.filepanda_image.show()
        self.filepanda.add(self.filepanda_image)
        
#...............................Table Cell Define Ends here ................................        

        label_Muzi = Gtk.Label()
        label_Muzi.set_markup("<span font_desc=\"10.0\" font_family = \"monospace\" weight = \"light\" color = \"#FF0000\">Muzi</span>")
        label_Muzi.set_line_wrap(True)
        vbox_Muzi = Gtk.VBox(False,2)
        vbox_Muzi.pack_start(self.Muzi,False,False,0)
        vbox_Muzi.pack_start(label_Muzi,False,False,0)
        self.grid.attach(vbox_Muzi,0,1,0,1)
        
        
        label_CV = Gtk.Label()
        label_CV.set_markup("<span font_desc=\"10.0\" font_family = \"monospace\" weight = \"light\" color = \"#FF0000\">CodeVillage</span>")
        label_CV.set_line_wrap(True)
        vbox_CV = Gtk.VBox(False,2)
        vbox_CV.pack_start(self.CV,False,False,0)
        vbox_CV.pack_start(label_CV,False,False,0)
        self.grid.attach(vbox_CV, 1, 2, 0, 1)
        
        label_SP = Gtk.Label()
        label_SP.set_markup("<span font_desc=\"10.0\" font_family = \"monospace\" weight = \"light\" color = \"#FF0000\">StudyPortal</span>")
        label_SP.set_line_wrap(True)
        vbox_SP = Gtk.VBox(False,2)
        vbox_SP.pack_start(self.SP,False,False,0)
        vbox_SP.pack_start(label_SP,False,False,0)
        self.grid.attach(vbox_SP , 2,3,0,1)
        
        label_erodos = Gtk.Label()
        label_erodos.set_markup("<span font_desc=\"10.0\" font_family = \"monospace\" weight = \"light\" color = \"#FF0000\">Erdos</span>")
        label_erodos.set_line_wrap(True)
        vbox_erodos = Gtk.VBox(False,2)
        vbox_erodos.pack_start(self.erodos,False,False,0)
        vbox_erodos.pack_start(label_erodos,False,False,0)
        self.grid.attach(vbox_erodos ,0,1,1,2)
        
        
        label_echo = Gtk.Label()
        label_echo.set_markup("<span font_desc=\"10.0\" font_family = \"monospace\" weight = \"light\" color = \"#FF0000\">Echo</span>")
        label_echo.set_line_wrap(True)
        vbox_echo = Gtk.VBox(False,2)
        vbox_echo.pack_start(self.echo,False,False,0)
        vbox_echo.pack_start(label_echo,False,False,0)
        self.grid.attach(vbox_echo, 1, 2, 1, 2)
        
        
        label_filepanda = Gtk.Label()
        label_filepanda.set_markup("<span font_desc=\"10.0\" font_family = \"monospace\" weight = \"light\" color = \"#FF0000\">Filepanda</span>")
        label_filepanda.set_line_wrap(True)
        vbox_filepanda = Gtk.VBox(False,2)
        vbox_filepanda.pack_start(self.filepanda,False,False,0)
        vbox_filepanda.pack_start(label_filepanda,False,False,0)
        self.grid.attach(vbox_filepanda, 2, 3, 1, 2)
      
        self.vbox.pack_start(self.hbox,False,False,5)
        self.vbox.pack_start(self.grid,False,False,0)
        self.add(self.vbox)
        
    def on_clicked_Muzi(self , widget,data = None):
        url = "https://sdslabs.co.in/muzi/"
        webbrowser.open(url,new = 2)
        print "Opening Muzi !! :)"
        print data
    
    def on_clicked_CV(self , widget):
        url = "https://codevillage.sdslabs.co.in/"
        webbrowser.open(url,new = 2)
        print "Opening codevillage !! :)"
        
    def on_clicked_SP(self , widget):
        url = "https://study.sdslabs.co.in/"
        webbrowser.open(url,new = 2)
        print "Opening Study Portal !! :)" 
    
    def on_clicked_erodos(self , widget):
        url = "http://erdos.sdslabs.co/login/"
        webbrowser.open(url,new = 2)
        print "Opening Erdos !! :)"
    
    def on_clicked_echo(self , widget):
        url = "https://echo.sdslabs.co.in/"
        webbrowser.open(url,new = 2)
        print "Opening Echo !! :)"
    
    def on_clicked_filepanda(self , widget):
        url = "https://filepanda.sdslabs.co.in/"
        webbrowser.open(url,new = 2)
        print "Opening Filepanda !! :)"
        

win = GridWindow()
win.connect("delete-event" , Gtk.main_quit)
win.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0.6745, 0.6745, 0.6745, 0))
#win.set_size_request(600,600)
win.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
win.set_default_icon_from_file("/home/yash/Desktop/GTK/logo.png")
win.show_all()
Gtk.main()

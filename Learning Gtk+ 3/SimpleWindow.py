
from gi.repository import Gtk


def on_clicked_button(widget):
	print "You have clicked a button !! ;)"
	print label.get_label()

win = Gtk.Window(title = "Simple Window !!")
win.connect("delete-event",Gtk.main_quit)


label = Gtk.Label()
label.set_label("Clicking Again !!")
label.set_angle(25)
label.set_halign(Gtk.Align.END)

button = Gtk.Button(label = "Yashpal")
handler_id = button.connect("clicked" , on_clicked_button)

#button.disconnect(handler_id)
win.add(button)
win.set_size_request(600,100)
win.show_all()
Gtk.main()


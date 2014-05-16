from gi.repository import Gtk, GObject
import urllib2
import threading
import os,sys
import time 

class ProgressWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self , title = "Download Progress !! " )
		self.set_resizable(False)
		self.set_border_width(10)
		self.set_size_request(400,200)
		self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
		self.vbox = Gtk.VBox(False , 2)
		self.add(self.vbox)
		self.label = Gtk.Label("Downloading the Requested file !!")
		self.vbox.pack_start(self.label,False,False,0)
		self.Progressbar = Gtk.ProgressBar()
		self.vbox.pack_start(self.Progressbar, False, True, 0)
		self.Progressbar.set_show_text(True)
		self.Progressbar.set_fraction(0.0)
		#self.timeout_id = GObject.timeout_add(50, self.on_timeout, None)
		self.scrolledwindow = Gtk.ScrolledWindow()
		self.scrolledwindow.set_hexpand(True)
		self.scrolledwindow.set_vexpand(True)
		self.scrolledwindow.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
		self.treestore = Gtk.TreeStore(str)
		self.details = self.treestore.append(None , ["Details :"])
		self.treestore.append(self.details , ["Downloading file from requested url"])
		self.data_download = self.treestore.append(self.details , ["Receving 0 out of 0 Bytes !!"])
		#self.speed = self.treestore.append(self.details , ["Downloading Speed : 0.0 KB/s"])
		
		
		self.treeview = Gtk.TreeView(model=self.treestore)
		treeviewcolumn = Gtk.TreeViewColumn("Expand to get more details !!")
		self.treeview.append_column(treeviewcolumn)
		cellrenderertext = Gtk.CellRendererText()
		treeviewcolumn.pack_start(cellrenderertext, True)
		treeviewcolumn.add_attribute(cellrenderertext, "text", 0)
		self.remove_index(2)
		self.vbox.pack_start(self.scrolledwindow ,True,True ,0)
		
		self.scrolledwindow.add(self.treeview)		
		

		

		self.connect("delete-event" , Gtk.main_quit)
		self.show_all()
	def on_timeout(self,user_data):
		current_fraction = self.Progressbar.get_fraction()
		if current_fraction >= 1.0:
			new_fraction = 0.0
		else :
			new_fraction = current_fraction + 0.05
		
		self.Progressbar.set_fraction(new_fraction)
		return True
	def set_progress(self , value):
		if value >= 1.0 :
			self.Progressbar.set_fraction(1)
		else :
			self.Progressbar.set_fraction(value)
	def remove_index(self,index):
		temp = self.treestore.get_iter_first()
		#treestore.iter_nth_child(parent, n)
		#self.treestore.remove(self.speed)
		#self.speed = self.treestore.append(self.details,["Mohit"])
		
	def run(self):
		Gtk.main()


class DownloadFile(threading.Thread):
	def __init__(self,url,win):
		threading.Thread.__init__(self)
		self.url = url
		self.win = win

	def run(self):
		
		temp = self.url.split(".")[-1]
		if temp.startswith("com"):
			temp = "html"
		
		urlfile = urllib2.urlopen(self.url)
		meta  = urlfile.info()
		size = 100000
		if meta.getheaders("Content-Length"):
			size = int(meta.getheaders("Content-Length")[0])
		current_path = os.getcwd()
		download_path = os.path.join(os.getcwd() , "download."+temp)
		
		filename = open(download_path , "wb")
		downloaded_bytes = 0
		chunk_size = 1024*32
		
		while 1:
			start_time = time.time()
			data = urlfile.read(chunk_size)
			if not data:
				print "Hurry Download Complete"
				break
			filename.write(data)
			get = 32.0/(time.time()-start_time)
			downloaded_bytes += len(data)*1.0
			win.treestore.remove(win.treestore.iter_next(win.treestore.iter_children(win.treestore.get_iter_first())))
			win.treestore.append(win.treestore.get_iter_first(),["Downloading Speed : %0.2f KB/s" % get])
			#win.treestore.remove(win.data_download)
			#win.data_download = win.treestore.append(win.details,["Receving %d out of %d Bytes !!" % (downloaded_bytes , size)])
			#print "Speed of downloading %0.2f" % get
			
			fraction = downloaded_bytes/(size*1.0)
			win.set_progress(fraction)



		
if __name__ == '__main__':
	win = ProgressWindow()
	#url = "http://www.comp.nus.edu.sg/~stevenha/myteaching/competitive_programming/cp1.pdf"
	url = raw_input("Enter the Url : ")	
	try :
		obj = DownloadFile(url,"win")
		obj.start()
		win.run()
	except:
		print "Exception ocurred !!"
		obj = DownloadFile(url,"win")
		obj.start()
		win.run()
		
	
	

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class DaWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Pajton")
        self.set_default_size(400, 200)
        self.showMe()
        self.box = Gtk.Box(Gtk.Orientation.VERTICAL, spacing=10)
        self.grid = Gtk.Grid()
        self.add(self.grid)

        self.button1 = Gtk.Button(label="Załaduj")
        self.button1.connect("clicked", self.on_button1_clicked)

        self.button2 = Gtk.Button(label="Tłumacz")
        self.button2.connect("clicked", self.on_button2_clicked)

        self.button3 = Gtk.Button(label="Zapisz")
        self.button3.connect("clicked", self.on_button3_clicked)

        self.grid.add(self.button1)
        self.grid.attach(self.button2, 1, 0, 1, 1)
        self.grid.attach(self.button3, 2, 0, 1, 1)

        scrolledwindow_left = Gtk.ScrolledWindow()
        scrolledwindow_left.set_hexpand(True)
        scrolledwindow_left.set_vexpand(True)
        self.grid.attach(scrolledwindow_left, 0, 1, 1, 1)
        self.textview_left = Gtk.TextView()
        self.textbuffer_left = self.textview_left.get_buffer()
        self.textbuffer_left.set_text("Left!.")
        scrolledwindow_left.add(self.textview_left)

        scrolledwindow_right = Gtk.ScrolledWindow()
        scrolledwindow_right.set_hexpand(True)
        scrolledwindow_right.set_vexpand(True)
        self.grid.attach(scrolledwindow_right, 2, 1, 1, 1)
        self.textview_right = Gtk.TextView()
        self.textbuffer_right = self.textview_right.get_buffer()
        self.textbuffer_right.set_text("Right!.")
        scrolledwindow_right.add(self.textview_right)

    def on_button1_clicked(self, widget):
        print("Loaded")

    def on_button2_clicked(self, widget):
        print("Translated")

    def on_button3_clicked(self, widget):
        print("Saved")

    def on_button_clicked(self, widget):
        print("Hello World")

    def showMe(self):
        print('Showing the window')


win = DaWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
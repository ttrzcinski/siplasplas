import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class DaWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Pajton")
        self.set_default_size(400, 200)
        self.showMe()
        self.box = Gtk.Box(Gtk.Orientation.VERTICAL, spacing=10)
        grid = Gtk.Grid()
        self.add(grid)

        self.button1 = Gtk.Button(label="Załaduj")
        self.button1.connect("clicked", self.on_button1_clicked)

        self.button2 = Gtk.Button(label="Tłumacz")
        self.button2.connect("clicked", self.on_button2_clicked)

        self.button3 = Gtk.Button(label="Zapisz")
        self.button3.connect("clicked", self.on_button3_clicked)

        grid.add(self.button1)
        grid.attach(self.button2, 1, 0, 1, 1)
        grid.attach(self.button3, 2, 0, 1, 1)

        self.create_textview()


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

    def create_textview(self):
        scrolledwindow_left = Gtk.ScrolledWindow()
        scrolledwindow_left.set_hexpand(True)
        scrolledwindow_left.set_vexpand(True)
        self.grid.attach(scrolledwindow_left, 0, 1, 1, 1)

        scrolledwindow_right = Gtk.ScrolledWindow()
        scrolledwindow_right.set_hexpand(True)
        scrolledwindow_right.set_vexpand(True)
        self.grid.attach(scrolledwindow_right, 3, 1, 1, 1)

        self.textview = Gtk.TextView()
        self.textbuffer = self.textview.get_buffer()
        self.textbuffer.set_text("This is some text inside of a Gtk.TextView. "
                                 + "Select text and click one of the buttons 'bold', 'italic', "
                                 + "or 'underline' to modify the text accordingly.")
        scrolledwindow.add(self.textview)


win = DaWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
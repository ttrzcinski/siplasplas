import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class DaWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Pajton")
        self.set_default_size(400, 200)
        #self.button = Gtk.Button(label="Click Here")
        #self.button.connect("clicked", self.on_button_clicked)
        #self.add(self.button)
        self.showMe()

    def on_button_clicked(self, widget):
        print("Hello World")

    def showMe(self):
        print('Showing the window')

win = DaWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
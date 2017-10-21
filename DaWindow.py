import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import configparser

# Rightful code
import os


class DaWindow(Gtk.Window):
    FILE_NAME = ""
    dictionaries = {}
    text_file = ''
    file_extension = ''
    file_name = ''
    file_content = []

    my_dictionary = {
        "if": "jeżeli",
        "else": "przeciwnie",
        "then": "wtedy",
        "format": "formatuj",
        "for": "dla",
        "loop": "zapętl",
        "while": "podczas",
        "do": "rób",
        "define": "zdefiniuj",
        "import": "importuj",
        "main": "główna",
        "class": "klasa",
        "string": "łańcuch",
        "integer": "całkowita",
        "float": "ułamek",
        "double": "długiułamek",
        "byte": "bajt",
        "array": "tablica",
        "list": "lista",
        "set": "zestaw",
        "hash": "hasz",
        "map": "mapa",
        "include": "załącz",
        "self": "sam",
        "id": "identyfikator",
        "def": "definicja",
        "your": "twoja",
        "momma": "mamusia",
        "polish": "polski",
        "python": "pajton",
        "package": "pakiet",
        "line": "linia",
        "split": "podziel",
        "replace": "podmień",
        "return": "zwróć",
        "result": "rezultat",
        "false": "fałsz",
        "true": "prawda",
        "rightful": "prawilny",
        "code": "kod",
        "letters": "litery",
        "letter": "litera",
        "translate": "tłumacz",
        "length": "długość",
        "width": "szerokość",
        "height": "wysokość",
        "word": "słowo",
        "file": "plik",
        "name": "nazwa",
        "in": "w",
        "da": "ten",
        "table": "tablica",
        "print": "wypisz",
        "lower": "do_małych",
        "upper": "do_wielkich",
        "close": "zamknij",
        "size": "rozmiar",
        "new": "nowy"
    }

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

        languages_definitions = [file for file in os.listdir("languages") if file.endswith('.ini')]
        for definition in languages_definitions:
            parser = configparser.ConfigParser()
            parser.read(os.path.join("languages", definition))
            new_dict = {}
            for word in parser.items('words'):
                new_dict[word[0]] = word[1]
            self.dictionaries[parser.get('language', 'extension')] = new_dict

    def on_button1_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose a file", self,
                                       Gtk.FileChooserAction.OPEN,
                                       (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                        Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            self.FILE_NAME = dialog.get_filename()

        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        if self.FILE_NAME:
            self.read_file(self.FILE_NAME)
            for line in self.text_file:
                self.file_content.append(line)
            self.textview_left.get_buffer().set_text("\n".join(self.file_content))

        dialog.destroy()

    def add_filters(self, dialog):
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)

        filter_py = Gtk.FileFilter()
        filter_py.set_name("Python files")
        filter_py.add_mime_type("text/x-python")
        dialog.add_filter(filter_py)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)

    def on_button2_clicked(self, widget):
        print("Translated")
        # self.translate_file(self.file_extension, self.file_name, self.text_file)
        result = self.translate_2("py", "\n".join(self.file_content))
        self.textview_right.get_buffer().set_text(result)

    def on_button3_clicked(self, widget):
        print("Saved")

    def on_button_clicked(self, widget):
        print("Hello World")

    def showMe(self):
        print('Showing the window')

    def translate_file(self, extension, file_name, text_file):
        if self.dictionaries.get(extension, False):
            # Przetworznie według kluczy ze słownika - linia po linii
            i = 0
            da_new_file = []
            print('Tlumaczenie:')
            for line in text_file:
                # Tlumacz linie jako calosc
                da_new_line = self.translate_2(extension, line.lower().rstrip('\n'))
                print('#{0}: {1}'.format(i, da_new_line))
                da_new_file.append(da_new_line)
                i += 1
            text_file.close()
            self.save_file(da_new_file, file_name)
            print("\n\nKoniec-Pliku")
        else:
            print("Format pliku nieobługiwany.")

    def read_file(self, file_name):
        # Odczyt pliku
        text_file = ""
        try:
            self.text_file = open(file_name)
            print("\nOdczytywac plik {}:".format(file_name))
        except FileNotFoundError:
            print('Nie ma takiego {0}..'.format(text_file))
            return

        self.file_extension = os.path.splitext(file_name)[1][1:]

    def save_file(self, da_new_file, old_file_name):
        with open("translated_" + old_file_name, 'w') as file_handler:
            file_handler.write("\n".join(da_new_file))

    def translate(self, line):
        result = line
        for elem in line.split(" "):
            if len(elem) > 0:
                if self.my_dictionary.get(elem, False):
                    result = result.replace(elem, self.my_dictionary[elem])
        return result

    def translate_2(self, extension, line):
        result = line
        letters = list(line)
        word = ""
        for letter in letters:
            if not letter.isalpha():
                word = ""
            else:
                word += letter
                if len(word) > 0:
                    if self.dictionaries.get(extension, False).get(word, False):
                        result = result.replace(word, self.dictionaries[extension][word])
        return result


win = DaWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

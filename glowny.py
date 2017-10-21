import configparser

# Rightful code
import os


class Jebaka:
    dictionaries = {}

    def __init__(self):
        languages_definitions = [file for file in os.listdir("languages") if file.endswith('.ini')]
        for definition in languages_definitions:
            parser = configparser.ConfigParser()
            parser.read(os.path.join("languages", definition))
            new_dict = {}
            for word in parser.items('words'):
                new_dict[word[0]] = word[1]
            self.dictionaries[parser.get('language', 'extension')] = new_dict

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

    def main(self):
        # Odczyt nazwy pliku
        file_name = input('Podaj nazwe pliku do przerobienia> ')
        file_extension = os.path.splitext(file_name)[1][1:]
        print(file_extension)

        # Odczyt pliku
        text_file = ""
        try:
            text_file = open(file_name)
            print("\nOdczytywac plik {}:".format(file_name))
        except FileNotFoundError:
            print('Nie ma takiego {0}..'.format(text_file))
            return

        self.translate_file(file_extension, file_name, text_file)

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
            # Zapis do pliku
            # TODO GET TIMESTAMP
            # TODO concatenate it in file name
            # f = open('myfile', 'w')
            # f.write('hi there\n')  # python will convert \n to os.linesep
            # f.close()
        else:
            print("Format pliku nieobługiwany.")

    def save_file(self, da_new_file, old_file_name):
        with open("translated_" + old_file_name, 'w') as file_handler:
            file_handler.write("\n".join(da_new_file))


if __name__ == "__main__":
    a = Jebaka()
    a.main()

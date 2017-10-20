# Rightful code
class Jebaka:
    my_dictionary = {"if": "jeżeli",
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

    def translate_2(self, line):
        result = line
        letters = list(line)
        word = ""
        for letter in letters:
            if not letter.isalpha():
                word = ""
            else:
                word += letter
                if len(word) > 0:
                    if self.my_dictionary.get(word, False):
                        result = result.replace(word, self.my_dictionary[word])
        return result

    def main(self):
        # Odczyt nazwy pliku
        file_name = input('Podaj nazwe pliku do przerobienia:')

        # Odczyt pliku
        text_file = ""
        try:
            text_file = open(file_name)
            print("\nOdczytywac plik {}:".format(file_name))
        except FileNotFoundError:
            print('Nie ma takiego {0}..'.format(text_file))
            return

        # Przetworznie według kluczy ze słownika - linia po linii
        i = 0
        da_new_file = "";
        for line in text_file:
            # Tlumacz linie jako calosc
            da_new_line = self.translate_2(line.lower().rstrip('\n'))
            print('Linia {0} przetłumaczona na: {1}'.format(i, da_new_line))
            da_new_file += da_new_line
            i += 1
        text_file.close()
        print("\n\nKoniec-Pliku")
        # Zapis do pliku


if __name__ == "__main__":
    a = Jebaka()
    a.main()

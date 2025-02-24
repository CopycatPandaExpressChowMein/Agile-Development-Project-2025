from File_handling import save_bin_file, load_bin_file

class Data_handler:
    # Privat dictionary för att lagra data
    __data_dictionary = {}

    def __init__(self, dictionary=None):
        """ Konstruktor: Initierar dictionary. Laddar från fil om det finns. """
        if dictionary is None:
            self.__data_dictionary = load_bin_file("entry.bin") or {}  # Ladda från fil eller skapa nytt
        else:
            self.__data_dictionary = dictionary

    def add_to_dict(self, key, value):
        """ Lägger till ett nytt värde i dictionary och sparar det. """
        if not isinstance(key, str) or not key.strip():
            raise ValueError("Ogiltig nyckel. Måste vara en icke-tom sträng.")

        self.__data_dictionary[key] = value
        save_bin_file(self.__data_dictionary, "entry.bin")  # Spara efter ändring

    def remove_from_dict(self, key):
        """ Tar bort ett värde från dictionary och sparar ändringen. """
        if key in self.__data_dictionary:
            del self.__data_dictionary[key]
            save_bin_file(self.__data_dictionary, "entry.bin")  # Uppdatera filen
        else:
            raise KeyError(f"Nyckeln '{key}' finns ej i dictionary.")

    def get_from_dict(self, key):
        """ Hämtar ett värde från dictionary med en given nyckel. """
        return self.__data_dictionary.get(key, None)  # Returnerar None om nyckeln ej finns

    def get_all_data(self):
        """ Returnerar hela dictionaryn. """
        return self.__data_dictionary

    def clear_data(self):
        """ Rensar all sparad data och sparar en tom dictionary. """
        self.__data_dictionary.clear()
        save_bin_file(self.__data_dictionary, "entry.bin")  # Spara tom dictionary


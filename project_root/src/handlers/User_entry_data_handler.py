from src.handlers.File_handling import *
import uuid

class Data_handler:
    # Privat dictionary för att lagra data
    __data_dictionary = None

    SAVEPATH = "/bin"
    FILENAME = "data"

    #Konstruktör, går att passera en fylld dictionary. 
    #Ifall inget värde passeras till konstruktören så används en tom dictionary som default
    def __init__(self):  
            self.__data_dictionary = load_bin_file(self.FILENAME+".bin", self.SAVEPATH)



    def add_to_dict(self, key, value):
        """ Lägger till ett nytt värde i dictionary och sparar det. """
        self.__data_dictionary[key] = value
        save_bin_file(self.__data_dictionary, self.FILENAME+".bin", self.SAVEPATH)  # Spara efter ändring

    def remove_from_dict(self, key):
        """ Tar bort ett värde från dictionary och sparar ändringen. """
        if key in self.__data_dictionary:
            del self.__data_dictionary[key]
            save_bin_file(self.__data_dictionary, self.FILENAME+".bin", self.SAVEPATH)  # Uppdatera filen
        else:
            raise KeyError(f"Nyckeln '{key}' finns ej i dictionary.")
    
    def get_from_dict(self, key):
        """ Hämtar ett värde från dictionary med en given nyckel. """
        return self.__data_dictionary.get(key, None)  # Returnerar None om nyckeln ej finns

    def get_all_data(self):
        """ Returnerar hela dictionaryn. """
        return self.__data_dictionary
    
    def get_all_keys(self):
        return self.__data_dictionary.keys()

    def clear_data(self):
        """ Rensar all sparad data och sparar en tom dictionary. """
        self.__data_dictionary.clear()
        save_bin_file(self.__data_dictionary, self.FILENAME+".bin", self.SAVEPATH)  # Spara tom dictionary



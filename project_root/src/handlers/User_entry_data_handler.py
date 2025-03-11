from src.handlers.File_handling import *

import uuid

class Data_handler:
    # Privat dictionary för att lagra data
    __data_dictionary = None
    __cloud_handler = None
    __UUID = None

    SAVEPATH = "/bin"
    FILENAME = "data"

    #Konstruktör, går att passera en fylld dictionary. 
    #Ifall inget värde passeras till konstruktören så används en tom dictionary som default
    def __init__(self, cloud_handler=None): 

            print("Constructing object of type data handler...") 
            
            self.__UUID = load_bin_file("user_info.bin", self.SAVEPATH)
            if not isinstance(self.__UUID, str):
                self.__UUID = str(uuid.uuid4())
                save_bin_file(self.__UUID, "user_info.bin", self.SAVEPATH)
            
            self.__cloud_handler = cloud_handler
            self.__data_dictionary = load_bin_file(self.FILENAME+".bin", self.SAVEPATH)
            
            


    def add_to_dict(self, key, value):
        """ Lägger till ett nytt värde i dictionary och sparar det. """

        print(f"Adding {key} and {value} to dictionary...")

        self.__data_dictionary[key] = value
        save_bin_file(self.__data_dictionary, self.FILENAME+".bin", self.SAVEPATH)  # Spara efter ändring
        if self.__cloud_handler != None:
            self.__cloud_handler.add_user_entries(self.__UUID, self.__data_dictionary)

    def remove_from_dict(self, key):
        """ Tar bort ett värde från dictionary och sparar ändringen. """

        print(f"Removing {key} and associated value from dictionary...")

        if key in self.__data_dictionary:
            del self.__data_dictionary[key]
            save_bin_file(self.__data_dictionary, self.FILENAME+".bin", self.SAVEPATH)  # Uppdatera filen

            print("Checking for cloud connection...")

            if self.__cloud_handler != None:

                print("Cloud connection found, adding to cloud...")

                self.__cloud_handler.add_user_entries(self.__UUID, self.__data_dictionary)
        else:
            raise KeyError(f"Nyckeln '{key}' finns ej i dictionary.")
    
    def get_from_dict(self, key):
        """ Hämtar ett värde från dictionary med en given nyckel. """

        print(f"Finding value associated with {key}...")

        return self.__data_dictionary.get(key, None)  # Returnerar None om nyckeln ej finns

    def get_all_data(self):
        """ Returnerar hela dictionaryn. """

        print("Returning complete dictionary...")

        return self.__data_dictionary
    
    def get_all_keys(self):

        print("Returning all keys...")

        return self.__data_dictionary.keys()

    def clear_data(self):
        """ Rensar all sparad data och sparar en tom dictionary. """

        print("Removing all data in dictionary...")

        self.__data_dictionary.clear()
        save_bin_file(self.__data_dictionary, self.FILENAME+".bin", self.SAVEPATH)  # Spara tom dictionary
        if self.__cloud_handler != None:
            self.__cloud_handler.add_user_entries(self.__UUID, self.__data_dictionary)

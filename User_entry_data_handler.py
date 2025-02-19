from File_handling import *

class Data_handler():
    #Privat dictionary, nyckel och värde par
    __data_dictionary = {}

    #Konstruktör, går att passera en fylld dictionary. 
    #Ifall inget värde passeras till konstruktören så används en tom dictionary som default
    def __init__(self, dictionary = {}):
        self.__data_dictionary = dictionary

    #Lägger till item i dictionary, nyckel : värde, där nyckeln är datum och värde är en user entry
    def add_to_dict(self, key, object):
        self.__data_dictionary.update({key : object})
        save_bin_file(self.__data_dictionary, "entry.bin")
        

    #Tar bort ett värde från dictionary, passera en key, som datum
    def remove_from_dict(self, key):
        self.__data_dictionary.pop(key)
    
    #Hämtar och returnerar ett värde från dictionary. Ifall det finns.
    def get_from_dict(self, key):
        return self.__data_dictionary.get(key)
    
    def get_all_keys(self):
        return self.__data_dictionary.keys()
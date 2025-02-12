#Besart was here

class User_entry:

    #Dubbel understreck för private
    __wellbeing = None
    __alcohol_boolean = None
    __drug_boolean = None
    __notes = None

    #__init__ funktionen är en inbyggd funktion (Konstruktör)
    # wellbeing = Heltals värde för mående (Int)
    # alcohol_boolean = sant/falskt, har man druckit? (Boolean)
    # drug_boolean = sant/falskt, har man missbrukat? (Boolean)
    # notes = egna anteckningar som text (String)
    def __init__(self, wellbeing, alcohol_boolean, drug_boolean, notes):
        self.__wellbeing = wellbeing
        self.__alcohol_boolean = alcohol_boolean
        self.__drug_boolean = drug_boolean
        self.__notes = notes

    #Returnerar en string med variabler ifall man endast kallar på objektet själv
    def __str__(self):
        return f'''
Wellbeing: {self.__wellbeing}
Alcohol consumed: {self.__alcohol_boolean}
Drug abused: {self.__drug_boolean}
Notes: {self.__notes}
                '''
    
    #Get och sets för åtkomst
    #------------------------------------

    def set_wellbeing(self, wellbeing):
        self.__wellbeing = wellbeing

    def get_wellbeing(self):
        return self.__wellbeing
    
    def set_alcohol_boolean(self, alcohol_boolean):
        self.__alcohol_boolean = alcohol_boolean

    def get_alcohol_boolean(self):
        return self.__alcohol_boolean
    
    def set_drug_boolean(self, drug_boolean):
        self.__drug_boolean = drug_boolean

    def get_alcohol_boolean(self):
        return self.__drug_boolean
    
    def set_notes(self, notes):
        self.__notes = notes

    def get_notes(self):
        return self.__notes
    
    #------------------------------------


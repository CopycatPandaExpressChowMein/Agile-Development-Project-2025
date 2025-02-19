

class User_entry:

    #Dubbel understreck för private
    __wellbeing = None
    __anxiety = None
    __meals = None
    __connected_boolean = None
    __rest_boolean = None
    __exercise_boolean = None
    __alcohol_boolean = None
    __drug_boolean = None
    __notes = None

    #__init__ funktionen är en inbyggd funktion (Konstruktör)
    # wellbeing = Heltals värde för mående (Int)
    # alcohol_boolean = sant/falskt, har man druckit? (Boolean)
    # drug_boolean = sant/falskt, har man missbrukat? (Boolean)
    # notes = egna anteckningar som text (String)
    def __init__(self, wellbeing, anxiety, meals, connected_boolean, rest_boolean, exercise_boolean, alcohol_boolean, drug_boolean, notes):
        self.__wellbeing = wellbeing
        self.__anxiety = anxiety
        self.__meals = meals
        self.__connected_boolean = connected_boolean
        self.__rest_boolean = rest_boolean
        self.__exercise_boolean = exercise_boolean
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
    
    def set_anxiety(self, anxiety):
        self.__anxiety = anxiety

    def get_anxiety(self):
        return self.__anxiety
    
    def set_meals(self, meals):
        self.__meals = meals

    def get_meals(self):
        return self.__meals
    
    def set_connected_boolean(self, connected_boolean):
        self.__connected_boolean = connected_boolean

    def get_connected_boolean(self):
        return self.__connected_boolean
    
    def set_rest_boolean(self, rest_boolean):
        self.__rest_boolean = rest_boolean

    def get_rest_boolean(self):
        return self.__rest_boolean
    
    def set_exercise_boolean(self, exercise_boolean):
        self.__exercise_boolean = exercise_boolean

    def get_exercise_boolean(self):
        return self.__exercise_boolean
    
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


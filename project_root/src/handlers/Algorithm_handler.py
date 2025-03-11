class Algorithm_handler():
    
    __data = None

    def __init__(self, data):

        print("Constructing an object of type algorithm handler...")

        self.__data = data

    def wellbeing_statistics(self):
        """Itererar över alla nycklarna i datahanteraren.
            Lägger till värdet av wellbeing i en lista och returnerar listan"""

        wellbeing = []
        for key in self.__data.get_all_keys():

            user_entry = self.__data.get_from_dict(key)
            wellbeing.append(user_entry.get_wellbeing())
        return wellbeing

    def anxiety_statistics(self):
        """Itererar över alla nycklarna i datahanteraren.
            Lägger till värdet av anxiety i en lista och returnerar listan"""
        
        anxiety = []
        for key in self.__data.get_all_keys():

            user_entry = self.__data.get_from_dict(key)
            anxiety.append(user_entry.get_anxiety())
        return anxiety

    def meals_statistics(self):
        """Itererar över alla nycklarna i datahanteraren.
            Lägger till värder av meals i en lista och returnerar listan"""

        meals = []
        for key in self.__data.get_all_keys():
            user_entry = self.__data.get_from_dict(key)
            meals.append(user_entry.get_meals())
        return meals

    def average_statistics(self):
        """Itererar över alla nycklarna i datahanteraren.
            Kalkulerar det genomsnittliga värdet av alla värden. 
            Ger arbiträrt värde till booleans och returnerar lista."""

        average = []
        for key in self.__data.get_all_keys():
            
            
            user_entry = self.__data.get_from_dict(key)
            
            #Code for average 
            val = 40
            val -= user_entry.get_wellbeing()
            val -= user_entry.get_anxiety()
            val -= user_entry.get_meals()

            if(user_entry.get_connected_boolean()):
                val -= 3
            if(user_entry.get_rest_boolean()):
                val -= 3
            if(user_entry.get_exercise_boolean()):
                val -= 3
            if not (user_entry.get_alcohol_boolean()):
                val -= 8
            if not (user_entry.get_drug_boolean()):
                val -= 8
            
            
            average.append(val/8)
        return average
    
    def drug_boolean_pattern(self):
        """Iterar över alla nycklar, summerar varje "drug" boolean som är true och summan av alla dagar. 
            Returnerar True ifall summan av True booleans är mer än eller lika med hälften av mängden dagar"""

        temp_val = 0
        entry_num = 0
        for key in self.__data.get_all_keys():
            entry_num += 1
            if self.__data.get_from_dict(key).get_drug_boolean():
                temp_val += 1
        return temp_val >= entry_num/2

    def alcohol_boolean_pattern(self):
        """Iterar över alla nycklar, summerar varje "alcohol" boolean som är true och summan av alla dagar. 
            Returnerar True ifall summan av True booleans är mer än eller lika med hälften av mängden dagar"""

        temp_val = 0
        entry_num = 0
        for key in self.__data.get_all_keys():
            entry_num += 1
            if self.__data.get_from_dict(key).get_alcohol_boolean():
                temp_val += 1
        return temp_val >= entry_num/2

    def exercise_boolean_pattern(self):
        """Iterar över alla nycklar, summerar varje "exercise" boolean som är true och summan av alla dagar. 
            Returnerar True ifall summan av True booleans är mer än eller lika med hälften av mängden dagar"""

        temp_val = 0
        entry_num = 0
        for key in self.__data.get_all_keys():
            entry_num += 1
            if self.__data.get_from_dict(key).get_exercise_boolean():
                temp_val += 1
        return temp_val <= entry_num/2

    def rest_boolean_pattern(self):
        """Iterar över alla nycklar, summerar varje "rest" boolean som är true och summan av alla dagar. 
            Returnerar True ifall summan av True booleans är mer än eller lika med hälften av mängden dagar"""

        temp_val = 0
        entry_num = 0
        for key in self.__data.get_all_keys():
            entry_num += 1
            if self.__data.get_from_dict(key).get_rest_boolean():
                temp_val += 1
        return temp_val <= entry_num/2

    def connected_boolean_pattern(self):
        """Iterar över alla nycklar, summerar varje "connected" boolean som är true och summan av alla dagar. 
            Returnerar True ifall summan av True booleans är mer än eller lika med hälften av mängden dagar"""

        temp_val = 0
        entry_num = 0
        for key in self.__data.get_all_keys():
            entry_num += 1
            if self.__data.get_from_dict(key).get_connected_boolean():
                temp_val += 1
        return temp_val <= entry_num/2
        

    def entry_amount(self):
        """Räknar från 0 till antalet dagar, varje värde läggs till i en lista som returneras."""

        days = []
        num = 1
        for key in self.__data.get_all_keys():
            days.append(num)
            num += 1
        return days
    

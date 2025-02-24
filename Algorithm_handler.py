import num

class Algorithm_handler():
    
    __data = None

    def __init__(self, data):
        self.__data = data

    def wellbeing_statistics(self):
        wellbeing = []
        for key in self.__data.get_all_keys():
            user_entry = self.__data.get_from_dict(key)
            wellbeing.append(user_entry.get_wellbeing())
        return wellbeing

    def anxiety_statistics(self):
        anxiety = []
        for key in self.__data.get_all_keys():
            user_entry = self.__data.get_from_dict(key)
            anxiety.append(user_entry.get_anxiety())
        return anxiety

    def meals_statistics(self):
        meals = []
        for key in self.__data.get_all_keys():
            user_entry = self.__data.get_from_dict(key)
            meals.append(user_entry.get_meals())
        return meals

    def average_statistics(self):
        average = []
        for key in self.__data.get_all_keys():
            user_entry = self.__data.get_from_dict(key)
            
            #Code for average here

            average.append(user_entry.get_meals())
        return average

    def entry_amount(self):
        days = []
        num = 1
        for key in self.__data.get_all_keys():
            days.append(num)
            num += 1
        return days
from win11toast import toast
import random

class Notification_handler:
    __algorithm_handler = None

    __Encouraging_MESSAGES = ["Oh my! You're absolutely marvelous!", 
                              "You are capable of amazing things. Keep believing in yourself!", 
                              "Your hard work is paying off, even if you don’t see it yet. Keep going!", 
                              "You have the strength to overcome any challenge that comes your way.",
                              "You are enough, just as you are. Embrace your uniqueness!",
                              "Small steps lead to big changes. Keep moving forward, no matter how slow.",
                              "Today is a fresh start, filled with endless possibilities.",
                              "You bring so much light and positivity to the world. Don’t forget that!",
                              "Believe in your dreams, they’re closer than you think.",
                              "You have everything it takes to create the life you desire. Keep pushing!",
                              "Surround yourself with people whose eyes light up when they see you coming.",
                              "Slowly is the fastest way to get to where you want to be.",
                              "The top of one mountain is the bottom of the next."]

    def __init__(self, Algorithm_handler):
        
        print("Constructing an object of type notification handler...")

        self.__algorithm_handler = Algorithm_handler


    def show_notification(self):
        """Visar en notifikation, försöker generera text, ifall det inte går så 
            används en förbestämd text."""

        print("Showing notification...")

        try:
            __NOTIFICATION_TEXT, __NOTIFICATION_STYLE = self.get_notification_content()
        except:
            __NOTIFICATION_TEXT = "No entries found."
            __NOTIFICATION_STYLE = "reminder"

        toast("HabitTrack - Advice!", __NOTIFICATION_TEXT, scenario=__NOTIFICATION_STYLE)
        

    def get_notification_content(self):
        """Skapar text för notifikation, returnerar 2 strings med text och stil."""

        print("Generating notification text...")

        notification_text = ""
        notification_style = "reminder"

        Wellbeing = self.__algorithm_handler.average_statistics()
        list_length = len(Wellbeing)-1

        if Wellbeing[list_length] < 2.5:
            notification_text += self.__Encouraging_MESSAGES[self.random_number()]
        elif Wellbeing[list_length] == 2.5:
            notification_text += self.__Encouraging_MESSAGES[self.random_number()]
            notification_text += "\nDon't hesitate to talk to a friend if you need to"
        else:
            notification_text += self.__Encouraging_MESSAGES[self.random_number()]
            notification_text += "\nWe recommend contacting the Emergency Mental health reception on 044-309 21 38. \nIf you're in a critical state, call 112"
            notification_style = "urgent"
            return notification_text, notification_style

        if self.__algorithm_handler.drug_boolean_pattern():
            notification_text += "\nIf you or someone you know is struggling with substance use, contact the National Drug Helpline at 020-91 91 91."

        if self.__algorithm_handler.alcohol_boolean_pattern():
            notification_text += "\nNeed support with alcohol-related issues? Call the Alcohol Helpline at 020-84 44 48."

        if self.__algorithm_handler.exercise_boolean_pattern():
            notification_text += "\nIf you’re dealing with compulsive exercise habits, reach out to the Eating Disorder Helpline at 020-20 80 18."

        if self.__algorithm_handler.rest_boolean_pattern():
            notification_text += "\nStruggling with sleep or rest? Contact the Sleep Helpline at 0771-13 80 00 for advice."

        if self.__algorithm_handler.connected_boolean_pattern():
            notification_text += "\nFeeling isolated? Call the Red Cross support line at 0771-900 800 for someone to talk to."

        return notification_text, notification_style

    def random_number(self):
        """Returnerar ett slumpat tal mellan 0 och längden av listan med meddelande"""

        print("Generating random number...")

        LOWER_RANGE = 0
        UPPER_RANGE = len(self.__Encouraging_MESSAGES)-1

        return random.randint(LOWER_RANGE, UPPER_RANGE)
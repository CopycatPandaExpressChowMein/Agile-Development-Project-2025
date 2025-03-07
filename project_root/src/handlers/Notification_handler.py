from win11toast import toast
import random

class Notification_handler:
    __algorithm_handler = None

    __GOOD_MESSAGES = ["Oh my! You're absolutely marvelous!", "Example good", "Example good", "Example good"]
    __NEUTRAL_MESSAGES = ["Wow! You're doing great! Keep it up! Don't hesitate to talk to a friend if you need to", "Example neutral", "Example neutral", "Example neutral"]
    __BAD_MESSAGES = ["Don't give up!", "Example bad", "Example bad", "Example bad"]

    def __init__(self, Algorithm_handler):
        self.__algorithm_handler = Algorithm_handler


    def show_notification(self):
        try:
            __NOTIFICATION_TEXT, __NOTIFICATION_STYLE = self.get_notification_content()
        except:
            __NOTIFICATION_TEXT = "No entries found."
            __NOTIFICATION_STYLE = "reminder"

        toast("HabitTrack - Advice!", __NOTIFICATION_TEXT, scenario=__NOTIFICATION_STYLE)
        

    def get_notification_content(self):
        notification_text = ""
        notification_style = "reminder"

        Wellbeing = self.__algorithm_handler.average_statistics()
        list_length = len(Wellbeing)-1

        if Wellbeing[list_length] > 1:
            notification_text += self.__GOOD_MESSAGES[self.random_number()]
        elif Wellbeing[list_length] == 1:
            notification_text += self.__NEUTRAL_MESSAGES[self.random_number()]
        else:
            notification_text += self.__BAD_MESSAGES[self.random_number()]
            notification_text +="\nWe recommend contacting the Emergency Mental health reception on 044-309 21 38. If you're in a critical state, call 112"
            notification_style = "urgent"


        return notification_text, notification_style

    def random_number(self):

        LOWER_RANGE = 0
        UPPER_RANGE = 3

        return random.randint(LOWER_RANGE, UPPER_RANGE)
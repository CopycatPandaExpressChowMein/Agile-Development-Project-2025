from Algorithm_handler import Algorithm_handler
from gui.Menu import Ui_menu_window
from gui.Register import Ui_register_window
from gui.Registration_form import Ui_registration_form
from gui.Statistics import Ui_statistics_window

from PyQt5.QtWidgets import *
from handlers.User_entry_object import User_entry

# I Gui_components finns klasser för alla typer av fönster vi ska ha. Dessa kan man sedan göra objekt av

# Fönster för Menyn
class Menu_window(QMainWindow, Ui_menu_window):
    # Konstruktören, detta körs när ett nytt objekt initieras
    def __init__(self, qWidget):
        super(Menu_window, self).__init__() 
        self.setupUi(self)  # Funktion som finns i respektive Ui/Py fil, lägger till alla komponenter (knapp, text osv)
        self.setupButtons(qWidget)  # Funktion som kopplar knapparna, finns nedan
    
    def setupButtons(self, qWidget):
        self.menu_button_register.clicked.connect(lambda: self.menu_button_press_register(qWidget))
        self.menu_button_statistics.clicked.connect(lambda: self.menu_button_press_statistics(qWidget))

    def menu_button_press_register(self, qWidget):
        qWidget.setCurrentIndex(1)

    def menu_button_press_statistics(self, qWidget):
        qWidget.setCurrentIndex(2)
        

# Fönster för registrering, med kalender
class Register_window(QMainWindow, Ui_register_window):
    
    __data = None
    
    # Konstruktören, detta körs när ett nytt objekt initieras
    def __init__(self, qWidget, data_handler):
        super(Register_window, self).__init__()
        self.setupUi(self, data_handler) #Funktion som finns i Register.oy, lägger till alla komponenter (knapp, text osv)
        self.__data = data_handler
        self.setupButtons(qWidget)  # Funktion som kopplar knapparna, finns nedan
    
    def setupButtons(self, qWidget):
        self.register_button_back.clicked.connect(lambda: self.register_menu_press_back(qWidget))
        self.calendarWidget.clicked.connect(lambda: self.register_calendar_widget_pressed())

    def register_menu_press_back(self, qWidget):
        qWidget.setCurrentIndex(0)

    def register_calendar_widget_pressed(self):
        date = self.calendarWidget.selectedDate()
        Registration_form = Registration_form_window(self.__data, date)
        Registration_form.setWindowTitle(Registration_form.windowTitle() + " - [" + date.toString("yyyy-MM-dd") + "]")
        Registration_form.exec()



#Fönster för registrering, med frågor och anteckningar
class Registration_form_window(QDialog, Ui_registration_form):
    
    __data = None
    __date = None

    # Konstruktören, detta körs när ett nytt objekt initieras
    def __init__(self, data_handler, date):
        super(Registration_form_window, self).__init__()
        self.setupUi(self)  # Funktion som finns i Registration_form.py, lägger till alla komponenter (knapp, text osv)
        self.__data = data_handler
        self.__date = date
        self.registration_form_date_label.setText(self.__date.toString())
        self.try_load_entry_data()
        self.setupButtons() #Funktion som kopplar knapparna, finns nedan
    
    def setupButtons(self):
        self.registration_form_button_save.clicked.connect(lambda: self.registration_form_button_press_save())

    def try_load_entry_data(self):
        if self.__date in self.__data.get_all_keys():
            print("Previous entry found")

            user_entry = self.__data.get_from_dict(self.__date)

            wellbeing = self.Registration_form_feeling_buttons.button(-abs(user_entry.get_wellbeing())-1)
            if wellbeing != None:
                wellbeing.setChecked(True)

            anxiety = self.Registration_form_anxiety_buttons.button(-abs(user_entry.get_anxiety())-1)
            if anxiety != None:
                anxiety.setChecked(True)

            meals = self.Registration_form_meals_buttons.button(-abs(user_entry.get_meals())-1)
            if meals != None:
                meals.setChecked(True)

            connected_boolean = self.Registration_form_family_buttons.button(-abs(user_entry.get_connected_boolean())-1)
            if connected_boolean != None:
                connected_boolean.setChecked(True)

            rest_boolean = self.Registration_form_rest_buttons.button(-abs(user_entry.get_rest_boolean())-1)
            if  rest_boolean != None:
                 rest_boolean.setChecked(True)

            exercise_boolean = self.Registration_form_exercise_buttons.button(-abs(user_entry.get_exercise_boolean())-1)
            if exercise_boolean != None:
                exercise_boolean.setChecked(True)

            alcohol_boolean = self.Registration_form_alcohol_buttons.button(-abs(user_entry.get_alcohol_boolean())-1)
            if alcohol_boolean != None:
                alcohol_boolean.setChecked(True)

            drug_boolean = self.Registration_form_drugs_buttons.button(-abs(user_entry.get_drug_boolean())-1)
            if drug_boolean != None:
                drug_boolean.setChecked(True)

            self.registration_form_notepad.setPlainText(user_entry.get_notes())


           

    def registration_form_button_press_save(self):
        
        #TODO - Kod för att spara information härr
        wellbeing = abs(self.Registration_form_feeling_buttons.checkedId())-1
        anxiety = abs(self.Registration_form_anxiety_buttons.checkedId())-1
        meals = abs(self.Registration_form_meals_buttons.checkedId())-1
        connected_boolean = self.Registration_form_family_buttons.checkedId() == -2
        rest_boolean = self.Registration_form_rest_buttons.checkedId() == -2
        exercise_boolean = self.Registration_form_exercise_buttons.checkedId() == -2
        alcohol_boolean = self.Registration_form_alcohol_buttons.checkedId() == -2
        drug_boolean = self.Registration_form_drugs_buttons.checkedId() == -2
        notes = self.registration_form_notepad.toPlainText()
        user_entry = User_entry(wellbeing, anxiety, meals, connected_boolean, rest_boolean, exercise_boolean, alcohol_boolean, drug_boolean, notes)
        self.__data.add_to_dict(self.__date, user_entry)
        self.reject()



#Fönster för statistik#Funktion som kopplar knapparna
class Statistics_window(QMainWindow, Ui_statistics_window):
    # Konstruktören, detta körs när ett nytt objekt initieras
    def __init__(self, qWidget, data): 
        super(Statistics_window, self).__init__()
        self.setupUi(self, Algorithm_handler(data))  # Funktion som finns i Statistics.py, lägger till alla komponenter (knapp, text osv)
        self.setupButtons(qWidget)  # Funktion som kopplar knapparna, finns nedan

    def setupButtons(self, qWidget):
        self.statistics_button_back.clicked.connect(lambda: self.statistics_button_press_back(qWidget))

    def statistics_button_press_back(self, qWidget):
        qWidget.setCurrentIndex(0)

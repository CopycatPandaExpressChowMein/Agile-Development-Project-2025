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
        self.setupUi(self)  # Funktion som finns i Register.py, lägger till alla komponenter (knapp, text osv)
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

# Fönster för registrering, med frågor och anteckningar
class Registration_form_window(QDialog, Ui_registration_form):
    
    __data = None
    __date = None

    # Konstruktören, detta körs när ett nytt objekt initieras
    def __init__(self, data_handler, date):
        super(Registration_form_window, self).__init__()
        self.setupUi(self)  # Funktion som finns i Registration_form.py, lägger till alla komponenter (knapp, text osv)
        self.__data = data_handler
        self.__date = date
        self.registration_form_date_label.setText(self.__date.toString("yyyy-MM-dd"))
        self.setupButtons()  # Funktion som kopplar knapparna, finns nedan
    
    def setupButtons(self):
        self.registration_form_button_save.clicked.connect(lambda: self.registration_form_button_press_save())

    def registration_form_button_press_save(self):
        # Convert the date to a string (ensuring it's not empty)
        date_str = self.__date.toString("yyyy-MM-dd") if hasattr(self.__date, "toString") else str(self.__date)

        if not date_str.strip():  # Ensure the date is not empty
            print("ERROR: Date is empty!")
            return  # Stop execution if the date is invalid

        # Create a user entry and save it
        user_entry = User_entry(None, None, None, self.registration_form_notepad.toPlainText())
        self.__data.add_to_dict(date_str, user_entry)  # Use the fixed date string

        self.reject()

# Fönster för statistik
class Statistics_window(QMainWindow, Ui_statistics_window):
    # Konstruktören, detta körs när ett nytt objekt initieras
    def __init__(self, qWidget): 
        super(Statistics_window, self).__init__()
        self.setupUi(self)  # Funktion som finns i Statistics.py, lägger till alla komponenter (knapp, text osv)
        self.setupButtons(qWidget)  # Funktion som kopplar knapparna, finns nedan

    def setupButtons(self, qWidget):
        self.statistics_button_back.clicked.connect(lambda: self.statistics_button_press_back(qWidget))

    def statistics_button_press_back(self, qWidget):
        qWidget.setCurrentIndex(0)

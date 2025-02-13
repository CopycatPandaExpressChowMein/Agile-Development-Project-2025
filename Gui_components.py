
from Menu import Ui_menu_window
from Register import Ui_register_window
from Registration_form import Ui_registration_form
from Statistics import Ui_statistics_window

from PyQt5.QtWidgets import *

#I Gui_components finns klasser för alla typer av fönster vi ska ha. Dessa kan man sedan göra objekt av

#Fönster för Menyn
class Menu_window(QMainWindow, Ui_menu_window):
    #Konstruktören, detta körs när ett nytt objekt initieras
    def __init__(self):
        super(Menu_window, self).__init__() 
        self.setupUi(self) #Funktion som finns i respektive Ui/Py fil, lägger till alla komponenter (knapp, text osv)
        self.setupButtons() #Funktion som kopplar knapparna, finns nedan
    
    def setupButtons(self):
        pass

#Fönster för registrering, med kalender
class Register_window(QMainWindow, Ui_register_window):
    #Konstruktören, detta körs när ett nytt objekt initieras
    def __init__(self):
        super(Register_window, self).__init__()
        self.setupUi(self) #Funktion som finns i Register.oy, lägger till alla komponenter (knapp, text osv)
        self.setupButtons() #Funktion som kopplar knapparna, finns nedan
    
    def setupButtons(self):
        pass

#Fönster för registrering, med frågor och anteckningar
class Registration_form_window(QDialog, Ui_registration_form):
    #Konstruktören, detta körs när ett nytt objekt initieras
    def __init__(self):
        super(Registration_form_window, self).__init__()
        self.setupUi(self) #Funktion som finns i Registration_form.py, lägger till alla komponenter (knapp, text osv)
        self.setupButtons() #Funktion som kopplar knapparna, finns nedan
    
    def setupButtons(self):
        pass

#Fönster för statistik#Funktion som kopplar knapparna
class Statistics_window(QMainWindow, Ui_statistics_window):
    #Konstruktören, detta körs när ett nytt objekt initieras
    def __init__(self): 
        super(Statistics_window, self).__init__()
        self.setupUi(self) #Funktion som finns i Statistics.py, lägger till alla komponenter (knapp, text osv)
        self.setupButtons() #Funktion som kopplar knapparna, finns nedan

    def setupButtons(self):
        pass
    
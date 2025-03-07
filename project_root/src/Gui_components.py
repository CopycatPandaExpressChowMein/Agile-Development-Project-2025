
from src.gui.Menu import Ui_menu_window
from src.gui.Register import Ui_register_window
from src.gui.Registration_form import Ui_registration_form
from src.gui.Statistics import Ui_statistics_window

from src.gui.Calendar_widget import Calendar_widget

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from src.handlers.User_entry_object import User_entry
import pyqtgraph as pg

# I Gui_components finns klasser för alla typer av fönster vi ska ha. Dessa kan man sedan göra objekt av

# Fönster för Menyn
class Menu_window(QMainWindow, Ui_menu_window):


    # Konstruktören, detta körs när ett nytt objekt initieras
    def __init__(self, qWidget, notification_handler):
        super(Menu_window, self).__init__() 
        self.setupUi(self)  # Funktion som finns i respektive Ui/Py fil, lägger till alla komponenter (knapp, text osv)
        self.setupTimer() #Lägger till en timer i huvudmenyn
        self.setupButtons(qWidget, notification_handler)  # Funktion som kopplar knapparna, finns nedan

    #Funktion som skapar en timer och sedan startar den med en tid på 0 sekunder 
    #(Innebär att den skickar ut en signal direkt)
    def setupTimer(self):

        __TIME = 0
        
        self.__timer = QTimer()
        self.__timer.start(__TIME)
        
    def setupButtons(self, qWidget, notification_handler):
        self.menu_button_register.clicked.connect(lambda: self.menu_button_press_register(qWidget))
        self.menu_button_statistics.clicked.connect(lambda: self.menu_button_press_statistics(qWidget))
        self.__timer.timeout.connect(lambda: self.timer_timeout(notification_handler))

    def menu_button_press_register(self, qWidget):
        qWidget.setCurrentIndex(1)

    def menu_button_press_statistics(self, qWidget):
        qWidget.widget(2).rePlot()
        qWidget.setCurrentIndex(2)
    
    #När den specifierade tiden i timern tar slut så kallas den här funktionen, vilket visar en notifikation
    #med hjälp av Notification_handler
    def timer_timeout(self, notification_handler):
        self.__timer.stop() #Stoppar timern så att den inte körs igen
        notification_handler.show_notification() #Visar notifikation


        #Bestämmer tiden för timern
        __TIME = 0 

        #Startar timern igen
        #self.__timer.star(__TIME)
        

# Fönster för registrering, med kalender
class Register_window(QMainWindow, Ui_register_window):
    
    __data = None
    
    # Konstruktören, detta körs när ett nytt objekt initieras
    def __init__(self, qWidget, data_handler, notification_handler):
        super(Register_window, self).__init__()
        self.setupUi(self, Calendar_widget(data_handler)) #Funktion som finns i Register.oy, lägger till alla komponenter (knapp, text osv)
        self.__data = data_handler
        self.setupButtons(qWidget, notification_handler)  # Funktion som kopplar knapparna, finns nedan
    
    def setupButtons(self, qWidget, notification_handler):
        self.register_button_back.clicked.connect(lambda: self.register_menu_press_back(qWidget))
        self.calendarWidget.clicked.connect(lambda: self.register_calendar_widget_pressed(notification_handler))

    def register_menu_press_back(self, qWidget):
        qWidget.setCurrentIndex(0)

    def register_calendar_widget_pressed(self, notification_handler):
        date = self.calendarWidget.selectedDate()
        Registration_form = Registration_form_window(self.__data, date, notification_handler)
        Registration_form.setWindowTitle(Registration_form.windowTitle() + " - [" + date.toString("yyyy-MM-dd") + "]")
        Registration_form.exec()



#Fönster för registrering, med frågor och anteckningar
class Registration_form_window(QDialog, Ui_registration_form):
    
    __data = None
    __date = None

    # Konstruktören, detta körs när ett nytt objekt initieras
    def __init__(self, data_handler, date, notification_handler):
        super(Registration_form_window, self).__init__()
        self.setupUi(self)  # Funktion som finns i Registration_form.py, lägger till alla komponenter (knapp, text osv)
        self.__data = data_handler
        self.__date = date
        self.registration_form_date_label.setText(self.__date.toString())
        self.try_load_entry_data()
        self.setupButtons(notification_handler) #Funktion som kopplar knapparna, finns nedan
    
    def setupButtons(self, notification_handler):
        self.registration_form_button_save.clicked.connect(lambda: self.registration_form_button_press_save(notification_handler))

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


           

    def registration_form_button_press_save(self, notification_handler):
        
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
        notification_handler.show_notification()
        



#Fönster för statistik#Funktion som kopplar knapparna
class Statistics_window(QMainWindow, Ui_statistics_window):

    __algorithm_handler = None

    # Konstruktören, detta körs när ett nytt objekt initieras
    def __init__(self, qWidget, algorithm_handler): 
        super(Statistics_window, self).__init__()

        self.__algorithm_handler = algorithm_handler

        graphs = []
        
        graphs.append(self.graphSetup("Wellbeing vs Time", "Wellbeing"))
        graphs.append(self.graphSetup("Anxiety vs Time", "Anxiety"))
        graphs.append(self.graphSetup("Meals vs Time", "Meals"))
        graphs.append(self.graphSetup("Average mental health vs Time", "Average"))

        self.setupUi(self, graphs)  # Funktion som finns i Statistics.py, lägger till alla komponenter (knapp, text osv)
        self.setupButtons(qWidget)  # Funktion som kopplar knapparna, finns nedan

    def setupButtons(self, qWidget):
        self.statistics_button_back.clicked.connect(lambda: self.statistics_button_press_back(qWidget))

    def graphSetup(self, title, yVal):
        graph = pg.PlotWidget()
        graph.setBackground((255,255,255,0))
        graph.setTitle(title)
        graph.setLabel("left", yVal)
        graph.setLabel("bottom", "Days")
        graph.setYRange(0, 5)


        return graph


    def rePlot(self):
        POINT_SYMBOl = "o"
        POINT_SYMBOl_COLOR = "k"
        POINT_SYMBOl_SIZE = 5
        LINE_COLOR = (255,0,0)
        pen = pg.mkPen(color=LINE_COLOR)

        days = self.__algorithm_handler.entry_amount()

        wellbeing = self.__algorithm_handler.wellbeing_statistics()
        self.graph_1.plot(days, wellbeing, pen=pen, symbol=POINT_SYMBOl, symbolSize = POINT_SYMBOl_SIZE , symbolBrush = POINT_SYMBOl_COLOR)

        anxiety = self.__algorithm_handler.anxiety_statistics()
        self.graph_2.plot(days, anxiety, pen=pen, symbol=POINT_SYMBOl, symbolSize = POINT_SYMBOl_SIZE , symbolBrush = POINT_SYMBOl_COLOR)

        meals = self.__algorithm_handler.meals_statistics()
        self.graph_3.plot(days, meals, pen=pen, symbol=POINT_SYMBOl, symbolSize = POINT_SYMBOl_SIZE , symbolBrush = POINT_SYMBOl_COLOR)

        average = self.__algorithm_handler.average_statistics()
        self.graph_4.plot(days, average, pen=pen, symbol=POINT_SYMBOl, symbolSize = POINT_SYMBOl_SIZE , symbolBrush = POINT_SYMBOl_COLOR)


        

    def statistics_button_press_back(self, qWidget):
        qWidget.setCurrentIndex(0)

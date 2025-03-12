import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from src.Gui_components import Menu_window, Register_window, Statistics_window
from src.handlers.User_entry_data_handler import Data_handler
from src.handlers.Cloud_handler import Cloud_handler
from src.handlers.Algorithm_handler import Algorithm_handler
from src.handlers.Notification_handler import Notification_handler
from src.handlers.Network_handler import *

# 🏃‍♂️ Funktion som startar programmet
def Runtime():

    print("program start...")

    app = QApplication(sys.argv)
    widget = QStackedWidget()
    
    # Kollar uppkoppling till internet.
    if check_connection():
        cloud_handler = Cloud_handler() # Skapar ett objekt för att hantera cloud information och funktioner
        data_handler = Data_handler(cloud_handler)  # Skapar ett objekt för att hantera data, med cloud funktioner
    else:
        data_handler = Data_handler() # Skapar ett objekt för att hantera data
    algorithm_handler = Algorithm_handler(data_handler) # Skapar ett objekt för att arbeta med data
    notification_handler = Notification_handler(algorithm_handler) # Skapar ett objekt för att hantera notifikationer
    

    # Skapa fönster för de olika vyerna i applikationen
    menu = Menu_window(widget, notification_handler)
    register = Register_window(widget, data_handler, notification_handler) 
    statistics = Statistics_window(widget, algorithm_handler)
    
    # Lägg till fönstren i det staplade widget-systemet
    widget.addWidget(menu)
    widget.addWidget(register)
    widget.addWidget(statistics)
    

    widget.resize(600, 500) # Förminskar storleken på fönstret innan det körs.
    widget.show()  # Visa huvudfönstret
    
    sys.exit(app.exec_())  # Kör applikationen tills den stängs
    

# 🔥 Kontrollera om skriptet körs direkt
if __name__ == "__main__":
    Runtime()  # Starta programmet

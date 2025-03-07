import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from src.Gui_components import Menu_window, Register_window, Statistics_window
from src.handlers.User_entry_data_handler import Data_handler
from src.handlers.Cloud_handler import Cloud_handler
from src.handlers.Algorithm_handler import Algorithm_handler
from src.handlers.Notification_handler import Notification_handler
from src.handlers.Network_handler import *
from src.security.security import check_access  # 🔐 Importera säkerhetsfunktionen

# 🏃‍♂️ Funktion som startar programmet
def Runtime():
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    
    if check_connection():
        cloud_handler = Cloud_handler()
        data_handler = Data_handler(cloud_handler)  # Skapar ett objekt för att hantera data
    else:
        data_handler = Data_handler()
    algorithm_handler = Algorithm_handler(data_handler)
    notification_handler = Notification_handler(algorithm_handler)
    

    # Skapa fönster för de olika vyerna i applikationen
    menu = Menu_window(widget, notification_handler)  
    register = Register_window(widget, data_handler, notification_handler)
    statistics = Statistics_window(widget, algorithm_handler)
    
    # Lägg till fönstren i det staplade widget-systemet
    widget.addWidget(menu)
    widget.addWidget(register)
    widget.addWidget(statistics)
    
    # 🛡️ Säkerhetskontroll: Förhindra obehörig åtkomst 🛡️
    user_role = "user"  # Detta kan ändras beroende på inloggning
    if not check_access(user_role, "read"):  
        print("❌ Åtkomst nekad!")
        return  # Stoppa programmet om användaren saknar behörighet

    widget.resize(600, 500)
    widget.show()  # Visa huvudfönstret
    
    sys.exit(app.exec_())  # Kör applikationen tills den stängs
    

# 🔥 Kontrollera om skriptet körs direkt
if __name__ == "__main__":
    Runtime()  # Starta programmet

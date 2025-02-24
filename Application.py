import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from Gui_components import Menu_window, Register_window, Statistics_window
from User_entry_data_handler import Data_handler
from security import check_access  # 🔐 Importera säkerhetsfunktionen

<<<<<<< HEAD


#Application.py innehåller all huvudkod, i princip en Main :)

#Runtime funktion för applikationen, här finns huvudkoden för programmet
=======
# 🏃‍♂️ Funktion som startar programmet
>>>>>>> 662b94d48ef0be2b6f293ccb1b21abdd4c170ad9
def Runtime():
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    
    data_handler = Data_handler()  # Skapar ett objekt för att hantera data
    
    # Skapa fönster för de olika vyerna i applikationen
    menu = Menu_window(widget)  
    register = Register_window(widget, data_handler)
    statistics = Statistics_window(widget)
    
    # Lägg till fönstren i det staplade widget-systemet
    widget.addWidget(menu)
    widget.addWidget(register)
    widget.addWidget(statistics)
    
    # 🛡️ Säkerhetskontroll: Förhindra obehörig åtkomst 🛡️
    user_role = "user"  # Detta kan ändras beroende på inloggning
    if not check_access(user_role, "read"):  
        print("❌ Åtkomst nekad!")
        return  # Stoppa programmet om användaren saknar behörighet

    widget.show()  # Visa huvudfönstret
    sys.exit(app.exec_())  # Kör applikationen tills den stängs

# 🔥 Kontrollera om skriptet körs direkt
if __name__ == "__main__":
    Runtime()  # Starta programmet

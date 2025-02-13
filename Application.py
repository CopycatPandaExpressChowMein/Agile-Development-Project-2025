import sys
from PyQt5.QtWidgets import *
from Gui_components import *

#Application.py innehåller all huvudkod, i princip en Main :)

#Runtime funktion för applikationen, här finns huvudkoden för programmet
def Runtime():
    app = QApplication(sys.argv)

    widget = QStackedWidget()
    
    menu = Menu_window(widget)
    register = Register_window(widget)
    statistics = Statistics_window(widget)
    
    widget.addWidget(menu)
    widget.addWidget(register)
    widget.addWidget(statistics)

    widget.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    Runtime()
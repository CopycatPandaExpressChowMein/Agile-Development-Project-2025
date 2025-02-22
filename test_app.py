import sys
import unittest
from PyQt5.QtWidgets import QApplication, QStackedWidget
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from Gui_components import Menu_window, Register_window, Statistics_window
from User_entry_data_handler import Data_handler

class TestApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """ Skapar QApplication (krävs för att testa PyQt5-komponenter) """
        if not QApplication.instance():
            cls.app = QApplication(sys.argv)
        else:
            cls.app = QApplication.instance()

    def setUp(self):
        """ Förbereder testmiljön för varje testfall """
        self.widget = QStackedWidget()
        self.data_handler = Data_handler()
        
        self.menu = Menu_window(self.widget)
        self.register = Register_window(self.widget, self.data_handler)
        self.statistics = Statistics_window(self.widget)

        self.widget.addWidget(self.menu)
        self.widget.addWidget(self.register)
        self.widget.addWidget(self.statistics)

        self.widget.setCurrentIndex(0)  # Börjar alltid på menyfönstret

    def tearDown(self):
        """ Städar upp efter varje testfall """
        self.widget = None

    def test_widget_count(self):
        """ Testar att alla fönster har lagts till korrekt """
        self.assertEqual(self.widget.count(), 3)

    def test_initial_widget(self):
        """ Testar att applikationen startar i menyn """
        self.assertEqual(self.widget.currentIndex(), 0)

    def test_navigation(self):
        """ Testar navigering mellan fönster """
        self.widget.setCurrentIndex(1)  # Flytta till Registreringsfönstret
        self.assertEqual(self.widget.currentIndex(), 1)

        self.widget.setCurrentIndex(2)  # Flytta till Statistikfönstret
        self.assertEqual(self.widget.currentIndex(), 2)

    def test_menu_buttons(self):
        """ Simulerar knapptryck i menyfönstret för att navigera """
        if hasattr(self.menu, 'menu_button_register'):
            QTest.mouseClick(self.menu.menu_button_register, Qt.LeftButton)
            self.assertEqual(self.widget.currentIndex(), 1)  # Bör navigera till registreringsfönstret

    def test_register_data_entry(self):
        """ Simulerar att skriva in text i ett textfält i registreringsfönstret """
        if hasattr(self.register, 'name_input'):
            QTest.keyClicks(self.register.name_input, "Test User")
            self.assertEqual(self.register.name_input.text(), "Test User")

    @classmethod
    def tearDownClass(cls):
        """ Avslutar QApplication vid testets slut """
        cls.app.quit()

if __name__ == "__main__":
    unittest.main()

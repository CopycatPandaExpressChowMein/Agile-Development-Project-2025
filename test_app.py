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
        """ Set up QApplication (needed for testing PyQt5 components) """
        cls.app = QApplication(sys.argv)

    def setUp(self):
        """ Set up the test environment for each test """
        self.widget = QStackedWidget()
        self.data_handler = Data_handler()
        
        self.menu = Menu_window(self.widget)
        self.register = Register_window(self.widget, self.data_handler)
        self.statistics = Statistics_window(self.widget)

        self.widget.addWidget(self.menu)
        self.widget.addWidget(self.register)
        self.widget.addWidget(self.statistics)

        self.widget.setCurrentIndex(0)  # Ensure it starts at the menu

    def tearDown(self):
        """ Clean up after each test """
        self.widget = None

    def test_widget_count(self):
        """ Test that all widgets are added properly """
        self.assertEqual(self.widget.count(), 3)

    def test_initial_widget(self):
        """ Test that the initial widget is set correctly """
        self.assertEqual(self.widget.currentIndex(), 0)  # Assuming first widget (menu) is active

    def test_navigation(self):
        """ Test navigating between widgets """
        self.widget.setCurrentIndex(1)  # Move to Register Window
        self.assertEqual(self.widget.currentIndex(), 1)

        self.widget.setCurrentIndex(2)  # Move to Statistics Window
        self.assertEqual(self.widget.currentIndex(), 2)

    def test_menu_buttons(self):
        """ Simulate clicking a button in the menu window (assuming it has buttons) """
        if hasattr(self.menu, 'register_button'):
            QTest.mouseClick(self.menu.register_button, Qt.LeftButton)
            self.assertEqual(self.widget.currentIndex(), 1)  # Should navigate to register window

    def test_register_data_entry(self):
        """ Simulate entering text in a register window input field (assuming it has one) """
        if hasattr(self.register, 'name_input'):
            QTest.keyClicks(self.register.name_input, "Test User")
            self.assertEqual(self.register.name_input.text(), "Test User")

    @classmethod
    def tearDownClass(cls):
        """ Cleanup QApplication """
        cls.app.quit()

if __name__ == "__main__":
    unittest.main()

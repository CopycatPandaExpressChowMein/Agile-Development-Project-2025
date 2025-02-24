from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Calendar_widget (QCalendarWidget):

    __data = None

    def __init__(self, data):
        super().__init__()
        self.__data = data

    def paintCell(self, painter, rect, date):
        super().paintCell(painter, rect, date)

        if date in self.__data.get_all_keys():
            painter.save()
            painter.setBrush(QBrush(QColor(0,200,0)))
            painter.drawEllipse(rect.topLeft() + QPoint(12, 7), 3, 3)
            painter.restore()


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Calendar_widget (QCalendarWidget):

    __keys = None

    def __init__(self, keys):
        super().__init__()
        self.__keys = keys

    def paintCell(self, painter, rect, date):
        super().paintCell(painter, rect, date)

        if date in self.__keys:
            painter.save()
            painter.setBrush(QBrush(QColor(174, 226, 255)))
            painter.setPen(QPen(QColor(255,255,255)))
            painter.drawEllipse(rect.topLeft() + QPoint(12, 12), 6, 6)
            painter.restore()


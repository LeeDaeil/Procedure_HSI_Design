from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from SAMG.guid_display_componet import *
from SAMG.COL import *
import sys


class guid_dis_area(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)

        self.w_scroll = QScrollArea(self)
        self.w_scroll.setWidgetResizable(True)

        self.sub_wid = TBS_top()
        self.w_scroll.setWidget(self.sub_wid)

        self.layout_All = QVBoxLayout(self)
        self.layout_All.addWidget(self.w_scroll)

        self.sub_wid.setMinimumHeight(500)


class TBS_top(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.wid_1 = QLabel(self)
        self.wid_1.setGeometry(0, 0, self.wid_1.max_w, 71 + 10 + 110 + 110)

    def paintEvent(self, event):
        painter = QPainter(self)
        # painter.setPen(QPen(######))
        painter.drawLine(20, 10 + self.wid_1.h/2, 20, 10 + self.wid_1.h + 40 + self.wid_2.h/2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = guid_dis_area()
    w.resize(1500, 800)
    w.show()
    app.exec_()
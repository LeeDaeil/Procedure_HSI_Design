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

        self.sub_wid = guid_dis_area_top()
        self.w_scroll.setWidget(self.sub_wid)

        self.layout_All = QVBoxLayout(self)
        self.layout_All.addWidget(self.w_scroll)

        self.sub_wid.setMinimumHeight(500)


class guid_dis_area_top(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.wid_1 = guid_dis_area_in(self, top_txt='AA\nA', second_txt='BBB', theard_txt='CCC')
        self.wid_1.setGeometry(0, 0, self.wid_1.max_w, 71 + 10 + 110 + 110)

        self.wid_2 = guid_dis_area_in(self, top_txt='AAA\n222\n2', second_txt='BB\nB2222', theard_txt='CCC2')
        self.wid_2.setGeometry(0, 110 + 110 + 110, self.wid_2.max_w, 71 + 10 + 110 + 110)

        self.wid_1.wid_1.open_close.clicked.connect(self.folding_top_1)
        self.wid_1.wid_2.open_close.clicked.connect(self.folding_top_2)

    def folding_top_1(self):
        if self.wid_1.wid_2.isVisible():
            self.wid_2.setGeometry(0, 110 + 110 + 110, self.wid_2.max_w, self.wid_2.max_h)
        else:
            self.wid_2.setGeometry(0, 110, self.wid_2.max_w, self.wid_2.max_h)

    def folding_top_2(self):
        if self.wid_1.wid_3.isVisible():
            self.wid_2.setGeometry(0, 110 + 110 + 110, self.wid_2.max_w, self.wid_2.max_h)
        else:
            self.wid_2.setGeometry(0, 110 + 110, self.wid_2.max_w, self.wid_2.max_h)


class guid_dis_area_in(QWidget):
    def __init__(self, parent=None, top_txt='', second_txt='', theard_txt=''):
        QWidget.__init__(self, parent=parent)
        self.ok_b_trig_1 = False
        self.ok_b_trig_2 = False

        self.wid_1 = Cont_wid(self, 1110, top_txt, ok_botton=False)
        self.wid_1.setGeometry(10, 10, self.wid_1.max_w, self.wid_1.h)

        self.wid_2 = Cont_wid(self, 1085, second_txt)
        self.wid_2.setGeometry(10 + self.wid_1.open_close_size + 5, 10 + 110, self.wid_2.max_w, self.wid_2.h)

        self.wid_3 = Cont_wid(self, 1065, theard_txt)
        self.wid_3.setGeometry(10 + self.wid_1.open_close_size * 2 + 5, 10 + 110 + 110, self.wid_3.max_w, self.wid_3.h)

        # ---------------------------------------------------------------------------------------------------
        self.max_w = self.wid_2.max_w
        self.max_h = 10 + self.wid_1.h + 110 + self.wid_2.h + 110 + self.wid_3.h

        self.wid_1_to_2 = QPen(Qt.black, 3)
        self.wid_2_to_3 = QPen(Qt.black, 3)

        self.wid_1.open_close.clicked.connect(self.folding_1)
        self.wid_2.open_close.clicked.connect(self.folding_2)
        self.wid_2.ok_b.clicked.connect(self.ok_b_1)
        self.wid_3.ok_b.clicked.connect(self.ok_b_2)

    def folding_log(self):
        if self.ok_b_trig_1:
            self.wid_1_to_2 = QPen(Qt.red, 3)
            if self.ok_b_trig_2:
                self.wid_2_to_3 = QPen(Qt.red, 3)
            else:
                self.wid_2_to_3 = QPen(Qt.black, 3)
        else:
            self.wid_1_to_2 = QPen(Qt.black, 3)
            if self.ok_b_trig_2:
                self.wid_2_to_3 = QPen(Qt.red, 3)
            else:
                self.wid_2_to_3 = QPen(Qt.black, 3)

    def folding_1(self):
        if self.wid_2.isVisible():
            self.wid_2.setVisible(False)
            self.wid_3.setVisible(False)
            self.folding_log()
            self.wid_1_to_2 = Qt.NoPen
            self.wid_2_to_3 = Qt.NoPen
        else:
            self.wid_2.setVisible(True)
            self.wid_3.setVisible(True)
            self.folding_log()
        self.update()

    def folding_2(self):
        if self.wid_3.isVisible():
            self.wid_3.setVisible(False)
            self.folding_log()
            self.wid_2_to_3 = Qt.NoPen
        else:
            self.wid_3.setVisible(True)
            self.folding_log()
        self.update()

    def ok_b_1(self):
        if self.ok_b_trig_1:
            self.wid_1_to_2 = QPen(Qt.black, 3)
            self.wid_1.change_all_dis(True)
            self.ok_b_trig_1 = False
        else:
            self.wid_1_to_2 = QPen(Qt.red, 3)
            self.wid_1.change_all_dis(False)
            self.ok_b_trig_1 = True
        self.update()

    def ok_b_2(self):
        if self.ok_b_trig_2:
            self.wid_1_to_2 = QPen(Qt.black, 3)
            self.wid_2_to_3 = QPen(Qt.black, 3)
            self.wid_1.change_all_dis(True)
            self.wid_2.change_all_dis(True)
            self.ok_b_trig_2 = False
            self.ok_b_trig_1 = False
        else:
            self.wid_1_to_2 = QPen(Qt.red, 3)
            self.wid_2_to_3 = QPen(Qt.red, 3)
            self.wid_1.change_all_dis(False)
            self.wid_2.change_all_dis(False)
            self.ok_b_trig_2 = True
            self.ok_b_trig_1 = True
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(self.wid_1_to_2)
        painter.drawLine(20, 10 + self.wid_1.h/2, 20, 10 + self.wid_1.h + 40 + self.wid_2.h/2)
        painter.drawLine(20, 10 + self.wid_1.h + 40 + self.wid_2.h/2, 45, 10 + self.wid_1.h + 40 + self.wid_2.h/2)
        painter.setPen(self.wid_2_to_3)
        painter.drawLine(45, 10 + self.wid_1.h + 40 + self.wid_2.h/2, 45,
                         10 + self.wid_1.h + 40 + self.wid_2.h + 40 + self.wid_3.h/2)
        painter.drawLine(45, 10 + self.wid_1.h + 40 + self.wid_2.h + 40 + self.wid_3.h/2, 70,
                         10 + self.wid_1.h + 40 + self.wid_2.h + 40 + self.wid_3.h/2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = guid_dis_area()
    w.resize(1500, 800)
    w.show()
    app.exec_()
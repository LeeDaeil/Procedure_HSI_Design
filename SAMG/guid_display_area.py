from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
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
        self.wid_1 = guid_dis_area_in(self, top_txt='AAA', second_txt='BBB')
        self.wid_1.setGeometry(0, 0, self.wid_1.max_w, 71 + 10 + 110)

        self.wid_2 = guid_dis_area_in(self, top_txt='AAA2222', second_txt='BBB2222')
        self.wid_2.setGeometry(0, 110 + 110, self.wid_2.max_w, 71 + 10 + 110)

        self.wid_1.wid_1.open_close.clicked.connect(self.folding_top)

    def folding_top(self):
        if self.wid_1.wid_2.isVisible():
            self.wid_2.setGeometry(0, 110 + 110, self.wid_2.max_w, self.wid_2.max_h)
        else:
            self.wid_2.setGeometry(0, 110, self.wid_2.max_w, self.wid_2.max_h)


class guid_dis_area_in(QWidget):
    def __init__(self, parent=None, top_txt='', second_txt=''):
        QWidget.__init__(self, parent=parent)
        self.ok_b_trig = False

        self.wid_1 = Cont_wid(self, top_txt)
        self.wid_1.setGeometry(10, 10, self.wid_1.max_w, self.wid_1.h)

        self.wid_2 = Cont_wid_2(self, second_txt)
        self.wid_2.setGeometry(10 + self.wid_1.open_close_size + 5, 10 + 110, self.wid_2.max_w, self.wid_2.h)

        self.max_w = self.wid_2.max_w
        self.max_h = 10 + self.wid_1.h + 110 + self.wid_2.h

        self.wid_1_to_2 = QPen(Qt.black, 3)

        self.wid_1.open_close.clicked.connect(self.folding)
        self.wid_2.ok_b.clicked.connect(self.ok_b_)

    def folding(self):
        if self.wid_2.isVisible():
            self.wid_2.setVisible(False)
            if self.ok_b_trig:
                self.wid_1_to_2 = QPen(Qt.red, 3)
            else:
                self.wid_1_to_2 = QPen(Qt.black, 3)
            self.wid_1_to_2 = Qt.NoPen
        else:
            self.wid_2.setVisible(True)
            if self.ok_b_trig:
                self.wid_1_to_2 = QPen(Qt.red, 3)
            else:
                self.wid_1_to_2 = QPen(Qt.black, 3)
        self.update()

    def ok_b_(self):
        if self.ok_b_trig:
            self.wid_1_to_2 = QPen(Qt.black, 3)
            self.wid_1.change_all_dis(True)
            self.ok_b_trig = False
        else:
            self.wid_1_to_2 = QPen(Qt.red, 3)
            self.wid_1.change_all_dis(False)
            self.ok_b_trig = True
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(self.wid_1_to_2)
        painter.drawLine(20, 10 + self.wid_1.h/2, 20, 10 + self.wid_1.h + 40 + self.wid_2.h/2)
        painter.drawLine(20, 10 + self.wid_1.h + 40 + self.wid_2.h/2, 45, 10 + self.wid_1.h + 40 + self.wid_2.h/2)

# ---------------------------------------------------------------------------------------------------------------------
# 하위 모듈


class Cont_wid(QWidget):
    def __init__(self, parent=None, text=None):
        QWidget.__init__(self, parent=parent)
        self.boton_1 = Cont_label(self, text)

        # self.h 는 글자 수 대로 70 -> 80 -> 90 -> 100 으로 증액
        self.h = 70
        self.w_label = 1110
        self.open_close_size = 20
        self.max_w = self.open_close_size + 5 + self.w_label + 5 + 30

        if True:
            self.boton_1.setGeometry(self.open_close_size + 5, 0, self.w_label, self.h)

            self.open_close = Cont_open_close(self)
            self.open_close.setGeometry(0, self.h/2 - 10, self.open_close_size, self.open_close_size)

    def change_all_dis(self, wid_on_off):
        if wid_on_off:
            self.open_close.setStyleSheet(button_switch_False)
            self.boton_1.setStyleSheet(button_False)
        else:
            self.open_close.setStyleSheet(button_switch_True)
            self.boton_1.setStyleSheet(button_True)


class Cont_wid_2(QWidget):
    def __init__(self, parent=None, text=None, ok_botton=True):
        QWidget.__init__(self, parent)
        self.wid_on_off = False

        # self.h 는 글자 수 대로 70 -> 80 -> 90 -> 100 으로 증액
        self.h = 70
        self.w_label = 1085
        self.open_close_size = 20
        self.max_w = self.open_close_size + 5 + self.w_label + 5 + 110 + 35

        if True:
            self.boton_1 = Cont_label(self, text)
            self.boton_1.setGeometry(self.open_close_size + 5, 0, self.w_label, self.h)

            self.open_close = Cont_open_close(self)
            self.open_close.setGeometry(0, self.h/2 - 10, self.open_close_size, self.open_close_size)

            self.ok_b = Cont_ok(self, '확인')
            self.ok_b.setGeometry(self.open_close_size + 5 + self.w_label + 5, self.h - 30, 110, 30)

        if ok_botton:
            self.ok_b.setVisible(True)
        else:
            self.ok_b.setVisible(False)

        self.ok_b.clicked.connect(self.change_all_dis)

    def change_all_dis(self):
        if self.wid_on_off:
            self.wid_on_off = False
            self.open_close.setStyleSheet(button_switch_False)
            self.boton_1.setStyleSheet(button_False)
            self.ok_b.setStyleSheet(button_ok_False)
        else:
            self.wid_on_off = True
            self.open_close.setStyleSheet(button_switch_True)
            self.boton_1.setStyleSheet(button_True)
            self.ok_b.setStyleSheet(button_ok_True)


class Cont_label(QLabel):
    def __init__(self, parent=None, text=None):
        QLabel.__init__(self, parent)
        self.setStyleSheet(button_False)
        self.setText(text)
        self.setAlignment(Qt.AlignVCenter)


class Cont_open_close(QPushButton):
    def __init__(self, parent=None):
        QPushButton.__init__(self, parent)
        self.setStyleSheet(button_switch_False)
        self.setText('●')


class Cont_ok(QPushButton):
    def __init__(self, parent=None, text=None):
        QPushButton.__init__(self, parent)
        self.setStyleSheet(button_ok_False)
        self.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = guid_dis_area()
    w.resize(1500, 300)
    w.show()
    app.exec_()
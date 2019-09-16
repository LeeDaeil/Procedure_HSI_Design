from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from SAMG.COL import *

# ---------------------------------------------------------------------------------------------------------------------
# 하위 모듈 - 공용 통적으로 동작


class Cont_wid(QWidget):
    def __init__(self, parent=None, w_level=1085, text=None, ok_botton=True):
        QWidget.__init__(self, parent)
        self.wid_on_off = False

        # self.h 는 글자 수 대로 70 -> 80 -> 90 -> 100 으로 증액
        # self.h = 60 + len(text.split('\n')) * 10
        self.h = 70
        self.w_label = w_level

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

        self.ok_b.clicked.connect(lambda: self.change_all_dis(self.wid_on_off))

    def change_all_dis(self, wid_on_off):
        if wid_on_off:
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


from PySide2.QtWidgets import *
from SAMG.SH import *
from SAMG.COL import *
from SAMG.guid_display_area import *
import sys


class main_window(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainForm()
        self.ui.setupUi(self)

        if True:
            self.B_list = [self.ui.B_1, self.ui.B_2, self.ui.B_3, self.ui.B_4, self.ui.B_5, self.ui.B_6, self.ui.B_7,
                           self.ui.B_8, self.ui.B_9]
            self.BC_list = [self.ui.per_num_17, self.ui.per_num_16, self.ui.per_num_15, self.ui.per_num_14,
                            self.ui.per_num_13, self.ui.per_num_12, self.ui.per_num_11, self.ui.per_num_10,
                            self.ui.per_num_9]
            self.ui.B_1.clicked.connect(lambda: self.change_guid_dis(1))
            self.ui.B_2.clicked.connect(lambda: self.change_guid_dis(2))
            self.ui.B_3.clicked.connect(lambda: self.change_guid_dis(3))
            self.ui.B_4.clicked.connect(lambda: self.change_guid_dis(4))
            self.ui.B_5.clicked.connect(lambda: self.change_guid_dis(5))
            self.ui.B_6.clicked.connect(lambda: self.change_guid_dis(6))
            self.ui.B_7.clicked.connect(lambda: self.change_guid_dis(7))
            self.ui.B_8.clicked.connect(lambda: self.change_guid_dis(8))
            self.ui.B_9.clicked.connect(lambda: self.change_guid_dis(9))

        self.guid_ui = guid_dis_area()
        self.ui.stackedWidget.addWidget(self.guid_ui)


    def change_guid_dis(self, guid_dis_nub):
        # guid_dis 창을 변경
        self.ui.stackedWidget.setCurrentIndex(guid_dis_nub)
        # 버튼의 색 변경
        for _ in self.B_list:
            if self.B_list.index(_) + 1 == guid_dis_nub:
                # Current guidline 업데이트
                self.ui.pur_title.setText(_.text())
                self.ui.pur_title.setStyleSheet(ti_b)
                # Count + 1
                if _.styleSheet() != b_g:
                    self.BC_list[self.B_list.index(_)].display(self.BC_list[self.B_list.index(_)].intValue() + 1)
                # 버튼 색 변경
                _.setStyleSheet(b_g)
            else:
                _.setStyleSheet(b_w)


# test 용 --------------------------------------------------------------------------------------------------------------
    def keyPressEvent(self, e):
        if e.key() == 65:
            current_nub = self.ui.stackedWidget.currentIndex() + 1
            if current_nub < self.ui.stackedWidget.count():
                self.ui.stackedWidget.setCurrentIndex(current_nub)
            else:
                self.ui.stackedWidget.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = main_window()
    w.show()
    app.exec_()
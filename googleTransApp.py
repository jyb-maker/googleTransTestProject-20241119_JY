import sys
import googletrans

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5 import uic

form_class = uic.loadUiType("ui/googleTrans2.ui")[0]

class GoogleTrans(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("구글 한줄 번역기")      # 프로그램 타이틀
        self.setWindowIcon(QIcon("img/google.png"))  # 아이콘 불러오기
        self.statusBar().showMessage("Google Trans App v1.0 Made by JYB")

app = QApplication(sys.argv)
win = GoogleTrans()
win.show()
sys.exit(app.exec_())
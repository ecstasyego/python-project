from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QMenuBar, QStatusBar

from src.windows.main_window import CentralWidget


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        centralwidget = CentralWidget()
        self.setCentralWidget(centralwidget)
        self.setMenuBar(QMenuBar(self))
        self.setStatusBar(QStatusBar(self))
        self.setGeometry(300, 300, 300, 200)
        QtCore.QMetaObject.connectSlotsByName(self)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())


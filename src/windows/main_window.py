from PyQt5.QtWidgets import QWidget, QVBoxLayout

class CentralWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QVBoxLayout())

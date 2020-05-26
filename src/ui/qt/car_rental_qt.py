from PyQt5.QtWidgets import QApplication

from ui.qt.views.main_menu_ui import MainMenuUi


class CarRentalQt:
    def __init__(self):
        self.app = QApplication([])
        self.ui = MainMenuUi()

    def run(self):
        self.ui.show()
        self.app.exec_()

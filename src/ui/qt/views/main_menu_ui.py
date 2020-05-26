from PyQt5 import uic

from core.configs.app_configs import AppConfigs
from src.ui.qt.views.qt_view import QtView


class MainMenuUi(QtView):
    form, window = uic \
        .loadUiType("{}/ui/qt/forms/qt_calculator.ui".format(AppConfigs.root_dir()))

    def __init__(self):
        super().__init__(MainMenuUi.window())
        self.form = MainMenuUi.form()
        self.form.setupUi(self.window)
        # Add components
        self.setup_ui()

    def setup_ui(self):
        pass

    def show(self):
        self.window.show()

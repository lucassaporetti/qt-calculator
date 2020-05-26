from PyQt5 import uic
from PyQt5.QtWidgets import QTabWidget, QLabel

from core.config.app_configs import AppConfigs
from core.enum.color import Color
from core.model.entity import Entity
from src.ui.qt.views.car.car_edit_view import CarEditView
from src.ui.qt.views.car.car_search_view import CarSearchView
from src.ui.qt.views.rental.rental_edit_view import RentalEditView
from src.ui.qt.views.rental.rental_search_view import RentalSearchView
from src.ui.qt.views.user.user_edit_view import UserEditView
from src.ui.qt.views.user.user_search_view import UserSearchView
from ui.qt.views.qt_view import QtView


class MainMenuUi(QtView):
    form, window = uic \
        .loadUiType("{}/ui/qt/forms/car_rental.ui".format(AppConfigs.root_dir()))

    def __init__(self):
        super().__init__(MainMenuUi.window())
        self.form = MainMenuUi.form()
        self.form.setupUi(self.window)
        self.tabPanel = self.qt.find_widget(self.window, QTabWidget, 'tabPanel')
        self.labelStatusBar = self.qt.find_widget(self.window, QLabel, 'labelStatusBar')
        self.car_search = CarSearchView(self.window, self)
        self.car_edit = CarEditView(self.window, self)
        self.user_search = UserSearchView(self.window, self)
        self.user_edit = UserEditView(self.window, self)
        self.rental_search = RentalSearchView(self.window, self)
        self.rental_edit = RentalEditView(self.window, self)
        self.setup_ui()
        self.set_status('Ready.')

    def setup_ui(self):
        self.tabPanel.setCurrentIndex(0)
        self.tabPanel.currentChanged.connect(self.tab_changed)

    def show(self):
        self.window.show()

    def tab_changed(self, idx: int):
        self.car_search.stackedPanelCars.setCurrentIndex(0)
        self.user_search.stackedPanelUsers.setCurrentIndex(0)
        self.rental_search.stackedPanelRentals.setCurrentIndex(0)
        self.log.info('Tab: tabPanel changed to {}'.format(idx))

    def set_status(self, message, color: Color = Color.BLACK):
        text = '<font color="{}">{}</font>'.format(str(color.name).lower(), message)
        self.labelStatusBar.setText(text)

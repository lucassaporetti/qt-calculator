from abc import ABC, abstractmethod

from PyQt5.QtWidgets import QWidget

from src.core.configs.app_configs import AppConfigs
from src.core.tools.commons import log_init
from src.core.tools.qt_finder import QtFinder


class QtView(ABC):
    def __init__(self, window: QWidget, parent=None):
        super().__init__()
        self.window = window
        self.parent = parent
        self.log = log_init(AppConfigs.log_file())
        self.qt = QtFinder(self.window)

    @abstractmethod
    def setup_ui(self):
        pass

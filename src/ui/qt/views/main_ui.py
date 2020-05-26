from PyQt5 import uic

from src.core.configs.app_configs import AppConfigs
from src.ui.qt.views.qt_view import QtView


class MainUi(QtView):
    form, window = uic \
        .loadUiType("{}/ui/qt/forms/qt_calculator.ui".format(AppConfigs.root_dir()))

    def __init__(self):
        super().__init__(MainUi.window())
        self.form = MainUi.form()
        self.form.setupUi(self.window)
        # Add components {
        self.btnAC = self.qt.find_tool_button('btnAC')
        self.btnSignal = self.qt.find_tool_button('btnSignal')
        self.btnPercent = self.qt.find_tool_button('btnPercent')
        self.btnDivision = self.qt.find_tool_button('btnDivision')
        self.btn7 = self.qt.find_tool_button('btn7')
        self.btn8 = self.qt.find_tool_button('btn8')
        self.btn9 = self.qt.find_tool_button('btn9')
        self.btnMultiplication = self.qt.find_tool_button('btnMultiplication')
        self.btn4 = self.qt.find_tool_button('btn4')
        self.btn5 = self.qt.find_tool_button('btn5')
        self.btn6 = self.qt.find_tool_button('btn6')
        self.btnMinus = self.qt.find_tool_button('btnMinus')
        self.btn1 = self.qt.find_tool_button('btn1')
        self.btn2 = self.qt.find_tool_button('btn2')
        self.btn3 = self.qt.find_tool_button('btn3')
        self.btnPlus = self.qt.find_tool_button('btnPlus')
        self.btn0 = self.qt.find_tool_button('btn0')
        self.btnComma = self.qt.find_tool_button('btnComma')
        self.btnEqual = self.qt.find_tool_button('btnEqual')
        # }
        self.setup_ui()

    def setup_ui(self):
        self.btnAC.clicked.connect(self.btn_ac_clicked)
        self.btnSignal.clicked.connect(self.btn_signal_clicked)
        self.btnPercent.clicked.connect(self.btn_percent_clicked)
        self.btnDivision.clicked.connect(self.btn_division_clicked)
        self.btn7.clicked.connect(self.btn7_clicked)
        self.btn8.clicked.connect(self.btn8_clicked)
        self.btn9.clicked.connect(self.btn9_clicked)
        self.btnMultiplication.clicked.connect(self.btn_multiplication_clicked)
        self.btn4.clicked.connect(self.btn4_clicked)
        self.btn5.clicked.connect(self.btn5_clicked)
        self.btn6.clicked.connect(self.btn6_clicked)
        self.btnMinus.clicked.connect(self.btn_minus_clicked)
        self.btn1.clicked.connect(self.btn1_clicked)
        self.btn2.clicked.connect(self.btn2_clicked)
        self.btn3.clicked.connect(self.btn3_clicked)
        self.btnPlus.clicked.connect(self.btn_plus_clicked)
        self.btn0.clicked.connect(self.btn0_clicked)
        self.btnComma.clicked.connect(self.btn_comma_clicked)
        self.btnEqual.clicked.connect(self.btn_equal_clicked)

    def show(self):
        self.window.show()

    def btn_ac_clicked(self):
        self.log.info("Clicked: AC")

    def btn_signal_clicked(self):
        self.log.info("Clicked: +-")

    def btn_percent_clicked(self):
        self.log.info("Clicked: %")

    def btn_division_clicked(self):
        self.log.info("Clicked: /")

    def btn7_clicked(self):
        self.log.info("Clicked: 7")

    def btn8_clicked(self):
        self.log.info("Clicked: 8")

    def btn9_clicked(self):
        self.log.info("Clicked: 9")

    def btn_multiplication_clicked(self):
        self.log.info("Clicked: x")

    def btn4_clicked(self):
        self.log.info("Clicked: 4")

    def btn5_clicked(self):
        self.log.info("Clicked: 5")

    def btn6_clicked(self):
        self.log.info("Clicked: 6")

    def btn_minus_clicked(self):
        self.log.info("Clicked: -")

    def btn1_clicked(self):
        self.log.info("Clicked: 1")

    def btn2_clicked(self):
        self.log.info("Clicked: 2")

    def btn3_clicked(self):
        self.log.info("Clicked: 3")

    def btn_plus_clicked(self):
        self.log.info("Clicked: +")

    def btn0_clicked(self):
        self.log.info("Clicked: 0")

    def btn_comma_clicked(self):
        self.log.info("Clicked: ,")

    def btn_equal_clicked(self):
        self.log.info("Clicked: =")

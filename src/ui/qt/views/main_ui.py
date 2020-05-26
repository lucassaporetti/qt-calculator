from PyQt5 import uic
from PyQt5.QtWidgets import QLCDNumber

from core.enum.calc_operations import CalcOperations
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
        self.operand = 0
        self.operand2 = 0
        self.display_text = '0'
        self.accumulated = 0
        self.waiting_digit = True
        self.op = CalcOperations.NO_OP
        self.lcdDisplay = self.qt.find_widget(self.window, QLCDNumber, 'lcdDisplay')
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

    def display(self, value):
        self.lcdDisplay.display(value)

    def calculate(self):
        if not self.op or not self.operand or not self.operand2:
            return
        elif self.op == CalcOperations.PERCENT:
            pass
        elif self.op == CalcOperations.SUM:
            self.accumulated = self.operand + self.operand2
        elif self.op == CalcOperations.SUBTRACTION:
            self.accumulated = self.operand - self.operand2
        elif self.op == CalcOperations.MULTIPLICATION:
            self.accumulated = self.operand * self.operand2
        elif self.op == CalcOperations.DIVISION:
            self.accumulated = self.operand / self.operand2
        self.display(self.accumulated)
        self.waiting_digit = False

    def change_op(self, op: CalcOperations):
        self.op = op
        if not self.operand and not self.waiting_digit:
            self.operand = self.lcdDisplay.value()
        elif not self.operand2 and not self.waiting_digit:
            self.operand2 = self.lcdDisplay.value()
            self.calculate()
            self.operand = self.accumulated
            self.display_text = ''
            self.operand2 = 0
        self.wait_digit()

    def wait_digit(self):
        self.display_text = ''
        self.waiting_digit = True

    def append_digit(self, digit: int, set_flag: bool = False):
        digits = self.lcdDisplay.digitCount()
        if self.display_text == '0' or set_flag:
            self.display_text = str(digit)
        else:
            self.display_text += str(digit)
        if len(self.display_text) > digits and digits < 12:
            self.lcdDisplay.setDigitCount(digits + 1)
        elif len(self.display_text) < digits and digits > 8:
            self.lcdDisplay.setDigitCount(digits - 1)
        self.display(self.display_text)
        self.waiting_digit = False

    def btn_equal_clicked(self):
        self.log.info("Clicked: =")
        if self.waiting_digit:
            self.operand2 = self.lcdDisplay.value()
        else:
            self.operand2 = float(self.display_text) if self.display_text else self.operand2
        self.calculate()
        self.operand = self.accumulated
        self.display_text = ''

    def btn_ac_clicked(self):
        self.log.info("Clicked: AC")
        self.operand = 0
        self.operand2 = 0
        self.display_text = '0'
        self.accumulated = 0
        self.waiting_digit = True
        self.op = CalcOperations.NO_OP
        self.lcdDisplay.setDigitCount(8)
        self.display(0)

    def btn_signal_clicked(self):
        self.log.info("Clicked: +-")
        self.display(self.lcdDisplay.value() * -1)

    def btn_percent_clicked(self):
        self.log.info("Clicked: %")
        self.change_op(CalcOperations.PERCENT)

    def btn_division_clicked(self):
        self.log.info("Clicked: /")
        self.change_op(CalcOperations.DIVISION)

    def btn7_clicked(self):
        self.log.info("Clicked: 7")
        self.append_digit(7)

    def btn8_clicked(self):
        self.log.info("Clicked: 8")
        self.append_digit(8)

    def btn9_clicked(self):
        self.log.info("Clicked: 9")
        self.append_digit(9)

    def btn_multiplication_clicked(self):
        self.log.info("Clicked: x")
        self.change_op(CalcOperations.MULTIPLICATION)

    def btn4_clicked(self):
        self.log.info("Clicked: 4")
        self.append_digit(4)

    def btn5_clicked(self):
        self.log.info("Clicked: 5")
        self.append_digit(5)

    def btn6_clicked(self):
        self.log.info("Clicked: 6")
        self.append_digit(6)

    def btn_minus_clicked(self):
        self.log.info("Clicked: -")
        self.change_op(CalcOperations.SUBTRACTION)

    def btn1_clicked(self):
        self.log.info("Clicked: 1")
        self.append_digit(1)

    def btn2_clicked(self):
        self.log.info("Clicked: 2")
        self.append_digit(2)

    def btn3_clicked(self):
        self.log.info("Clicked: 3")
        self.append_digit(3)

    def btn_plus_clicked(self):
        self.log.info("Clicked: +")
        self.change_op(CalcOperations.SUM)

    def btn0_clicked(self):
        self.log.info("Clicked: 0")
        self.append_digit(0)

    def btn_comma_clicked(self):
        self.log.info("Clicked: ,")

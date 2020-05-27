from threading import Thread
from time import sleep

from PyQt5 import uic
from PyQt5.QtWidgets import QLCDNumber

from src.core.configs.app_configs import AppConfigs
from src.core.enum.calc_operations import CalcOperations
from src.ui.qt.views.qt_view import QtView

DECIMAL_SEPARATOR = '.'
MIN_DIGITS = 8
MAX_DIGITS = 12


class MainUi(QtView):
    form, window = uic \
        .loadUiType("{}/ui/qt/forms/qt_calculator.ui".format(AppConfigs.root_dir()))

    class BlinkLcdThread(Thread):
        def __init__(self, lcd: QLCDNumber):
            Thread.__init__(self)
            self.lcd = lcd

        def run(self):
            palette = self.lcd.palette()
            fg_color = palette.color(palette.WindowText)
            bg_color = palette.color(palette.Background)
            palette.setColor(palette.WindowText, bg_color)
            self.lcd.setPalette(palette)
            sleep(0.1)
            palette.setColor(palette.WindowText, fg_color)
            self.lcd.setPalette(palette)

    def __init__(self):
        super().__init__(MainUi.window())
        self.form = MainUi.form()
        self.form.setupUi(self.window)
        # Add components {
        self.wait_operand = True
        self.wait_operand2 = True
        self.operand = 0
        self.operand2 = 0
        self.last_operand = 0
        self.memory_rec = 0
        self.display_text = ''
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
        self.btnDecimal = self.qt.find_tool_button('btnDecimal')
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
        self.btnDecimal.clicked.connect(self.btn_comma_clicked)
        self.btnDecimal.setText(DECIMAL_SEPARATOR)
        self.btnEqual.clicked.connect(self.btn_equal_clicked)

    def show(self):
        self.window.show()

    def display(self, value):
        future_digits = len(str(value)) if value else 0
        digits = len(str(self.lcdDisplay.value))
        if future_digits > digits:
            self.lcdDisplay.setDigitCount(min(future_digits, MAX_DIGITS))
        elif future_digits <= digits:
            self.lcdDisplay.setDigitCount(max(future_digits, MIN_DIGITS))
        self.lcdDisplay.display(value)

    def blink_lcd(self):
        blink = MainUi.BlinkLcdThread(self.lcdDisplay)
        blink.start()
        self.display_text = ''

    def soft_reset(self):
        self.wait_operand = True
        self.wait_operand2 = True
        self.last_operand = self.operand2
        self.operand = 0
        self.operand2 = 0
        self.memory_rec = 0
        self.display_text = ''

    def append_digit(self, digit: int):
        self.btnAC.setText('C')
        if not self.display_text or self.display_text == '0':
            self.display_text = str(digit)
        else:
            self.display_text += str(digit)
        self.display(self.display_text)

    def calculate(self):
        result = None
        if not self.op or not self.operand or not self.operand2:
            return
        elif self.op == CalcOperations.SUM:
            result = self.operand + self.operand2
        elif self.op == CalcOperations.SUBTRACTION:
            result = self.operand - self.operand2
        elif self.op == CalcOperations.MULTIPLICATION:
            result = self.operand * self.operand2
        elif self.op == CalcOperations.DIVISION:
            result = self.operand / self.operand2
        self.display(result)
        self.memory_rec = 0

    def change_op(self, op: CalcOperations):
        self.op = op
        if self.wait_operand:
            self.operand = self.lcdDisplay.value()
            self.memory_rec = self.operand
            self.wait_operand = False
        elif self.wait_operand2:
            self.operand2 = self.lcdDisplay.value()
            self.wait_operand2 = False
        if not self.wait_operand and not self.wait_operand2:
            self.calculate()
            self.operand = self.lcdDisplay.value()
            self.wait_operand2 = True
        self.blink_lcd()

    def btn_equal_clicked(self):
        self.log.info("Clicked: =")
        if self.wait_operand:
            self.operand = self.lcdDisplay.value()
            self.operand2 = self.last_operand
        elif self.wait_operand2:
            self.operand2 = self.lcdDisplay.value()
        self.calculate()
        self.soft_reset()
        self.blink_lcd()

    def btn_ac_clicked(self):
        self.log.info("Clicked: AC")
        if self.memory_rec:
            self.memory_rec = 0
        else:
            self.lcdDisplay.setDigitCount(MIN_DIGITS)
            self.display(0)
            self.soft_reset()
            self.btnAC.setText('AC')
        self.blink_lcd()

    def btn_signal_clicked(self):
        self.log.info("Clicked: +-")
        self.display(self.lcdDisplay.value() * -1)
        self.display_text = self.lcdDisplay.value()

    def btn_percent_clicked(self):
        self.log.info("Clicked: %")
        if not self.memory_rec:
            self.display(self.lcdDisplay.value() / 100)
        else:
            operand1 = self.memory_rec
            operand2 = self.lcdDisplay.value()
            self.display(operand1 * (operand2/100))
        self.display_text = self.lcdDisplay.value()
        self.memory_rec = self.lcdDisplay.value()

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
        if DECIMAL_SEPARATOR not in self.display_text:
            self.display_text += DECIMAL_SEPARATOR if self.display_text else '0' + DECIMAL_SEPARATOR
        self.display(self.display_text)

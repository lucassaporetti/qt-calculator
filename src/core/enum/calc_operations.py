from enum import Enum


class CalcOperations(Enum):
    NO_OP = None
    PERCENT = '%'
    DIVISION = '/'
    MULTIPLICATION = 'x'
    SUBTRACTION = '-'
    SUM = '+'

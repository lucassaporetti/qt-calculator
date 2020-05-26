#!/usr/bin/env python

import signal

from src.ui.qt.qt_calculator import QtCalculator


def exit_app(sig=None, frame=None):
    print(frame)
    print('\033[2J\033[H')
    print('Bye.')
    print('')
    exit(sig)


# Application entry point
if __name__ == "__main__":
    signal.signal(signal.SIGINT, exit_app)
    QtCalculator().run()
    exit_app(0)

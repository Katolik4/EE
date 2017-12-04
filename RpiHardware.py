import sys


class Rpi():

    def __init__(self):
        print('start Rpi Hardware')

    def __del__(self):
        print('End Rpi Hardware')

    def uart_TX(self, message):
        print('Uart TX: {}'.format(message))

    def gpio1(self):
        print('GPIO1')

    def gpio(self, number, state):
        print('Gpio {} in state {}'.format(number, state))


if __name__ == '__main__':

    test = Rpi()
    test.uart_TX('dupa')

from pyfirmata2 import Arduino
import pyfirmata2
global pin
def board_connect(port):
    """ e.g.: port='COM3' or Arduino.AUTODETECT"""
    board = Arduino(port)
    print('Connected to: ' + board.name)
    return board


def board_exit(board):
    """ Close the serial port to the Arduino """
    print('Closing board on:', board.name)
    board.exit()


def write_led(board, state: int):
    """ Set state of builtin LED"""
    board.digital[13].write(state)

def write_digital(board, _pin, state):
    global pin
    try:
        pin = board.get_pin('d:11:p')
    except pyfirmata2.pyfirmata2.PinAlreadyTakenError:
        pass
    if state == 1:
        pin.write(0.1)
    else:
        board.digital[_pin].write(state)


def main():
    print('Connecting...')
    board = board_connect(Arduino.AUTODETECT)
    print("Set state of BuiltinLED through terminal.")
    BOARD_CONN = True
    while BOARD_CONN:
        print("Enter:\n0: OFF\n1: ON\nstop: close connection")
        while True:
            state = input('[YOU]: ')
            if state == '0' or state == '1':
                write_led(board, int(state))
            elif state.lower() == 'stop':
                board_exit(board)
                BOARD_CONN = False
                break
            else:
                print("Enter:\n0: OFF\n1: ON\nstop: close connection")


if __name__=="__main__":
    main()



from microbit import uart, panic
import sys

PANICING = "I'm panicing!\n"

try :
    uart.init()
    uart.write(PANICING)
    panic()
except Exception as ex :
    sys.print_exception(ex)

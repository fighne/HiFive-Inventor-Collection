from hifive import uart, sys

PANICING = r"I'm panicing!\n"

try :
    uart.init()
    uart.write(PANICING)
    sys.panic()
except Exception as ex :
    sys.print_exception(ex)

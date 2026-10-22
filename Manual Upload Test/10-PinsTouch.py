from hifive import uart, sys, this, display
from hifive import pin0, pin1, pin2

DOT = "."
NEWLINE = r"\n"
NO = r"NO\n"
YES = r"YES\n"

pins = [pin0, pin1, pin2]

uart.init()

try :
    while True:
        for pin in pins :
            display.off()
            display.clear()
            if pin.is_touched():
                uart.write(YES)
                display.set_pixel(0, 0, 9)
            else:
                uart.write(NO)
                display.set_pixel(0, 0, 0)
            uart.write(pin)
            uart.write(NEWLINE)
            display.on()
            this.sleep(150)

except Exception as ex :
    sys.print_exception(ex)

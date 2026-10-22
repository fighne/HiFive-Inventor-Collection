from hifive import uart, button_a, sys, this, pin0, pin1, pin2, pin3, pin4
from hifive import pin5, pin6, pin7, pin8, pin9, pin10, pin11, pin12
from hifive import pin13, pin14, pin15, pin16, pin19, pin20

DOT = "."
NEWLINE = r"\n"

# Pin12 appears supported?? Once tested I expect it to fail
pins = [pin0, pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8, pin9, pin10,
        pin11, pin12, pin13, pin14, pin15, pin16, pin19, pin20]

uart.init()

try :
    while True:
        for pin in pins :
            pin.write_digital(1)  # ON
            uart.write(pin)
            while not button_a.was_pressed():
                uart.write(DOT)
                this.sleep(150)  # milliseconds, remain responsive
            pin.write_digital(0)  # OFF
except Exception as ex :
    sys.print_exception(ex)

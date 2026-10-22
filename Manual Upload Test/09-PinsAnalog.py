from hifive import uart, button_a, sys, this
from hifive import pin0, pin1, pin2, pin3, pin4, pin10

DOT = "."
NEWLINE = r"\n"

pins = [pin0, pin1, pin2, pin3, pin4, pin10]

uart.init()

try :
    while True:
        for pin in pins :
            pin.set_analog_period(1000)  # It's PWM
            uart.write(pin.get_mode())
            uart.write(NEWLINE)

            pin.write_analog(511)  # 3/4 0..1023 PWM
            uart.write(pin.get_mode())
            uart.write(NEWLINE)

            uart.write(pin)
            while not button_a.was_pressed():
                uart.write(DOT)
                this.sleep(150)  # milliseconds, remain responsive
            pin.write_analog(0)  # OFF
except Exception as ex :
    sys.print_exception(ex)

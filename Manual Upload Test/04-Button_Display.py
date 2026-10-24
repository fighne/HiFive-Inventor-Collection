from microbit import uart, display, button_a, button_b
import sys

BTNA = "Btn A: "
BTNB = "Btn B: "
NEWLINE = r"\n"

try:
    uart.init()
    while True:
        display.off()
        #display.clear()
        if button_a.is_pressed():
            display.set_pixel(0, 0, 9)
        elif button_b.is_pressed():
            display.set_pixel(0, 1, 9)
        display.on()

        uart.write(BTNA)
        uart.write(str(button_a.get_presses()))
        uart.write(NEWLINE)

        uart.write(BTNB)
        uart.write(str(button_b.get_presses()))
        uart.write(NEWLINE)

except Exception as ex :
    sys.print_exception(ex)

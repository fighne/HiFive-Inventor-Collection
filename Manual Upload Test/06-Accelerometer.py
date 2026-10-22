from hifive import uart, sys, accelerometer

ACCEL = r"Accelerometer\n"
X = "X: "
Y = "Y: "
Z = "Z: "
GEST = "Gestures: "
VAL = "Values: "
NEWLINE = r"\n"
try :
    uart.init()
    uart.write(ACCEL)

    uart.write(X)
    uart.write(accelerometer.get_x())
    uart.write(NEWLINE)

    uart.write(Y)
    uart.write(accelerometer.get_y())
    uart.write(NEWLINE)

    uart.write(Z)
    uart.write(accelerometer.get_z())
    uart.write(NEWLINE)

    uart.write(GEST)
    uart.write(accelerometer.get_gestures())
    uart.write(NEWLINE)

    uart.write(VAL)
    uart.write(accelerometer.get_values())
    uart.write(NEWLINE)
except Exception as ex :
    sys.print_exception(ex)

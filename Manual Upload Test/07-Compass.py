from hifive import uart, sys, compass

COMP = r"Compass\n"
CALIB = "Calibration: "
CALIBING = "Calibrating: "
CAL_CLEAR = r"Calibration Cleared\n"
DOT = "."
FIELDSTRENGTH = "Magnetic Field Strength: "
HEADING = "Heading: "
X = "X: "
Y = "Y: "
Z = "Z: "
GEST = "Gestures: "
VAL = "Values: "
DONE = r"Done\n"
NEWLINE = r"\n"

try :
    uart.init()
    uart.write(COMP)

    uart.write(CALIB)
    uart.write(compass.is_calibrated())
    uart.write(NEWLINE)

    if not compass.is_calibrated():
        uart.write(CALIBING)
        compass.clear_calibration()
        uart.write(CAL_CLEAR)
        compass.calibrate()
        uart.write(NEWLINE)
        while not compass.is_calibrated() :
            uart.write(DONE)
        uart.write(NEWLINE)

    uart.write(FIELDSTRENGTH)
    uart.write(compass.get_field_strength())
    uart.write(NEWLINE)

    uart.write(X)
    uart.write(compass.get_x())
    uart.write(NEWLINE)

    uart.write(Y)
    uart.write(compass.get_y())
    uart.write(NEWLINE)

    uart.write(Z)
    uart.write(compass.get_z())
    uart.write(NEWLINE)

    while True:
        uart.write(HEADING)
        uart.write(compass.heading())
        uart.write(NEWLINE)

except Exception as ex :
    sys.print_exception(ex)

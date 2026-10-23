set -x
./makecombinedhex.py mpy.hex 01-UART-Write_Info.py -o 01-UART-Write_Info.hex
./makecombinedhex.py mpy.hex 02-Button_Image_Display.py -o 02-Button_Image_Display.hex
./makecombinedhex.py mpy.hex 02a-Image_Display.py -o 02a-Image_Display.hex
./makecombinedhex.py mpy.hex 03-UART-Write_Random.py -o 03-UART-Write_Random.hex
./makecombinedhex.py mpy.hex 04-Button_Display.py -o 04-Button_Display.hex
./makecombinedhex.py mpy.hex 05-Panic_Test.py -o 05-Panic_Test.hex
./makecombinedhex.py mpy.hex 06-Accelerometer.py -o 06-Accelerometer.hex
./makecombinedhex.py mpy.hex 07-Compass.py -o 07-Compass.hex
./makecombinedhex.py mpy.hex 08-PinsDigital.py -o 08-PinsDigital.hex
./makecombinedhex.py mpy.hex 09-PinsAnalog.py -o 09-PinsAnalog.hex
./makecombinedhex.py mpy.hex 10-PinsTouch.py -o 10-PinsTouch.hex
./makecombinedhex.py mpy.hex 11-PinsDigitalRead.py -o 11-PinsDigitalRead.hex


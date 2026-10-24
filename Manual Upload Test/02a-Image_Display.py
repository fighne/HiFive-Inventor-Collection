import sys
import microbit
import hifive
hifive.display.on()

hifive.display.clear()
hifive.display.show(hifive.Image.HEART)
hifive.uart.write('SLEEPING')
hifive.sleep(5000)
hifive.uart.write('AWAKE')
hifive.uart.write('NEWLINE')
hifive.display.off()
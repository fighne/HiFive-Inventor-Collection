import sys
import os
import love
import this
import hifive
import microbit

RUNTIME = "RUN TIME: "
TEMP = "Temperature: "
FILELIST = "File List: "
UNAME = "uname: "
VERSION = "System Version: "
VERINFO = "Version Info: "
IMP = "Implementation: "
PLATFORM = "Platform: "
ENDIAN = "Endian: "
AUTHORS = "MicroPython Authors: "
LOVE = "Love.BadaBoom: "

SLEEPING = "Going to Sleep now ..."
AWAKE = "... Awake now"
NEWLINE = r"\n"

try :
    hifive.uart.init()

    hifive.uart.write(RUNTIME)
    hifive.uart.write(str(microbit.running_time()))
    hifive.uart.write(NEWLINE)

    hifive.uart.write(TEMP)
    hifive.uart.write(str(hifive.temperature()))
    hifive.uart.write(NEWLINE)

    hifive.uart.write(FILELIST)
    hifive.uart.write(str(os.listdir()))
    hifive.uart.write(NEWLINE)

    hifive.uart.write(UNAME)
    hifive.uart.write(str(os.uname()))
    hifive.uart.write(NEWLINE)

    hifive.uart.write(VERSION)
    hifive.uart.write(sys.version)
    hifive.uart.write(NEWLINE)

    hifive.uart.write(VERINFO)
    hifive.uart.write(str(sys.version_info))
    hifive.uart.write(NEWLINE)

    hifive.uart.write(IMP)
    hifive.uart.write(str(sys.implementation))
    hifive.uart.write(NEWLINE)

    hifive.uart.write(PLATFORM)
    hifive.uart.write(sys.platform)
    hifive.uart.write(NEWLINE)

    hifive.uart.write(ENDIAN)
    hifive.uart.write(sys.byteorder)
    hifive.uart.write(NEWLINE)

    hifive.uart.write(AUTHORS)
    hifive.uart.write(str(this.authors()))
    hifive.uart.write(NEWLINE)

    hifive.uart.write(LOVE)
    hifive.uart.write(str(love.badaboom()))
    hifive.uart.write(NEWLINE)

    hifive.uart.write(SLEEPING)
    hifive.sleep(5000)
    hifive.uart.write(AWAKE)
    hifive.uart.write(NEWLINE)

    hifive.uart.write(RUNTIME)
    hifive.uart.write(str(hifive.running_time()))
    hifive.uart.write(NEWLINE)
except Exception as ex :
    sys.print_exception(ex)

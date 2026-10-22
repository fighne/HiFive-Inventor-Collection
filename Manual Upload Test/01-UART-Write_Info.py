from hifive import uart, sys, love, this

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
    uart.init()

    uart.write(RUNTIME)
    uart.write(this.running_time())
    uart.write(NEWLINE)

    uart.write(TEMP)
    uart.write(this.temperature())
    uart.write(NEWLINE)

    uart.write(FILELIST)
    uart.write(os.listdir())
    uart.write(NEWLINE)

    uart.write(UNAME)
    uart.write(os.uname())
    uart.write(NEWLINE)

    uart.write(VERSION)
    uart.write(sys.version)
    uart.write(NEWLINE)

    uart.write(VERINFO)
    uart.write(sys.version_info)
    uart.write(NEWLINE)

    uart.write(IMP)
    uart.write(sys.implementation)
    uart.write(NEWLINE)

    uart.write(PLATFORM)
    uart.write(sys.platform)
    uart.write(NEWLINE)

    uart.write(ENDIAN)
    uart.write(sys.byteorder)
    uart.write(NEWLINE)

    uart.write(AUTHORS)
    uart.write(this.authors())
    uart.write(NEWLINE)

    uart.write(LOVE)
    uart.write(love.badaboom())
    uart.write(NEWLINE)

    uart.write(SLEEPING)
    this.sleep(5000)
    uart.write(AWAKE)
    uart.write(NEWLINE)

    uart.write(RUNTIME)
    uart.write(this.running_time())
    uart.write(NEWLINE)
except Exception as ex :
    sys.print_exception(ex)

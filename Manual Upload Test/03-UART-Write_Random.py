from hifive import uart, random, sys

RANDOM = "Random: "
RANDINT = "Random Integer: "
RANDBITS = "Random Bits: "
CHOICE = "Choice from List: "
RANDRANGE = "Random from 0 to {stop}: "
UNIFORM = "Float between {a} and {b}: "
NEWLINE = r"\n"

try :
    random.seed(5)

    uart.init()
    uart.write(random.random())
    uart.write(NEWLINE)

    uart.write(random.randint(1, 10))
    uart.write(NEWLINE)

    uart.write(random.getrandbits(3))
    uart.write(NEWLINE)

    listDozens = [12, 24, 36, 48, 60, 72, 84, 96]
    uart.write(CHOICE)
    uart.write(random.choice(listDozens))
    uart.write(NEWLINE)

    uart.write(RANDRANGE)
    uart.write(random.randrange(100))
    uart.write(NEWLINE)

    uart.write(UNIFORM)
    uart.write(random.uniform(0.25, 0.99))
    uart.write(NEWLINE)

except Exception as ex :
    sys.print_exception(ex)

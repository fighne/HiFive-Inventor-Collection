from hifive import display, button_a, button_b, Image, sys

def imageIndex(x):
    return {
        1: Image.HEART,
        2: Image.HEART_SMALL,
        3: Image.HAPPY,
        4: Image.SMILE,
        5: Image.SAD,
        6: Image.CONFUSED,
        7: Image.ANGRY,
        8: Image.ASLEEP,
        9: Image.SURPRISED,
        10: Image.SILLY,
        11: Image.FABULOUS,
        12: Image.MEH,
        13: Image.YES,
        14: Image.NO,
        15: Image.CLOCK12,
        16: Image.CLOCK11,
        17: Image.CLOCK10,
        18: Image.CLOCK9,
        19: Image.CLOCK8,
        20: Image.CLOCK7,
        21: Image.CLOCK6,
        22: Image.CLOCK5,
        23: Image.CLOCK4,
        24: Image.CLOCK3,
        25: Image.CLOCK2,
        26: Image.CLOCK1,
        27: Image.ARROW_N,
        28: Image.ARROW_NE,
        29: Image.ARROW_E,
        30: Image.ARROW_SE,
        31: Image.ARROW_S,
        32: Image.ARROW_SW,
        33: Image.ARROW_W,
        34: Image.ARROW_NW,
        35: Image.TRIANGLE,
        36: Image.TRIANGLE_LEFT,
        37: Image.CHESSBOARD,
        38: Image.DIAMOND,
        39: Image.DIAMOND_SMALL,
        40: Image.SQUARE,
        41: Image.SQUARE_SMALL,
        42: Image.RABBIT,
        43: Image.COW,
        44: Image.MUSIC_CROTCHET,
        45: Image.MUSIC_QUAVER,
        46: Image.MUSIC_QUAVERS,
        47: Image.PITCHFORK,
        48: Image.XMAS,
        49: Image.PACMAN,
        50: Image.TARGET,
        51: Image.TSHIRT,
        52: Image.ROLLERSKATE,
        53: Image.DUCK,
        54: Image.HOUSE,
        55: Image.TORTOISE,
        56: Image.BUTTERFLY,
        57: Image.STICKFIGURE,
        58: Image.GHOST,
        59: Image.SWORD,
        60: Image.GIRAFFE,
        61: Image.SKULL,
        62: Image.UMBRELLA,
        63: Image.SNAKE,
        64: Image.ALL_CLOCKS,
        65: Image.ALL_ARROWS,
    }.get(x, 0)

imgIdx = 1
idxChanged = True

try :
    display.on()

    while True:
        if button_a.was_pressed():
            imgIdx = imgIdx + 1
            idxChanged = True
        elif button_b.was_pressed():
            imgIdx = imgIdx - 1
            idxChanged = True

        if imgIdx > 65:
            imgIdx = 1

        if idxChanged :
            display.off()
            display.clear()
            display.show(imageIndex(imgIdx))
            display.on()
            idxChanged = False
except Exception as ex :
    sys.print_exception(ex)

import sys
import microbit
import hifive


def imageIndex(x):
    return {
        1: hifive.Image.HEART,
        2: hifive.Image.HEART_SMALL,
        
    }.get(x, 0)

imgIdx = 1
idxChanged = True

try :
    hifive.display.on()

    while True:
        if microbit.button_a.was_pressed():
            imgIdx = imgIdx + 1
            idxChanged = True
        elif microbit.button_b.was_pressed():
            imgIdx = imgIdx - 1
            idxChanged = True

        if imgIdx > 65:
            imgIdx = 1

        if idxChanged :
            hifive.display.off()
            hifive.display.clear()
            hifive.display.show(imageIndex(imgIdx))
            hifive.display.on()
            idxChanged = False
except Exception as ex :
    sys.print_exception(ex)

from microbit import *

display.show(Image.ASLEEP)

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        display.show(Image.CONFUSED)
    elif button_a.is_pressed():
        display.show(Image.HAPPY)
    elif button_b.is_pressed():
        display.show(Image.SAD)
    elif accelerometer.was_gesture("shake"):
        display.show(Image.ANGRY)
    elif pin0.is_touched():
        display.show(Image.SURPRISED)

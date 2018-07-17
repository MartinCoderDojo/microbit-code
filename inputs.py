from microbit import *

display.show(Image.ASLEEP)

while True:
    
    if button_a.is_pressed():
        display.show(Image.HAPPY)

    if button_b.is_pressed():
        display.show(Image.SAD)

    if accelerometer.was_gesture("shake"):
        display.show(Image.ANGRY)
    
    if pin0.is_touched():
        display.show(Image.SURPRISED)
   

from microbit import *
import random

answers = [
    "Yes",
    "No",
    "Maybe",
]

while True:
    display.show("8")
    if accelerometer.was_gesture("shake"):
        display.clear()
        sleep(1000)
        display.scroll(random.choice(answers))

from microbit import *

happy_face = Image("00000:"
              "09090:"
              "00000:"
              "90009:"
              "09990")

sad_face = Image("00000:"
              "09090:"
              "00000:"
              "09990:"
              "90009")

all_faces = [happy_face, sad_face]
while True:
    display.show(all_faces, delay=200)

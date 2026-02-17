"""
Created by: Jayden Okafor
Created on: Feb 2026
This module is a Micro:bit MicroPython program that calculates the perimeter and area of a rectangle
"""

from microbit import *

display.clear()
sleep(1)

display.scroll("A rectangle has dimensions 5 cm & 3 cm")
display.show(Image.HAPPY)
sleep(0.5)
display.clear()


display.scroll("The perimeter would be: " + str(2 * (5 + 3)) + ' cm')
display.show(Image.HAPPY)
sleep(0.5)
display.clear()

display.scroll("The area would be: " + str(5 * 3) + ' cm^2')
display.show(Image.HAPPY)
sleep(0.5)
display.clear()

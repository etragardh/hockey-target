#
#
# 2x boards x8 leds
#
# OBS!
# The only GPIO.PIN I could get to work was 18
# For that to work the rpi sound must be disabled.
# /boot/firmware/config.txt -> "dtparam=audio=off" -> reboot
#
# Install neopixel lib
# sudo pip3 install adafruit-circuitpython-neopixel --break-system-packages
#

import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 16)
for i in range(8):
#    pixels[i] = (255, 0, 0)
    n = i +8
    pixels[n] = (0, 0, 255)


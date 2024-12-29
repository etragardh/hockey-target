# Why does edge detection fail some times?
#
# This code works in a fresh install
# run:
# apt-get update
# apt-get upgrade
# python3 preassure.py

import RPi.GPIO as GPIO
import time


UPPER_GPIO = 23
#LOWER_GPIO = 24

def hit_callback(HIT_GPIO):
  print('HIT: ' + str(HIT_GPIO))

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(UPPER_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #initial value = DOWN/LOW/OFF
GPIO.add_event_detect(UPPER_GPIO,GPIO.RISING,callback=hit_callback)

test = input("Press enter to quit")

GPIO.cleanup()

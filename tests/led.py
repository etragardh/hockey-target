# This lights up the left, green LED for 1s

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

print("LED on")
GPIO.output(18, GPIO.HIGH)
GPIO.output(23, GPIO.HIGH)

time.sleep(1)
print ("LED off")
GPIO.output(18, GPIO.LOW)
GPIO.output(23, GPIO.LOW)

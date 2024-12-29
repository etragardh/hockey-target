# Why does edge detection fail some times?

import RPi.GPIO as GPIO
import time

UPPER_GPIO = 23     # 23 is the correct UPPER value when mode is BCM
#LOWER_GPIO = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(UPPER_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #initial value = DOWN/LOW/OFF
#GPIO.add_event_detect(UPPER_GPIO,GPIO.RISING,callback=hit_callback) # Setup event on pin 10 rising edge

try:
  while True: # Run forever
    if GPIO.input(UPPER_GPIO) == GPIO.HIGH:
      print("Button was pushed!")
except KeyboardInterrupt:
  GPIO.cleanup()
  print("Exiting")
  
GPIO.cleanup()

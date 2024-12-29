import RPi.GPIO as GPIO

def button_callback(c):
    print("button pressed", c)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #initial value = DOWN/LOW/OFF
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #initial value = DOWN/LOW/OFF

GPIO.add_event_detect(17, GPIO.RISING, callback=button_callback)
GPIO.add_event_detect(4, GPIO.RISING, callback=button_callback)

message = input('press enter to quit')

GPIO.cleanup()

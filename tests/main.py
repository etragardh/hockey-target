import time, random
import RPi.GPIO as GPIO
import I2C_LCD_driver

mylcd = I2C_LCD_driver.lcd()
def lcdp(text, line = 1):
    mylcd.lcd_display_string(text, line)

LEFT_CROSS_LED_GPIO = 18
LEFT_CROSS_PUSH_GPIO = 17

RIGHT_CROSS_LED_GPIO = 23
RIGHT_CROSS_PUSH_GPIO = 4

areas = [
    {
        'slug': 'left-cross',
        'led':  LEFT_CROSS_LED_GPIO,
        'push': LEFT_CROSS_PUSH_GPIO
    },
    {
        'slug': 'right-cross',
        'led':  RIGHT_CROSS_LED_GPIO,
        'push': RIGHT_CROSS_PUSH_GPIO
    },
]

# Score
score = 0

# Active area
active_area = False

# Last hit
last_hit = 0 

def hit_callback(area_push_gpio):
    #do not accept hits to fast
    global last_hit
    accepted_time_buffer = last_hit + 250
    now = round(time.time() * 1000)
    if now <= accepted_time_buffer:
        return

    # Set last hit to "now"
    last_hit = now 

    global score
    if areas[active_area]['push'] == area_push_gpio:
        score = score + 1
        lcdp("SCORE: " + str(score))
        change_active_area()
    else:
        score = score - 1
        lcdp("SCORE: " + str(score))

def change_active_area():
    # Turn of previous active area LED (if it exists)
    global active_area
    if active_area is not False:
        GPIO.output(areas[active_area]['led'], GPIO.LOW)

    # New random area
    active_area = random.randrange(0, len(areas))
    # Turn it on
    GPIO.output(areas[active_area]['led'], GPIO.HIGH)


# Setup RPi GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for area in areas:
    # Setup Push
    GPIO.setup(int(area['push']), GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #initial value = DOWN/LOW/OFF
    GPIO.add_event_detect(area['push'], GPIO.RISING, callback=hit_callback)

    # Setup LED
    GPIO.setup(int(area['led']), GPIO.OUT)

# Start with a random area
#active_area = random.randrange(0, len(areas))
change_active_area()

# Start
mylcd.lcd_clear()
lcdp("Lets GO!")
lcdp("", 2)

# Exit after 60 seconds
timer = 20
run = True
while run:
    time.sleep(1)
    timer = timer -1
    lcdp("Time left:" + "{:02d}".format(timer), 2)
    #print("timer:",timer)
    if timer <= 0:
        run = False

#lcdp("TOTAL: "+ str(score))
mylcd.lcd_clear()
lcdp("Final score: " + str(score))
if score >= 5:
    lcdp("Good job!", 2)
else:
    lcdp("Oh, come on :/", 2)

GPIO.cleanup()


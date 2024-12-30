from lcd import LCD
#import RPi.GPIO as GPIO
from cprint import CPrint
from games.base import GameBase
import time

p = CPrint()
lcd = LCD(debug=True)

#UPPER_GPIO = 23
#LOWER_GPIO = 24

# Test
#def hit_callback(HIT_GPIO):
#  print('HIT: ' + HIT_GPIO)

#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)

#GPIO.setup(UPPER_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #initial value = DOWN/LOW/OFF
#GPIO.add_event_detect(UPPER_GPIO,GPIO.RISING,callback=hit_callback)

# Game: Single Player
class Game(GameBase):
  # Single player game has only one area active at a time
  active_area = 0
  play_time = 60 # 60s

  def __init__(self, debug = False):
    super().__init__('Single Player', 'single', debug)

    if debug:
      p.enable_debug(debug)
  #
  # Local override
  def hit_callback(self, area):
    p.v('GAME: HIT: ', area)
    self.score += 1
    self.print_score()

  #
  # Local override
  def reset(self):
    super().reset()
    self.score = 0        # default score is array
    lcd.p1('Score: 0')
  
  #
  # Called once at game start
  def play(self):
    p.v('GAME: this is a play loop')
    lcd.p1('Playing')
    self.print_score()

  #
  # Called every second
  def tick(self, time_left, time_elapsed):
    lcd.p1('Playing: ' + str(time_left))
    p.vvv("Tick: ", time_left, time_elapsed)

  def print_score(self):
    lcd.p2('Score: ' + str(self.score))

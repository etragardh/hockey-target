from lcd import LCD
import RPi.GPIO as GPIO
from cprint import CPrint
from games.base import GameBase
import time

p = CPrint()
lcd = LCD()

UPPER_GPIO = 23
LOWER_GPIO = 24
# Test
def hit_callback(HIT_GPIO):
  print('HIT: ' + HIT_GPIO)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(UPPER_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #initial value = DOWN/LOW/OFF
GPIO.add_event_detect(UPPER_GPIO,GPIO.RISING,callback=hit_callback)


# Game: Single Player
class Game(GameBase):
  # Single player game has only one area active at a time
  active_area = 0
  play_time = 60 # 60s

  def __init__(self, debug = False):
    super().__init__('Single Player', 'single', debug)

    if debug:
      p.enable_debug()

    self.init()

  def init(self):
    p.vv('Init GPIO')
#    GPIO.setwarnings(False)
#    GPIO.setmode(GPIO.BCM)

#    GPIO.setup(UPPER_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #initial value = DOWN/LOW/OFF
#    GPIO.add_event_detect(UPPER_GPIO,GPIO.RISING,callback=self.hit_callback.__func__)

  def hit_callback(self, area):
    p.vvv('HIT CB: ' + area)
    # make some conditions to be met for register hits
    self.hit(area)

  def hit(area):
    p.v('HIT: ' + area)
    self.score

  def reset(self):
    super().reset()
    self.score = 0      # default score is array
  
  def play(self):
    p.v('this is a play loop')

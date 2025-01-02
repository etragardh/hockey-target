from lcd import LCD
#import RPi.GPIO as GPIO
from cprint import CPrint
from games.base import GameBase
import time

p = CPrint()
lcd = LCD(debug=True)

UPPER_GPIO = 23
LOWER_GPIO = 24

# Game: Single Player
class Game(GameBase):
  # Single player game has only one area active at a time
  active_area = 0
  areas = [LOWER_GPIO, UPPER_GPIO]
  
  def __init__(self, debug = False):
    super().__init__('Single Player', 'single', debug)

    if debug:
      p.enable_debug(debug)
  #
  # Local override
  def hit_callback(self, area):
    # If we are not playing (ie showing stats)
    if not self.playing:
      p.vv('GAME: Hit while not playing')
      return

    # If it was not the active area
    if self.areas[self.active_area] != area:
      p.vv('GAME: WRONG HOLE')
      return

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
    #lcd.p1('GO! GO! GO!')
    self.print_score()
    self.active_area = 0 # UPPER
    self.led_sync()

  def led_sync(self):
    active = self.active_area
    inactive = 1 - active # the opposite

    self.light(active, 'green')
    self.off(inactive)

  #
  # Called every second
  def tick(self, time_left, time_elapsed):
    time_left = str(time_left).zfill(2)

    lcd.p1('Time: ' + time_left)
    p.vvv("Tick: ", time_left, time_elapsed)

    # Do we switch active area?
    if time_elapsed != 0 and time_elapsed % 4 == 0:
      self.active_area ^= 1 # Toggle 0/1
      p.v("GAME: New Area")
      p.vv(self.active_area)
      self.led_sync()

  def print_score(self):
    lcd.p2('Score: ' + str(self.score))

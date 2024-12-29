from lcd import LCD
import RPi.GPIO as GPIO
from cprint import CPrint
from games.base import GameBase
import time

p = CPrint()
lcd = LCD()

UPPER_GPIO = 23
LOWER_GPIO = 24

# Game: Single Player
class Game(GameBase):
  # Single player game has only one area active at a time
  active_area = 0
  play_time = 60 # 60s

  def __init__(self, debug = False):
    super().__init__('Single Player', 'single', debug)

    if debug:
      p.enable_debug()


  def start(self):
    p.v('Starting Game: ' + self.name)
    self.welcome()
    time.sleep(1)
    while True:
      self.play()
      self.done()
      time.sleep(3)
      self.reset()

  def done(self):
    lcd.p1('Score: ' + self.score)
    lcd.p2("High score: ", self.cfg('highscore'))
    p.vvv('Game Done: update high scores etc..')

  # Play one (1) round
  def play(self):
    playing = True
    timer = 5
    while playing:
      timer -= 1
      p.vvv('Sleeping 1')
      time.sleep(1)

      if timer <= 0:
        playing = False

    p.v('Game ended')

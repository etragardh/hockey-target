from lcd import LCD
from neo import Neo
import json, time
from cprint import CPrint
p = CPrint()
lcd = LCD()
neo = Neo([[0,1,2,3,4,5,6,7],[8,9,10,11,12,13,14,15]])

class GameBase:

  score   = [0,0]
  config  = False
  name    = False
  slug    = False

  def __init__(self, name = 'SinglePlayer', slug = 'single', debug = False):
    self.name = name
    self.slug = slug
    if debug:
      p.enable_debug(debug)

    with open('config.json', 'r') as fp:
      self.config = json.load(fp)
      p.vv('BASE: Config loaded')
      p.vvv(self.config)

      # Reset active game, points etc
      self.reset()

  def cfg(self, key = False, value = False):
    if not value:
      value = self.config[key] if key in self.config else False
      p.vvv(f'BASE CFG: Get {key} => {value}')
      return value
    else:
      p.vvv(f'BASE CFG: Set {key} => {value}')
      self.config[key] = value

  def welcome(self):
    lcd.p1(self.name)
    lcd.p2("High score: " + str(self.cfg('highscore')))
    p.vv('BASE: Game welcome')

  def start(self):
    p.vv('BASE: Starting Game: ' + self.name)
    self.welcome()
    time.sleep(1)
    while True:
      self._play()
      self.done()
      time.sleep(3)
      self.reset()

  def _play(self):
    timer = 5
    while timer <= 0:
      timer -= 1

      self.play()

    p.v('Game ended')

  def done(self):
    lcd.p1('Score: ' + self.score)
    lcd.p2("High score: ", self.cfg('highscore'))
    p.vvv('BASE: Game Done: update high scores etc..')

  def reset(self):
    self.score = [0, 0]
    p.vv('BASE: resetting score to [0, 0]')
    lcd.c()
    neo.off()

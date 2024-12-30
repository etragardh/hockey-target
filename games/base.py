from lcd import LCD
from neo import Neo
import RPi.GPIO as GPIO
import json, time, copy
from cprint import CPrint
p = CPrint()
lcd = LCD()
neo = Neo([[0,1,2,3,4,5,6,7],[8,9,10,11,12,13,14,15]])

WELCOME_TIME = 5      # First welcome on startup
PLAY_TIME = 10        # seconds to play one game
BETWEEN_GAME_TIME = 5

UPPER_GPIO = 23
LOWER_GPIO = 24

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

    p.vv('GAME: Init GPIO')
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    
    # UPPER
    GPIO.setup(UPPER_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #initial value = DOWN/LOW/OFF
    GPIO.add_event_detect(UPPER_GPIO,GPIO.RISING,callback=self.hit_callback, bouncetime=200)

    # LOWER
    GPIO.setup(LOWER_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #initial value = DOWN/LOW/OFF
    GPIO.add_event_detect(LOWER_GPIO,GPIO.RISING,callback=self.hit_callback, bouncetime=200)

  def exit(self):
    p.vvv('BASE: destructor')
    lcd.c()
    GPIO.cleanup()
    lcd.p1('Bye Bye!')
    
  def hit_callback(self, area):
    p.vvv('BASE: HIT CB: ', area)

  def cfg(self, key = False, value = False):
    if not value:
      value = self.config[key] if key in self.config else False
      p.vvv(f'BASE CFG: Get {key} => {value}')
      return value
    else:
      p.vvv(f'BASE CFG: Set {key} => {value}')
      self.config[key] = value

  def welcome(self):
    lcd.c()
    lcd.p1(self.name)
    self.print_highscore()
    p.vv('BASE: Game welcome')

  def start(self):
    p.vv('BASE: Starting Game: ' + self.name)
    self.welcome()
    time.sleep(WELCOME_TIME)
    lcd.c()
    while True:
      self._play()
      self.done()
      time.sleep(BETWEEN_GAME_TIME)
      self.reset()

  def _play(self):
    timer = copy.deepcopy(PLAY_TIME)
    self.play()
    while timer >= 0:
      self.tick(str(timer).zfill(2), str(PLAY_TIME-timer).zfill(2))
      timer -= 1
      time.sleep(1)
    p.v('Game ended')

  def done(self):
    p.vvv('BASE: Game Done: update high scores etc..')
    lcd.c()
    if isinstance(self.score, list):
      lcd.p1('P1: ' + str(self.score[0]) + ' | P2: ' + str(self.score[1]))
    else:
      lcd.p1('Score: ' + str(self.score))
    self.print_highscore()

  def print_highscore(self):
    highscore = self.cfg('highscore')
    highscore = str(highscore) if highscore else "0"
    lcd.p2("High score: " + highscore)
    p.vvv('BASE score, highscore', self.score, highscore)

  def reset(self):
    p.vv('BASE: reset score, lcd, neo')
    self.score = [0, 0]
    lcd.c()
    neo.off()

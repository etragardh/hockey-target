#!/usr/bin/env python3

from lcd import LCD
import os, time, json
from importlib.machinery import SourceFileLoader
from cprint import CPrint

DEBUG = 3 # False | 1 | 2 | 3
p = CPrint(debug = DEBUG)

# MyPath
base_path = os.path.dirname(os.path.realpath(__file__))

# Welcome message
lcd = LCD()
lcd.p1('Hockey Target')

# CFG
if os.path.exists(f'{base_path}/config.json'):
  with open(f'{base_path}/config.json', 'r') as fp:
    config = json.load(fp)
    p.vvv('loaded config', config)

else:
  config = {
    'game': 'single',
    'single': { 'highscore': 0 },
    'multi': { 'highscore': 0 }
  }
  with open(f'{base_bath}/config.json', 'w+') as fp:
    fp.write(json.dumps(config))
  p.vvv('created config', config)

def cfg(key = False, value = False):
  if not value:
    p.vvv(f'get cfg {key} = {config[key]}')
    return config[key]
  else:
    p.vvv(f'set cfg {key} = {value}')
    config[key] = value

game  = SourceFileLoader("Source Module",f'{base_path}/games/{cfg("game")}.py').load_module().Game(debug = DEBUG)

try:
  game.start()
except KeyboardInterrupt as e:
  p.v('Exiting')
  game.exit()

#with open('config.json', 'w+') as fp:
#  fp.write(json.dumps(config))

#p.vvv('save config on exit', config)
exit()
#
# Main
# Choose a game mode
#



from neo import Neo
import time

lamps = Neo([[0,1,2,3,4,5,6,7],[8,9,10,11,12,13,14,15]])
lamps.light(0, 'green')
time.sleep(5)
lamps.light(0, 'red')
lamps.light(1, 'blue')

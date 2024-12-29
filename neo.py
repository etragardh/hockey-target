import neopixel
import board

class Neo:
  lamps = [[1,2,3,4,5,6,7,8],[9,10,11,12,13,14,15,16]]
  state = []

  colors = {
      'off': (0,0,0),
      'white': (255, 255, 255),
      'red': (255, 0, 0),
      'green': (0, 255, 0),
      'blue': (0, 0, 255)
  }

  def __init__(self, lamps):
      self.lamps = lamps

      for lamp in lamps:
          self.state.append('off')

      # Change for dynamic init
      self.pixels = neopixel.NeoPixel(board.D18, 16)


      #print('Init done', self.lamps, self.state, self.colors)

  def light(self, lamp = 0, color = 'green'):
    for i, l in enumerate(self.lamps):
      if i == lamp:
        self.state[i] = color

    self.sync_state()

  def off(self, lamp = 0):
    for i, l in enumerate(self.lamps):
      if i == lamp:
        self.state[i] = 'off' 
    self.sync_state()


  def sync_state(self):
    for i, lamp in enumerate(self.lamps):
      color = self.state[i]
      for led in lamp:
        #print('setting color')
        #print(color)
        self.pixels[led] = self.colors[color]

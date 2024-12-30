import I2C_LCD_driver
mylcd = I2C_LCD_driver.lcd()

class LCD:

  def __init__(self, debug = False):
    self.debug = debug

  def p(self, text, line):
    mylcd.lcd_display_string(text, line)
    self.d(text, line)

  def p1(self, text):
    self.p(text, 1)

  def p2(self, text):
    self.p(text, 2)

  def c(self):
    mylcd.lcd_clear()
    self.d('_c_', 1)
    self.d('_c_', 2)

  def d(self, text, line):
    if self.debug:
      print("LCD("+str(line)+"): " + text)

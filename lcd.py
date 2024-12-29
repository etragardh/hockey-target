import I2C_LCD_driver
mylcd = I2C_LCD_driver.lcd()

class LCD:

    def __init__(self):
        pass

    def p(self, text, line):
        mylcd.lcd_display_string(text, line)

    def p1(self, text):
        self.p(text, 1)

    def p2(self, text):
        self.p(text, 2)

    def c(self):
        mylcd.lcd_clear()

import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string("Boo Hockey!", 1)
mylcd.lcd_display_string("Pro shooter", 2)

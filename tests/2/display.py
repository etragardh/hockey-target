#
# I2C must be enabled in pi config
# raspi-config
# Interfaces -> I2C -> enable -> finninsh -> reboot
#
#
# Depends on:
# apt install python3-smbus

import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string("Boo Hockey!", 1)
mylcd.lcd_display_string("Pro shooter", 2)

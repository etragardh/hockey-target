#!/bin/bash

# Setup python environment
mkdir ~/code
cd ~/code
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get install -y git
sudo apt-get install -y python3-pip
sudo apt-get install -y vim 
git clone https://github.com/etragardh/hockey-target
cd hockey-target
python3 -m venv .venv
source .venv/bin/activate
pip3 install adafruit-circuitpython-neopixel 
# this goes from rpi-lgpio to rpi.gpio
# # install the original again
pip3 install rpi-lgpio            # For preassure plates "edge"
pip3 install smbus                # For LEDs

# Configure pi for I2C (display)
# Interfaces -> I2C -> enable -> finnish
deactivate
sudo raspi-config nonint do_i2c 1

# Setup adhoc wifi


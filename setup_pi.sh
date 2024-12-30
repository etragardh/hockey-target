#!/bin/bash

# Setup python environment
mkdir ~/code
cd ~/code
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get install -y git python3-pip vim i2c-tools
git clone https://github.com/etragardh/hockey-target
cd hockey-target
python3 -m venv .venv
source .venv/bin/activate
pip3 install adafruit-circuitpython-neopixel 
# this goes from rpi-lgpio to rpi.gpio
# # install the original again
pip3 install rpi-lgpio                          # For preassure plates "edge"
# pip3 uninstall -y RPi.GPIO                    # Fix if fucked up =) run with line below
# pip3 install --force-reinstall rpi-lgpio      # run this as well for fuckups with "edge"
pip3 install smbus                              # For LEDs
pip3 install tabulate                           # For CPrint

# Configure pi for I2C (display)
# Interfaces -> I2C -> enable -> finnish
deactivate
sudo raspi-config nonint do_i2c 0

# Neopixels must be run as root
sudo su
source .venv/bin/activate

# Setup adhoc wifi


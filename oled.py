#!/usr/bin/env python
# File    : oled.py : Read buttons on Sparkfun OLED Block for edison and display
# Author  : Joe McManus joe@alumni.cmu.edu
# Version : 0.1  12/10/2016
# Copyright (C) 2016 Joe McManus
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import time
import pyupm_i2clcd as lcdObj
import mraa
import argparse 

parser = argparse.ArgumentParser(description='Demo App for Sparkfun OLED Edison Shield')
parser.add_argument('--debug', help="Display button readings on terminal", action="store_true")
parser.add_argument('--version', action='version',version='%(prog)s 0.1')
args=parser.parse_args()


print("Starting Sparkfun OLED Edison Block Demo")
# setup with default values
lcd = lcdObj.EBOLED()
lcd.clear()
lcd.setTextWrap(1)
lcd.setCursor(10, 5)
lcd.write("Button")
lcd.setCursor(30, 5)
lcd.write("Example")
lcd.refresh()
time.sleep(2)
lcd.clearScreenBuffer()
lcd.refresh()

buttonA=mraa.Gpio(47)
buttonA.dir(mraa.DIR_IN)

buttonB=mraa.Gpio(32)
buttonB.dir(mraa.DIR_IN)

buttonUp=mraa.Gpio(46)
buttonUp.dir(mraa.DIR_IN)

buttonDown=mraa.Gpio(31)
buttonDown.dir(mraa.DIR_IN)

buttonLeft=mraa.Gpio(15)
buttonLeft.dir(mraa.DIR_IN)

buttonRight=mraa.Gpio(45)
buttonRight.dir(mraa.DIR_IN)

buttonSelect=mraa.Gpio(33)
buttonSelect.dir(mraa.DIR_IN)

buttons={ buttonA:"A", 
        buttonB: "B", 
        buttonUp: "Up",
        buttonDown: "Down",
        buttonLeft: "Left",
        buttonRight: "Right",
        buttonSelect: "Select" }

while 1:
    try:
        for button, msg in buttons.iteritems():
            if button.read() == 0: 
                if args.debug:
                        print("Button " + msg + " pressed.")
                lcd.setCursor(5, 0);
                lcd.write("Button")
                lcd.setCursor(15, 0);
                lcd.write(msg)
                lcd.refresh()
                time.sleep(0.01)
                lcd.clearScreenBuffer()
                lcd.refresh()

    except KeyboardInterrupt:
        print("Exiting Sparkfun OLED Edison Block Demo")
        quit() 
            
    except Exception,e: 
        print("Error: {:s}". format(e))
        quit()

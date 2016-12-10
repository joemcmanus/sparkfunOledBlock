#!/usr/bin/env python
# File    : lcdWakeUp.py : Print the IP of Edison to Sparkfun Block
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
import os
import subprocess

#Get IP address
ip=subprocess.Popen("ifconfig wlan0 | grep inet | cut -d':' -f2 | cut -d' ' -f1", shell=True, stdout=subprocess.PIPE).stdout.read()

lcd = lcdObj.EBOLED()
lcd.clear()
lcd.setTextWrap(1)
lcd.setCursor(10, 0)
lcd.write("IP Addr:")
lcd.setCursor(30, 0)
lcd.write(ip)
lcd.refresh()
time.sleep(10)

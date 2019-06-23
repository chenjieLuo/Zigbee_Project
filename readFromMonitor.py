# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 19:42:30 2019

@author: dell-pc
"""

import serial
#import syslog
#import time

#This line is for serial over GPIO
port = 'COM7'


ard = serial.Serial(port,9600,timeout=5)

#i is the number of samplings
i = 0

while (i < 20):
    msg = ard.readline()
    readout = msg.decode("utf-8") 
    if (readout[-7] == '8'):
        print ("D3 is on")
    elif (readout[-7] == '4'):
        print ("D2 is on")
    elif (readout[-7] == 'C'):
        print ("Both are off")
    i = i + 1

print ("Exiting")
exit()

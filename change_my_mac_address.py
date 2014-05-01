#!/usr/local/bin/python

"""
This script changes the MAC address each period of time
Please run it as root
Make sure you already have 'macchanger'
"""

import os
from time import sleep
from threading import Timer


min_time = float(raw_input('Please enter the looping time in minutes: '))
time = min_time*60
device_name = raw_input('Please enter the device name (example: wlan0): ')


down_command     = "sudo ifconfig "+device_name+" down"
changing_command = "sudo macchanger -r "+device_name
up_command       = "sudo ifconfig "+device_name+" up"

def change_loop():
    try:
        print "-"*30
        print "Changing Address :"
        print "-"*30
        os.system(down_command)
        os.system(changing_command)
        os.system(up_command)
        print "-"*30
        t = Timer(time, change_loop)
        t.start()
    except:
        print "Damn! there's something wrong"

change_loop()

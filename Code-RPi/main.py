#!/usr/bin/env python3
# coding: utf-8


import max7219.led as led
import time

l = led.matrix()
t = time.sleep

def mainfunction():
    global mainfunction
    l.show_message("Booting up...")
    t(10)
    l.show_message("")
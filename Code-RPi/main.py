#!/usr/bin/env python3
# coding: utf-8

import max7219.led as led

l = led.matrix()
l.show_message("Hello world!")
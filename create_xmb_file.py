#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 19:34:10 2018

@author: RedKnite
"""

from PIL import Image

im = Image.open("/home/RedKnite/Dropbox/Python/Calculator/Calculator_5122x.png")
im = im.convert("RGB")
im.save("calculator_fed_pic.xbm", "XBM")
















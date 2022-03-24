# caterpillar.py

import time

width = 30

for i in range(width):
    print(" " * (i) + ("_"*5 if i % 2 else "_⊓_  "), end="\r")
    time.sleep(.5)
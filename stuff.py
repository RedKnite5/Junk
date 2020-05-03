#!C:\Users\RedKnite\AppData\Local\Programs\Python\Python38\python

# stuff.py

from collections import namedtuple

from recordclass import recordclass
import numpy as np

Point1 = namedtuple("Point1", "x y")
Point2 = recordclass("Point2", "x y")

named = Point1(2, 3)
record = Point2(2, 3)

arr = np.arange(30).reshape((5, 6))

print(arr[named])
print(arr[record])